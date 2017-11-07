
# https://leetcode.com/problems/rotate-array/description/
def rotate(nums, k):
    n = len(nums)
    k = k % n
    if k == 0 or n == 0:
        return
    a = [0] * n
    for i in range(0, n):
        if i < n - k:
            a[i + k] = nums[i]
        else:
            a[i + k - n] = nums[i]
    for i in range(0, n):
        nums[i] = a[i]
    return 

# https://leetcode.com/problems/reverse-integer/description/
def reverse(n):
    top = 2 ** 31 
    down = -1 * 2**31 
    if n > top or n < down:
        return 0
    if n == 0:
        return n
    while n % 10 == 0:
        n = n / 10
    b = ""
    if n < 0:
        n = n * -1
        b = b + '-'
    s = str(n)
    b = b + s[::-1]
    n = int(b)
    if n > top or n < down:
        return 0
    return n

# https://leetcode.com/problems/contains-duplicate-iii/description/
def contains_nearby_almost_duplicate(nums, k, t):
    n = len(nums)
    if n == 0 or n == 1:
        return False
    if k > n:
        k = n
    for i in range(0, n - 1):
        for j in range(i + 1, k + i + 1):
            if j < n:
                s = abs(nums[j] - nums[i])
                if s <= t:
                    return True
    return False

# https://leetcode.com/problems/largest-palindrome-product/description/
def largest_palindrome(n):
    start = 10 ** (n - 1)
    end = start * 10 - 1
    for a in range(end, start, -1):
        for b in range(a, start, -1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]:
                    n = a * b
    print(n % 1337)

#https://leetcode.com/problems/non-decreasing-array/description/
def check_possibility(nums):
    n = len(nums)
    a = None
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            if a is not None:
                return False
            a = i
    if a == None:
        return True
    if a == 0 or a == n - 2:
        return True
    if nums[a - 1] <= nums[a + 1]:
        return True
    if nums[a] <= nums[a + 2]:
        return True
    return False
