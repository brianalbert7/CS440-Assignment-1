class PriorityQueue():

    def __init__(self):
        self.queue = []

    def insert(self,elm):
        self.queue.append(elm)
   
    def isEmpty(self):
        return len(self.queue) == 0

    def pop(self):
        #Node properties:
        #[x,y,h,g]: x coordinate, y coordinate, estimated herustic, current total cost
        if len(self.queue) == 1:
            elm = self.queue[0]
            del self.queue[0]
            return elm
        min = 0
        for i in range(len(self.queue)):
            elm = self.queue[i]
            minNode = self.queue[min]
            elmCost = elm[2] + elm[3]
            minCost = minNode[2] + minNode[3]
            if elmCost < minCost:
                min = i
            
        elm = self.queue[min]
        del self.queue[min]
        return elm