from relay.main import Main as m

def close():
	com_signal = m.com
	if com_signal == 1:
		return True # It should always be 1 else NO is activated