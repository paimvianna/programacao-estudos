#entrada
n=float(input('Uma distância em metros: '))
cm= n *100
mm= n*1000
dm=n*10
dam=n/10
hm=n/100
km=n/1000
print (f'A mediada de {n}m corresponde a {km:.4f}km e {hm:.3f}hm e {dam:.2f}dam e {dm:.2f}dm a {cm:.2f}cm e {mm:.2f}mm')