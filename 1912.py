def max_dp(lst):
    n = len(lst)

    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = lst[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + lst[i], lst[i])

    return max(dp)


n = int(input())
lst = list(map(int, input().split()))
ans = max_dp(lst)

print(ans)
