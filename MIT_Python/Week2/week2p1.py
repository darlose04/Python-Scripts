# -*- coding: utf-8 -*-
"""
Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
"""

'''def cc_balance(bal,r,mo):
    
    
    Returns the remaining balance on a credit card after one year.
    bal = original balance
    r = annual interest rate
    mo = monthly minimum payment rate
    min_pmt = minimum monthly payment
    unpd_bal = unpaid balance
    
    
    month = 0
    'min_pmt = bal * mo
    unpd_bal = bal - min_pmt
    interest = r / 12.0 * unpd_bal'
    
    while month in range(0,12):
        min_pmt = round((bal * mo),2)
        unpd_bal = round((bal - min_pmt),2)
        interest = round((r / 12.0 * unpd_bal),2)
        bal -= round((min_pmt - interest),2)
        month += 1
    return 'Remaining balance: {}'.format(round(bal,2))
    '''


balance = 5000
monthlyPaymentRate = 0.02
annualInterestRate = 0.18
month = 0
while month in range(0,12):
    min_pmt = round((balance * monthlyPaymentRate),2)
    unpd_bal = round((balance - min_pmt),2)
    interest = round((annualInterestRate/12.0*unpd_bal),2)
    balance = round(balance-(min_pmt - interest),2)
    
    month += 1
print('Remaining balance: {}'.format(balance))





