def maxDiff(a, n):
    max_diff = a[1] - a[0]

    for i in range(0, n):
        for j in range(i + 1, n):
            if (a[j] - a[i] > max_diff):
                max_diff = a[j] - a[i]

    return max_diff


# Driver program to test above function
a = [5,4,3,1,2,6,8,9]
s = len(a)
print("Maximum difference is", maxDiff(a, s))
