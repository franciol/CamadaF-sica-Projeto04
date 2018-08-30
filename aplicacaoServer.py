
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
# Camada Fisica da Computacao
#Carareto
#17/02/2018
#  Aplicacao
####################################################

def fromByteToInt(bytes):
    result=0

    for b in bytes:
        result=result*256+int(b)

    return result


print("comecou")

from enlace import *
import time
from PIL import Image,ImageDraw
import io,os


# voce deveradescomentar e configurar a porta com atraves da qual ira fazer a
# comunicacao
# Serial Com Port
#  para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
serialName = "/dev/tty.usbmodem1421" # Mac    (variacao de)
#serialName = "COM4"                  # Windows(variacao de)



print("porta COM aberta com sucesso")



def main():


    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()


    #verificar que a comunicacao foi aberta
    print("comunicacao aberta")




    # Faz a recepcao dos dados

    #A FAZER: listener de pacotes
    #SE RECEBEU 1,
    com.sendData(None, 2)
    

    SentMessage2 = time.time()

    while time.time() < SentMessage2 + 5:
        resultData, resultDataLen, messageType = com.getData();
        if messageType == 3:

        #A FAZER: receber message3
        #SE RECEBIDO: goto recebendo dados

    if time.time() > SentMessage2 + 5:
        com.sendData(None, 9)
        goto comStart



    print ("Recebendo dados .... ")
    bytesSeremLidos=com.rx.getBufferLen()
    print(bytesSeremLidos)
    #confirmar que se trata de message4


    rxBuffer, nRx = com.getData(bytesSeremLidos)
    print(rxBuffer)


    # log
    print ("Lido              {} bytes ".format(nRx))

    print ('rxBuffer 'rxBuffer)
    print('len(rxBuffer)'len(rxBuffer))

    #A FAZER: LISTENER MENSAGEM
    #SE recebeu Message7, goto ComEnd

    # Encerra comunicacao
    print("-------------------------")
    print("Comunicacao encerrada")
    print("-------------------------")
    com.disable()
    rxBuff = io.BytesIO(rxBuffer)
    img = Image.open(rxBuff)
    draw = ImageDraw.Draw(img)
    img.show()
    #img.save('/home/francisco/Documentos/Insper /Semestre4/Camada Física da Computação/Projeto02/SalvarArquivo/ImagemEnviadaFinal.jpg')
    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
