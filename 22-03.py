# #1
# try:
#     num= int(input('Digite um número:'))
#     if num >= 0:
#         print('O número é positivo.')
#     else:
#         print('O número é negativo.')
#     print('')
# except:
#     print('Digite apenas números.')
#
# #2
# num1= int(input('Digite um número:'))
# num2= int(input('Digite outro número:'))
# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# else:
#     print('Os números são iguais.')
# print('')
#
# #3
# a= int(input('Digite o valor de A:'))
# b= int(input('Digite o valor de B:'))
# c= int(input('Digite o valor de C:'))
# if (a+b)<c:
#     print(c,' é maior que ',a+b)
# elif (a+b)==c:
#     print('Os números são iguais.')
# else:
#     print(a+b, 'é maior que ', c)
#
# #4
#
# sexo= (input('Sexo (F ou M):'))
# if sexo == 'f' or sexo == "F":
#     print('Feminino.')
# elif sexo == 'm' or sexo == 'M':
#     print('Masculino.')
# else:
#     print('Sexo inválido.')
# print('')
#
# #5
# try:
#
#     num= int(input('Digite um número:'))
#     if  (num%2==0):
#         print('O número é par.')
#     else:
#         print('O número é impar.')
# except:
#     print('Digite apenas números inteiros!')
#
# #6
# try:
#     num= int(input('digite um número: '))
#     if (num%2==0):
#         print(num, ' + 5 = ', num+5)
#     else:
#         print(num,'+ 8 = ', num+8)
# except:
#     print('Digite apenas números inteiros!')
#
# #7
# try:
#     prova= float(input('Digite a nota da prova: '))
#     trabalho= float(input('Digite a nota do trabalho:'))
#     if (prova+trabalho)/2>=60:
#         print('Média: ',(prova+trabalho)/2, 'Aprovado!')
#     else:
#         print('Média: ',(prova+trabalho)/2, 'Reprovado!')
# except:
#     print('Digite apenas números!')
#
# #8
# try:
#     a= float(input('Digite o valor de A: '))
#     b= float(input('Digite o valor de B: '))
#     c= float(input('Digite o valor de C: '))
#     if a>b and a>c:
#         print ('O maior é:',a)
#     elif b>a and b> c:
#         print('O maoir é: ',b)
#     else:
#         print('O maior é: ',c)
# except:
#     print('Digite apenas números!')
#
# #9
# try:
#     a= float(input('Digite o valor de A: '))
#     b= float(input('Digite o valor de B: '))
#     c= float(input('Digite o valor de C: '))
#     if a>b and a>c and b>c:
#         print(a,',',b,',',c)
#     elif a>b and a>c and c>b:
#         print(a,',',c,',',b)
#     elif b>a and b>c and a>c:
#         print(b,',',a,',',c)
#     elif b>a and b>c and c>a:
#         print(b,',',c,',',a)
#     elif c>a and c>b and b>a:
#         print(c,',',b,',',a)
#     else:
#         print(c,',',a,',',b)
# except:
#     print('Digite apenas números!')
#
#10
# try:
#     print('=====Menu de opções:=====')
#     print('1. Soma de 2 números:')
#     print('2. Potência de um número:')
#     print('3. Raiz de grau N:')
#     op= int(input('Digite a opção desejada: '))
#     if op==1:
#         num1= int(input('Digite o primeiro número: '))
#         num2= int(input('Digite o segundo número: '))
#         print('A soma é:', num1+num2)
#     elif op==2:
#         num3= int(input('Digite um número: '))
#         pot= int(input('Digite a potencia a ser elevado: '))
#         print(num3, 'elevado à ',pot,'é igual a: ',num3**pot)
#     elif op==3:
#         num4= int(input('Digite um número:'))
#         raiz= int(input('Digite o valor da potência da raiz:'))
#         print('A raiz',raiz, 'de',num4,'é: ',num4**(1/raiz))
#     else:
#         print('Escolha entre 1, 2 e 3!')
# except:
#     print('Digite apenas números!')

#11
try:
    preco=float(input('Digite o valor do produto:'))
    print
