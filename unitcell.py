import sys
import math

#importuje pierwszy plik
file=sys.argv[1]  #importuje pierwszy plik TEMP
infile=open(file,"r") #read file
data=infile.readlines() #czyta linie 'infile'

s=data[0].split()
scale=float(s[0])

p=data[1].split() #p to tupla z 1-szej linii rozdzielonej spacjami, w kazdej, kolejne ich elementy to kolumny
q=data[2].split() #p to tupla z 2-giej linii
r=data[3].split() #p to tupla z 3-ciej linii

for i in range(3): #zaokragla liczby 1,2,3, z tupli (wierszy) do zmiennoprzecinkowych
    p[i]=float(p[i])
    q[i]=float(q[i])
    r[i]=float(r[i])
dlug=[] #tworzy tuple na 'dlug' = dlugosc wektora w kierunkach 0,1,2 = stale a,b,c
for w in [p,q,r]: #dla kazdej wartosci 'w' z wierszy p,q,r liczy 'const' - stala sieci (dlugosc wektora w kier. 0,1,2)
    const=math.sqrt(w[0]**2+w[1]**2+w[2]**2)*scale
    print(const)
    dlug.append(const)
print(math.acos((q[0] * r[0] + q[1] * r[1] + q[2] * r[2])*scale**2 / (dlug[1] * dlug[2])) / math.pi * 180) #printuje katy alfa, beta, gamma
print(math.acos((p[0] * r[0] + p[1] * r[1] + p[2] * r[2])*scale**2 / (dlug[0] * dlug[2])) / math.pi * 180)
print(math.acos((p[0] * q[0] + p[1] * q[1] + p[2] * q[2])*scale**2 / (dlug[0] * dlug[1])) / math.pi * 180)