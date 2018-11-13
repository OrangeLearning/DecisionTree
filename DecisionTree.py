"""
    This file is the core of the algorithm

    author : GeekVitaminC
"""
import copy

from DecisionTreeTool import checkDataInHavingSameY
from DecisionTreeTool import findMaxLabel
from DecisionTreeTool import splitDateSet
from DecisionTreeTool import findBestFeature

"""
    the core algorithm of building a decision tree
"""
def build_tree(data,labels,div_function,tree):
    node = tree.newTreeNode()
    print("node: ",node.getNodeId())
    print("data size = ",len(data))
    for item in data:
        print(item)
    print(labels)

    node.setLabels(labels)

    if checkDataInHavingSameY(data):
        node.setTag(data[0]['y'])
        return node.getNodeId()

    if len(labels) == 0:
        maxLabel = findMaxLabel(data)
        node.setTag(maxLabel)
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


"""
    More robust build tree algorithm
    solve the problem for data disappearing when come to one node
    
"""
def build_tree_robust(data,labels,features,div_function,tree):
    node = tree.newTreeNode()
    print("node: ", node.getNodeId())
    print("data size = ", len(data))
    for item in data:
        print(item)
    print(labels)

    node.setLabels(labels)

    if checkDataInHavingSameY(data):
        node.setTag(data[0]['y'])
        return node.getNodeId()

    if len(labels) == 0:
        maxLabel = findMaxLabel(data)
        node.setTag(maxLabel)
        return node.getNodeId()

    bestIndex = findBestFeature(data, labels, div_function)
    bestFeature = labels[bestIndex]
    node.setTag(bestFeature)
    newLabels = copy.copy(labels)
    newLabels.remove(bestFeature)
    divideFeature = [item['x'][bestIndex] for item in data]
    uniqueFeature = set(divideFeature)

    print(bestFeature)
    for feature in features[bestFeature]:
        print("\t",feature)
        if feature in uniqueFeature:
            sonNodeId = build_tree_robust(splitDateSet(data, bestIndex, feature), newLabels, features,div_function, tree)
            node.add_son(sonNodeId, bestIndex, feature)
        else:
            sonNode = tree.newTreeNode()
            sonNode.setTag(findMaxLabel(data))
            sonNodeId = sonNode.getNodeId()
            node.add_son(sonNodeId, bestIndex, feature)
    return node.getNodeId()