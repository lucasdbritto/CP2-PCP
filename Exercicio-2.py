A=float(input("Digite o valor do lado A do triângulo:"))
B=float(input("Digite o valor do lado B do triângulo:"))
C=float(input("Digite o valor do lado C do triângulo:"))
if A>=B+C:
    print("não forma um triângulo")
else:
    if (A ** 2) == (B ** 2 + C ** 2):
        print("TRIANGULO RETANGULO")
    elif (A ** 2) > (B ** 2 + C ** 2):
        print("TRIANGULO OBTUSANGULO")
    elif (A ** 2) < (B ** 2 + C ** 2):
        print("TRIANGULO ACUTANGULO")
if A==B==C:
    print("triângulo retângulo")
elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")