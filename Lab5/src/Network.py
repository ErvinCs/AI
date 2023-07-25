from src.Layer import Layer
from copy import deepcopy

class Network:
    def __init__(self, m, r, h):
        '''
        :param m: number of input nodes (attributes)
        :param r: number of output nodes (results)
        :param h: number of hidden layers
        '''
        self.structure = [m] + h + [r]
        self.layers = [Layer(m, 1)]
        for i in range(1, len(self.structure)):
            self.layers.append(Layer(self.structure[i], self.structure[i - 1]))

    def activate(self, inputs):
        '''
        Calculate the output of each neuron
        '''
        list = []
        for i in range(self.structure[0]):
            self.layers[0].neuronList[i].setOutput(inputs)  #initial inputs
            list.append(self.layers[0].neuronList[i].out)
        for j in range(1, len(self.structure)):  #iterate trough the hidden layers
            aux = []
            for i in range(self.structure[j]):
                self.layers[j].neuronList[i].setOutput(list)
                aux.append(self.layers[j].neuronList[i].out)
            list = deepcopy(aux)

    def errorBackPropagation(self, err, learnRate, initInput):
        '''
        For each data sample establish and backward propagate the error.
        Re-adjut the weights
        '''
        for i in range(len(self.structure) - 1, -1, -1):  #start from "top" layer
            if i == len(self.structure) - 1:
                for j in range(self.structure[i]):
                    self.layers[i].neuronList[j].setError(err[j])   #calculate errors
            else:
                for j in range(self.structure[i]):
                    delta = 0
                    for k in range(self.structure[i + 1]):
                        delta += self.layers[i + 1].neuronList[k].error * self.layers[i + 1].neuronList[k].w[j]
                    self.layers[i].neuronList[j].setError(delta)

        for i in range(len(self.structure)):    #adjust weights
            if i == 0:
                for j in range(self.structure[0]):
                    self.layers[0].neuronList[j].w[0] -= initInput[j] * learnRate * self.layers[0].neuronList[j].error
            else:
                for j in range(self.structure[i]):
                    for k in range(self.structure[i - 1]):
                        self.layers[i].neuronList[j].w[k] -= self.layers[i - 1].neuronList[k].out * learnRate * self.layers[i].neuronList[j].error

    def learn(self, learnRate, inputData):
        '''
        Activate all the neurons.
        Backward propagate the error
        '''
        error = [100, 100, 100]
        i = 1
        while (abs(error[0]) > 10):
            for line in inputData:
                input = line[:7]
                self.activate(input)

                error = []
                error.append(float(self.layers[2].neuronList[0].out) - line[7])
                error.append(float(self.layers[2].neuronList[1].out) - line[8])
                error.append(float(self.layers[2].neuronList[2].out) - line[9])

                self.errorBackPropagation(error, learnRate, input)
                print('Iteration#' + str(i) + ' = ' + str(error))
                i += 1

    def run(self, inputData):
        error = [100, 100, 100]
        globalErr = [0, 0, 0]
        for line in inputData:
            initial_input = line[:7]
            self.activate(initial_input)
            error = []
            error.append(float(self.layers[2].neuronList[0].out) - line[7])
            error.append(float(self.layers[2].neuronList[1].out) - line[8])
            error.append(float(self.layers[2].neuronList[2].out) - line[9])
            for i in range(3):
                globalErr[i] += error[i]
        return globalErr