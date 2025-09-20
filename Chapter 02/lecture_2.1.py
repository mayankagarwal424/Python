'''Topic: Variables; A programer's perspective''' 

ram_bank_balance = 100000
# ram's bank balance, note that this is +ve
ram_loan_amount = 500000
# ram's loan, this is to be returned by him and hence will count as negative

lakshman_bank_balance = 2000000
# lakshman's bank balance, note that this is +ve
lakshman_loan_amount = 1000000
# lakshman's loan, this is to be returned by him and hence will count as negative

net_income = ram_bank_balance + lakshman_bank_balance 
# net_income is total bank balance of two brothers
net_liability = ram_loan_amount + lakshman_loan_amount
# net_liability is the total loan of the brothers

final_amount = net_income - net_liability
# final_amount is the family's final money (it may be +ve or -ve)


print("So, the family has", final_amount)
