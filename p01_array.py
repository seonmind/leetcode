#Remove Duplicates from Sorted Array
#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

#tempt1
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         global list
#         list=nums
#         length=len(list)
#         for i in range(0,length):
#             if list[i]=='_':
#                 return i
#             for j in range(i,length):
#                 if list[j]==list[i]:
#                     j+=1
#                 else:
#                     break
#             for k in range(i+1,length-j+i+1):
#                 list[k]=list[k+j-i-1]
#             for p in range(length-j+i+1,length):
#                 list[p]='_'

#tempt2
class Solution:
    def removeDuplicates(self, nums):
        global list
        list=nums
        length=len(list)
        r=1
        for i in range(1,length):
            if list[i]==list[i-1]:
                continue
            else:
                list[r]=list[i]
                r+=1
        for k in range(r,length):
            list[k]='_'
        return r
