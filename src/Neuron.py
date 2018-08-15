from random import random
from math import *

MIN_WEIGHT = -1
MAX_WEIGHT = 1

class Neuron:
    def __init__(self, noInputs=0):
        '''
        :param noInputs: the number of synapses
        '''
        self.noInputs = noInputs
        self.weights = [(random() * 2 - 1) for k in range(self.noInputs)]   #(-1,1)
        self.output = 0
        self.err = 0

    def activate(self, info):
        '''
        Compute the output of the neuron
        '''
        out = 0.0
        for i in range(self.noInputs):
            out += info[i] * self.weights[i]
        self.output = 1 / (1.0 + exp(-out)) # sigmoidal

    def setErr(self, val):
        '''
        Linear error computation
        '''
        self.err = val

    def setErrSigmoidal(self, val):
        '''
        Sigmoidal error computation
        '''
        self.err = self.output * (1 - self.output) * val

