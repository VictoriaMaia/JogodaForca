from classCliente import Cliente
import json

C = Cliente()

def continuarJogo():
    while True:
        continuar = input("Deseja continuar jogando ? [s/n] ")
        if continuar == "s" or continuar == "n":
            continuajogo = json.dumps(continuar)
            C.enviarRequisicao(continuajogo)
            break
        else:
            print("Por favor me responda direito. Oxe!")

    respostaContinuar = json.loads(C.recebeResposta())
    return respostaContinuar



if __name__ == "__main__":
    print("Bem vindo ao jogo da Forca mais cuti cutinho que você já jogou ;)")
    while True:
        palavra = C.recebeResposta()
        informacoes = json.loads(palavra)
        dica = informacoes["dica"]
        tamanho = int(informacoes["tamanho"])
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
                letra = json.dumps(letraDigitada[0])
                C.enviarRequisicao(letra)
                respostaRecebida = C.recebeResposta()
                respostaRecebida = json.loads(respostaRecebida)
                continua = respostaRecebida["continua"]
                if continua == "n":
                    print("Errou!")

                elif continua == "end":
                    posicao = respostaRecebida["posicao"]
                    posicao = int(posicao)
                    palavraAcertar[posicao] = letraDigitada[0]
                    print(''.join(palavraAcertar))
                    print("You win!")
                    break

                else:
                    posicao = respostaRecebida["posicao"]
                    posicao = int(posicao)
                    palavraAcertar[posicao] = letraDigitada[0]
                    print(''.join(palavraAcertar))
        
        if not continuarJogo():
            print("Ok. Obrigada por jogar")
            break
        

    print("Fechando conexão e indo simbora")
    C.fechaConexao()
