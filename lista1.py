'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    print ("helio")

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print ("30 e 37")
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    print (f'media {((5+8+12)/3)}')
#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    nu = int(input('insira o numero:'))
    print (nu)
#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    n1 = float(input('bota o 1º numero:'))
    n2 = float(input('bota o 2º numeor:'))
    print ('1º numero ', n1, ' 2º numeoro ', n2)
#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    n = int(input('bota o numero'))
    print(f'numero menos {n-1} numero normal {n} numero mais {n+1}')
#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input('bota o nome')
    endereco = input('bota o endereço')
    telefone = input('bota o telefone')
    print (f'nome: {nome} endereço: {endereco} telefone: {telefone}')
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    n1 = float(input('bota o primeiro numero'))
    n2 = float(input('bota o segundo numero'))
    print(n1 - n2)
#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9(): 
    n1 = float(input('bota o numero ai:'))
    print(n1/4)
#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    n1 = float(input('bota o numeor'))
    n2 = float(input('bota o numeor'))
    n3 = float(input('bota o numeor'))
    print(f'a media de {n1,n2,n3} é {(n1+n2+n3)/3}')
#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    n1 = float(input('bota ai o numeor'))
    n2 = float(input('boga ai mais um numeor'))
    print(f'as operaçoes: \nsoma: {n1+n2} \nsubtração {n1-n2} \ndivisão {n1/n2} \nmultiplicação {n1*n2} ')
#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    n1 = float(input('bota o numeor ai'))
    print(f'o quadrado: {n1**2}')
#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.


#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    


#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    c = int(input('Centígrados: '))
    f = (9 * c + 160) / 5
    print(f'{c} C = {f} F')

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    tempo_decorrido = int(input('Tempo Decorrido (min): '))
    velocidade_media = int(input('Velocidade Média (km/h): '))
    distancia = tempo_decorrido/60 * velocidade_media
    litros_consumidos = distancia / 12
    print(f'Distância: {distancia}')
    print(f'Litros Consumidos: {litros_consumidos}')

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    valor_prestacao_vencida = float(input('Valor da Prestação Vencida: R$ '))
    taxa_juros = int(input('Taxa de Juros Diária(%): '))
    dias_atraso = int(input('Dias de Atraso: '))
    juros = valor_prestacao_vencida * (dias_atraso*taxa_juros/100)
    valor_prestacao_final = valor_prestacao_vencida + juros
    print(f'Multa por atraso: R$ {juros}')
    print(f'Valor da Prestação Atualizada: R$ {valor_prestacao_final}')

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    dolares = round(float(input('US$: ')),2)
    cotacao = round(float(input('Valor do dólar: R$ ')),2)
    print(f'Qtde de Reais: R$ {round(dolares*cotacao,2)}')