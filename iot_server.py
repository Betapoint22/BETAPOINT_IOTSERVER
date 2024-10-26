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
    result = subprocess.run(["ping", "-c", "10", "8.8.8.8"], capture_output=True)
    if result.returncode == 0:
        print("Internet connection is available.")
    else:
        print("Internet connection is not available.")

def register_user():
    print("Please Enter username below:")
    print('\n')
    name = str(input("Enter Name"))
    flag_name = 0
    while flag_name<=0:
        if name.isalpha():
            print("validated")
            flag_name = 2
        else:
            print("Not a valid name contain not alphabet character")
            name = input("Enter Name")
            flag_name = 0

if __name__ == "__main__":
    check_mosquitto()
    check_internet_connection()
    register_user()