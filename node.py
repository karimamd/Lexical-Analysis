from graph import Edge

class Node:
    def __init__(self):
        self.edges = []
        self.isStart = False
        self.isFinish = False

    def addEdge(self,to,val):
        self.edges.append((to,val))
