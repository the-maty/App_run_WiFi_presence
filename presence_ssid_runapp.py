import time
import subprocess

wifi_ssid = "YOUR-WIFI-SSID"
previous_ssid = None

def is_app_running(app_name):
    # Check if the application is running
    result = subprocess.run(["pgrep", "-x", app_name], capture_output=True, text=True)
    return len(result.stdout.strip()) > 0

def check_wifi():
    global previous_ssid
    # Check if connected to Wi-Fi SSID
    ssid_info = subprocess.run(["networksetup", "-getairportnetwork", "en0"], capture_output=True, text=True)
    if ": " in ssid_info.stdout:
        connected_ssid = ssid_info.stdout.split(": ")[1].strip()

        if connected_ssid == wifi_ssid:
            if connected_ssid == previous_ssid:
                # Run your first command here
                print(f"Still connected to {connected_ssid}, SKIPPING COMMANDS...")
            else:
                if not is_app_running("Sideloadly") and not is_app_running("sideloadly-daemon"):
                    # If the app and its daemon are not already running, open it
                    print(f"Connected to {connected_ssid}, OPENING APP...")
                    subprocess.run(["open", "-a", "Sideloadly"])  # Replace "Sideloadly" with the name of the application
                else:
                    # If the app or its daemon is already running, notify // ADD pass to bypass no print
                    print("The application or its daemon is already running.")

                # Update previous_ssid
                previous_ssid = connected_ssid
        else:
            # Reset previous_ssid since we are not connected to the desired SSID
            previous_ssid = None
            print(f"Not connected to {wifi_ssid}, doing nothing...")
    else:
        print("Not connected to any network.")

def main():
    global previous_ssid
    while True:
        check_wifi()
        time.sleep(60)

if __name__ == "__main__":
    main()
