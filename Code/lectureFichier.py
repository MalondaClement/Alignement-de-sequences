import os

def LIRE_FICHER_AD(path):
    file = open(path,"r")
    data = file.read()
    data = data.split("\n",4)
    file.close()
    return data[2].replace(" ",""), data[3].replace(" ","")
