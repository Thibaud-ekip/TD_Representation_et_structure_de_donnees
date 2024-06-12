import struct







def open_wav(path):

    """Open file wav and give its content"""

    with open(path, mode='rb') as wavFile:

        read = wavFile.read()

    return read



def getData(read):

    """Separate stereo pistes"""

    leftEar = list()

    rightEar = list()

    dataSize = struct.unpack('I', read[40:44])[0]

    for i in range(dataSize//4):

        leftEar.append(struct.unpack('h', read[44 + i*4:44 + i*4 + 2])[0])

        rightEar.append(struct.unpack('h', read[44 + i*4 + 2:44 + i*4 + 4])[0])

    return leftEar, rightEar



def writeWavFile(fileName, header, leftEar, rightEar):

    """Create a file wav fileName with header leftEar and rightEar"""

    with open(f"SÃ©ance8/{fileName}.wav", 'wb') as wavFile:

        wavFile.write(header)

        for i in range(len(leftEar)):

            wavFile.write(struct.pack('h', leftEar[i]))

            wavFile.write(struct.pack('h', rightEar[i]))



def copyWavFile(header, leftEar, rightEar):

    """don't modify the data"""

    writeWavFile("the_wall_copied", header, leftEar, rightEar)



def removeOneEachTwo(header, leftEar, rightEar):

    """delete one value out of two (speed up the audio)"""

    newLeftEar = list()

    newRightEar = list()

    for i in range(len(leftEar)//2):

        newLeftEar.append(leftEar[i*2])

        newRightEar.append(rightEar[i*2])

    header = header[:40] + struct.pack('I', len(newLeftEar)*4)

    writeWavFile("the_wall_halfed", header, newLeftEar, newRightEar)



def addOneEachTwo(header, leftEar, rightEar):

    """slow down the audio"""

    newLeftEar = [leftEar[0]]

    newRightEar = [rightEar[0]]

    for i in range(1, len(leftEar)):

        newLeftEar.append((leftEar[i] + leftEar[i-1]) // 2)

        newRightEar.append((rightEar[i] + rightEar[i-1]) // 2)

        newLeftEar.append(leftEar[i])

        newRightEar.append(rightEar[i])

    header = header[:40] + struct.pack('I', len(newLeftEar)*4)

    writeWavFile("the_wall_doubled", header, newLeftEar, newRightEar)



def multiplyCadence(f, header, leftEar, rightEar):

    """Speed up the audio by multiplying the frequency by f"""

    newLeftEar = [leftEar[0]]

    newRightEar = [rightEar[0]]

    x = 0

    for _ in range(1, int(len(leftEar)/f)):

        x += f

        y = int(x)

        if y+1 >= len(leftEar): # Corrections des erreurs d'arrondi de python

            break

        newLeftEar.append(interpol(leftEar[y], leftEar[y+1], x-y))

        newRightEar.append(interpol(rightEar[y], rightEar[y+1], x-y))

    header = header[:40] + struct.pack('I', len(newLeftEar)*4)

    writeWavFile(f"the_wall_multiplied_by_{f}", header, newLeftEar, newRightEar)



def interpol(a, b, x):


    return int(a + (b-a) * x)



# ========= Main ========= #



if __name__ == "__main__":



    path = "SÃ©ance8/the_wall.wav"

    read = open_wav(path)

    leftEar, rightEar = getData(read)

    header = read[:44]



    #copyWavFile(header, leftEar, rightEar)



    #removeOneEachTwo(header,  leftEar, rightEar)



    #addOneEachTwo(header, leftEar, rightEar)



    #multiplyCadence(10, header, leftEar, rightEar)



    pass


