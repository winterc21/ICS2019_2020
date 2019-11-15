class Node:
    def __init__(self,weights,offset):
        self.weights=weights
        self.offset=offset
        
    def eval(self,inputList):
        total=self.offset
        for w,v in zip(self.weights,inputList):
            total+=w*v
        return 1 if total>0 else 0
        #return total>0?1:0    In java
        
        
ned=Node([1,1],-1)
print(ned.eval([1,1]))
print(ned.eval([1,0]))
print(ned.eval([0,1]))
print(ned.eval([0,0]))

jim=Node
jim=ned.eval([1,1])
print(jim)
