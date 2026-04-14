codigo_do_estado=int(input("Qual o codigo de origem da carga do caminhão(1 a 5):"))
peso_da_carga=float(input("Qual o peso total da carga do caminhão(em Toneladas):"))
codigo_da_carga=int(input("Qual o codigo da carga:"))
peso_kg=peso_da_carga*1000

print(f"O peso da carga em quilos é {peso_kg:.0f} kg")
if peso_da_carga >=10 and peso_da_carga <=20:
    print()

