# python fast host discovery
import colors as c
import os
import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime


active_hosts = []

def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-w", "1", str(ip)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if "ttl" in result.stdout.lower():
            return str(ip)

    except Exception:
        return None


def main():
    os.system("clear")

    print(c.green() + "================================================")
    print(c.light_blue() + "=           FAST HOST DISCOVERY SCANNER        =")
    print(c.green() + "================================================")
    print("Enter subnet (example: 192.168.1.0/24)\n")

    while True:
        try:
            subnet = input(": ")
            network = ipaddress.ip_network(subnet, strict=False)
            break
        except ValueError:
            print("Invalid subnet. Try again.")

    max_scan = int(input("Enter max hosts to scan: "))

    print("\nScanning...\n")

    counter = 0
    futures = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        for ip in network.hosts():
            if counter >= max_scan:
                break

            futures.append(executor.submit(ping_host, ip))
            counter += 1

        for future in as_completed(futures):
            result = future.result()
            os.system("clear")

            if result:
                active_hosts.append(result)

    print("\nScan Completed.")
    print("================================================")
    print("=                  SCAN REPORT                 =")
    print("================================================")
    print(f"Scan Time: {datetime.now()}")
    print(f"Total Hosts Scanned: {counter}")
    print(f"Active Hosts Found: {len(active_hosts)}\n")

    for host in active_hosts:
        print(f"[+] {host} is UP")


if __name__ == "__main__":
    main()
