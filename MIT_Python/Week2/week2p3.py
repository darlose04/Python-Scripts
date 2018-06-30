# -*- coding: utf-8 -*-
'''
Problem 3 - Using Bisection Search to Make the Program Faster

You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? 
You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). 
Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. 
(Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, 
so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)
'''
balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance
lowestBalance = 0.01 # Error margin e.g. $0.01

# Keep testing new payment values until the balance is +/- lowestBalance
while abs(balance) > lowestBalance:
    # Reset the value of balance to its original value
    balance = originalBalance
    # Calculate a new monthly payment value from the bounds
    payment = (upperBound - lowerBound) / 2 + lowerBound

    # Test if this payment value is sufficient to pay off the entire balance in 12 months
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    # Reset bounds based on the final value of balance
    if balance > 0:
        # If the balance is too big, need higher payment so we increase the lower bound
        lowerBound = payment
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        upperBound = payment

# When the while loop terminates, we know we have our answer
print("Lowest Payment:", round(payment, 2))
    
