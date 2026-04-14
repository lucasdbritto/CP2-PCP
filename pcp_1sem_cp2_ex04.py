nome_funcionario=input("Digite o nome do funcionario completo:")

cargo=int(input("Digite o cargo do funcionario: 1(gerente), 2(analista), 3(assistente), 4(estagiario):"))

salario=float(input("Digite o salario do funcionario:"))

horas_extras=float(input("Digite a quantidade de horas extras trabalhadas do funcionario:"))

faltas=int(input("Digite a quantidade de faltas no mes:"))

bonus=input("O funcionario recebeu bonus por desempenho? Sim(s) ou Não(n)").lower()

def calcular_bonus(cargo, bonus):
    if bonus.lower() != "s":
        return 0.0

    tabela_bonus = {
    1:1000,
    2:500,
    3:300,
    4:100
}
    return tabela_bonus.get(cargo, 0.0)
def calular_horas_extras(salario, horas_extras):
    return (salario * 0.015) * horas_extras
def descontos(salario, faltas):
    return (salario*0.02)*faltas
valor_bonus=calcular_bonus(cargo, bonus)

valor_descontos = descontos(salario, faltas)

valor_extras= calular_horas_extras(salario, horas_extras)

acrescimos = valor_bonus + horas_extras

salario_bruto = salario + acrescimos

salario_final = salario_bruto-valor_descontos

#respostas
print(salario_bruto)
print(acrescimos)
print(valor_descontos)
print(salario_final)