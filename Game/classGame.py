from classServidor import Server
from classWord import Word
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


    def palavra_do_jogo(self, sockJogador):
        while True:
            palavraEscolhida = self.listaWords[random.randint(0, len(self.listaWords) -1)]        
            #mandar as informações dica e tamanho
            informacoes = palavraEscolhida.dica
            informacoes += "!" + str(palavraEscolhida.tamanho)
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
        #print(''.join(listaLetrasJogadas))
        acertou = 0
        while True:                
            achou = 0
            letraRecebida = self.S.recebeRequisicao(sockJogador)
            #print("recebi : " + letraRecebida)
            for i in range(palavraEscolhida.tamanho):
                if letraRecebida == palavraEscolhida.palavra[i] and listaLetrasJogadas[i] == '_ ':
                    achou = 1
                    acertou += 1
                    listaLetrasJogadas[i] = letraRecebida                   
                    self.S.enviaRespostaRequisicao(sockJogador, str(i))
                    break
            if acertou == palavraEscolhida.tamanho:  
                #print("Ganhou, vamos continuar?") 
                continua = self.S.recebeRequisicao(sockJogador)
                if continua == "s":
                    return True
                else:
                    return False
            if achou == 0:
                self.S.enviaRespostaRequisicao(sockJogador, "n")
  