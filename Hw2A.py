### Chat GPT was used for this problem ###
import math

def PDF(xMuSigma):  # Calculates the probability density at a given x value
    x, mu, sigma = xMuSigma
    return 1 / (sigma * math.sqrt(2*math.pi)) * math.exp(-0.5 * ((x-mu) / sigma) ** 2)

def SimpMethod(PDF, args1):  # Calculates the approximate integral of PDF using Simpson's 1/3 rule
    EvenSum = 0
    OddSum = 0
    n = 20  # Number of steps
    mu, sigma, b, c = args1
    h = (c - b) / n  # Simpson rule step size
    s0 = PDF((0, mu, sigma)) + PDF((round(c), mu, sigma))  # Sum for s0 term
    for i in range(1, n, 2):  # Sum for even values
        EvenSum += 2 * PDF((round(b) + i * h, mu, sigma))
    for i in range(2, n-1, 2):  # Sum for odd values
        OddSum += 4 * PDF((round(b) + i * h, mu, sigma))
    totalSum = EvenSum + OddSum + s0
    return (h / 3) * totalSum

def Probability(PDF, args, c, GT):  # Calculates the probability with specified arguments by calling PDF & SimpMethod
    mu, sigma = args
    b = mu - 5 * sigma  # Lower boundary
    args1 = (mu, sigma, b, c)
    prob = SimpMethod(PDF, args1)
    if GT == True:  # if/else: determines appropriate probability depending on if x>c or x<c
        return prob
    else:
        return 1 - prob

def main(): # Collects user input for c, mu, GT and sigma. Using that data, Probability() is called to approximate probability
    c = float(input("Enter a number."))
    mu = float(input("Enter a the population mean."))
    sigma = float(input("Enter the standard deviation."))
    GT = input("If P|x<c| is desired, enter True. If P|x>c| is desired, enter False")
    if GT.lower() == "true":  # if/else: Depending on value pf GT, Probability() is called and appropriate print statement is printed
        GT = True
        args = mu, sigma
        p = Probability(PDF, args, c, GT)
        print(f"P(x < {c} | N({mu}, {sigma})) ~= {p}")
    else:
        GT = False
        args = mu, sigma
        p = Probability(PDF, args, c, GT)
        print(f"P(x > {c} | N({mu}, {sigma})) ~= {p}")

if __name__ == "__main__":
    main()



