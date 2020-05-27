from math import ceil

"""
Karatsuba multiplication algorithm:

Step 1. Break the two integers x and y into a, b, c and d  (e.g. 'a' is half-length of n-digit 'x')
Step 2. Recursively compute ac
Step 3. Recursively compute bd
Step 4. Recursively compute (a + b)(c + d)
Step 5. Calculate (ab + bc) as (a + b)(c + d) – ac – bd
Result: Product formula is (10**n/2) * ac) + (10**n * (ad + bc)) + bd
Good explanation here: https://www.codeandgadgets.com/karatsuba-multiplication-python/

Complexity: O(N**log 3)
"""


class Solution:
    def multiply(self, num1: str, num2: str):
        if len(num1) == 1 or len(num2) == 1:
            return int(num1) * int(num2)

        # if arguments have different length, add leading zeros to shorter argument
        if len(num1) != len(num2):
            x = max(num1, num2, key=len)
            y = '0' * abs(len(num1) - len(num2)) + min(num1, num2, key=len)
        else:
            x, y = num1, num2
        n = len(x)
        half_n = ceil(n / 2)

        # if arguments have odd length, add leading zero to make them even
        if n % 2 != 0:
            x = '0' + x
            y = '0' + y

        a, b = int(x[0:half_n]), int(x[half_n:])
        c, d = int(y[0:half_n]), int(y[half_n:])

        ac = self.multiply(str(a), str(c))
        bd = self.multiply(str(b), str(d))
        ad_plus_bd = self.multiply(str(a + b), str(c + d))

        ten_n = 10 ** n
        ten_half_n = 10 ** half_n
        return (ten_n * ac) + (ten_half_n * (ad_plus_bd - ac - bd)) + bd


sol = Solution()
x = '1234'
y = '5678'
print(sol.multiply(x, y))
