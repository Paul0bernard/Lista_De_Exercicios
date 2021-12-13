# 8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas #são: 
#a. "Telefonou para a vítima?" 
#b. "Esteve no local do crime?" 
#c. "Mora perto da vítima?" 
#d. "Devia dinheiro para a vítima?" 
#e. "Já trabalhou com a vítima?" 
# No final, o programa deve emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"; 
# entre 3 e 4, como "Cúmplice", e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

listas = []

print("Responda sim ou não para as pegunta a seguir. \n")

a = input("Telefonou para a vitima ? ")            
b = input("Esteve no local do crime? ")
c = input("Mora perto da vítima? ")
d = input("Devia dinheiro para a vítima? ")
e = input("Já trabalhou com a vítima? ")  

resp = a,b,c,d,e  

if "sim" not in resp:
    print('\n')
    print("vimos que voce nao respondeu sim ou não por favor reinicie o jogo")
    print('\n')
    quit()


for i in (resp):
   if i == "sim":
      listas.append(i)
if len(listas) == 2:
   print("hum te achei suspeita")  
if len(listas) > 2 and len(listas) <= 4:
   print("voce é cumplice")
if len(listas) > 4:
   print("assasino!")
if len(listas) < 2:
    print("Voce é inocente")    