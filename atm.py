class ATM():
	def __init__(self,balance,bank_name):
		self.balance = balance
		self.bank_name = bank_name
		self.withdrawl_list = []

	def withdraw(self,a):
		if a <= self.balance:
			print 'Welcome To : ' + self.bank_name
			print 'Current Balance : ' + str(self.balance)
			print '================================='
			self.withdrawl_list.append(a)
			while a > 0:
				if a >= 100:
					print 'give 100'
					a -= 100
				elif a >= 50:
					print 'give 50'
					a -= 50
				elif a >= 20:
					print 'give 20'
					a -= 20
				elif a >= 10:
					print 'give 10'
					a -= 10
				elif a >= 5:
					print 'give 5'
					a -= 5
				elif a < 5:
					print 'give 1'
					a -= 1
		else:
			self.withdrawl_list.append(a)
			print 'Welcome to : ' + self.bank_name
			print '================================='
			print "NO SUFFICIENT FUNDS"

	def show_withdraw(self):
		for amount in self.withdrawl_list:
			print amount