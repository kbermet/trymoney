expense = 0


def costs(day):
    global expense
    expense += day


costs(17)
costs(20)
costs(21)
print(expense)


def costs2(*expense1):
    for day in expense1:
        day += day
    return day


print(costs2(56, 114, 17))
