class solution(object):
    def twosum(self,nums,target):
        dic = {}
        for index ,value in enumerate(nums):
            if target-value in dic:
                return dic[target-value], index
            dic[value] = index