
def summ(*num):
    result = 0

    for i in num:
        result += i
    return result

a = summ(1, 2, 3, 98, 80)
print(a)
