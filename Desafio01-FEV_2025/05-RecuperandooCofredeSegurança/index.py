# Enunciado : O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo. Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

senha = input("Por favor, insira a senha: ")

if senha == "Python123":
  print("Acesso concedido!")
else:
  print("Senha errada, tente outra vez.")