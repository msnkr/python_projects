# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# This function calculates the number of distinct ways to climb a staircase with 'n' steps.
def climbStairs(n):
    # We create a list 'ways' of size 'n+1' to store the number of ways to reach each step.
    # The index 'i' in the list represents the 'i-th' step.
    ways = [0] * (n+1)
    print(ways)

    # There is only one way to reach the first step (by taking one step), so we set ways[0] = 1.
    ways[0] = 1

    # Similarly, there is only one way to reach the second step (by taking one step twice or two steps at once), so we set ways[1] = 1.
    ways[1] = 1

    # Now, for each subsequent step 'i' (from 2 to 'n'), we calculate the number of ways to reach it.
    for i in range(2, n+1):
        # We can reach the 'i-th' step either from the '(i-1)-th' step (by taking one step) or from the '(i-2)-th' step (by taking two steps).
        # So, the number of ways to reach the 'i-th' step is the sum of the number of ways to reach the '(i-1)-th' and '(i-2)-th' steps.
        ways[i] = ways[i-1] + ways[i-2]

    # Finally, we return the number of ways to reach the 'n-th' step, which is stored in ways[n].
    return ways[n]


result = climbStairs(3)
print(result)
