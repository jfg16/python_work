class Fibonacci:
    def __init__(self, num):
        self.count = num
        self.index = 0
        self.nums = [0,1]
        for x in range(2, num):
            self.nums.append(self.nums[x-2] + self.nums[x-1])
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        else:
            val = self.nums[self.index]
            self.index += 1
            return val
    def get_nums(self):
        return self.nums
    def __str__(self):
        return str(self.nums)

def fibonacci_gen(num = -1):
    if(num == -1):
        nums = [0,1]
        index = 2
        while(True):
            nums.append(nums[index-2] + [index-1])
            index += 1
    elif(num == 1):
        return [0]
    else:
        for i in range(2, nums):
            nums.append(nums[i-2] + nums[i-1])
        return nums