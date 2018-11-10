from classServidor import Server
from classWord import Word
import json
import random
class Game():
    def __init__(self):
        self.S = Server()
        self.listaWords = []
        self.listaWords.append(Word(['g','i','r','a','f','a'], "Animal"))
        self.listaWords.append(Word(['b','a','l','e','i','a'], "Animal"))
        self.listaWords.append(Word(['g','a','t','o'], "Animal"))
        self.listaWords.append(Word(['c','o','p','o'], "Objeto"))
        self.listaWords.append(Word(['p','o','r','t','a'], "Objeto"))
        self.listaWords.append(Word(['p','e','n','t','e'], "Objeto"))
        self.listaWords.append(Word(['i','n','g','l','a','t','e','r','r','a'], "Lugar"))
        self.listaWords.append(Word(['b','r','a','s','i','l'], "Lugar"))
        self.listaWords.append(Word(['k','u','r','o','s','h','i','t','s','u','j','i'], "Anime"))


    def palavra_do_jogo(self, sockJogador):
        while True:
            palavraEscolhida = self.listaWords[random.randint(0, len(self.listaWords) -1)]        
            informacoes = {"dica" : palavraEscolhida.dica,
                           "tamanho" : palavraEscolhida.tamanho}
            informacoes = json.dumps(informacoes)
            self.S.enviaRespostaRequisicao(sockJogador, informacoes)
            continuar = self.testar_letra(sockJogador, palavraEscolhida)
            if not continuar:
                print("End Game")
                break
            #print("vamos continuar com a festa!")

        self.S.fecharConecServer(sockJogador)


    def testar_letra(self, sockJogador, palavraEscolhida):
        listaLetrasJogadas = []
        for i in range(palavraEscolhida.tamanho):
            listaLetrasJogadas += ['_ ']    
        acertou = 0
        while True:                
            achou = 0
            letraRecebida = self.S.recebeRequisicao(sockJogador)
            letraRecebida = json.loads(letraRecebida)
            #print("recebi : " + letraRecebida)
            for i in range(palavraEscolhida.tamanho):
                if letraRecebida == palavraEscolhida.palavra[i] and listaLetrasJogadas[i] == '_ ':
                    achou = 1
                    acertou += 1
                    listaLetrasJogadas[i] = letraRecebida     
                    if acertou == palavraEscolhida.tamanho:                 
                        resposta = json.dumps({"continua" : "end" , "posicao" : str(i)})
                    else:
                        resposta = json.dumps({"continua" : "s" , "posicao" : str(i)})
                    self.S.enviaRespostaRequisicao(sockJogador, resposta)
                    break
            if acertou == palavraEscolhida.tamanho:
                continua = self.S.recebeRequisicao(sockJogador)
                continua = json.loads(continua)
                if continua == "s":
                    self.S.enviaRespostaRequisicao(sockJogador, json.dumps(True))
                    return True
                else:
                    self.S.enviaRespostaRequisicao(sockJogador, json.dumps(False))
                    return False
            if achou == 0:
                resposta = json.dumps({"continua" : "n"})
                self.S.enviaRespostaRequisicao(sockJogador, resposta)
  