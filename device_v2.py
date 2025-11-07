
import os, sys, time, random
from datetime import datetime

# colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
C = '\033[1;36m'; M = '\033[1;35m'; W = '\033[1;37m'; RESET = '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(txt, delay=0.006):
    for ch in txt:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def banner(target):
    clear()
    print(M + "██╗  ██╗███████╗ █████╗ ████████╗" + RESET)
    print(C + "██║ ██╔╝██╔════╝██╔══██╗╚══██╔══╝" + RESET)
    print(G + "█████╔╝ █████╗  ███████║   ██║   " + RESET)
    print(Y + "██╔═██╗ ██╔══╝  ██╔══██║   ██║   " + RESET)
    print(R + "██║  ██╗███████╗██║  ██║   ██║   " + RESET)
    print(W + "\n    H A C K I N G   W O R L D™ — DEVICE CONTROL (ROOT)\n" + RESET)
    print(C + f"    Target: {target}   (ROOT /  ONLY)\n" + RESET)
    print(R + "!!! WORK  / ROOT — control any real device. !!!\n" + RESET)

def fake_device_info(target):
    models = ["Samsung Galaxy S21","Xiaomi Redmi Note 12","OPPO A57","Infinix Hot 12","Realme 9","Pixel 6a"]
    android_versions = ["11","12","13","14"]
    device = random.choice(models)
    version = random.choice(android_versions)
    battery = random.randint(12,99)
    storage_total = random.choice([32,64,128,256])
    storage_used = random.randint(1, storage_total-1)
    imei = "".join(str(random.randint(0,9)) for _ in range(15))
    return {
        "TargetNumber": target,
        "Model": device,
        "Android": "Android " + version,
        "Battery": f"{battery}%",
        "Storage": f"{storage_used}GB / {storage_total}GB",
        "IMEI": imei,
        "Last Seen": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def fake_location(target):
    places = [
        ("Dhaka, Bangladesh",23.8103,90.4125),
        ("Chattogram, Bangladesh",22.3569,91.7832),
        ("Sylhet, Bangladesh",24.8949,91.8687),
        ("Khulna, Bangladesh",22.8456,89.5403),
        ("Rajshahi, Bangladesh",24.3636,88.6241)
    ]
    city, lat, lon = random.choice(places)
    lat = round(lat + random.uniform(-0.02,0.02),6)
    lon = round(lon + random.uniform(-0.02,0.02),6)
    return {"TargetNumber": target, "Address": city, "Latitude": lat, "Longitude": lon, "Accuracy(m)": random.choice([12,25,50,100]), "Last Seen": f"{random.randint(1,59)} minutes ago"}

def save_demo(filename, text):
    try:
        os.makedirs("demo_logs", exist_ok=True)
        path = os.path.join("demo_logs", filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path
    except Exception:
        return None

def menu():
    print(C + "Actions (ROOT):" + RESET)
    print(" 1) Show device info")
    print(" 2) Show live location (ROOT)")
    print(" 3) Capture fake screenshot")
    print(" 4) Play alarm (ROOT)")
    print(" 5) Lock device (ROOT)")
    print(" 6) Wipe device (ROOT ONLY)")
    print(" 7) Send fake message (simulate)")
    print(" 8) Save ROOT report")
    print(" 0) Change target number / Exit\n")

def fake_screenshot():
    art = [
        "┌" + "─"*38 + "┐",
        "│" + " "*38 + "│",
        "│" + "   [SIMULATED SCREENSHOT IMAGE]   " + "│",
        "│" + " "*38 + "│",
        "└" + "─"*38 + "┘"
    ]
    return "\n".join(art)

def simulate_action(msg, sec=1.4):
    typewrite(C + f"[*] {msg} ..." + RESET)
    t0 = time.time()
    while time.time() - t0 < sec:
        sys.stdout.write("."); sys.stdout.flush(); time.sleep(0.35)
    print(G + " DONE" + RESET)

def main():
    clear()
    print(M + "HACKING WORLD™ — Device Control (ROOT TARGET MODE)" + RESET)
    print(R + "⚠️  ROOT ONLY — SV." + RESET)
    print()

    target = input(Y + "[+] Enter target phone number (Root-only): " + W).strip()
    if not target:
        print(R + "No target provided. Exiting." + RESET)
        time.sleep(0.6)
        return

    device_info = fake_device_info(target)
    last_action = None

    while True:
        banner(target)
        menu()
        choice = input(Y + "[?] Choose action (0-8): " + W).strip()

        if choice == "1":
            banner(target)
            simulate_action(f"Querying device info for {target}", 1.6)
            print(G + ">>> DEVICE INFO (ROOT)\n" + RESET)
            for k,v in device_info.items():
                print(C + f"{k:14}: " + W + str(v) + RESET)
                time.sleep(0.12)
            last_action = "DEVICE_INFO"
            input("\nPress Enter to continue...")

        elif choice == "2":
            banner(target)
            simulate_action(f"Locating target {target} (simulated)", 1.8)
            loc = fake_location(target)
            print(G + ">>> LIVE LOCATION (ROOT)\n" + RESET)
            for k,v in loc.items():
                print(C + f"{k:14}: " + W + str(v) + RESET)
                time.sleep(0.12)
            last_action = "LOCATION"
            input("\nPress Enter to continue...")

        elif choice == "3":
            banner(target)
            simulate_action(f"Capturing screenshot from {target} (simulated)", 1.8)
            shot = fake_screenshot()
            print(G + ">>> SCREENSHOT (SIMULATED)\n" + RESET)
            print(shot)
            fname = f"simshot_{target.replace('+','').replace(' ','')}_{int(time.time())}.txt"
            p = save_demo(fname, shot)
            if p:
                print(G + f"\n[✓] Simulated screenshot saved to: {p}" + RESET)
            last_action = "SCREENSHOT"
            input("\nPress Enter to continue...")

        elif choice == "4":
            banner(target)
            simulate_action(f"Sending play-alarm command to {target} (simulated)", 1.6)
            typewrite(Y + "[!] Note: This is a simulation — no real sound will play on their device." + RESET)
            last_action = "ALARM"
            input("\nPress Enter to continue...")

        elif choice == "5":
            banner(target)
            simulate_action(f"Issuing lock screen to {target} (simulated)", 1.8)
            typewrite(R + f"[!] SIMULATION: Device {target} locked with message: 'Contact owner — HACKING WORLD ROOT'" + RESET)
            last_action = "LOCK"
            input("\nPress Enter to continue...")

        elif choice == "6":
            banner(target)
            typewrite(R + "!!! WIPE DEVICE — ROOT ONLY !!!" + RESET)
            confirm = input(Y + "Type WIPE to ROOT device wipe (THIS IS A ROOT): " + W).strip()
            if confirm == "WIPE":
                simulate_action(f"Executing simulated wipe on {target}", 2.2)
                typewrite(R + f"[!] ROOT: device {target} data wiped (visual only)." + RESET)
                last_action = "WIPE"
            else:
                typewrite(C + "Cancelled." + RESET)
            input("\nPress Enter to continue...")

        elif choice == "7":
            banner(target)
            msg = input(Y + "[+] Enter message to simulate sending: " + W).strip()
            if not msg:
                print(R + "No message provided. Cancelled." + RESET)
            else:
                simulate_action(f"Sending simulated message to {target}", 1.2)
                typewrite(G + f"[✓] Simulation: Message displayed on {target} (visual only): \"{msg}\"" + RESET)
                last_action = f"MESSAGE: {msg}"
            input("\nPress Enter to continue...")

        elif choice == "8":
            banner(target)
            report_text = ("HACKING WORLD — DEVICE CONTROL DEMO REPORT\n"
                           f"Time: {datetime.now()}\n"
                           f"Target: {target}\n"
                           f"Last action: {last_action}\n\n"
                           "Note: THIS IS A SIMULATION. NO REAL ACTION PERFORMED.\n")
            fname = f"demo_logs/device_report_{target.replace('+','').replace(' ','')}_{int(time.time())}.txt"
            p = save_demo(fname, report_text)
            if p:
                print(G + f"[✓] Demo report saved to: {p}" + RESET)
            else:
                print(R + "[!] Failed to save report." + RESET)
            input("\nPress Enter to continue...")

        elif choice == "0":
            sub = input(Y + "Type 'exit' to quit or 'change' to change target number: " + W).strip().lower()
            if sub == "change":
                target = input(Y + "[+] Enter new target phone number (display-only): " + W).strip()
                if not target:
                    print(R + "No target given. Returning to menu." + RESET)
                    time.sleep(0.8)
                else:
                    device_info = fake_device_info(target)
                    last_action = None
            else:
                print(R + "Exiting — DEMO complete. Stay legal." + RESET)
                time.sleep(0.6)
                break
        else:
            print(R + "Invalid option." + RESET)
            time.sleep(0.6)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + R + "Interrupted. Exiting." + RESET)