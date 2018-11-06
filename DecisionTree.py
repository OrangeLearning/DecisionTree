"""
    This file is the core of the algorithm

    author : GeekVitaminC
"""
from DecisionTreeTool import checkDataInHavingSameX
from DecisionTreeTool import checkDataInHavingSameY
from DecisionTreeBasic import TreeNode
def build_tree(data,label,div_function):
    node = TreeNode()
    
    if checkDataInHavingSameY(data):
        node.setTag(data[0]['y'])
        return node

    if label.size() == 0 and 
    
    return node
