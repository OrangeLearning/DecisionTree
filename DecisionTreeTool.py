"""
    This is for aux tools for decision Tree

    author: GeekVitaminC

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

    notice the order of the labels and the order of the data_x should always be the same
"""
import math
import copy


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
        if item['x'][axis] == value:
            newItem = {}

            newItem['y'] = item['y']
            newItem['x'] = copy.copy(item['x'][:axis])
            newItem['x'].extend(copy.copy(item['x'][axis + 1:]))

            ret.append(newItem)
    return ret

"""
    this function is used to calc the shannon ent which is one of the div_function
"""
def calcShannonEnt(dataSet):
    num = len(dataSet)
    labelChannel = {}
    for item in dataSet:
        y = item['y']
        if y not in labelChannel.keys():
            labelChannel[y] = 0
        labelChannel[y] += 1

    ent = 0.0

    for item in labelChannel.keys():
        prob = float(labelChannel[item]) / num
        ent -= prob * math.log2(prob)

    return ent

"""
    calc Gini value 
"""
def calcGini(dataSet):
    number = len(dataSet)
    map_y = {}
    for item in dataSet:
        y = item['y']
        if y not in map_y.keys():
            map_y[y] = 0
        map_y[y] += 1

    gini = 1.0
    for item in map_y.keys():
        gini -= (float(map_y[item]) / float(number)) ** 2

    return gini


"""
    use Gain to divide the data
"""
def calcGain(dataSet,i):
    baseEntropy = calcShannonEnt(dataSet)
    # select the data in dataSet
    dataSet_x = [item['x'][i] for item in dataSet]
    # delete the same item in dataSet_x
    featureUniqueSet = set(dataSet_x)
    newGain = 0.0
    for value in featureUniqueSet:
        subDataSet = splitDateSet(dataSet, i, value)
        prob = float(len(subDataSet)) / float(len(dataSet))
        newGain += prob * calcShannonEnt(subDataSet)

    newGain = baseEntropy - newGain
    return newGain

"""
    use Gain_radio to divide the data
"""
def calcGain_radio(dataSet,i):
    iv = 0.0
    baseEntropy = calcShannonEnt(dataSet)
    # select the data in dataSet
    dataSet_x = [item['x'][i] for item in dataSet]
    # delete the same item in dataSet_x
    featureUniqueSet = set(dataSet_x)
    newGain = 0.0
    for value in featureUniqueSet:
        subDataSet = splitDateSet(dataSet, i, value)
        prob = float(len(subDataSet)) / float(len(dataSet))
        newGain += prob * calcShannonEnt(subDataSet)
        iv += - prob * math.log2(prob)

    newGain = baseEntropy - newGain
    return newGain / iv

"""
    use Gini_index to divide the data
"""
def calcGini_index(dataSet,i):
    dataSet_x = [item['x'][i] for item in dataSet]
    featureUniqueSet = set(dataSet_x)

    gini_index = 0.0
    for value in featureUniqueSet:
        subDataSet = splitDateSet(dataSet, i, value)
        prob = float(len(subDataSet)) / float(len(dataSet))
        gini_index += prob * calcGini(subDataSet)
    return - gini_index


"""
    find max label in a data set
"""
def findMaxLabel(dataSet) : 
    labels = [item['y'] for item in dataSet]
    maxlabel = None
    maxcnt = 0
    cnt_mapper = {}
    for item in labels:
        if item not in cnt_mapper.keys() :
            cnt_mapper[item] = 0
        cnt_mapper[item] += 1
        if cnt_mapper[item] > maxcnt:
            maxcnt = cnt_mapper[item]
            maxlabel = item

    return maxlabel

"""
    find the best feature in the situation

    div_function is selected by user which the divide function to change the decision tree
        div_function should use the following format:
            
            def div_function(dataSet,index):
            
                return res
            
        note　that we will always choose the biggest number
        so if the value is opposite , just add a minus sign before the number you return
    
    return value is the index
"""
def findBestFeature(dataSet,label,div_function):
    number_feature = len(label)

    # calc the first result directly
    bestIndex = 0
    bestValue = div_function(dataSet,0)

    # start from index = 1
    for i in range(1,number_feature):
        newValue = div_function(dataSet,i)
        if newValue > bestValue:
            bestValue = newValue
            bestIndex = i

    return bestIndex


def main():
    import DecisionTreeData as Data

    print(Data.getWaterMelonData())
if __name__ == '__main__':
    main()
