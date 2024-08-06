def add_polynomials(p1, p2): 
    result = []
    c1 = c2 = 0
    while(c1 < len(p1) and c2 < len(p2)):
        if p1[c1][1] == p2[c2][1]:
            c = p1[c1][0] + p2[c2][0]
            result.append([c, p1[c1][1]])
            c1 += 1
            c2 += 1
        elif p1[c1][1] > p2[c2][1]:
            result.append([c1, p1[c1][1]])
            c1+=1
        elif p1[c1][1] < p2[c2][1]:
            result.append([c2, p2[c2][1]])
            c2+=1
    
    while(c1 < len(p1)):
        result.append([c1, p1[c1][1]])
        c1+=1
    while(c2 < len(p2)):
        result.append([c2, p2[c2][1]])
        c2+=1
    return result


def multiply_polynomials(poly1, poly2):
    result = []

    for coeff1, deg1 in poly1:
        for coeff2, deg2 in poly2:
            new_coeff = coeff1 * coeff2
            new_deg = deg1 + deg2
            found = False
            for i in range(len(result)):
                if result[i][1] == new_deg:
                    result[i][0] += new_coeff
                    found = True
                    break
            if not found:
                result.append([new_coeff, new_deg])
    
    result = [term for term in result if term[0] != 0]
    result.sort(key=lambda x: x[1], reverse=True)
    return result

def evaluate_polynomial(poly, x):
    result = 0
    for coeff, deg in poly:
        result += coeff * (x ** deg)
    return result


def evaluate_polynomial(poly, x):
    result = 0
    for coeff, deg in poly:
        result += coeff * (x ** deg)
    return result

def input_polynomial():
    poly = []
    while True:
        coeff = int(input("Enter coefficient: "))
        deg = int(input("Enter degree: "))
        poly.append([coeff, deg])
        done = input("Type 'n' to finish or press Enter to continue: ").lower()
        if done == 'n':
            break
    return poly


while True:
    print("\nPolynomial Operations Menu:")
    print("1. Add Polynomials")
    print("2. Multiply Polynomials")
    print("3. Evaluate Polynomial")
    print("4. Exit")
    choice = input("Select an option (1/2/3/4): ").strip()
    if choice == '1':
        print("")
        print("Enter the first polynomial:")
        poly1 = input_polynomial()
        print("")
        print("Enter the second polynomial:")
        poly2 = input_polynomial()
        result = add_polynomials(poly1, poly2)
        print("The result of adding the polynomials is:")
        print(result)
    elif choice == '2':
        print("")
        print("Enter the first polynomial:")
        poly1 = input_polynomial()
        print("Enter the second polynomial:")
        print("")
        poly2 = input_polynomial()
        result = multiply_polynomials(poly1, poly2)
        print("The result of multiplying the polynomials is:")
        print(result)
    elif choice == '3':
        print("Enter the polynomial to evaluate:")
        poly = input_polynomial()
        x = float(input("Enter the value of x: "))
        result = evaluate_polynomial(poly, x)
        print("The result of evaluating the polynomial at x = %d is: %d"%(x, result))
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

