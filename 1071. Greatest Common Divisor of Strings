class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if the concatenation of both strings equals each other
        if str1 + str2 != str2 + str1:
            return ""

        # Helper function to find the GCD of two numbers using Euclidean algorithm
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        # Calculate the length of the GCD
        gcd_length = gcd(len(str1), len(str2))

        # Extract a substring of length gcd_length from either string
        return str1[:gcd_length]


