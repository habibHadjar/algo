class Heap:
    def __init__(self, list):
        self.list = list
        self.length = len(list)
    
    def __str__(self):
        return str(self.list)
    
    def __getitem__(self, index):
        return self.list[index]
        
    def push(self, value_to_push):
        if self.length <= 1:
            if self.length == 0:
                self.list.append(value_to_push)
            elif value_to_push > self.list[0]:
                self.list.append(value_to_push)
            else:
                self.list.insert(0, value_to_push)
            self.length += 1
            return self.list

        low = 0
        high = self.length - 1
        while low <= high:
            mid = (low + high) // 2
            if value_to_push < self.list[mid]:
                high = mid - 1
            elif value_to_push >= self.list[mid]:
                low = mid + 1
            # else:
            #     return self.list
        self.list.insert(low, value_to_push)
        self.length += 1
        return self.list


p = Heap([0,1,2,3,4,5,6,7,8,9])
# print(p[0])
while True:
    n = int(input())
    print(p.push(n),", ",p.length)