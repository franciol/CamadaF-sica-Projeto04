
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

    #img = Image.open('dragon.jpg', mode='r')

    #imgByteArr = io.BytesIO()
    #img.save(imgByteArr, format='JPEG')
    #imgByteArr = imgByteArr.getvalue()
    # Inicializa enlace ... variavel com possui todos os metodos e propriedades do enlace, que funciona em threading
    com = enlace(serialName)

    # Ativa comunicacao
    com.enable()

    #verificar que a comunicacao foi aberta
    print("comunicacao aberta")


    # a seguir ha um exemplo de dados sendo carregado para transmissao
    # voce pode criar o seu carregando os dados de uma imagem. Tente descobrir
    '''
    #como fazer isso
    print ("gerando dados para transmissao :")



    txBuffer = imgByteArr
    txLen2 = 20
    '''

    '''
    print(txLen)

    # Transmite dado
    print("tentado transmitir .... {} bytes".format(txLen))
    com.sendData(txBuffer)


    # Atualiza dados da transmissao
    txSize = com.tx.getStatus()
    '''

    # Faz a recepcao dos dados
    print ("Recebendo dados .... ")
    bytesSeremLidos=com.rx.getBufferLen()
    print(bytesSeremLidos)


    rxBuffer, nRx = com.getData(bytesSeremLidos)
    print(rxBuffer)


    # log
    print ("Lido              {} bytes ".format(nRx))

    print (rxBuffer)
    print(len(rxBuffer))


    # Encerra comunicacao
    print("-------------------------")
    print("Comunicacao encerrada")
    print("-------------------------")
    com.disable()
    rxBuff = io.BytesIO(rxBuffer)
    img = Image.open(rxBuff)
    draw = ImageDraw.Draw(img)
    img.show()
    img.save('/home/francisco/Documentos/Insper /Semestre4/Camada Física da Computação/Projeto02/SalvarArquivo/ImagemEnviadaFinal.jpg')
    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
