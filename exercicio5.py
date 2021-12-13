"5. Faça um Programa que leia as idades e alturas de 10 alunos e determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos."


soma = 0
count = 0
veta = []
veti = []
for i in range (1,11):
    print("Dados do aluno "+str(i))
    for j in range (1):
        idade = int(input("Digite a idade do aluno "+str(i)+" : "))
        altura = float(input("Digite a estatura do aluno "+str(i)+" : "))
        veta.append(altura)
        veti.append(idade)
        soma = soma + altura
        resultado = soma / i
        print("\n")
for veti, veta  in zip(veti ,veta):
    if veti > 13 and veta < resultado:
       count = count + 1 
print ("Um total de "+str(count)+" aluno/s tem a estatura a baixo da media da turma")         
