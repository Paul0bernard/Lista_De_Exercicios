"6. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). "

vetm = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
        'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
vetemp = []
soma = 0

for i in vetm:
    temperatura =(int(input("digite o valor para o mes de "+str(i)+" : ")))
    vetemp.append(temperatura)
    soma = soma + temperatura
    media = soma / 12

for x ,y in zip(vetm,vetemp):
    if y > media :
       print('\n')
       print('Temperatura acima da media no mes de '+str(x)+' com um valor de :'+str(y)+' graus celcius')
       print('\n')
     