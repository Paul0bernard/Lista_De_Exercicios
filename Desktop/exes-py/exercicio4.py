"4. Faça um Programa que peça duas notas de 5 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0." 

vet = []
count = 0
for i in range(1,6):
    print("Digite a nota do aluno : "+str(i))
    
    for j in range(1):
      a = (int(input("digite o valor da nota n1: ")))
      b = (int(input("digite o valor da nota n2: ")))
      c = ((a+b)/2)
      vet.append(c)
      print ("A media do aluno "+str(i)+" é igual a "+str(c))
      print ('\n')
for k in vet:
   if k >= 7:
      count = count + 1 
print("um total de "+str(count)+" alunos tiveram uma nota a cima da media")