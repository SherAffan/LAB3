n = 0
s = 0
m = float('inf')

while True:
    number = int(input("Enter a natural number (or -1 to terminate): "))
    
    if number == -1:
        break
    else:
        n += 1
        s += number
        m = min(m, number)

a = s / n if n > 0 else 0