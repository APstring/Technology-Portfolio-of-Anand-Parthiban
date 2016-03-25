def make_withdraw_protected(balance, password):
	def withdraw(amount, string):
		nonlocal balance
		nonlocal password
		k = 0
		k += 1
		if string == password:
			if amount > balance:
			   return 'Insufficient funds'
			
			else:
				balance = balance - amount
				return balance
			return withdraw
		else:
                    def wrong(p1, p2 , p3):
                        
