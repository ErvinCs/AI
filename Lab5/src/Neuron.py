from random import uniform

class Neuron:
    def __init__(self, nrInput):
        '''
        :param nrInput: the number of synapses
        '''
        self.nrInputs = nrInput
        self.w = [uniform(-1, 1) for _ in range(nrInput)]
        self.out = 0
        self.error = 0

    def activate(self, info):
        '''
        Compute the output of the neuron
        '''
        result = 0
        for i in range(self.nrInputs):
            result += info[i] * self.w[i]
        return result  # linear

    def setOutput(self, val):
        '''
        Compute and set the output of the neuron
        '''
        self.out = self.activate(val)

    def setError(self, val):
        '''
        Linear error computation
        '''
        self.error = val