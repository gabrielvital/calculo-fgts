print("Bem vindo à Calculadora FGTS!")
print("Descubra qual o seu saldo de FGTS acumulado!")
nome = input("Primeiro, informe seu nome: ")
salario = float(input("Agora, informe seu salário: "))
periodo = int (input ("Há quantos meses está trabalhando? "))
juros = 0.03

saldo = (salario*0.08)*periodo

for mes in range (1, (periodo+1)):
    print ("Mês", mes, "=", (salario*0.08))

if periodo >= 12:
    extrato = saldo + (saldo*juros)
    print("Juros acumulados dos últimos 12 meses: {}".format(saldo*juros))
else:
    extrato = saldo

print("{}, seu saldo de FGTS acumulado é de R$ {}".format(nome, extrato))