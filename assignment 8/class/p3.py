class Subsets:
    def get_subsets(self, nums):
        result=[[]]
        for num in nums:
            new_subsets=[]
            for subset in result:
                new_subsets.append(subset + [num])
            result+=new_subsets
        return result

s=Subsets()
print(s.get_subsets([4,5,6]))
