from src.Neuron import Neuron

class Layer:
    def __init__(self, noNeurons=0, noInputs=0):
        '''
        A layer of the neural netwok
        :param noNeurons: the number of neurons in the layer
        :param noInputs: the number of synapses
        '''
        self.noNeurons = noNeurons
        self.noInputs = noInputs
        self.neuronList = [Neuron(noInputs) for n in range(self.noNeurons)]