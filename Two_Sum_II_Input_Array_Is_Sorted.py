def twoSum2(numbers, target):
    hashmap = {}
    
    for i in range(len(numbers)):
        diff = target - numbers[i]

        if diff in hashmap:
            return [hashmap[diff] + 1, i + 1]
        
        hashmap[numbers[i]] = i