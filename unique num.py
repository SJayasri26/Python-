# In the given range [L, R], print all numbers having unique digits. e.g. In range 10 to 20 should print all numbers except 11.

# Input:
# L = 10
# R = 20

# output:
# 10 12 13 14 15 16 17 18 19 20

class Solution:
    def uniqueNumbers(self, L, R):
        def has_unique_digits(num):
            num_str = str(num)
            return len(num_str) == len(set(num_str))

        result = []
        for num in range(L, R + 1):
            if has_unique_digits(num):
                result.append(num)
        return result

sol = Solution()
L = 10
R = 20
print(" ".join(map(str, sol.uniqueNumbers(L, R))))
