ladoa= float(input("Digite o lado A do triângulo\n"))
ladob= float(input("Digite o lado B do triângulo\n"))
ladoc= float(input("Digite o valor C do triângulo\n"))


if ladob > ladoa:
    ladoa, ladob = ladob, ladoa
if ladoc > ladoa:
    ladoa, ladoc = ladoc, ladoa
if ladoc > ladob:
    ladob, ladoc = ladoc, ladob

if ladoa>= ladob+ladoc:
    print("NÃO FORMA TRIâNGULO")

elif ladoa**2== ladob**2+ladoc**2:
    print("TRIÂNGULO RETÂNGULO")

elif ladoa**2>ladob**2+ladoc**2:
    print("TRIÂNGULO OBTUSÂNGULO")

elif ladoa**2<ladob**2+ladoc**2:
    print("TRIÂNGULO ACUTÂNGULO")

if ladoa==ladob==ladoc:
    print("TRIÂNGULO EQUILÁTERO")

elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print("TRIÂNGULO ISÓSCELES")