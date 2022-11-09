#Precision problem
#Given an array of integers, 
# calculate the ratios of its elements that are positive,
#  negative, and zero. Print the decimal value of each fraction
#  on a new line with  places after the decimal.
def plusMinus(arr):
    # Write your code here
    pos=0
    zero=0
    neg=0
    
    for num in arr:
        if num>0:
            pos+=1
        elif num<0:
            neg+=1
        else:
            zero+=1
            
    ans=[pos/len(arr),neg/len(arr),zero/len(arr)]
    print(*ans,sep='\n')

#Given five positive integers, find the minimum 
# and maximum values that can be calculated by summing
#  exactly four of the five integers. 
# Then print the respective minimum and
#  maximum values as a single line 
# of two space-separated long integers.