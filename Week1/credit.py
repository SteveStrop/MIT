def outstanding_balance(balance, rate, payment, months=12):
    """ Return residual balance after successive loan repayments
    :param balance: initial amount of loan (float)
    :param rate: monthly interest rate (0 < float < 1)
    :param payment: fixed monthly payment (float)
    :param months: number of repayments (int)
    :returns float
    """
    for _ in range(months):
        balance = (balance - payment) + (balance - payment) * rate
    return balance


def bisect_min_repay(balance, rate, l_bound, u_bound):
    """ Use bisect search to find minimum monthly repayment that will clear a credit card balance
:param balance: initial amount of loan (float)
:param rate: annaul interest rate (0 < float < 1)
:param l_bound: lower limit for search (float)
:param u_bound: upper limit for search (int)
:returns minimum repayment rounded to 2 dp (float)
"""

    test_payment = (u_bound + l_bound) / 2
    test_balance = outstanding_balance(balance, rate, test_payment)
    if abs(test_balance) < 0.01:
        return round(test_payment, 2)
    if test_balance > 0.01:
        l_bound = test_payment
    if test_balance < -0.01:
        u_bound = test_payment
    return bisect_min_repay(balance, rate, l_bound, u_bound)


def min_repay(balance, rate):
    """ Calculate the minimum fixed monthly repayment to reduce a given loan balance to zero
    given the annual interest rate. Uses a bisect search to find the result
    :param rate: annual interest rate as a percentage between 0 and 1 (float)
    :param balance: initial loan amount (float)
    :returns the string "Lowest Payment: " + float
    """
    monthly_rate = rate / 12
    # set initial values for bisect search
    l_bound = balance / 12
    u_bound = balance * (1 + monthly_rate) ** 12 / 12
    return f'Lowest payment: {bisect_min_repay(balance, monthly_rate, l_bound, u_bound)}'
