#Aluno1: padronizar nome do filme
def formatar(nome):
    return nome.upper()
#aluno2: Verificador de idade
def verificar_idade(idade):
    if idade >= 18:
        return "autorizado"
    else:
        return "não autorizado"
#Aluno3: Mensagem de retorno
def gerar_mensagem(status):
    if status == "Autorizado":
        return "Tenha uma otima sessão!"
    else:
        return "Sentimos, mas você não tem a idade minima!"
    #Aluno4: Execução do algoritimo
    filme_entrada = input("Digite o nome do filme escolhido!")
    idade_entrada = int(input("Digite sua idade!"))
    nome_final = formatar(filme_entrada)
    status_acesso = verificar_idade(idade_entrada)
    mensagem = gerar_mensagem(status_acesso)
    print(f"\nfilme:{nome_final}")
    print(f"Status:{status_acesso}")
    print(f"menssagem:{mensagem}")


    
