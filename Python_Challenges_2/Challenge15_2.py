#this program identifies the second largest number using loops

nums = [3456, 12536671, 90987675, 17, 56676218, 1, 393990329]
second_largest = largest = float("-inf")

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(f"The second largest number in the list is: {second_largest}")
        