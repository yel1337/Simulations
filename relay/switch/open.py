from relay.main import Main as m

def open():
	com_signal = m.com
	if com_signal == 0:
		return False # It should always be 0 else NC is activated