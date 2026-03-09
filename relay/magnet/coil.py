from relay.main import CurrentException 

class ElectroMagnet(): 
	def __init__ (self, v, r):
		self.v_value = v
		self.r_value = r

	def current_measurement(self):
		I = self.v_value / self.r_value
		
		try:
			if I > 1 and I != 0:
				return I
			else:
				raise CurrentException("amps shoudn't be equal to 0")
		except CurrentException as e:
			pass

	def gen_magnetic(self):
		current = self.current_measurement()
		if current:
			return True
		else:
			return False
