# ENTRADAS
cod_estado = int(input('Digite código do estado de origem (1 a 5):'))
cod_carga = int(input('Digite código da carga (10 a 40):'))
pesocarga_tn = float(input('Digite peso da carga em tonelada:'))

# PESO DA CARGA EM QUILOS
pesocarga_kg = pesocarga_tn * 1000

# PRECO POR QUILO SEGUNDO CODIGO
preco_kg = float
if 10 <= cod_carga <= 20:
    preco_kg = 100.00
elif 21 <= cod_carga <= 30:
    preco_kg = 250.00
elif 31 <= cod_carga <= 40:
    preco_kg = 340.00

# PRECO CARGA POR QUILO
preco_carga = preco_kg * pesocarga_kg

# PRECO IMPOSTO SEGUNDO CODIGO DO ESTADO
porc_imposto = float
if cod_estado == 1:
    porc_imposto = 0.35
elif cod_estado == 2:
    porc_imposto = 0.25
elif cod_estado == 3:
    porc_imposto = 0.15
elif cod_estado == 4:
    porc_imposto = 0.05
elif cod_estado == 5:
    porc_imposto = 0

valor_imposto = preco_carga * porc_imposto

# PRECO TOTAL
preco_total = valor_imposto + preco_carga

# SAIDAS
print(f'Peso da carga em kg é: {pesocarga_kg}kg')
print(f'Preço da carga por kg é:R${preco_kg:.2f}')
print(f'Imposto do estado é: R${valor_imposto:.2f}')
print(f'\nPreço da total da carga é: R${preco_total:.2f}')