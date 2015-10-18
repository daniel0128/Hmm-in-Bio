from hmm import *
class HidenMarkov:

    statesSet = {'S1', 'S2', 'S3'}
    #pi:
    start_probability = {'S1': -2, 'S2': -1, 'S3': -2}
    #tau:
    trans_probability = {'S1': {'S1': -1,  'S2': -1.321928,     'S3': -3.321928},
                         'S2': {'S1': -float('Inf'),  'S2': -1.,     'S3': -1.},
                         'S3': {'S1': -1.736966,  'S2': -2.321928,     'S3': -1.}}
    #e:
    emit_propability = {'S1': {'A': -1.321928,    'C': -1.736966,  'T': -2.321928,  'G': -3.321928},
                        'S2': {'A': -2.,   'C': -2., 'T': -2., 'G': -2.},
                        'S3': {'A': -3.321928,    'C': -2.321928,  'T': -1.736966,  'G': -1.321928}}



    def print_dptable(self,V):
        print "    ",
        for i in range(len(V)): print "%7s" % i,
        print

        for y in V[0].keys():
            print "%.5s: " % y,
            for t in range(len(V)):
                print "%.7s" % ("%f" % V[t][y]),
            print

    def viterbi(self,obs, states, start_p, trans_p, emit_p):
        V = [{}]
        path = {}

        # Initialize base cases (t == 0)
        for y in states:
            V[0][y] = start_p[y] + emit_p[y][obs[0]]
            path[y] = [y]

        # Run Viterbi for t > 0
        for t in range(1,len(obs)):
            V.append({})
            newpath = {}

            for y in states:
                (prob, state) = max([(V[t-1][y0] + trans_p[y0][y] + emit_p[y][obs[t]], y0) for y0 in states])
                print(type(max([(V[t-1][y0] + trans_p[y0][y] + emit_p[y][obs[t]], y0) for y0 in states])))
                print(prob,state)
                V[t][y] = prob
                newpath[y] = path[state] + [y]

            # Don't need to remember the old paths
            path = newpath

        self.print_dptable(V)
        print 'V:'
        print V
        (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
        print(prob, path[state])
        return prob, path[state]

if __name__ == '__main__':
    inputs = FileIO(sys.argv[1],'result_'+sys.argv[1])
    txt = inputs.readFile()
    txt_list = PreProc(txt).preProc()
    hm = HidenMarkov()
    hm.viterbi(txt_list,hm.statesSet,hm.start_probability,hm.trans_probability,hm.emit_propability)

