"""
    
"""
import math

import DecisionTreeData as Data
from DecisionTree import build_tree
from DecisionTreeTool import calcShannonEnt
from DecisionTreeBasic import Tree
from DecisionTreeUI import getMermaid

def main():
    data = Data.getWaterMelonData()
    label = Data.getWaterMelonLabel()
    tree = Tree()
    tree.setRoot(0)
    print(tree.getRoot())

    nodeId = build_tree(data,label,calcShannonEnt,tree)

    print(nodeId)

    nodes,edges = tree.bfs()
    print(nodes)
    print(edges)

    getMermaid(nodes,edges)



if __name__ == '__main__':
    main()
