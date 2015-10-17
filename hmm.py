import sys
import numpy as np


class HMMPara:
    states = ['S1', 'S2', 'S3']
    #pi:
    start_probability = {'S1': .25, 'S2': .5, 'S3': .25}
    #tau:
    trans_probability = {'S1': {'S1': .5,  'S2': .4,     'S3': .1},
                         'S2': {'S1': 0.,  'S2': .5,     'S3': .5},
                         'S3': {'S1': .3,  'S2': .2,     'S3': .5}}
    #e:
    emit_propability = {'S1': {'A': .4,    'C': .2,  'T': .3,  'G': .1},
                        'S2': {'A': .25,   'C': .25, 'T': .25, 'G': .25},
                        'S3': {'A': .1,    'C': .2,  'T': .3,  'G': .4}}

class HMMProc:

    def __init__(self,fasta):
        self.para = HMMPara()
        self.fastaList = fasta

    def hmmProc(self):
        #todo: hmm process
        emit = self.para.emit_propability
        trans= self.para.trans_probability
        pi   = self.para.start_probability
        stat = self.para.states
        resultMatrix = [[None for col in range(len(self.fastaList))] for row in range(3)]

        for i in xrange(3):
            resultMatrix[i][0] = pi[stat[i]]*emit[stat[i]][self.fastaList[0]]

        for j in xrange(1, len(self.fastaList)):
            for i in xrange(3):
                resultMatrix[i][j] = emit[stat[i]][self.fastaList[j]]*max(resultMatrix[0][j-1] *trans['S1'][stat[i]],resultMatrix[1][j-1] *trans['S2'][stat[i]],resultMatrix[2][j-1] *trans['S3'][stat[i]])
        print len(resultMatrix[0])
        print resultMatrix[1]
        print resultMatrix[2]


class PreProc:
    def __init__(self, text):
        self.text = str.upper(text)

    def preProc(self):
        lst = list(self.text)
        return [x for x in lst if x == 'A' or x == 'C' or x == 'G' or x == 'T']


class FileIO:
    def __init__(self,inFileName,outFileName):
        self.inFileName = inFileName
        self.outFileName = outFileName

    def readFile(self):
        inFile = open(self.inFileName)
        text = inFile.read()
        return text

    def outFile(self,text):
        outFile = open(self.outFileName,'w')
        outFile.write(text)

DEBUG = True
if __name__ == '__main__':
    fileStream = None
    if len(sys.argv) < 2:
        print "arg length error"
    elif len(sys.argv) == 2:
        fileStream = FileIO(sys.argv[1], 'result_'+sys.argv[1])
    else:
        fileStream = FileIO(sys.argv[1], sys.argv[2])

    if DEBUG:#todo: remember delete
        print fileStream.inFileName, fileStream.outFileName

    DNA = fileStream.readFile()
    if DEBUG:#todo remove
        print DNA

    DNA_list = PreProc(DNA).preProc()
    if DEBUG:#todo
        print DNA_list
        print len(DNA_list)

    hmmProc = HMMProc(DNA_list)
    hmmProc.hmmProc()








