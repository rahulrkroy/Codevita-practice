def printPairs(arr, arr_size, sum): 
    c=0  
    s = set() 
    for i in range(0, arr_size): 
        temp = sum-arr[i] 
        if (temp in s): 
            c+=1
        s.add(arr[i])
    return c
sum=0  

string_dictionery = { 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 20: 'twenty', 21: 'twentyone', 22: 'twentytwo', 23: 'twentythree', 24: 'twentyfour', 25: 'twentyfive',  31: 'thirtyone', 32: 'thirtytwo', 33: 'thirtythree', 34: 'thirtyfour', 35: 'thirtyfive',26: 'twentysix', 27: 'twentyseven', 28: 'twentyeight', 29: 'twentynine', 30: 'thirty', 36: 'thirtysix', 37: 'thirtyseven', 38: 'thirtyeight', 39: 'thirtynine',  45: 'fortyfive', 46: 'fortysix', 47: 'fortyseven', 48: 'fortyeight', 49: 'fortynine',40: 'forty', 41: 'fortyone', 42: 'fortytwo', 43: 'fortythree', 44: 'fortyfour', 56: 'fiftysix', 57: 'fiftyseven', 58: 'fiftyeight', 59: 'fiftynine', 60: 'sixty',  50: 'fifty', 51: 'fiftyone', 52: 'fiftytwo', 53: 'fiftythree', 54: 'fiftyfour', 55: 'fiftyfive',61: 'sixtyone', 62: 'sixtytwo', 63: 'sixtythree', 64: 'sixtyfour', 65: 'sixtyfive', 66: 'sixtysix', 67: 'sixtyseven', 68: 'sixtyeight', 69: 'sixtynine',  75: 'seventyfive', 76: 'seventysix', 77: 'seventyseven', 78: 'seventyeight', 79: 'seventynine', 70: 'seventy', 71: 'seventyone', 72: 'seventytwo', 73: 'seventythree', 74: 'seventyfour',86: 'eightysix', 87: 'eightyseven', 88: 'eightyeight', 89: 'eightynine', 90: 'ninety',80: 'eighty', 81: 'eightyone', 82: 'eightytwo', 83: 'eightythree', 84: 'eightyfour', 85: 'eightyfive',  91: 'ninetyone', 92: 'ninetytwo', 93: 'ninetythree',  97: 'ninetyseven', 98: 'ninetyeight', 99: 'ninetynine',94: 'ninetyfour', 95: 'ninetyfive', 96: 'ninetysix', 100: 'hundred'}


nop=int(input())
A = list(map(int,input().split()))
vowe_list=[2,1,2,2,2,1,2,2,2,1,
            3,2,3,4,3,3,4,4,4,1,
            3,2,3,3,3,2,3,3,3,1,
            3,2,3,3,3,2,3,3,3,2,
            4,3,4,4,4,3,4,4,4,1,
            3,2,3,3,3,2,3,3,3,1,
            3,2,3,3,3,2,3,3,3,2,
            4,3,4,4,4,3,4,4,4,2,
            4,3,4,4,4,3,4,4,4,2,
            4,3,4,4,4,3,4,4,4,2]
for i in A:
    sum+=vowe_list[i-1]
count=printPairs(A, len(A), sum)
print(string_dictionery[count])