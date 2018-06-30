# -*- coding: utf-8 -*-
"""
Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
"""
balance = 3926
annualInterestRate = 0.2
n = 12
monthly_interest = annualInterestRate/12
ans = round(monthly_interest / (1-(1+monthly_interest)**-n) * balance)
string = list(str(ans))

while ans % 10 != 0:
    if int(string[-1]) >= 5:
        ans += 1
    elif int(string[-1]) < 5:
        ans -= 1
print(ans)

        
    
    
