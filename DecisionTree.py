"""
    This file is the core of the algorithm

    author : GeekVitaminC
"""
import copy
import time

from DecisionTreeTool import checkDataInHavingSameY
from DecisionTreeTool import findMaxLabel
from DecisionTreeTool import splitDateSet
from DecisionTreeTool import findBestFeature

"""
    the core algorithm of building a decision tree
"""
def build_tree(data,labels,div_function,tree):
    # print("in build_tree")
    node = tree.newTreeNode()
    print("node: ",node.getNodeId())
    print("data size = ",len(data))
    for item in data:
        print(item)
    print(labels)
    time.sleep(1)

    node.setLabels(labels)

    if checkDataInHavingSameY(data):
        node.setTag(data[0]['y'])
        return node.getNodeId()

    if len(labels) == 0:
        maxlabel = findMaxLabel(data)
        node.setTag(maxlabel)
        return node.getNodeId()

    bestIndex = findBestFeature(data,labels,div_function)
    bestFeature = labels[bestIndex]
    node.setTag(bestFeature)
    newLabels = copy.copy(labels)
    newLabels.remove(bestFeature)
    divideFeature = [item['x'][bestIndex] for item in data]
    uniqueFeature = set(divideFeature)

    for feature in uniqueFeature:
        sonNodeId = build_tree(splitDateSet(data,bestIndex,feature) , newLabels , div_function , tree)
        node.add_son(sonNodeId,bestIndex,feature)
    return node.getNodeId()

