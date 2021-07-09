class PriorityQueue():

    def __init__(self):
        self.queue = []

    def insert(self,elm):
        self.queue.append(elm)
   
    def isEmpty(self):
        return len(self.queue) == 0

    def pop(self):
        if len(self.queue) == 1:
            elm = self.queue[0]
            del self.queue[0]
            return elm
        min = 0
        for i in range(len(self.queue)):
            elm = self.queue[i]
            minNode = self.queue[min]
            if elm[2] < minNode[2]:
                min = i
            
        elm = self.queue[min]
        del self.queue[min]
        return elm