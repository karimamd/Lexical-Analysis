

# helper class for NFAs
#
class Edge:
    def __init__(self,to,val):
        self.to = to
        self.val = val


class Graph:
    def addEdge(self, n , Edge):
        self.edges[n].append(Edge)

    def __init__(self , start , finish , size,names):
        self.start = start
        self.finish = finish # prefered to be a list : can be more than one
        self.finish_names = names # finish states may have names -> id , number ...etc
        self.size = sizes
        self.edges = [[] * self.size]

    @staticmethod
    def Or(nodes):
        return None
        # merge a list of NFAs' by or operation

    @staticmethod
    def concatenate(a,b):
        # conc 2 NFAs
        return None

    @staticmethod
    def star(a):
        # apply * operator to node
        return None


