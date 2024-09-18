nums = [1,2,3,4,5,8,10]

number = int(input('enter your number : '))

def binary_search(nums,number):
    if len(nums)<2:
        if nums[0] == number:
            print('found')
        else:
            print("not found")
    else:
        mid = len(nums)//2
        if number == nums[mid]:
            print('found')
        elif nums[mid]<number:
            return binary_search(nums[mid:], number)
        else:
            return binary_search(nums[:mid], number)
    

binary_search(nums, number)