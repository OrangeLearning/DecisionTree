"""
    This file build the basic class for build a Decision Tree
    
    author: GeekVitaminC
"""
from enum import Enum

class TreeNodeType(Enum):
    VOID = 0
    LEAF = 1



class TreeNode:
    def __init__(self):
        self.type = TreeNodeType.VOID
        self.tag = None

    def add_son(self):
        pass

    def setTag(self,newTag):
        self.tag = newTag
