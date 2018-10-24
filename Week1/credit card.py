balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def monthly_balance(balance, annualInterestRate, monthlyPaymentRate, periods=12):
    """ Calculate remaining balance after m months, repaying monthlyPaymentRate * outstanding balance per month
    :param balance: float > 0
    :param annualInterestRate: decimal percentage between 0 and 1
    :param monthlyPaymentRate: decimal percentage between 0 and 1
    :param periods int defaults to 12 (one year)
    :returns: float"""
    # outstanding balance after deduction of monthly payment
    balance = balance - monthlyPaymentRate * balance
    # outstanding balance after addition of interest
    unpaid_balance = balance * (1 + annualInterestRate / 12)
    # repeat for all periods
    if periods == 1:
        return unpaid_balance
    return monthly_balance(unpaid_balance, annualInterestRate, monthlyPaymentRate, periods - 1)


print(f'Remaining balance: {round(monthly_balance(balance, annualInterestRate, monthlyPaymentRate),2)}')
