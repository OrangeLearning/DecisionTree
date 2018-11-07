"""
    This is for aux tools for decision Tree

    author: GeekVitaminC
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
    find max label in a data set
"""
def findMaxLabel(dataSet) : 
    labels = [item[-1] for item in dataSet]
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

    return value is the index
"""
def findBestFeature(dataSet,label,div_function):
    number_feature = len(label)
    # 全局的
    baseEntropy = div_function(dataSet)
    
    bestIndex = -1
    bestGain = 0.0

    for i in range(number_feature):
        # select the data in dataSet
        dataSet_x = [item['x'][i] for item in dataSet]
        # delete the same item in dataSet_x
        featureUniqueSet = set(dataSet_x)
        newGain = 0.0
        
        for value in featureUniqueSet:
            subDataSet = splitDateSet(dataSet,i,value)
            prob = float(len(subDataSet)) / float(len(dataSet))
            # print("i = ",i," ",label[i]," value = ",value," prob = ",prob)
            newGain += prob * div_function(subDataSet)

        newGain = baseEntropy - newGain
        # print("in findBestFeature i = ",i," newGain = ",newGain)
        if newGain > bestGain:
            bestGain = newGain
            bestIndex = i
    # print("in findBestFeature bestIndex = ",bestIndex)
    return bestIndex

def main():
    import DecisionTreeData as Data
    print(calcShannonEnt(Data.getWaterMelonData()))

    findBestFeature(Data.getWaterMelonData(),Data.getWaterMelonLabel(),calcShannonEnt)

if __name__ == '__main__':
    main()
