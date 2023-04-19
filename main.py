"""
Title: Tax Calculation
Group:
Gagol Egor
Tarlo Evgeny
Karpenko Nikolay
"""

import ru_local as ru
yes = ru.ans_yes
no = ru.ans_no

print(ru.q0)
if str.lower(input()) == yes:  # tax resident
    None
else:  # non-tax resident
    print(ru.q00)
    if str.lower(input()) == yes:  # have income

    else:  # don't have income
