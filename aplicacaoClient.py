
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

def sistemaEnvio(payload, com):
    com.enable()
    print("porta COM aberta com sucesso")


    #Variaveis
    ouvindoresposta1 = True



    while ouvindoresposta1:
        #Tipo 1: Ver se tem alguem ouvindo
        com.sendData(None,1)
        print("Mensagem 1 enviada")
        SentMessage1 = time.time()
        bytesSeremLidos = None
        while time.time() < SentMessage1 + 5:
            print("Entrou na leitura de Buffer para 2")
            bytesSeremLidos=com.rx.getBufferLen()
        if bytesSeremLidos != None:
            print("bytesseremlidos: ",bytesSeremLidos)
            resultData, resultDataLen, messageType = com.getData(bytesSeremLidos)
            if messageType == 2:
                print("mensagem tipo 2 Chegou\n")
                print("comunicacao aberta")
                ouvindoresposta1 = False
                break
        print("Resposta do servidor não recebida, reenvio do mensagem de tipo 1")


    print("Enviando mensagem para confirmar que ouviu")
    com.sendData(None,3)

    time.sleep(10)

    #print("tentado transmitir .... {} bytes".format(txLen))
    print("Enviando Informação")
    com.sendData(payload,4)




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
serialName = "COM4"                  # Windows(variacao de)






def main():

    nasme = fdlg.askopenfilename()
    img = Image.open(nasme, mode='r')

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    sistemaEnvio(imgByteArr, com)
    #verificar que a comunicacao foi aberta


    # Atualiza dados da transmissao
    txSize = com.tx.getStatus()



    #A FAZER: listener de dados recebidos
    #SE RECEBEU 6, goto comStart

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
