initial_balance = 999999
annual_interest_rate = 0.18
monthly_interest_rate = annual_interest_rate / 12
lowest = initial_balance / 12
highest = initial_balance * (1 + monthly_interest_rate) ** 12 / 12


def outstanding_balance(balance, annualInterestRate, monthlyPayment):
    def monthly_balance(balance):
        balance = balance - monthlyPayment
        unpaid_balance = balance * (1 + annualInterestRate / 12)
        return unpaid_balance

    for m in range(12):
        balance = monthly_balance(balance)
    return balance


def get_lowest_payment(l_bound, u_bound):
    mid = (u_bound + l_bound) / 2
    monthly_repayment = outstanding_balance(initial_balance, annual_interest_rate, mid)
    if abs(monthly_repayment) < 0.01:
        return round(mid, 2)
    if monthly_repayment > 0.01:
        l_bound = mid
    if monthly_repayment < -0.01:
        u_bound = mid
    return get_lowest_payment(l_bound, u_bound)


print(f'Lowest Payment: {get_lowest_payment(lowest, highest)}')
