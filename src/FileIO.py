from math import sqrt

turnDict = {}
turnDict["Slight-Right-Turn"] = 0
turnDict["Sharp-Right-Turn"] = 1
turnDict["Move-Forward"] = 2
turnDict["Slight-Left-Turn"] = 3
turnDict["Sharp-Left-Turn"] = 4

class FileIO:
    def __init__(self, file2, file4, file24):
        '''
        Read the data for the robot sensors
        :param file2: string; 2 sensors data
        :param file4:  string 4 sensors data
        :param file24: string 24 sensors data
        '''
        self.file2 = file2
        self.file4 = file4
        self.file24 = file24

    def readFile(self, sensorNo):
        '''
        :param sensorNo: integer; the number of sensors on the robot that provide inputs
        :return: (inputData, result)
        '''
        X = []  # input
        Y = []  # output
        filename = "C:\\_MyFiles\\_FMI\\Workspace\\AI\\Lab4\\src\\files\\"
        if sensorNo == 2:
            filename += self.file2
        elif sensorNo == 4:
            filename += self.file4
        elif sensorNo == 24:
            filename += self.file24
        f = open(filename, 'r')
        line = f.readline().strip()
        while (line != ""):
            v = line.split(',')
            X.append([float(v[z]) for z in range(len(v) - 1)])
            Y.append(turnDict[v[len(v) - 1]])
            line = f.readline().strip()
        return (X, Y)

    def normaliseData(self, noExamples, noFeatures, trainData):
        '''

        :param noExamples:
        :param noFeatures:
        :param trainData:
        '''
        for j in range(noFeatures):
            s = 0.0
            for i in range(noExamples):
                s += trainData[i][j]
            mean = s / noExamples
            squareSum = 0.0
            for i in range(0, noExamples):
                squareSum += (trainData[i][j] - mean) ** 2
            deviation = sqrt(squareSum / noExamples)
            for i in range(0, noExamples):
                trainData[i][j] = (trainData[i][j] - mean) / deviation