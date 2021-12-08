"2. Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes"

entrada = str(input("Digite aqui a sua palavra : "))
vtuple = tuple(entrada)
count = 0
for i in vtuple:
    if i not in 'aeiou':
     print (i)
     count = count + 1 
print ("a palavra tem "+str(count)+(' consoantes'))     