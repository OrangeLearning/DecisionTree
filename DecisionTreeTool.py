"""
    This is for aux tools for decision Tree

    author: GeekVitaminC
"""
import math


"""
    check whether in this dataSet all the x is the same
"""
def checkDataInHavingSameX(dataSet):
    stdlabel = dataSet[0]['x']
    
    for i in range(1,len(dataSet)):
        x = dataSet[i]['x']
        
        if not len(stdlabel) == len(x):
            return False

        for j in range(0, len(stdlabel)):
            if not x[j] == stdlabel[j]:
                return False
    return True

"""
    check whether in this dataSet all the y is the same
"""
def checkDataInHavingSameY(dataSet):
    y0 = dataSet[0]["y"]
    
    for i in range(1,len(dataSet)):
        if not dataSet[i]["y"] == y0:
            return False
    
    return True

"""
    this function is used to divide dataSet
    
    dataSet : data set itself
    axis : which x
    value : which x == value
"""
def splitDateSet(dataSet,axis,value):
    ret = []
    for item in dataSet:
        if item[axis] == value:
            tmp = item[:axis]
            tmp.extend(item[axis+1:])
            ret.append(tmp)
    return ret

"""
    note :
    The format of dataSet is following:
        dataSet = [
            {
                "x" ：[x0,x1,...,xn],
                "y" : y
            },
        ]

    The format of labelSet is following:
        label = [label1,label2,...,labeln]
"""
def calcEnt(dataSet):
    num = len(dataSet)
    labelChannel = []
    for item in dataSet:
        y = item[-1]
        
        if y not in labelChannel.keys():
            labelChannel[y] = 0
        labelChannel[y] += 1

    ent = 0.0

    for item in labelChannel:
        prob = float(labelChannel[item]) / num
        ent -= prob * math.log2(prob)

    return ent













