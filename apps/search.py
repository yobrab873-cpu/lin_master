# search.py
import requests
import os
from colorama import Fore, init

init(autoreset=True)

def lin_dict():
    while True:
        os.system("clear")
        os.system("figlet Lin_Dict")

        print(Fore.YELLOW + "[ Type 'exit' to go back ]\n")

        query = input(Fore.CYAN + "Search: ").strip()

        # Exit condition
        if query.lower() in ["exit", "quit", "back"]:
            print(Fore.RED + "\n[!] Exiting dictionary...\n")
            break

        # Empty input check
        if not query:
            print(Fore.RED + "❌ Empty search query")
            input("\nPress Enter to continue...")
            continue

        # Format query for URL
        query_url = query.replace(" ", "%20")

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query_url}"
        headers = {"User-Agent": "LinMaster/1.0"}

        print(Fore.GREEN + f"\n[+] Searching for: {query}...\n")

        try:
            res = requests.get(url, headers=headers, timeout=5)

            if res.status_code == 200:
                try:
                    data = res.json()
                    result = data.get("extract", "No summary found")

                    print(Fore.WHITE + result)

                    # Save to report
                    os.makedirs("reports", exist_ok=True)
                    with open("reports/dictionary.txt", "a") as f:
                        f.write(f"\n=== {query} ===\n{result}\n")

                    print(Fore.GREEN + "\n[✓] Saved to reports/dictionary.txt")

                except Exception:
                    print(Fore.RED + "❌ Failed to parse JSON")
                    print(res.text)

            else:
                print(Fore.RED + f"❌ Failed (status: {res.status_code})")


        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"❌ Network error: {e}")
            print(Fore.RED + "Please connect to the internet and try again")

        input(Fore.YELLOW + "\nPress Enter to search again...")

if __name__ == "__main__":
    lin_dict()
