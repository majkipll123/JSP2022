def countAndSay(n):
    if n == 1:
        return '1'
    prevString = '1'
    
    for i in range(1, n):
        res = ''
        count = 1
        for j in range(1, len(prevString)):
            if prevString[j] == prevString[j-1]:
                count += 1
            else:
                res = res + str(count) + str(prevString[j-1])
                count = 1
        res = res + str(count) + str(prevString[-1])
        prevString = res
    return prevString
print(countAndSay(5))