salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = salario + salario*(15/100)

print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,aumento))