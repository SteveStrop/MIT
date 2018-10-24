def monthly_balance(balance, annual_interest_rate, monthlyPayment, periods=12):
    """ Calculate remaining balance after m months, repaying monthlyPaymentRate * outstanding balance per month
    :param balance: float > 0
    :param annual_interest_rate: decimal percentage between 0 and 1
    :param monthlyPayment: int multiple of 10
    :param periods int defaults to 12 (one year)
    :returns: float"""
    # outstanding balance after deduction of monthly payment
    balance = balance - monthlyPayment
    # outstanding balance after addition of interest
    unpaid_balance = balance * (1 + annual_interest_rate / 12)
    # repeat for all periods
    if periods == 1:
        return unpaid_balance
    return monthly_balance(unpaid_balance, annual_interest_rate, monthlyPayment, periods - 1)


def lowest_repayment(balance, annual_interest_rate):
    test_payment = int(balance / 12) - int(balance / 12) % 10
    print(test_payment, monthly_balance(balance, annual_interest_rate, test_payment))

    if monthly_balance(balance, annual_interest_rate, test_payment) <= 0:
        return test_payment
    return monthly_balance(balance, annual_interest_rate, test_payment + 10)


balance = 3329
annualInterestRate = 0.2
print(f'Lowest Payment: {round(lowest_repayment(balance,annualInterestRate),2)}')
