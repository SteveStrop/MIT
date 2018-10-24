def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    #if base case is true:
    #   return answer
    #else
    # return recursive call
    low=0
    high=len(aStr)
    mid=(high-low)//2
    if len(aStr)==1 or len(aStr)==0:
        return False
    if char == aStr[mid]:
        return True
    if char > aStr[mid]:
       low=mid
    elif char < aStr[mid]:
        high=mid
    print(aStr[low:high])
    return isIn(char,aStr[low:high])


print(isIn('b','aaabcccc'))
