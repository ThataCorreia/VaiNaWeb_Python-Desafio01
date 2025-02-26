# Enunciado : O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

nota = int(input("Insira sua nota:"))

if nota >= 6:
    print("Parabéns, voce foi aprovado !")
else:
    print("Que pena, você foi reprovado, mas não desista, estude um pouco mais e vamos mudar essa situação :D")