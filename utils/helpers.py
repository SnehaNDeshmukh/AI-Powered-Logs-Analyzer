import re
import json
from datetime import datetime

def extract_ip(log_line):
    match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', log_line)
    return match.group(0) if match else None

def clean_log(log_line):
    log_line = log_line.lower()
    log_line = re.sub(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', 'IPADDR', log_line)
    log_line = re.sub(r'\d+', 'NUM', log_line)
    log_line = re.sub(r'[^a-zA-Z\s_]', ' ', log_line)
    log_line = re.sub(r'\s+', ' ', log_line).strip()
    return log_line

def calculate_threat_score(predictions, brute_force_ips):
    score = 0
    weights = {
        "Normal": 0,
        "Failed Login": 3,
        "Suspicious": 7,
        "Critical": 10,
        "Brute Force": 15,
        "Malware Attempt": 20
    }
    for pred in predictions:
        score += weights.get(pred, 2)
    score += len(brute_force_ips) * 15
    return min(score, 100)

def save_text_report(report_path, summary, results, recommendations):
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("AI POWERED LOGS ANALYZER - SECURITY REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"Generated At: {datetime.now()}\n\n")
        f.write("SUMMARY\n")
        f.write("-" * 60 + "\n")
        for key, value in summary.items():
            f.write(f"{key}: {value}\n")
        f.write("\nDETAILED RESULTS\n")
        f.write("-" * 60 + "\n")
        for item in results:
            f.write(f"[{item['prediction']}] (Confidence: {item['confidence']:.2f}) {item['log']}\n")
        f.write("\nRECOMMENDATIONS\n")
        f.write("-" * 60 + "\n")
        for rec in recommendations:
            f.write(f"- {rec}\n")

def save_json_report(report_path, summary, results, recommendations):
    report_data = {
        "generated_at": str(datetime.now()),
        "summary": summary,
        "results": results,
        "recommendations": recommendations
    }
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4)
