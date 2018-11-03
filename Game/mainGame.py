from threading import Thread
from classGame import Game

if __name__ == "__main__":
    G = Game()
    while True:
        socJogador = G.S.conectar()
        Thread(target=G.palavra_do_jogo, args=(socJogador,)).start()