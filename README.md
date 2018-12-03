#PD6 - Ultilização de uma CNN projetada para classificar imagens no contexto de reconhecimento de fala

Igor Bispo de Moraes = 170050432
Hevelyn Sthefany = 170059031

## Pré-requisitos

O programa foi escrito em Python 3 e requer as seguinte bibliotecas:
- cv2
- numpy
- matplotlib
- glob
- keras
- scipy
- sounddevice
- os 
- plaidml-keras


## Execucao

### Treinamento e Teste:



#### É preciso estar contido no diretório principal a pasta com a base de dados. Tal base de dados pode ser .... lugar

### Predição
Para executar, vá até a pasta src e execute:

python predict_live.py

Por meio de um microfone, fale por 1 segundo a palavra a ser predita. O programa mostrará uma janela com a imagem real do espectrograma do áudio obtido e apresentará no terminal a palavra predita.

A palavra falada deve estar contido no seguinte conjunto: 'backward', 'bed', 'bird', 'cat', 'dog', 'down', 'eight', 'five', 'follow', 'forward', 'four', 'go', 'happy', 'house', 'learn', 'left', 'marvin', 'nine', 'no', 'off', 'on', 'one', 'right', 'seven', 'sheila', 'six', 'stop', 'three', 'two', 'up', 'visual', 'wow', 'yes', 'zero'.
