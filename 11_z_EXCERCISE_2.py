# Price of a house is $1m
# if buyer has good credit, put down 10%
# otherwise put down 20%
# Write a program to calculate down payment required

good_credit = True
price = 1000000
down_payment = interest = 0

if good_credit:
    interest = 10
else:
    interest = 20

down_payment = interest / 100 * price
down_payment = "{:,}".format(down_payment)
print(f'Down Payment required is ${down_payment}')
