from PIL import Image,ImageDraw
import io,os

EOP = b'/00/00/00/00'
stuffingByte = b'/7a/'



def int_to_byte(values, length):
    result = []
    for i in range(0,length):
        result.append(values >> (i*8)& 0xff)

    result.reverse()

    return result

def fromByteToInt(bytes):
    result=0

    for b in bytes:
        result=result*256+int(b)

    return result


def encapsulate(payload, messageType):



    txLen = len(payload)
    print('txLen: 'txLen)
    '''
        Head = 10 bytes:
            payloadLen = 5 bytes
            EOP = 13 bytes
            stuffing = 3 bytes
    '''
    payloadfinal = bytes()
    for i in range(0, len(payload)):
        if EOP == payload[i:i+13]:
            payloadfinal+=stuffingByte
            payloadfinal+=payload[i:i+1]
        else:
            payloadfinal+=payload[i:i+1]

    payloadLen = int_to_byte(txLen,5)
    
    if messageType == 1:
        head = bytes([1])+bytes(payloadLen)+EOP+stuffingByte
        #Cliente manda pedido de comunicação para servidor
    
    elif messageType == 2:
        head = bytes([2])+bytes(payloadLen)+EOP+stuffingByte
        #Servidor responde cliente dizendo que recebeu mensagem tipo 1

    elif messageType == 3:
        head = bytes([3])+bytes(payloadLen)+EOP+stuffingByte    
        #Cliente responde servidor dizendo que recebeu mensagem tipo 2
        #e servidor sabe que a próxima mensagem é tipo 4

    elif messageType == 4:
        head = bytes([4])+bytes(payloadLen)+EOP+stuffingByte
        #Cliente faz efetivamente transmissão para servidor

    elif messageType == 5:
        head = bytes([5])+bytes(payloadLen)+EOP+stuffingByte
        #acknowledge do servidor para cliente confirmando recebimento 
        #correto do payload

    elif messageType == 6:
        head = bytes([6])+bytes(payloadLen)+EOP+stuffingByte
        #nacknowledge do servidor para cliente pedindo reenvio do pacote por 
        #erro de transmissão

    elif messageType == 7:
        head = bytes([7])+bytes(payloadLen)+EOP+stuffingByte
        #Pedido de encerramento da mensagem

    elif messageType == 8:
        head = bytes([8])+bytes(payloadLen)+EOP+stuffingByte
        #Erro tipo 1: cliente não recebeu mensagem tipo 2

    elif messageType == 9:
        head = bytes([9])+bytes(payloadLen)+EOP+stuffingByte
        #Erro tipo 2: servidor não recebeu mensagem tipo 3

    elif messageType == 0:
        head = bytes([0])+bytes(payloadLen)+EOP+stuffingByte
        #Erro tipo 3: não recebeu ack ou nack em 5 segundos

    else:
        head = None 
        #messageType fora do protocolo e portanto byte não deve ser formado com HEAD


    all = bytes()
    all += head
    all += payload
    all += EOP
    print("\n Head len:  ",len(head))

    return all



def readHeadNAll(receivedAll):

    head = receivedAll[0:21]

    txLen = fromByteToInt(head[0:5])

    eopSystem = head[5:17]
    print('END OF PACKAGE', eopSystem)
    stuffByte = head[17:21]

    sanityCheck = bytearray()
    stuffByteCount = 0

    for i in range(21, len(receivedAll)):
        if receivedAll[i:i+1] == stuffByte:
            sanityCheck += receivedAll[i+1:i+14]
            i +=14
        elif eopSystem == receivedAll[i:i+13]:
            print('EOP: 'receivedAll[i:i+13])
            break

        else:
            sanityCheck += receivedAll[i:i+1]


    print('SanityCheck ', sanityCheck)
    if len(sanityCheck) == txLen:

        print ("sanityCheck = okay")
        return sanityCheck, txLen

    '''
    ATENÇÃO: TROCAR ELSE POR TRATAMENTO DE ERROS VIA PROTOCOLO MESSAGETYPE

    '''

    # else:
    #     print ("\n\n ERRO  \n\n HOUVE FALHA NA TRANSMISSÃO. FECHANDO APLICAÇÃO… TENTE NOVAMENTE.")
    #     quit()




def teste():
    img = Image.open('circuit.jpg', mode='r')
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    testeSubject = encapsulate(imgByteArr)
    print('testeSubject 'testeSubject)
    txLenRead, txLenRead2 = readHeadNAll(testeSubject)

    print("\n Reading TxLen:     ",txLenRead )
    print("\n Reading Txlen: ", txLenRead2)
