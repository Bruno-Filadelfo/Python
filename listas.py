carros = ["Ferrari", "Mercedez", "Fusca", "Mazarack", "Toyota"] #01
print("Eu " 'Gostaria de ter uma ' + carros[0]) #01

carros = ["Ferrari", "Mercedez", "Fusca", "Mazarack", "Toyota"]  #02
print(carros)   #02

carros[2] = "Cadilac" #troquei de carro  #03
print(carros)  #03

carros.append("BMW") #adiciona o ultimo elementos ao final de uma lista existente, acrescenta   #04
print(carros)   #04

carros.insert(1, "Porshe") #Insere um item em uma dada posição.  #05
print(carros)   #05

carros.extend("Fusca") #extend adiciona vários valores  #06
print(carros)    #06

del carros[0]  #08 apaga definitivamente 
print(carros)  #08  

carros.pop()  #09 Ele tira o ultimo elemento da letra da lista
print(carros) #09

carros.remove("Toyota") #10pode remover um valor especificado dentro dos parênteses. 
print(carros)           #10

carros.sort() #serve para deixar a lista em ordem alfábetica
print(carros)

carros.sort(reverse=True) #deixa a lista em ordem alfábetica porem em versa 
print(carros)

print(sorted(carros)) #classificado volta ao normal
print(carros)

print(len(carros))  #o len vai trazer a quantidade de elementos que eu tenho da lista 

carros.reverse() #serve para inverter a ordem dos elementos em uma lista Python usando o método reverse()
print(carros)

