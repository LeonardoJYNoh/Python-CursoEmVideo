vel = int(input('Qual é a velocidade atual do carro? '))

if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${:.2f}!'.format((vel-80)*7))
print('Tenha um bom dia! Dirija com segurança!')