# take inputs

number = int(input())
numbers_list = list(map(int, input().split()))



# creating a dictionery
string_dictionery = { 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 20: 'twenty', 21: 'twentyone', 22: 'twentytwo', 23: 'twentythree', 24: 'twentyfour', 25: 'twentyfive',  31: 'thirtyone', 32: 'thirtytwo', 33: 'thirtythree', 34: 'thirtyfour', 35: 'thirtyfive',26: 'twentysix', 27: 'twentyseven', 28: 'twentyeight', 29: 'twentynine', 30: 'thirty', 36: 'thirtysix', 37: 'thirtyseven', 38: 'thirtyeight', 39: 'thirtynine',  45: 'fortyfive', 46: 'fortysix', 47: 'fortyseven', 48: 'fortyeight', 49: 'fortynine',40: 'forty', 41: 'fortyone', 42: 'fortytwo', 43: 'fortythree', 44: 'fortyfour', 56: 'fiftysix', 57: 'fiftyseven', 58: 'fiftyeight', 59: 'fiftynine', 60: 'sixty',  50: 'fifty', 51: 'fiftyone', 52: 'fiftytwo', 53: 'fiftythree', 54: 'fiftyfour', 55: 'fiftyfive',61: 'sixtyone', 62: 'sixtytwo', 63: 'sixtythree', 64: 'sixtyfour', 65: 'sixtyfive', 66: 'sixtysix', 67: 'sixtyseven', 68: 'sixtyeight', 69: 'sixtynine',  75: 'seventyfive', 76: 'seventysix', 77: 'seventyseven', 78: 'seventyeight', 79: 'seventynine', 70: 'seventy', 71: 'seventyone', 72: 'seventytwo', 73: 'seventythree', 74: 'seventyfour',86: 'eightysix', 87: 'eightyseven', 88: 'eightyeight', 89: 'eightynine', 90: 'ninety',80: 'eighty', 81: 'eightyone', 82: 'eightytwo', 83: 'eightythree', 84: 'eightyfour', 85: 'eightyfive',  91: 'ninetyone', 92: 'ninetytwo', 93: 'ninetythree',  97: 'ninetyseven', 98: 'ninetyeight', 99: 'ninetynine',94: 'ninetyfour', 95: 'ninetyfive', 96: 'ninetysix', 100: 'hundred'}
d2 = {'a', 'e', 'i', 'o', 'u'}
count = 0



def convert_to_letter(a):
    if (a>100) or (a<0) :
        return
    temp=0
    for j in string_dictionery[a]:
        if j in d2:
            temp+=1
    return temp

def calculate(d, numbers_list):
    temp = [] 
    while numbers_list: 
        r= numbers_list.pop() 
        s = count - r
        if s in numbers_list: 
            temp.append([s, r])
    temp.reverse() 
    return temp 

for i in numbers_list:
    count += convert_to_letter(i)





print(string_dictionery[len(calculate(count, numbers_list))])