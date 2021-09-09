#Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        global list
        list=nums
        length=len(list)
        for i in range(0,length):
            if list[i]=='_':
                return i
            for j in range(i,length):
                if list[j]==list[i]:
                    j+=1
                else:
                    break
            for k in range(i+1,length-j+i+1):
                list[k]=list[k+j-i-1]
            for p in range(length-j+i+1,length):
                list[p]='_'
