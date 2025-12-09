#Your entire fortune is in your investment-account ("your account").

#Every year on your birthday:
#(a) You get the annualRateOfReturn% of your balance added to your account.
#(b) Then your "Genie in a Bottle"** puts $annualGenieMoney into your account.

#Today is your birthday; you are turning yourAge.
#You have $moneyNow in your account now, after (a) and (b) described above.

#How old will you be when you become a millionaire?
currentBalance = int(input("Whats your current balance?"))
currentAge = int(input("Whats your age?"))
annualRateOfReturn=float(input("What percentage u revceive?"))
annualGenieMoney=int(input("What much u get from the Genine money?"))

while currentBalance < 1000000:
    currentBalance += (annualRateOfReturn / 100) * currentBalance# the += adds the right handside of the eqaul to the left hand side
    currentBalance += annualGenieMoney
    # Increment age
    currentAge += 1# all the opertaions that has happened would be +1

# Output the result
print(f"You will become a millionaire at the age of {currentAge}.")