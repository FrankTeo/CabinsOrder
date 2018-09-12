import datetime
from Order_Class import *

class Cabin(object):
	no = 0
	name = ""
	capacity = 0
	peakPrice = 0
	offPeakPrice = 0

	orders = list()

	"""docstring for Cabin"""
	def __init__(self, no, name, capacity, peakPrice, offPeakPrice):
		super(Cabin, self).__init__()
		self.no = no
		self.name = name
		self.capacity = capacity
		self.peakPrice = peakPrice
		self.offPeakPrice = offPeakPrice
		self.orders = []

	def IsAvailable(self, weekNo):
		for order in self.orders:
			if order.weekNo == weekNo:
				return False

		return True

	def GenerateBookingCode(self, startWeek):
		return "%02d"%self.no + "%02d"%startWeek + datetime.datetime.now().strftime('%Y%m%d%H%M%S')

	def AddOrder(self, startWeek, weekNumber):
		BookingCode = self.GenerateBookingCode(startWeek)

		newOrders = []

		for loop in range(0, weekNumber):
			order = Order(startWeek + loop, BookingCode)
			if(self.IsAvailable(order.weekNo)):
				newOrders.append(order)
			else:
				print("\n\t\tWeek %d in this order has been taken, please choose others week\n" % (startWeek + loop))
				return False

		self.orders += newOrders
		return True

	def CalculateCost(self, startWeek, weekNumber, peakPeriod, cost):
		for loop in range(startWeek, startWeek + weekNumber):
			if(loop not in peakPeriod):
				cost[0] += self.offPeakPrice
			else:
				cost[0] += self.peakPrice

		if(weekNumber >= 3):
			cost[1] = cost[0] * (1 - 0.1)
		else:
			cost[1] = cost[0]

		print("\n\t\tYour cost is %.2lf " % cost[0], end='')

		if(cost[0] != cost[1]):
			print(", you got 10 percent discount and final cost is %.2lf\n" % cost[1])

		print()

	def ShowBase(self):
		print("* %4s%20s%15s%20s%20s" % ("No.", "Cabin Name", "Capacity", "Price in Peak", "Price in Non-Peak" ))
		print("%s%s" % (' '*2, '-'*(4 + 20 + 15 + 20 + 20)))
		print("  %4s%20s%15s%20s%20s" % (self.no, self.name, self.capacity, self.peakPrice, self.offPeakPrice))

		print("")
		print("%s%s" % (' '*2, '-'*(4 + 20 + 15 + 20 + 20)))

	def GetAvailable(self, availablePeriod, outPuts = []):
		for loop in availablePeriod:
			if(self.IsAvailable(loop)):
				outPuts.append(loop)

	def GetOrdered(self, availablePeriod, outPuts = []):
		for loop in availablePeriod:
			if(not self.IsAvailable(loop)):
				outPuts.append(loop)

	def Show(self, availablePeriod):
		self.ShowBase()

		availableList = []
		self.GetAvailable(availablePeriod, availableList)

		if(len(availableList) > 0):
			print("  => Available Week(s): [", end = '')
			for item in availableList:
				print("%d" % item, end = ', ')

			print("]")
		else:
			print("  => Available: None")

		orderedList = []
		self.GetOrdered(availablePeriod, orderedList)
		if(len(orderedList) > 0):
			print("  => Ordered Week(s): [", end = '')
			for item in orderedList:
				print("%d" % item, end = ', ')

			print("]")
		else:
			print("  => Ordered: None")

		print("\n")

	def ShowOrders(self):
		for order in orders:
			print("weekNo = [%s], bookingCode = [%s]" % (order.weekNo, order.bookingCode))