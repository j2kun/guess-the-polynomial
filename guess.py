from polynomial import Polynomial


answer = input("What is f(1)? ")
sum_of_coeffs = int(answer)
N = 1 + sum_of_coeffs

answer = input("What is f({})? ".format(N))
y = int(answer)

coeffs = []
while y > 0:
    coeff = y % N
    coeffs.append(int(coeff))
    y = (y - coeff) / N

p = Polynomial(coeffs)
print("Your polynomial is: \n\n\t{}\n".format(p))
