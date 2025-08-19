# log_analyzer.py
# Author: Graywolf0
# 📌 Educational Project - For Portfolio Use

import re

def analyze_log(file_path):
    failed_logins = {}

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                # Örn: "Failed password for invalid user root from 192.168.1.10 port 22"
                match = re.search(r"Failed password.*from ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", line)
                if match:
                    ip = match.group(1)
                    failed_logins[ip] = failed_logins.get(ip, 0) + 1
    except FileNotFoundError:
        print("⚠️ Log file not found.")
        return

    print("\n🔍 Failed Login Attempts Report:\n")
    if not failed_logins:
        print("✅ No failed login attempts found.")
    else:
        for ip, count in failed_logins.items():
            print(f"❌ {ip} => {count} failed attempts")


if __name__ == "__main__":
    print("🔐 Log Analyzer 🔐")
    log_file = input("Enter path to log file: ")
    analyze_log(log_file)
