### Chat GPT was used for this problem ###
import math

def SecantMethod(fcn, x0, x1, maxiter=10, xtol=1e-5):  # Calculates the next value of a function given x0,x1,maxiter, and xtol.
    for iteration in range(maxiter):
        f_x0 = fcn(x0)
        f_x1 = fcn(x1)
        if abs(f_x1 - f_x0) < xtol:  # Loop exits if |xb-xa| < xtol and returns x1 and iteration
            return x1, iteration
        value = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)  # Secant Method formula
        x0, x1 = x1, value
    return value, maxiter

def fcn(x):  # Problem 1
    return x - 3 * math.cos(x)

def fcn2(x):  # Problem 2
    return math.cos(2 * x) * x ** 3

def fcn3(x):  # Problem 3
    return math.cos(2 * x) * x ** 3

def main():  # Function that assigns variables p1,p2, & p3 to respective calls of SecantMethod() for each problem and then prints the contents of the variables
    p1 = SecantMethod(fcn, 1, 2, 5, 1e-4)
    p2 = SecantMethod(fcn2, 1, 2, 15, 1e-8)
    p3 = SecantMethod(fcn3, 1, 2, 3, 1e-8)
    print("All functions start with: x0 = 1 & x1 = 2 and results are output as: (ANSWER, iteration)")
    print("The Secant Method approximation of x-3cos(x) = 0 with maxiter = 5 & xtol = 1e-5 is: ", p1)
    print("The Secant Method approximation of cos(2x)x^3 = 0 with maxiter = 15 & xtol = 1e-8 is: ", p2)
    print("The Secant Method approximation of cos(2x)x^3 = 0 with maxiter = 3 & xtol = 1e-8 is: ", p3)

main()
