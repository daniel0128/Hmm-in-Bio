import sys
import math
DEBUG = False


class HMMPara:
    states = ['S1', 'S2', 'S3']
    #pi:
    start_probability = {'S1': -2, 'S2': -1, 'S3': -2}
    #tau:
    trans_probability = {'S1': {'S1': -1,  'S2': -1.321928,     'S3': -3.321928},
                         'S2'  : {'S1': -float('Inf'),  'S2': -1.,     'S3': -1.},
                         'S3': {'S1': -1.736966,  'S2': -2.321928,     'S3': -1.}}
    #e:
    emit_propability = {'S1': {'A': -1.321928,    'C': -1.736966,  'T': -2.321928,  'G': -3.321928},
                        'S2': {'A': -2.,   'C': -2., 'T': -2., 'G': -2.},
                        'S3': {'A': -3.321928,    'C': -2.321928,  'T': -1.736966,  'G': -1.321928}}


class HMMProc:

    def __init__(self,fasta):
        self.para = HMMPara()
        self.fastaList = fasta
        self.resultMatrix = [[0 for col in range(len(self.fastaList))] for row in range(len(self.para.states))]

    def hmmProc(self):
        #todo: hmm process
        emit = self.para.emit_propability
        trans = self.para.trans_probability
        pi = self.para.start_probability
        states = self.para.states
        result = self.resultMatrix
        path = {}

        for i in xrange(len(states)):
            result[i][0] = pi[states[i]]+emit[states[i]][self.fastaList[0]]
            path[states[i]] = [states[i]]

        for j in xrange(1, len(self.fastaList)):
            newpath = {}

            for i in xrange(len(states)):
                (prob, state) = max([ (emit[states[i]][self.fastaList[j]] + result[k][j-1] +trans[states[k]][states[i]],states[k] ) for k in xrange(3) ])
                result[i][j] = prob
                newpath[states[i]] = path[state] + [states[i]]
            path = newpath
        if DEBUG:
            print len(result[0])
            print result[0]
            print result[1]
            print result[2]
        return result,path

    def printMatrix(self):
        print "    ",
        for i in xrange(len(self.fastaList)):
            print "%7s" % self.fastaList[i],
        print

        for i in xrange(len(self.para.states)):
            print "%.6s: " % self.para.states[i],
            for j in xrange(len(self.resultMatrix[0])):
                print "%.7s" % ("%f" % self.resultMatrix[i][j]),
            print


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
        infi = -float('Inf')
        print infi+3
        print '.1: ',  math.log(.1,2)
        print '.2: ',  math.log(.2,2)
        print '.25: ', math.log(.25,2)
        print '.3: ',  math.log(.3,2)
        print '.4: ',  math.log(.4,2)
        print '.5: ',  math.log(.5,2)

    hmmProc = HMMProc(DNA_list)
    result, path = hmmProc.hmmProc()
    print path
