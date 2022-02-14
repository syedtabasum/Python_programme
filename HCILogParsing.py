import re
import sys
import os
import messageMappingDict

logFile = ""

myformula = re.compile("Sending command 0x([0-9A-Fa-f]+)")

sendingMessage = []

def validate_args():
    global logFile
    if (len(sys.argv) > 1) and os.path.exists(sys.argv[1]):
        print('Using Command Line File Path '+str(sys.argv))
        logFile = sys.argv[1]
    elif os.path.exists('HCILog.log'):
        print('Using Default File Path Since the Command Path is worng')
        logFile = "HCILog.log"
    else:
        assert False, ("Sorry Log File is misisng")


def processLog(fname):
    flines = ""
    with open(fname, 'r', encoding='utf-8') as flog:
        flines = flog.readlines()
    for fline in flines:
        global myformula
        message = re.search(myformula, fline)
        if message:
            sendingMessage.append(message.group(0))


def printRawMessage():
    for tmessage in sendingMessage:
        print(tmessage)


def printProcessedMessage():
    for tmessage in sendingMessage:
        #print(tmessage.split()[2])
        try:
            reqMessage = tmessage.split()
            mymap = messageMappingDict.HCIMessage[reqMessage[2]]
        except KeyError as e:
            print("Seems like the Dictionary is missing the Key "+reqMessage[2])
            mymap = "???????????? Missing Key ??????????"
        print(reqMessage[0]+" "+reqMessage[1]+" **"+mymap+"**")

if __name__ == '__main__':
    print("Command Line Arguments "+str(sys.argv))
    validate_args();
    print("Log File name is "+logFile)
    processLog(logFile)
    #printRawMessage()
    printProcessedMessage()



