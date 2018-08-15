from src.Layer import Layer
from math import *

LEARN_RATE = 0.01
EPOCH_LIMIT = 100
VALID = 0.05

class Network:
    def __init__(self, m=0, r=0, p=0, h=0):
        '''
        :param m: number of input nodes (attributes)
        :param r: number of output nodes (results)
        :param p: number of hidden layers
        :param h: size of hidden layers
        Classification problem
        '''
        self.noInputs = m
        self.noOutputs = r
        self.noHiddenLayers = p
        self.noNeuronsPerHiddenLayer = h
        self.layers = [Layer(self.noInputs,0)]
        self.layers += [Layer(self.noNeuronsPerHiddenLayer, self.noInputs)]
        self.layers += [Layer(self.noNeuronsPerHiddenLayer,
                              self.noNeuronsPerHiddenLayer) for k in range(self.noHiddenLayers - 1)]
        self.layers += [Layer(self.noOutputs,self.noNeuronsPerHiddenLayer)]

    def activate(self, inputs):
        '''
        Calculate the output of each neuron
        '''
        i = 0
        for n in self.layers[0].neurons:
            n.output = inputs[i]    #initial inputs
            i += 1
        for l in range(1, self.noHiddenLayers + 2):
            for n in self.layers[l].neurons:
                info = []
                for i in range(n.noInputs):
                    info.append(self.layers[l-1].neurons[i].output)
                n.activate(info)

    def errorBackpropagate(self, err):
        '''
        For each data sample establish and backward propagate the error
        Establish the errors of neurons from the output layer
        '''
        for layerCount in range(self.noHiddenLayers+1, 0, -1): #start from "top" layer
            i = 0
            for n1 in self.layers[layerCount].neurons:
                if(layerCount == self.noHiddenLayers + 1):
                    n1.setErr(err[i] - n1.output)
                else:
                    sumErr = 0.0
                    for n2 in self.layers[layerCount+1].neurons:
                        sumErr += n2.weights[i] * n2.err
                    n1.setErrSigmoidal(sumErr)
                for j in range(n1.noInputs):
                    netWeight = n1.weights[j] + LEARN_RATE * n1.err * self.layers[layerCount-1].neurons[j].output
                    n1.weights[j] = netWeight
                i += 1

    def errorComputationClassification(self, target, noLabels):
        '''
        Convert the single value (analog) into a set of values (softmax); softmax values sum is 1
        '''
        transfOutputs = []
        maxx = self.layers[self.noHiddenLayers + 1].neurons[0].output
        for i in range(noLabels):
            if(self.layers[self.noHiddenLayers + 1].neurons[i].output > maxx):
                maxx = self.layers[self.noHiddenLayers + 1].neurons[i].output
        sumExp = 0.0
        for i in range(noLabels):
            sumExp += exp(self.layers[self.noHiddenLayers + 1].neurons[i].output - maxx)
        for i in range(noLabels):
            transfOutputs.append(exp(self.layers[self.noHiddenLayers + 1].neurons[i].output - maxx)/sumExp)
        maxx = transfOutputs[0]
        computedlabel = 0
        for i in range(noLabels):
            if(transfOutputs[i] > maxx):
                maxx = transfOutputs[i]
                computedlabel = i
        if(target == computedlabel):
            return 0
        else:
            return 1

    def checkGlobalErr(self, err):
        '''
        :return: true if the error is negligible; false otherwise
        '''
        correct = sum(err)
        error = correct / len(err)
        if error < VALID:
            return True
        else:
            return False

    def learning(self, inData, outData):
        '''
        Activate all the neurons and forward propagate their results.
        Backward propagate the error
        '''
        stopCondition = False
        epoch = 0
        globalErr = []
        while ((not stopCondition) and (epoch < EPOCH_LIMIT)):
            globalErr = []
            for d in range(len(inData)):
                self.activate(inData[d])
                err = [0 for x in range(4)]
                err[outData[d]] = 1
                globalErr.append(self.errorComputationClassification(outData[d], len(self.layers[self.noHiddenLayers + 1].neurons))) #4
                self.errorBackpropagate(err)

            print("Iteration#" + str(epoch) + "\nGlobal Error: " + str(sum(globalErr)) + "\n")
            stopCondition = self.checkGlobalErr(globalErr)
            epoch += 1


    def run(self, inData, outData):
        globalErr = []
        for d in range(0, len(inData)):
            self.activate(inData[d])
            globalErr.append(self.errorComputationClassification(outData[d], 2))
        return sum(globalErr)