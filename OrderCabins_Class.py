from Cabin_Class import *
import os

class OrderCabins(object):
	cabins = []

	availablePeriod = tuple(range(23, 39 + 1))
	peakPeriod = tuple(range(27, 35 + 1))

	"""docstring for OrderCabins"""
	def __init__(self):
		super(OrderCabins, self).__init__()
		self.cabins.append(Cabin(1,	"Hetty", 				4, 	400, 	250))
		self.cabins.append(Cabin(2,	"Poppy", 				4, 	400, 	250))
		self.cabins.append(Cabin(3,	"Blue Skies", 			4, 	500, 	350))
		self.cabins.append(Cabin(4,	"Bay View", 			6, 	650, 	500))
		self.cabins.append(Cabin(5,	"Happy Days", 			6, 	695, 	550))
		self.cabins.append(Cabin(6,	"Summer Joy", 			6, 	800, 	600))
		self.cabins.append(Cabin(7,	"Walkers' Rest", 		8, 	950, 	750))
		self.cabins.append(Cabin(8,	"Nertie", 				8, 	1050, 	850))
		self.cabins.append(Cabin(9,	"Green Forest Lodge", 	10, 1200, 	950))
		self.cabins.append(Cabin(10,"Coppice Lodge", 		10, 1500, 	1150))

	def ValidateCabinNo(self, cabinNo):
		if (not str.isdigit(cabinNo)):
			print("\n\t\tcabin number has to be a number (1 ~ %d)\n" % len(self.cabins))
			return False

		cabinNo = int(cabinNo)
		if(cabinNo not in range(1, len(self.cabins) + 1)):
			print("\n\t\tcabin number has to be between 1 to %d\n" % len(self.cabins))
			return False

		return True

	def ValidateStartWeek(self, startWeek):
		if(not str.isdigit(startWeek)):
			print("\n\t\tError:Start week has to be a number\n")
			return False

		if(int(startWeek) not in self.availablePeriod):
			print("\n\t\tStart Week not in avalilable period from week %d to week %d \n" % (self.availablePeriod[0], self.availablePeriod[-1]))
			return False

		return True

	def ValidateStayWeeks(self, stayWeeks, startWeek):
		if(not str.isdigit(stayWeeks)):
			print("\n\t\tStay weeks has to be a number\n")
			return False

		if(int(stayWeeks) <= 0):
			print("\n\t\tWeeks you want to stay should be great than 0")
			return False

		if(int(startWeek) + int(stayWeeks) - 1 not in self.availablePeriod):
			print("\n\t\tWeeks you want to stay are not available")
			print("\t\tAccording the week you want to start, stay weeks [1, %d] could be chosen\n" % (self.availablePeriod[-1] - int(startWeek) + 1))
			return False

		return True

	def ShowStatus(self):
		while(True):
			cabinNo = input("\n\t\tPlease input cabin No you want to check or input 'R/r' to return: ")
			if(cabinNo == 'r' or cabinNo == 'R'):
				return

			if(not self.ValidateCabinNo(cabinNo)):
				continue
			
			print("")
			self.cabins[int(cabinNo) - 1].Show(self.availablePeriod)
			print("")

	def ShowAllStatus(self):
		for cabin in self.cabins:
			cabin.Show(self.availablePeriod)
		cabinNo = input("\n\t\tPress any key to return: ")

	def Booking(self):
		cabinNo = input("\t\tPlease input cabin's No.: ")
		if(not self.ValidateCabinNo(cabinNo)):
			return

		startWeek = input("\t\tPlease input week No. you want to start: ")
		if(not self.ValidateStartWeek(startWeek)):
			return

		stayWeeks = input("\t\tPlease input how many weeks you want to stay: ")
		if(not self.ValidateStayWeeks(stayWeeks, startWeek)):
			return

		for cabin in self.cabins:
			if(int(cabinNo) == cabin.no):
				cost = [0.00, 0.00]
				if(cabin.AddOrder(int(startWeek), int(stayWeeks))):
					cabin.CalculateCost(int(startWeek), int(stayWeeks), self.peakPeriod, cost)
				break;

def main():
	oc = OrderCabins()

	while(True):
		
		print("\t\t\t%s" % (40 * '='))
		print("\t\t\t1 => Cabins booking status")
		print("\t\t\t2 => List all cabins and status")
		print("\t\t\tC => Clean Screen")
		print("\t\t\tB => Booking cabin")
		print("\t\t\tQ => Quit Program")
		print("")
		print("\t\t\t%s" % (40 * '='))
		print("")

		ipt = input("\t\tPlease input choose an option: ")

		if(ipt == "1"):
			oc.ShowStatus()
		elif(ipt == "2"):
			oc.ShowAllStatus()
		elif(ipt == "C" or ipt == "c"):
			os.system("cls")
		elif(ipt == "B" or ipt == "b"):
			oc.Booking()
		elif(ipt == "q" or ipt == "Q"):
			break;
		else:
			print("\nUnexpected input: %s\n" % ipt)

	exit(0)

if __name__ == '__main__':
	main()