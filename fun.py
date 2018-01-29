# Implement modulo without using the (%) operator.
def modulo(a, b):
    ret = a/b
    print (a-ret*b)
    return a-ret*b


# Take an input string and determine if exactly 3 question marks 
# exist between every pair of numbers that add up to 10.
# If so, return true, otherwise return false. 
def question_mark(s):
    questionMarks = 0
    prevDigit = 0
    sum_10 = False
    for char in s:
        if char.isdigit(): #check if char is number
            if int(char) + prevDigit == 10:
                if questionMarks != 3:
                    return 'false'
                sum_10 = True
            prevDigit = int(char)
            questionMarks = 0
        elif char == '?': #check if char is qnMark
            questionMarks += 1
    return sum_10

    
