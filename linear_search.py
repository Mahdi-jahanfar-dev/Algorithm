nums = [1,2,3,5,9,7,4,8]
number = int(input('enter your number : '))

for i in nums:
    if i == number:
        print("found")
        break
else:
    print('not found')