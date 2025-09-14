#this program identifies the second largest number in a sorted list

nums = [3456, 12536671, 90987675, 17, 56676218, 1, 393990329]

sorted_nums = sorted(nums, reverse=True)

second_largest= sorted_nums[1]

print(f"The second largest number in the list is: {second_largest}")
    