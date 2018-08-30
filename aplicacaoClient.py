
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Fisica da Computacao
#Carareto
#17/02/2018

####################################################



def int_to_byte(values, length):
    result = []
    for i in range(0,length):
        result.append(values >> (i*8)& 0xff)

    result.reverse()

    return result


print("comecou")

from enlace import *
import time
from PIL import Image,ImageDraw
import io,os
import tkinter as tk
import tkinter.filedialog as fdlg


# voce devera descomentar e configurar a porta com atraves da qual ira fazer a
# comunicacao
# Serial Com Port
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/cu.usbmodem1421" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)



print("porta COM aberta com sucesso")



def main():

    nasme = fdlg.askopenfilename()
    img = Image.open(nasme, mode='r')

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    label: comStart
    com.enable()
    com.sendData(None, 1)
    SentMessage1 = time.time()

    while time.time() < SentMessage1 + 5:
        #A FAZER: receber message2
        #SE RECEBIDO: goto comOpen

    if time.time() > SentMessage1 + 5:
        com.sendData(None, 8)
        goto comStart 



    #verificar que a comunicacao foi aberta
    label: comOpen
    print("comunicacao aberta")


    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    #como fazer isso
    print ("gerando dados para transmissao :")
    com.sendData(None, 3)



    txBuffer = imgByteArr
    txLen = len(imgByteArr)

    label: comSend
    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))

    com.sendData(txBuffer, 4)


    # Atualiza dados da transmissao
    txSize = com.tx.getStatus()



    #A FAZER: listener de dados recebidos
    #SE RECEBEU 6, goto comStart
    #SE RECEBEU 7, goto comEnd
    #SE RECEBEU 5, goto comEnd
    
    label: comEnd
    # Encerra comunicacao
    print("-------------------------")
    print("Comunicacao encerrada")
    print("-------------------------")
    com.sendData(None, 7)
    com.disable()


    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
