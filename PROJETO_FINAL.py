titulo = '\n****** PROJETO FINAL DO CURSO DE INTRODUÇÃO Á PROGRAMAÇÃO PYTHON ******\n'
print(titulo.center(20,'*'))

  
totalAlunos = 0
totalAprovados_F = 0
totalAprovados_M = 0
totalExame_F = 0
totalExame_M = 0
totalReprovados_F = 0
totalReprovados_M = 0
totalAlunos_Feminino = 0
totalAlunos_Masculino = 0

while True:
    novo = input('Deseja iniciar o cadastro das notas do aluno (S/N)? ').upper()
    if novo == 'S' or novo == 's':
        totalAlunos += 1
        nome_aluno = input('\nInforme o nome do aluno: ')
        sexo_aluno = input('Informe o sexo do aluno (F/M): ').upper()
        if sexo_aluno != 'F' and sexo_aluno != 'M':
            raise EnvironmentError
    
    else:
        break
    
  

while (novo == 'S'):
    
    while (sexo_aluno != 'F' and sexo_aluno != 'M'):
        print('Opção Invalida')
        sexo_aluno = input('Informe "F" para o sexo Feminino e "M" para o sexo Masculino: ').upper()

    #alunos por sexo
    if (sexo_aluno == 'F'):
        totalAlunos_Feminino += 1
    else:
        totalAlunos_Masculino += 1

    nota1 = float(input('\nInforme a primeira nota: '))
    while (nota1 <0 or nota1 >10):
        print('Opção Invalida')
        nota1 = float(input('O valor da nota deve estar entre "0" e "10", digite novamente: '))

    nota2 = float(input('Informe a segunda nota: '))
    while (nota2 < 0 or nota2 > 10):
        print('Opção Invalida')
        nota2 = float(input('O valor da nota deve estar entre "0" e "10", digite novamente: '))

    nota3 = float(input('Informe a terceira nota: '))
    while (nota3 < 0 or nota3 > 10):
        print('Opção Invalida')
        nota3 = float(input('O valor da nota deve estar entre "0" e "10", digite novamente: '))

    media = float (nota1 + nota2 + nota3) / 3
    print('%.2f' % media)

    #teste de notas

    if sexo_aluno == 'F':
        if media >= 7:
            totalAprovados_F += 1
    else:
        if media >= 7:
            totalAprovados_M += 1
    if sexo_aluno == 'F':
        if 4 <= media < 7:
            totalExame_F += 1
    else:
        if 4 <= media < 7:
            totalExame_M += 1
    if sexo_aluno == 'F':
        if media < 4:
            totalReprovados_F += 1
    else:
        if media < 4:
            totalReprovados_M += 1

    novo = input('\nDeseja continuar o cadastro das notas do aluno (S/N)? ').upper()
    while (novo != 'S' and novo != 'N'):
        print('Opção Invalida')
        novo = input('Informe "S" para Sim e "N" para Não: ').upper()
else:
    resultados = '\n\n****** Apesentar os resultados finais ******\n\n'
    print(resultados.center(20,"*"))

print('Total de Alunos Cadastrados', totalAlunos)

print('Percentual de alunos Aprovados: ', (totalAprovados_F + totalAprovados_M)*100/totalAlunos, '%')
print('Percentual de alunos de Exame: ', (totalExame_F + totalExame_M)*100/totalAlunos, '%')
print('Percentual de alunos Reprovados: ', (totalReprovados_F + totalReprovados_M)*100/totalAlunos, '%')

print('Total de alunos do sexo Feminino: ', totalAlunos_Feminino)
print('Total de alunos do sexo Masculino: ', totalAlunos_Masculino)
print('Total de alunos do sexo Feminino Aprovados: ', totalAprovados_F )
print('Total de alunos do sexo Masculino Aprovados: ', totalAprovados_M)
print('Total de alunos do sexo Feminino de Exame: ', totalExame_F)
print('Total de alunos do sexo Masculino de Exame: ', totalExame_M)
print('Total de alunos do sexo Feminino Reprovados: ', totalReprovados_F)
print('Total de alunos do sexo Masculino Reprovados: ', totalReprovados_M)
