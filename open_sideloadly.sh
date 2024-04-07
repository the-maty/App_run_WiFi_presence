#!/bin/bash

# Function to check if a process is running
is_app_running() {
    pgrep -x "$1" >/dev/null
}

# Check if both "Sideloadly" and "sideloadly-daemon" are not running
if ! is_app_running "Sideloadly" && ! is_app_running "sideloadly-daemon"; then
    # If the app and its daemon are not already running, open it
    echo "Connected to $connected_ssid, OPENING APP..."
    open -a "Sideloadly"  # Replace "Sideloadly" with the name of the application
else
    # If the app or its daemon is already running, notify
    echo "The application or its daemon is already running."
fi
