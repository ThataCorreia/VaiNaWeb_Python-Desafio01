# Enunciado : O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = int(input("Por favor, insira sua idade:"))

if idade >= 16:
  print ("Ok, você pode votar!")
else:
  print ("Você ainda não pode votar, volte quando tiver 16 anos.")