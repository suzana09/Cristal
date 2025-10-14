#Arquivos-


#Extensões de arquivos

#.pdf
#.jpeg/ .jpg
#.png
#.py



#Abrindo arquivos-

#open()-Recebe o caminho até o arquivo 

#arquivo= open('./texto.txt')

#operacoes em arquivos

#r(ready only)-> Apenas leitura
#w(write only)-> Apenas escrita
#a(append)-> Escreve algo no final do arquivo
#r+(read and write)-> le e escreve dentro de um arquivo

#Lendo um arquivo
#read()

#print(arquivo.read())

#Seek- Volta o ponteiro para o inicio do arquivo
#print(arquivo.seek)

#Readline()- le linhas do arquivo, obs: linhas vazias serao lidas
#print(arquivo.readline())



#Lendo arquivos com loop for

#for i, linha in enumerate(arquivo):
 #   print(f)


#Escrevendo um arquivo
#write()- Funcao usada para escreverem em um

#arquivo= open('./texto.txt,write')

#arquivo.write('testando a funcao write')





#Exercicio-1

def guarda_nome(nome):
    with open('./exercicio.txt') as arquivo:
        arquivo.write(nome+'\n')
    print('o nome foi adicionado com sucesso')


#nome= input('digite um nome para ser  adicionado a lista: \n----->')
guarda_nome


              












