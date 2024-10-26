class User:
    def __init__(self, user_id, username, password, role,region):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.region = region

        self.devices = []

    def authenticate(self, username, password):
        # Implement authentication logic
        if username == self.username and password == self.password:
            return True
        else:
            return False

    def add_device(self, device):
        self.devices.append(device)

    def remove_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                self.devices.remove(device)

    def view_device_data(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                # Retrieve and display device data
                print(device.name, device.status)

    def control_device(self, device_id, command):
        for device in self.devices:
            if device.device_id == device_id:
                device.receive_command(command)