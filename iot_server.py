import subprocess

def check_mosquitto():
    """Checks if Mosquitto MQTT broker is running."""
    result = subprocess.run(["systemctl", "status", "mosquitto"], capture_output=True)
    if "active (running)" in result.stdout.decode():
        print("Mosquitto MQTT broker is running.")
    else:
        print("Mosquitto MQTT broker is not running.")

def check_internet_connection():
    """Checks internet connectivity."""
    result = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True)
    if result.returncode == 0:
        print("Internet connection is available.")
    else:
        print("Internet connection is not available.")

if __name__ == "__main__":
    check_mosquitto()
    check_internet_connection()


    https://github.com/Betapoint22/BETAPOINT_IOTSERVER.git