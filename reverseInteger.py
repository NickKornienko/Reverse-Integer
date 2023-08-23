class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            x = -int(str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])

        if x < -2**31 or x > 2**31 - 1:
            return 0
        else:
            return x

# Main
def main():
    x = int(input("Enter a number: "))
    solution = Solution()
    print(solution.reverse(x))
2

if __name__ == "__main__":
    main()
