# Author: Mahtab Zilaie
# Date: 10/3/2019
# Description:  asks the user for a integer (0 to 99 cents) then send
# out fewest number for coins needed

cent = int(input('Please enter an amount in cents less than a dollar.'))
print(cent)
quarter = int(cent/25)
rem_q = int(cent%25)
dime = int(rem_q/10)
rem_d = int(rem_q%10)
nickel = int(rem_d/5)
rem_n = int(rem_d%5)
penny = int(rem_n/1)
print('Your change will be:')
print('Q:', quarter)
print('D:', dime)
print('N:', nickel)
print('P:', penny)