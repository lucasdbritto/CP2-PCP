nota_cp1 = float(input ("Insira a nota da cp 1 "))
nota_cp2 = float(input ("Insira a nota da cp 2 "))
nota_cp3 = float(input ("Insira a nota da cp 3 "))
nota_sprint1 = float(input ("Insira a nota do sprint 1 "))
nota_sprint2 = float(input ("Insira a nota do sprint 2 "))
nota_global_solution = float(input ("Insira a nota do Global Solution "))
menor = nota_cp1
if nota_cp2 < menor:
    menor = nota_cp2
if nota_cp3 < menor:
    menor = nota_cp3
print(f"A menor nota de Checkpoint desconsiderada foi: {menor}")
media_sem_peso = (nota_cp1 + nota_cp2 + nota_cp3 - menor + nota_sprint1 + nota_sprint2) / 4
media = (media_sem_peso * 0.4) +  (nota_global_solution * 0.6)
media_com_peso = media * 0.4
print(f"\nMédia do semestre: {media:.1f}")
print(f"Média com peso (40%): {media_com_peso:.1f}")