investment,interest = input("Enter investment and expected intrest:").split()
investment = float(investment)
interest = float(interest) * .01
for i in range(10):
    investment = investment + (investment * interest)
print("invetment after 10 years is {:.2f}".format(investment))
