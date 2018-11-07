"""
    This file is used to show the decision tree by other tools.

    author : GeekVitaminC
"""

"""
    This function is used show decision tree by mermaid.js
    
    :param
        nodes : the set of nodes
        edges : the set of edges
        format 
"""
def getMermaid(nodes,edges,format = "TB"):
    res = "graph " + format + "\n"

    for node in nodes:
        id = "_t" +str(node['id'])
        tag = node['tag']

        res += id + "[" + "tag = " + tag + "]\n"

    for edge in edges:
        start_node = "_t" + str(edge['start'])
        end_node = "_t" + str(edge['end'])
        text = edge['edge']
        res += start_node + "--" + text + "-->" + end_node + "\n"

    print(res)
    return res
