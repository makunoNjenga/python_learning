# and - both true
# or - either true
# not - negation

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for a loan - and operator")

if has_high_income or has_good_credit:
    print("Eligible for a loan - or operator")


if has_good_credit and not has_criminal_record:
    print("Eligible for a loan - not operator")