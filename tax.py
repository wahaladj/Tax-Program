status = int(input("Enter filing status (0-3): "))
income = float(input("Enter taxable income: "))

tax = 0

if status == 0:  # single
    if income > 8350:
        tax += 8350 * 0.10
        income -= 8350
        tax += min(income, 25600) * 0.15
    else:
        tax = income * 0.10

elif status == 1:  # married jointly
    if income > 16700:
        tax += 16700 * 0.10
        income -= 16700
        tax += min(income, 51200) * 0.15
    else:
        tax = income * 0.10

elif status == 2:  # married separately
    if income > 8350:
        tax += 8350 * 0.10
        income -= 8350
        tax += min(income, 25600) * 0.15
    else:
        tax = income * 0.10

elif status == 3:  # head of household
    if income > 11950:
        tax += 11950 * 0.10
        income -= 11950
        tax += min(income, 33550) * 0.15
    else:
        tax = income * 0.10

print("Tax:", round(tax, 2))
