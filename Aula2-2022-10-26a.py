# comando input(): quero permitir que
# o usuário digite algo...
nome = input("Informe seu nome: ")
#pede a idade para o usuário "Qual sua idade?"
idade= int(input("Digite sua idade: "))

#comando de saída..exibir na tela
print(f"boa noite, seu nome é {nome}")
#exiba "Sua idade é..."
print("Sua idade é {}".format(idade))

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O obro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else: 
  print("Voce é xóven ainda, xóven ainda..")

#E se eu quissese perguntar o gênero (M= Masculino e F = Feminino)
#Mostre (...e voce também precisa/precisou prestar serviço militar obrigatório)
  
genero = input("Informe seu genêro M= Masculino, F= Feminino, O=Outros: ")
if idade >=18 and genero == "M":
  print("... e você também precisa/precisou prestar serviço militar obrigatório")
