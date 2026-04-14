# FUNÇÕES
def pode_aprovar(idade, renda, valor_emprestimo):
    idadeok = idade >= 18
    rendaok = (renda * 20) >= valor_emprestimo
    return idadeok and rendaok

def definir_taxa(numerodeparcelas):
    if numerodeparcelas <= 6:
        return 0.05
    elif 7 <= numerodeparcelas <= 12:
        return 0.08
    elif 13 <= numerodeparcelas <= 24:
        return 0.1
    else:
        return print(f"valor da parcela invalido {numerodeparcelas}")

def calcular_parcela(valor_emprestimo, taxa, numerodeparcelas):
    den = taxa * (1 + taxa) ** numerodeparcelas
    num = (1 + taxa)**numerodeparcelas - 1
    return valor_emprestimo * (den / num)

def calcular_total (valorparcela, numerodeparcelas):
    return valorparcela * numerodeparcelas

def calcular_juros(valor_total, valor_emprestimo):
    return valor_total - valor_emprestimo

def conversãoparaporc(taxa):
    return taxa * 100

# ENTRADAS
nome = input('Digite o nome do cliente: ')
idade = int(input('Digite a idade do cliente: '))
renda = float(input('Digite a renda mensal do cliente: '))
valor_emprestimo = float(input('Digite o valor desejado do empréstimo: '))
numerodeparcelas = int(input('Digite a números de parcelas (de 3 até 24): '))

# APROVAÇÃO
if pode_aprovar(idade, renda, valor_emprestimo):
    print("\nRenda e Idade APROVADAS\n")

    taxa = definir_taxa(numerodeparcelas)

    valorparcela = calcular_parcela(valor_emprestimo, taxa, numerodeparcelas)

    valor_total = calcular_total(valorparcela, numerodeparcelas)

    juros = calcular_juros(valor_total, valor_emprestimo)

    taxaporcentagem = conversãoparaporc(taxa)

    print(f"Nome do cliente:{nome}")
    print(f"Valor do emprestimo: R${valor_emprestimo:.2f}")
    print(f"Taxa de juros aplicada: {taxaporcentagem}%")
    print(f"Valor da parcela: R${valorparcela:.2f}")
    print(f"Valor da total a ser pago: R${valor_total:.2f}")
    print(f"Total de juros pago: R${juros:.2f}")

else:
    print("Renda e Idade DESAPROVADAS")