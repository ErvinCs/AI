from src.Network import Network

LEARN_INDEX = 85
LEARN_RATE = 0.000001

def getData(filename):
    with open(filename) as f:
        data = f.readlines()
    learnData = []
    testData = []

    lines = [line.rstrip('\n') for line in data]
    for line in lines[:LEARN_INDEX]:
        tokens = line.split(',')
        newLine = []
        for i in range(0, len(tokens)):
            newLine.append(float(tokens[i]))
        learnData.append(newLine)

    for line in lines[84:]:
        tokens = line.split(',')
        newLine = []
        for i in range(0, len(tokens)):
            newLine.append(float(tokens[i]))
        testData.append(newLine)

    return (learnData, testData)

if __name__ == '__main__':
    '''
    P1.Build a system that approximates the quality of a concrete mixture
    based on the used ingredients.
    Input variables: 7
    Output variables: 3
    '''
    learnData, testData = getData("C:\\_MyFiles\\_FMI\\Workspace\\AI\\Lab5\\files\\data.data")

    net = Network(7, 3, [4])

    net.learn(LEARN_RATE, learnData)
    err = net.run(testData)
    err[0] = int(err[0])
    err[1] = int(err[1])
    err[2] = int(err[2])
    print('\nSLUMP, FLOW, 28-day Compressive Strength = ' + str(err))