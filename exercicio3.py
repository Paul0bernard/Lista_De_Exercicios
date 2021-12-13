"3. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores."

vet1 = []
vet2 = []
vet3 = []
for i in range(20):
   num = int(input("Dgite um numero: "))
   vet1.append(num)
for j in vet1:
    if j % 2 == 0:
        par = vet2.append(j)
    else:
        imp = vet3.append(j)   
print (vet1)       
print (vet2)
print (vet3)
