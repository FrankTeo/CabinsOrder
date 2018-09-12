class Order(object):
	weekNo = 0
	bookingCode = ""

	"""docstring for Order"""
	def __init__(self, weekNo, bookingCode = ""):
		super(Order, self).__init__()
		self.weekNo = weekNo
		self.bookingCode = bookingCode

	def Show(self):
		print("weekNo = [%s], bookingCode = [%s]" % (self.weekNo, self.bookingCode))