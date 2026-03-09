from magnet.coil import ElectroMagnet as em
from switch.close import close as c
from switch.open  import open as o

class RelayException(Exception):
	# 0 if core is not connected with the armature
	# 2 if no current flow 
	def __init__(self, signal):
		self.signal = signal
		self.message = f""

		if self.signal == 0:
			self.message = f"CORE_ERR: NOT CONNECTED WITH ARMATURE "
		elif self.signal == 2:
			self.message = f"CORE_ERR: NO FLOW FROM THE COIL"
	
	def __str__(self):
		return self.message

class CurrentException(RelayException):
	pass
		 
class Main():
	def __init__(self, m, v, r, fc_value):
		self.v_value = v
		self.r_value = r
		self.magnetic = m
		self.attach = 0
		self.fc = fc_value

	# Once there is a positive magnetic field
	# the core of the coil must be attached
	# with the armature along with the
	# return spring
	def connect_core(self):
		if self.magnetic:
			self.attach = 1
		elif self.magnetic is False:
			self.attach = 0
	
	# fc is for NC and NO return value
	# com will depends either to
	# both fixed contact
	def com(self, fc):
		fc = self.fc
		c = 0
		if fc:
			return 1 # com connected to NC 
		else:
			return c # as 0 means com connected to NO
	
	def signal_output(com):
		if com == 1 and c is True:
			val = f"com_value is {com}, NORMALLY CLOSED"
			print(val)
		elif com == 0 and o is False:
			val = f"com_value is {com}, NORMALLY OPEN"

	def light(contact_status):
		# Light can only be turned on if a NC is closed
		# otherwise NO is triggered 
		if contact_status is 1:
			return True
		elif contact_status is 0:
			return False 

	def main(self):
		try:
			current = em(self.v_value, self.r_value).current_measurement()
			magnetic_field_val = em.gen_magnetic(current)
			if magnetic_field_val is False:
				raise CurrentException()
		except CurrentException as e:
			pass

		cc = self.connect_core()
		com_val = self.com(self.fc)
		if cc:
			if com_val is 1:
				self.signal_output(com_val)
		elif cc is False:
			raise RelayException(self.attach)
		
		if self.light(cc) is 0:
			print("no light")
		else:
			print("light on")

	if __name__ == "__main__":
		main()