
# thompson algorithm:

# 1. for each symbol in our language construct its NFA
# 2. for each regular expression -> merge symbols NFA in appropriate way to construct its NFA
  #  ex : number NFA node(1) -(\L)> node(2) -> 10 edges with values [0-10] -> 10(\L) edges -> node(finish)
# 3. merge all theeeeeeeese together so that we have NFA for our language now



def convertRegexToNFA(regex):
    # regex is a list of pairs : first is regex name and second is its description


    # returns graph

# now we have NFA for the language in the form of Graph instance
# each Graph has a set of edges and a start state and finish state(s)



