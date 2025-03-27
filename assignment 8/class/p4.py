class Pair:
    def f_pair(self,nums,target):
        seen={}
        result=[]
        for i, num in enumerate(nums):
            diff=target-num
            if diff in seen:
                result=[seen[diff],i]
            seen[num]=i
        return result

obj=Pair()
print(obj.f_pair([90, 20, 10, 40, 50, 60, 70], 50))
