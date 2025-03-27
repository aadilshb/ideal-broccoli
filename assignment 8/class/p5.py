class Threesum:
    def find_triplets(self, nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return result

obj=Threesum()
print(obj.find_triplets([-25,-10,-7,-3,2,4,8,10]))