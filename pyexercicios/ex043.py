peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você esta Abaixo do Peso')
elif imc < 25:
    print('Você esta Peso Ideal')
elif imc < 30:
    print('Você esta com Sobrepeso')
elif imc < 40:
    print('Você esta com Obesidade')
elif imc > 40:
    print('Você esta com Obesidade Mórbida')