class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht={}
        for y in range(len(nums)):
            x = nums[y]
            key = str(x)
            ht[key] = ht.get(key, [])
            ht[key].append(y)
        print(ht)

        for y in range(len(nums)): 
            x = nums[y]
            d = target - x
            print(y,x,d)
            if str(d) in ht:
                print([ht[str(x)][0], ht[str(d)][-1]])
                if  (x == d and len(ht[str(x)]) < 2): continue
                return [ht[str(x)][0], ht[str(d)][-1]]
        return [-1000,-1000]

                    

