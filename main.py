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
res_tax = 0

print(ru.q0)
if str.lower(input()) == yes:  # tax resident
    None
else:  # non-tax resident
    print(ru.q00)
    if str.lower(input()) == yes:  # tax is 30% by income
        print(ru.in_am_non_res)
        non_res_in = int(input())
        res_tax += non_res_in * 0.3

    print(ru.q01)
    if str.lower(input()) == yes:  # tax is 30% by income
        print(ru.in_am_non_res_shares)
        non_res_in_shares = int(input())
        res_tax += non_res_in_shares * 0.3

    print(ru.q02)
    if str.lower(input()) == yes:  # tax is 5% by income
        print(ru.in_am_non_res_divs)
        non_res_in_divs = int(input())
        res_tax += non_res_in_divs * 0.05

    print(ru.q03)
    if str.lower(input()) == yes:  # tax is 15% by income
        print(ru.in_am_non_res_divs)
        non_res_in_divs = int(input())
        res_tax += non_res_in_divs * 0.15

    print(ru.q04)
    if str.lower(input()) == yes:
        print(ru.q040)
        if str.lower(input()) == yes:
            print(ru.in_am)
            if str.lower(input()) == yes:  # tax is 15% + 650000
                print(ru.in_am_non_res)
                in_am = int(input())
                res_tax += in_am * 0.15 + 650000
            else:
                print(ru.in_am_non_res)  # tax is 13%
                in_am = int(input())
                res_tax += in_am * 0.13

    else:
        print(ru.in_am_non_res_zero)
