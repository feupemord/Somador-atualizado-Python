cont = 0
resp = 0
number2 = 0
number1 = 0

nome = str(input('\nQual seu nome\t\n' '\n Resp: ' ))
idade = int(input('\nQual sua idade\n[Idade Permitida Maior de 13 e Menor de 90]\t\n''Resp: '))
while (nome == None):
   nome = str(input('\nQual seu nome\t' '\n Resp: ' ))

#for nomes in nome == None:
#   print(nome,"Esta fazendo Errado")

while( idade <=12 or idade>90):
    idade = int(input('\nQual sua idade\t''\n Resp: '))

print('\nNome: ', nome, '\nIdade: ', idade)
cont = cont+1


print('Seu primeiro numero: ',number1)
number1 = int(input('\nNumero [1] ''\n Resp: '))

while(number1 == 0):
    print('\nDigite um número maior que 0\n' *5)

    number1 = int(input('\nNumero [1] ''\n Resp: '))
    print('Seu primeiro numero: ',number1)

number2 = int(input('\nNumero [2]' '\nResp: '))
print(number2)

while(number2 == 0):
    print('\nDigite um número maior que 0\n' *5)
    number2 = int(input('\nNumero [2] ''\n Resp: '))
    print('Seu segundo numero:',number2)

resp = (number1+number2)
print('\nSua Resposta é igual [Soma]: ', resp)

resp = (number1 - number2)
print('\nSua Resposta é igual[Subtração]', resp)

resp = (number1/number2)
print('\nSua Resposta é igual [Divisão]', resp)

resp = (number1 * number2)
print('\nSua Resposta é igual [Vezes 2]', resp)    

print("\nObrigado por utilizar: ", nome ,'\nCriador -> FeupeMord')

