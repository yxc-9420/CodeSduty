import collections
class Solution:

    def __init__(self,arr):
        self.arr = arr
    
    # 冒泡排序 时间：O(n^2) 空间：O(1) 
    def BubbleSort(self):
        for i in range(len(self.arr)-1):
            for j in range(len(self.arr)-1-i):
                if(self.arr[j] > self.arr[j+1]):
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = temp
    
    # 选择排序 时间：O(n^2) 空间：O(1)
    def SelectionSort(self):
        for i in range(len(self.arr)-1):
            minIndex = i
            for j in range(i+1,len(self.arr)):
                if(self.arr[minIndex]>self.arr[j]):
                    minIndex = j
            if minIndex != i:
                temp = self.arr[minIndex]
                self.arr[minIndex] = self.arr[i]
                self.arr[i] = temp

if __name__ == "__main__":
    arr = [3,44,2,46,23,24,35,7,34,70,9,4]
    s = Solution(arr)
    s.SelectionSort()
    s = collections.Counter(arr,a=2,b=3)
    
    print(arr)