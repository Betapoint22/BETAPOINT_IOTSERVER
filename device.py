class Device(object):
	"""docstring for Device"""
	def __init__(self, device_id, device_name, device_type, device_metadata, device_state):
		super(Device, self).__init__()
		self.device_id = device_id
		self.device_name = device_name
		self.device_type = device_name
		self.device_metadata = device_metadata
		self.device_state = device_state
		print("Success in creating device")
		print("....***....")
	def device_details(self):
		print("Device Name {}".format(self.device_name))
		print("Device ID {}".format(self.device_id))
		print("Device Type {}".format(self.device_type))
		print("Device Metadata {}".format(self.device_metadata))
		print("Device State {}".format(self.device_state))
		