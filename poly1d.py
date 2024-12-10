# Function to input and output polynomials
def input_polynomial():
    degree = int(input("Enter the degree of the polynomial: "))
    coeffs = []
    for i in range(degree, -1, -1):  # Start from the highest degree
        coeff = int(input(f"Enter coefficient of x^{degree - i}: "))
        coeffs.append(coeff)
    return coeffs

def output_polynomial(coeffs):
    degree = len(coeffs) - 1
    poly_str = ""
    for i in range(degree, -1, -1):
        if coeffs[i] != 0:
            if poly_str:
                poly_str += " + " if coeffs[i] > 0 else " - "
            if abs(coeffs[i]) != 1 or i == 0:
                poly_str += str(abs(coeffs[i]))
            if i > 0:
                poly_str += f"x^{i}"
    if not poly_str:
        poly_str = "0"
    print("Polynomial: ", poly_str)

# Function to evaluate polynomial at a given value of x
def evaluate_polynomial(coeffs, x):
    result = 0
    degree = len(coeffs) - 1
    for i in range(degree + 1):
        result += coeffs[i] * (x ** (degree - i))
    return result

# Function to add two polynomials
def add_polynomials(coeffs1, coeffs2):
    # Ensure both polynomials have the same degree
    degree1 = len(coeffs1) - 1
    degree2 = len(coeffs2) - 1
    if degree1 > degree2:
        coeffs2 = [0] * (degree1 - degree2) + coeffs2
    elif degree2 > degree1:
        coeffs1 = [0] * (degree2 - degree1) + coeffs1
    
    # Add coefficients
    result = [coeffs1[i] + coeffs2[i] for i in range(len(coeffs1))]
    return result

# Function to multiply two polynomials
def multiply_polynomials(coeffs1, coeffs2):
    degree1 = len(coeffs1) - 1
    degree2 = len(coeffs2) - 1
    result_degree = degree1 + degree2
    result = [0] * (result_degree + 1)
    
    # Multiply coefficients
    for i in range(degree1 + 1):
        for j in range(degree2 + 1):
            result[i + j] += coeffs1[i] * coeffs2[j]
    
    return result

# Main function to demonstrate the polynomial operations
def main():
    print("Enter first polynomial:")
    poly1 = input_polynomial()
    output_polynomial(poly1)

    print("\nEnter second polynomial:")
    poly2 = input_polynomial()
    output_polynomial(poly2)

    # Evaluate the first polynomial at x = 2
    x_value = float(input("\nEnter the value of x to evaluate the first polynomial: "))
    print(f"Evaluation of first polynomial at x = {x_value}: {evaluate_polynomial(poly1, x_value)}")

    # Add the polynomials
    sum_poly = add_polynomials(poly1, poly2)
    print("\nSum of polynomials:")
    output_polynomial(sum_poly)

    # Multiply the polynomials
    product_poly = multiply_polynomials(poly1, poly2)
    print("\nProduct of polynomials:")
    output_polynomial(product_poly)

# Execute the program
main()
