import subprocess
import datetime
import os

def run_nslookup(domain):
    try:
        result = subprocess.run(['nslookup', domain], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

def main():
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    log_file = f"logs/dns_log_{timestamp}.txt"

    with open("domains.txt", "r") as f:
        domains = [line.strip() for line in f if line.strip()]

    with open(log_file, "w") as log:
        for domain in domains:
            output = run_nslookup(domain)
            log.write(f"=== {domain} ===\n{output}\n\n")

if __name__ == "__main__":
    main()
