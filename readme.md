# Trabalho final da cadeira de Sistemas Distribuidos 2018.2 - Jogo da forca


Nesse jogo o jogador recebe duas dicas sobre a palavra a ser descoberta:

1. O tamanho;

2. Sobre o que é a palavra. Exemplo: objeto, animal, etc.

A funcionalidade é igual ao jogo original. O jogador digita uma letra e é mostrado se a letra pertence ou não a palavra até o jogador acertar todas as letras. As chances são ilimitadas, sem ter perigo de morrer, como acontece no jogo original.




O jogo da força foi desenvolvido utilizando:

- Python 3.6;
- Comunicação em socket utilizando TCP;
- Representação externo dos dados com JSON.


Existe 4 classes no algoritmo:

- ClassCliente - responsável por:
    - mandar e receber mensagens,
    - fechar a conexão da parte do cliente; 
- ClassServidor - responsável por:
    - conectar um cliente,
    - mandar e receber mensagens,
    - fechar a conexão;
- ClassWord - responsável por armazenar: 
    - a palavra,
    - a dica ,
    - o tamanho;
- ClassGame - responsável por:
    - mandar uma palavra aleatória para o cliente, 
    - receber uma letra do cliente ,
    - testar se a letra recebida pertence a palavra.
