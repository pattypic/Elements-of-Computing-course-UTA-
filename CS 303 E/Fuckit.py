def f(lst):
    if lst[-1] > 5:
        lst.append(8)
    print(lst, end=" ")
nums = [1, 9]
f(nums)
print(nums, end=" ")
f(nums)