# Auto Start App on Specified SSID Connection

This Python script allows you to automatically start an application when connected to a specific SSID (Wi-Fi network). The recommended way to run this script is via `nohup` at boot time.

## How it Works

The script continuously monitors the Wi-Fi connection and when it detects connection to the specified SSID, it triggers the application start process.

## Requirements

- Python 3.x
- `subprocess` module (for running shell commands)
- `time` module (for time-related functions)

## Usage

1. **Modify the Script**: Open the script file and modify the `SSID_TO_MONITOR` and `APPLICATION_COMMAND` variables according to your requirements. 
   
2. **Run via nohup**: You can run this script at boot time using `nohup` to ensure it runs in the background even after you log out of the terminal. Here's an example command:

   ```bash
   nohup python3 auto_start_app_on_ssid.py &
