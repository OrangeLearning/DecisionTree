# encoding:utf-8
"""
    This file is used to get data

    the format of the data is like following:
        dataSet = [
            {
                "x" : [x0,x1,....,xn],
                "y" : y
            }
        ]

    author : GeekVitaminC

"""

init_watermelon = [
    ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
    ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
    ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
    ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', '好瓜'],
    ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', '好瓜'],
    ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '好瓜'],
    ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', '好瓜'],
    ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', '好瓜'],
    ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜'],
    ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', '坏瓜'],
    ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', '坏瓜'],
    ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', '坏瓜'],
    ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', '坏瓜'],
    ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', '坏瓜'],
    ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', '坏瓜'],
    ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', '坏瓜'],
    ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '坏瓜']
]

labels = ['色泽', '根蒂', '敲击', '纹理', '脐部', '触感']

def getWaterMelonLabel():
    return labels

def getWaterMelonData():
    dataSet = []
    for item in init_watermelon:
        x = item[:-1]
        y = item[-1]

        tmp = {}
        tmp["x"] = x
        tmp["y"] = y

        dataSet.append(tmp)
    return dataSet

def getWatermelonFeatures():
    dataSet = getWaterMelonData()
    featureNumber = len(labels)

    print("featureNumber = ",featureNumber)

    features = {}

    for i in range(featureNumber):
        features[labels[i]] = set()

    for item in dataSet:
        for i in range(featureNumber):
            features[labels[i]].add(item['x'][i])

    return features

if __name__ == '__main__':
    print(getWaterMelonData())
    print(getWaterMelonLabel())
