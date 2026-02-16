def grades(g):
    r = ''
    if 2.00 <= g <= 2.99:
        r = 'Fail'
    elif 3.00 <= g <= 3.49:
        r = 'Poor'
    elif 3.50 <= g <= 4.49:
        r = 'Good'
    elif 4.50 <= g <= 5.49:
        r = 'Very Good'
    elif 5.50 <= g <= 6:
        r = 'Excellent'

    return r


print(grades(float(input())))
