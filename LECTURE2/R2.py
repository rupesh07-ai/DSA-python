def printNumber(i,n):
    if i>n:
        return
    print(i , end = '')
    
    printNumber(i+1 ,n)
    
printNumber(1,5)