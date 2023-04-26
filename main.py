"""
Title: Tax Calculation
Group:
Gagol Egor - 5
Tarlo Evgeny - 64
Karpenko Nikolay
"""

import ru_local as ru

a = [ru.q040, ru.q041, ru.q042, ru.q043, ru.q044, ru.q045]
yes = ru.ans_yes
no = ru.ans_no
res_tax = 0

print(ru.q0)
if str.lower(input()) == yes:  # tax resident
    print(ru.q10)
    if str.lower(input()) == yes:
        print(ru.in_am_res)
        in_am = int(input())
        res_tax += in_am * 0.15 + 650000
    else:
        print(ru.in_am_res)
        in_am = int(input())
        res_tax += in_am * 0.13

    print(ru.q11)
    if str.lower(input()) == yes:
        print(ru.in_am_res)
        in_am = int(input())
        res_tax += in_am * 0.13

    print(ru.q12)
    if str.lower(input()) == yes:
        print(ru.in_am_res)
        in_am = int(input())
        res_tax += in_am * 0.35

    print(ru.q13)
    if str.lower(input()) == yes:
        print(ru.in_am_res)
        in_am = int(input())
        res_tax += in_am * 0.09

    print(ru.q14)  # additional question
    if str.lower(input()) == yes:
        print(ru.q15)
        if str.lower(input()) == yes:
            print(ru.in_am_res)
            in_am = int(input())
            res_tax += in_am * 0.15

    if res_tax > 0:
        print(ru.res_tax, res_tax)
    else:
        print(ru.in_am_non_res_zero)

else:  # non-tax resident
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

    x = 0
    print(ru.q04)
    if str.lower(input()) == yes:
        for i in range(6):
            print(a[i])
            if str.lower(input()) == yes:
                x += 1
        if x > 0:
            print(ru.in_am)
            if str.lower(input()) == yes:  # tax is 15% + 650000
                print(ru.in_am_non_res)
                in_am = int(input())
                res_tax += in_am * 0.15 + 650000
            else:
                print(ru.in_am_non_res)  # tax is 13%
                in_am = int(input())
                res_tax += in_am * 0.13
    if res_tax > 0:
        print(ru.res_tax, res_tax)
    else:
        print(ru.in_am_non_res_zero)