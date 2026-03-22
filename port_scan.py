import subprocess
import os
from datetime import datetime

REPORT_DIR = "reports"
REPORT_FILE = f"{REPORT_DIR}/port_scan.txt"


def create_report_dir():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)


def save_report(data):
    with open(REPORT_FILE, "a") as f:
        f.write(data)
        f.write("\n" + "="*60 + "\n")


def run_scan(command):
    print(f"\n[+] Running: {' '.join(command)}\n")
    
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout + result.stderr
        print(output)

        save_report(output)

    except Exception as e:
        print(f"[!] Error: {e}")


def menu():
    print("""
======== PORT SCANNER MENU ========
1. Fast Scan (Top 100 ports)
2. TCP Connect Scan
3. SYN Scan (Stealth)
4. UDP Scan
5. All Ports Scan
6. Service Version Detection (-sV)
7. Aggressive Scan (-A)
8. Custom Scan (manual flags)
==================================
""")


def main():
    create_report_dir()

    target = input("Enter target (IP / domain / subnet / range): ")

    while True:
        menu()
        choice = input("Select option: ")

        timestamp = f"\nScan Time: {datetime.now()}\nTarget: {target}\n"
        save_report(timestamp)

        if choice == "1":
            run_scan(["nmap", "-F", target])

        elif choice == "2":
            run_scan(["nmap", "-sT", target])

        elif choice == "3":
            run_scan(["nmap", "-sS", target])

        elif choice == "4":
            run_scan(["nmap", "-sU", target])

        elif choice == "5":
            run_scan(["nmap", "-p-", target])

        elif choice == "6":
            run_scan(["nmap", "-sV", target])

        elif choice == "7":
            run_scan(["nmap", "-A", target])

        elif choice == "8":
            flags = input("Enter custom Nmap flags: ")
            cmd = ["nmap"] + flags.split() + [target]
            run_scan(cmd)

        else:
            print("[!] Invalid choice")

        again = input("\nRun another scan? (y/n): ").lower()
        if again != "y":
            print(f"\n[+] Report saved to {REPORT_FILE}")
            break


if __name__ == "__main__":
    main()
