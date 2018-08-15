from src.Network import Network
from src.FileIO import FileIO

LEANING_ENTRIES = 4500

if __name__ == '__main__':
    '''
    P3.Establish the moving direction of a robot (forward, slight turn to left,
    slight turn to right, strong turn to left, strong turn to right) based on the collected
    data from the sensors.
    The training data is composed from previous such decisions (informations from 24
    sensors from the robot). The sensor position is given by the deviation angle:
    180 (front), 165, 150, ..., 15, 0 (back), 15, 30, ...., 150, 165.
    '''
    reader = FileIO("input2.data", "input4.data", "input24.data")
    (inData, outData) = reader.readFile(24)

    learnIn = inData[:LEANING_ENTRIES]
    learnOut = outData[:LEANING_ENTRIES]

    testIn = inData[LEANING_ENTRIES:]
    testOut = outData[LEANING_ENTRIES:]

    noExamples = len(inData)
    noFeatures = len(inData[0])

    reader.normaliseData(noExamples, noFeatures, inData)
    noOutputs = 4
    network = Network(noFeatures, noOutputs, 2, 10)

    network.learning(learnIn, learnOut)
    err = network.run(testIn, testOut)
    print("Error:" + str(err))