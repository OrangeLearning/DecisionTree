"""
    This file build the basic class for build a Decision Tree
    
    author: GeekVitaminC
"""
import copy
import queue

"""
    define the tree node

    tag ---  what kind of the decision tree
    labels --- what labels when come to this node
    sons --- a dict define like following:
        {
            "id" : the id of the son,
            "edge" : which feature of which label will come to that place
        }
        a edge should describe two info:
            1. the label used to divide in this node
            2. the feature will lead to that son
"""
class TreeNode:
    def __init__(self,id = -1):
        self.id = id
        self.tag = None
        self.sons = []
        self.labels = []
        
    def add_son(self,sonId,labelId,feature):
        son = {}
        son['id'] = sonId
        son['edge'] = {}
        son['edge']['label'] = labelId
        son['edge']['feature'] = feature

        self.sons.append(son)

    def setTag(self,newTag):
        self.tag = newTag

    def setLabels(self,labels):
        self.labels = copy.copy(labels)

    def getNodeId(self):
        return self.id

    def getSons(self):
        return self.sons

    def getLabels(self):
        return self.labels

    def getTag(self):
        return self.tag


class Tree:
    def __init__(self):
        self.tot = 0
        self.nodes = []
        self.root = -1

    def newTreeNode(self):
        node = TreeNode(self.tot)
        self.tot += 1
        self.nodes.append(node)
        return node

    def getAllNodes(self):
        return self.nodes

    def getNodeSize(self):
        return self.tot

    def getNode(self,index):
        if index not in range(0,self.tot):
            return None
        else:
            return self.nodes[index]

    def setRoot(self,root):
        self.root = root

    def getRoot(self):
        return self.root

    def bfs(self):
        q = queue.Queue(maxsize=-1)
        q.put(self.nodes[self.root])

        res = []
        edge = []
        while not q.empty():
            cur = q.get()
            res.append({
                "id":cur.getNodeId(),
                "label":cur.getLabels(),
                "tag": cur.getTag()
            })

            for son in cur.getSons():
                print(son)
                id = son['id']
                q.put(self.getNode(id))
                edge.append({
                    "start": cur.getNodeId(),
                    "end": son['id'],
                    "edge": son['edge']['feature']
                })
        return res,edge
