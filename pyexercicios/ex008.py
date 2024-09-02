x = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{}dm \n{}cm \n{}mm'.format(x,(x/1000),(x/100),(x/10),(x*10),(x*100),(x*1000)))