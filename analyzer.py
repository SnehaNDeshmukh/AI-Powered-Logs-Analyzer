import os
import joblib
from collections import Counter, defaultdict

from colorama import Fore, Style, init
from utils.helpers import extract_ip, clean_log, calculate_threat_score, save_text_report, save_json_report

init(autoreset=True)

MODEL_PATH = "model/log_model.pkl"
ENCODER_PATH = "model/label_encoder.pkl"

class LogAnalyzer:
    def __init__(self):
        if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODER_PATH):
            raise FileNotFoundError("Model files not found. Run 'python3 train_model.py' first.")
        self.model = joblib.load(MODEL_PATH)
        self.label_encoder = joblib.load(ENCODER_PATH)

    def analyze_logs(self, log_file_path, brute_force_threshold=3):
        if not os.path.exists(log_file_path):
            raise FileNotFoundError(f"Log file not found: {log_file_path}")

        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_logs = [line.strip() for line in f if line.strip()]

        if not raw_logs:
            raise ValueError("Log file is empty.")

        cleaned_logs = [clean_log(log) for log in raw_logs]
        predictions_encoded = self.model.predict(cleaned_logs)
        predictions = self.label_encoder.inverse_transform(predictions_encoded)

        probabilities = None
        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(cleaned_logs)

        results = []
        failed_login_counter = defaultdict(int)
        suspicious_ip_counter = Counter()

        for i, log_line in enumerate(raw_logs):
            pred = predictions[i]
            ip = extract_ip(log_line)
            confidence = max(probabilities[i]) if probabilities is not None else 0.0

            if pred in ["Failed Login", "Suspicious", "Critical", "Brute Force", "Malware Attempt"] and ip:
                suspicious_ip_counter[ip] += 1
            if pred == "Failed Login" and ip:
                failed_login_counter[ip] += 1

            results.append({
                "log": log_line,
                "prediction": pred,
                "confidence": float(confidence),
                "ip": ip
            })

        brute_force_ips = [ip for ip, count in failed_login_counter.items() if count >= brute_force_threshold]

        for item in results:
            if item["ip"] in brute_force_ips and item["prediction"] == "Failed Login":
                item["prediction"] = "Brute Force"

        final_predictions = [item["prediction"] for item in results]
        class_counts = Counter(final_predictions)
        threat_score = calculate_threat_score(final_predictions, brute_force_ips)

        summary = {
            "Total Logs Processed": len(raw_logs),
            "Normal": class_counts.get("Normal", 0),
            "Failed Login": class_counts.get("Failed Login", 0),
            "Brute Force": class_counts.get("Brute Force", 0),
            "Suspicious": class_counts.get("Suspicious", 0),
            "Critical": class_counts.get("Critical", 0),
            "Malware Attempt": class_counts.get("Malware Attempt", 0),
            "Threat Score (0-100)": threat_score,
            "Brute Force IPs": brute_force_ips,
            "Top Suspicious IPs": suspicious_ip_counter.most_common(5),
            "Failed Login Counts": dict(failed_login_counter)
        }

        recommendations = self.generate_recommendations(summary)
        return summary, results, recommendations

    def generate_recommendations(self, summary):
        recommendations = []
        if summary["Brute Force"] > 0:
            recommendations += [
                "Enable fail2ban or account lockout policies to block brute-force attempts.",
                "Review SSH access and restrict root login."
            ]
        if summary["Malware Attempt"] > 0:
            recommendations += [
                "Investigate suspicious commands and scan the affected host for malware.",
                "Review executed shell commands and recent downloaded files."
            ]
        if summary["Critical"] > 0:
            recommendations += [
                "Check service failures and critical errors immediately.",
                "Review system logs for crashes, kernel issues, or service interruptions."
            ]
        if summary["Suspicious"] > 0:
            recommendations += [
                "Inspect suspicious IP addresses and web requests for scanning or exploitation attempts.",
                "Consider adding WAF/firewall rules or IDS signatures."
            ]
        if summary["Threat Score (0-100)"] >= 70:
            recommendations.append("High threat level detected. Escalate to security team immediately.")
        if not recommendations:
            recommendations.append("System appears stable. Continue regular monitoring and patching.")
        return recommendations

    def print_results(self, summary, results):
        print("\n" + "=" * 70)
        print(" AI POWERED LOGS ANALYZER - RESULTS ")
        print("=" * 70)

        for item in results:
            pred, log_line, conf = item["prediction"], item["log"], item["confidence"]
            color = Fore.WHITE
            if pred == "Normal":
                color = Fore.GREEN
            elif pred == "Failed Login":
                color = Fore.YELLOW
            elif pred == "Brute Force":
                color = Fore.RED
            elif pred == "Suspicious":
                color = Fore.MAGENTA
            elif pred == "Critical":
                color = Fore.RED
            elif pred == "Malware Attempt":
                color = Fore.LIGHTRED_EX
            print(f"{color}[{pred}] ({conf:.2f}) {log_line}{Style.RESET_ALL}")

        print("\n" + "=" * 70)
        print(" SUMMARY ")
        print("=" * 70)
        for key, value in summary.items():
            print(f"{key}: {value}")

    def save_reports(self, summary, results, recommendations):
        os.makedirs("reports", exist_ok=True)
        text_report = "reports/analysis_report.txt"
        json_report = "reports/analysis_report.json"
        save_text_report(text_report, summary, results, recommendations)
        save_json_report(json_report, summary, results, recommendations)
        print(f"\n[+] Text report saved to: {text_report}")
        print(f"[+] JSON report saved to: {json_report}")
