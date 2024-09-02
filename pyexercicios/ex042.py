l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Esse triangulo não pode existe')
else:
    if l1 == l2 and l2 == l3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif l1 == l2 or l2 == l3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓCELES')
    elif l1 != l2 and l1 != l3 and l1 != l3:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')