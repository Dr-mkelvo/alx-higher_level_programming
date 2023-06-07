def farenheit(T):
    return  ((float(9)/5)* T + 32)
def celsius(T):
    return ((float(9)/5)* T -32)

temps = (23, 43, 45, 12)
F = map(farenheit, temps)
C = map(celsius, F)
temp_far = list(map(farenheit, temps))
temp_cel = list(map(celsius, temp_far))
print(temp_far)
print(temp_cel)