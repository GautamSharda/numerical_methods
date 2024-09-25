from math import factorial

def derivative_at_a(f, a):
    h = 0.000001
    return ( f(a + h) - f(a) ) / h
    # could also just do 
    return e_x(a)

def e_x(x):
    return 2.71828**x

def p1(f, a, x):
    return f(a) + (x - a)*derivative_at_a(f, a)

print("linear TP approx. of e^x around 0 at 0: ", p1(e_x, 0, 0))
print("e^0: ", e_x(0))
print("\n")

for i in range(1, 11):
    print(f"linear TP approx. of e^x around 0 at {i}: ", p1(e_x, 0, i))
    print(f"e^{i}: ", e_x(i))

def n_derivative_at_a(f, a, n):
    if n == 0:
        return f(a)
    h = 0.0001
    for i in range(n):
        a = ( f(a + h) - f(a) ) / h
    return a

def pn(f, a, x, n):
    appxmtn = None
    for i in range(n):
        appxmtn = (((x - a)**n)/factorial(n))*n_derivative_at_a(f, a, n)
    return appxmtn

print("\n")
for i in range(1, 11):
    print(f"{i}th order TP approx. of e^x around 0 at x=10: ", pn(e_x, 0, 10, i))
    print(f"e^10: ", e_x(10))
