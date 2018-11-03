from classCliente import Cliente

C = Cliente()

def continuarJogo():
    while True:
        continuar = input("Deseja continuar jogando ? [s/n]")
        if continuar == "s":
            C.enviarRequisicao("s")
            return True
        if continuar == "n":
            print("Ok. Obrigada por jogar")
            C.enviarRequisicao("n")
            return False
        else:
            print("Por favor me responda direito. Oxe!")




if __name__ == "__main__":
    print("Bem vindo ao jogo da Força mais cuti cutinho que você já jogou ;)")
    while True:
        palavra = C.recebeResposta()
        informacoes = palavra.split('!')
        dica = informacoes[0]
        tamanho = int(informacoes[1])
        acertou = 0
        palavraAcertar = []
        for i in range(tamanho):
            palavraAcertar += ['_ ']    
        print("A palavra é um : " + dica)
        print(''.join(palavraAcertar))
        while True:
            letraDigitada = input("Digite uma letra: ")
            if len(letraDigitada) == 0:
                print("Desculpe, mas tem que digitar algo seu mané")
            else:
                C.enviarRequisicao(letraDigitada[0])
                resposta = C.recebeResposta()
                if resposta == "n":
                    print("Errou!")
                else:
                    acertou += 1
                    posicao = int(resposta)
                    palavraAcertar[posicao] = letraDigitada[0]
                    print(''.join(palavraAcertar))
                    if acertou == tamanho:
                        print("You win!")
                        break
        
        if not continuarJogo():
            break
        

    print("Fechando conexão e indo simbora")
    C.fechaConexao()
