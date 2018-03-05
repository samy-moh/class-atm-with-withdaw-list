import atm
balance1 = 500
balance2 = 1000

atm1 = atm.ATM(balance1, "Smart Bank")
atm2 = atm.ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)