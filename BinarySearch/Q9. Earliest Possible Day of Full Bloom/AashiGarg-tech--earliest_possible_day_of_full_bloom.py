class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        seeds = list(zip(growTime, plantTime))
        seeds.sort(reverse=True) 

        day = 0
        ans = 0

        for g, p in seeds:
            day += p
            ans = max(ans, day + g)

        return ans