#relembrando aula 6

#tupla- um tipo de lista que nao pode ter seus valores alterados
# sets- uma lista que so aceita valores unicos

#Dicionarios-estrutura que armazena chave e valor

#carro={'marca':'peugeot',
#    'motor': 'V12'
# } 
#carro['cor']= 'branco'
#print(carro)



#Aula 7- Funçoes-

#Para declarar uma funcao utilizamos a palavra reservada: def

def boas_vindas():
    print('Seja bem vindo!')
boas_vindas()

#Funcao com parametros

def boas_vindas_usuario(nome):
    print('seja bem vindo',nome)
boas_vindas_usuario('maria')
boas_vindas_usuario('susu')


# Exercicios

#1-Crie uma funcao que exiba uma informacao qualquer no console

def lista_de_classificados():
    print('Voce não foi classificado!')
lista_de_classificados()


#2- Crie uma funcao que receba uma parametro e mostre uma mensagem utilizando esse parametro

def lista_de_desclassificados_feminino(nome):
    print('nao foi',nome)
lista_de_desclassificados_feminino('maria')


def somar(a,b):
   print(a+b)
somar(10,25)

def velocidade(distancia,tempo):
    print(distancia/tempo)





#arguments
def prepara_acai(itens, tamanho):
    print('preparando um acai de', tamanho, 'com os ingredientes')

    for ingrediente in itens:
        print('-',ingrediente)
prepara_acai(ingrediente='amendoim',tamanho='1L')



#Funcoes que retornam valores

def diminuir(a,b):
    return a-b
resultado= diminuir(5,2)
print('O resultado é:', resultado)

#Funcoes recursivas- Funcoes que chama 

def dobra_lencol(lencol, gaveta):
    if lencol< gaveta:
        return 0 
    else:
        return 1+ dobra_lencol(lencol/2, gaveta)
print(dobra_lencol(200,25))




