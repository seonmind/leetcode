#Remove Duplicates from Sorted Array
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

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
