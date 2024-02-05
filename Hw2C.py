### Chat GPT was used for this problem ###
def GaussSeidel(Aaug, x, Niter=15):
    n = len(Aaug)

    for k in range(Niter):
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += Aaug[i][j] * x[j]

            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][i]
    return x

def AaugMatrix():
    n = int(input("Enter the number of rows: "))
    Aaug = []
    for i in range(n):
        row = []
        for j in range(n):
            element = float(input(f"Enter element for row {i + 1}, column {j + 1}: "))
            row.append(element)
        # Append the right-hand side value for each equation
        b = float(input(f"Enter the value for the right-hand side of equation {i + 1}: "))
        row.append(b)
        Aaug.append(row)
    return Aaug

def MakeDiagDom(A):
    n = len(A)

    # Iterate through each row
    for i in range(n):
        # Find the index of the maximum element in the current row
        max_index = max(range(n), key=lambda j: abs(A[i][j]))

        # Swap the current row with the row containing the maximum element
        A[i], A[max_index] = A[max_index], A[i]

    return A

def main():
    Aaug = AaugMatrix()

    # Optionally make the matrix diagonally dominant
    Aaug = MakeDiagDom(Aaug)

    n = len(Aaug)
    x = [0] * n  # Initial guess for the solution

    Niter = int(input("Enter the number of iterations: "))
    x = GaussSeidel(Aaug, x, Niter)

    print("Solution:")
    for i in range(n):
        print(f"x{i+1} = {x[i]}")

if __name__ == "__main__":
    main()
