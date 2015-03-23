#!/usr/bin/python
import sys
import argparse
def caesercipher(string,shift):
    cipher=""
    for x in string:
        temp=""
        if(ord(x)>64 and ord(x)<91):
            temp=chr(ord(x) + shift)
            if(ord(temp) > 90 ):
                temp=chr(ord(temp) - 26)
        elif(ord(x)>96 and ord(x)<123):
            temp=chr(ord(x) + shift)
            if(ord(temp) > 122 ):
                temp=chr(ord(temp) - 26)
        else:  
            temp=x
        cipher+=temp
    return cipher
def main(argv):
    desc="""Print all possible shifts/rot combinations (only 0-25)"""
    epilog="""Credits (C) Pramod.S """
    parser = argparse.ArgumentParser(description=desc,epilog=epilog)
    parser.add_argument("--f",help="Enter the file path",dest='filePath',required=True)
    parser.add_argument("--r",help="[Optional] Shift/Rotation by",type=int,dest='shift',required=False)
    temp=parser.parse_args()
    filePath=temp.filePath
    shift=temp.shift
    inputFile = open(filePath,'r')
    outputFile = open('output.txt','w')
    if(shift is None):
        for i in range(1,26):
            inputFile.seek(0,0)
            print("ROT {0}: {1}".format(i,caesercipher(inputFile.read().split('\n'),i)))
            inputFile.seek(0,0)
            outputFile.write("ROT {0}: {1}\n".format(i,caesercipher(inputFile.read().split('\n'),i)))
    else:
        if(shift>0 and shift <26):
            print("ROT {0}: {1}".format(shift,caesercipher(inputFile.read().split('\n'),shift)))
            inputFile.seek(0,0)
            outputFile.write("ROT {0}: {1}\n".format(shift,caesercipher(inputFile.read().split('\n'),shift)))
    inputFile.close()
    outputFile.close()
                                 
if __name__ == "__main__":
    main(sys.argv[1:])
