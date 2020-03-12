def cardinalitySort(nums):
    # Write your code here
    nums.sort()
    bin_count = []
    for i in range(len(nums)):
        ones = 0
        bin = "{0:b}".format(nums[i])
        for num in bin:
            if (num == '1'):
                ones += 1
        bin_count.append((nums[i], ones))

    bin_count.sort(key=lambda x: x[1])
    sort_bin = []
    for tup in bin_count:
        sort_bin.append(tup[0])
    return sort_bin

nums = [12, 37, 44, 2, 9, 6, 5]

print(cardinalitySort(nums))