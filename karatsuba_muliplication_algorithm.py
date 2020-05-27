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
    def multiply(self, num1, num2):
        def karatsuba(num1: int, num2: int):
            len1, len2 = len(str(num1)), len(str(num2))
            if len1 == 1 or len2 == 1:
                return num1 * num2

            x, y = int(num1), int(num2)
            half_n = max(len1, len2) // 2

            a = x // 10 ** half_n
            b = x % 10 ** half_n
            c = y // 10 ** half_n
            d = y % 10 ** half_n

            ac = karatsuba(a, c)
            bd = karatsuba(b, d)
            ad_plus_bd = karatsuba(a + b, c + d)

            # writing n as 2*half_n takes care of both even and odd n
            ten_n = 10 ** (2 * half_n)
            ten_half_n = 10 ** half_n
            return (ten_n * ac) + (ten_half_n * (ad_plus_bd - ac - bd)) + bd

        return str(karatsuba(int(num1), int(num2)))


sol = Solution()
x = '1234'
y = '5678'
print(sol.multiply(x, y))
