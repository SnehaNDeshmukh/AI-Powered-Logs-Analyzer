# 🔐 AI Powered Logs Analyzer

## 📌 Project Overview

**AI Powered Logs Analyzer** is a terminal-based cybersecurity project built using Python on Kali Linux.
It leverages Machine Learning to intelligently analyze system, application, and security logs to detect suspicious activities, anomalies, and potential cyber threats.

Unlike traditional rule-based log analyzers, this project uses a **custom-trained AI/ML model** to classify log events into meaningful security categories.

---

## 🎯 Objective

To build a **fully functional cybersecurity tool** that:

* Detects threats from logs in real-time
* Classifies logs using Machine Learning
* Identifies brute-force attacks and suspicious patterns
* Generates detailed analysis reports

---

## 🚀 Features

* ✅ Terminal-based (Kali Linux compatible)
* ✅ AI/ML-powered log classification (not just regex)
* ✅ Detects:

  * Failed logins
  * Brute-force attacks
  * Suspicious IP activity
  * Malware/Exploit attempts
  * System warnings & critical errors
* ✅ Categories:

  * Normal
  * Warning
  * Critical
  * Suspicious
  * Failed Login
  * Brute Force
  * Malware/Exploit Attempt
* ✅ Highlights critical logs with colors
* ✅ Tracks attacker IPs
* ✅ Generates reports (TXT/JSON)
* ✅ Beginner-friendly & professional structure

---

## 🛠️ Technologies Used

* Python 3
* scikit-learn
* pandas
* numpy
* joblib
* colorama

---

## 📂 Project Structure

```
AI_Powered_Logs_Analyzer/
├── main.py
├── train_model.py
├── analyzer.py
├── model/
│   └── log_model.pkl
├── logs/
│   └── sample_logs.log
├── data/
│   └── training_logs.csv
├── utils/
│   └── helpers.py
├── reports/
│   └── analysis_report.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup (Kali Linux)

### 1. Create Project Directory

```bash
mkdir AI_Powered_Logs_Analyzer
cd AI_Powered_Logs_Analyzer
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Environment

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the AI Model

```bash
python3 train_model.py
```

This will:

* Train ML model on log dataset
* Save model to `/model/log_model.pkl`

---

## 🔍 Run Log Analyzer

```bash
python3 main.py logs/sample_logs.log
```

---

## 📊 Sample Output

```
========================================
 AI POWERED LOG ANALYZER
========================================

[CRITICAL] Failed password for root from 192.168.1.10
[SUSPICIOUS] SQL Injection attempt detected
[NORMAL] User login successful

----------------------------------------
Total Logs Processed: 50
Normal: 20
Failed Login: 10
Suspicious: 8
Critical: 5

⚠️ Brute Force Detected from:
- 192.168.1.10 (7 attempts)

Top Attacker IPs:
- 192.168.1.10
- 10.0.0.5
```

---

## 📄 Report Generation

Reports are saved in:

```
reports/analysis_report.txt
```

Includes:

* Timestamp
* Total logs analyzed
* Classification results
* Suspicious IPs
* Brute-force detection
* Security recommendations

---

## 🧪 Dataset

### Training Data

Located at:

```
data/training_logs.csv
```

Contains labeled logs for ML training.

### Test Logs

Located at:

```
logs/sample_logs.log
```

Used to test analyzer.

---

## ⚠️ Important Notes

* Ensure Python 3 is installed
* Always activate virtual environment before running
* Do not upload sensitive logs to public repositories
* Add `.gitignore` for security

---

## 🔮 Future Enhancements

* Real-time log monitoring
* Integration with SIEM tools
* Deep Learning models (LSTM/NLP)
* Web dashboard (Streamlit)
* Email/SMS alerts
* Threat intelligence API integration

---

## 👩‍💻 Author

**Sneha Deshmukh**
Cybersecurity Enthusiast  🚀

---
