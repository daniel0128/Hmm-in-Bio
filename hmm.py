import math


class HMMPara:
    states = {'S1', 'S2', 'S3'}
    #pi:
    start_probability = {'S1': -2., 'S2': -1., 'S3': -2.}
    #tau:
    trans_probability = {'S1': {'S1': -1.000000,  'S2': -1.321928,     'S3': -3.321928},
                         'S2': {'S1': None,       'S2': -1.000000,     'S3': -3.000000},
                         'S3': {'S1': -1.736966,  'S2': -2.321928,     'S3': -1.000000}}
    #e:
    emit_propability = {'S1': {'A': -1.321928,    'C': -1.736966,  'T': -2.321928,  'G': -3.321928},
                        'S2': {'A': -2.000000,    'C': -2.000000,  'T': -2.000000,  'G': -2.000000},
                        'S3': {'A': -3.321928,    'C': -2.321928,  'T': -1.736966,  'G': -1.321928}}

if __name__ == '__main__':
    print '.5: ',  math.log(.5, 2)
    print '.4: ',  math.log(.4, 2)
    print '.3: ',  math.log(.3, 2)
    print '.25: ', math.log(.25, 2)
    print '.2: ',  math.log(.2, 2)
    print '.1: ',  math.log(.1, 2)
