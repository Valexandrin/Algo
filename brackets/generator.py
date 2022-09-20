import sys
n = int(sys.stdin.readline())
def bracket(count, s='', left=0, right=0, step = 1):    
    if left == count and right == count:        
        print(s)
    else:        
        if left < count:            
            bracket(count, s + '(', left+1, right, step)               
            step += 1
        if right < left:            
            bracket(count, s + ')', left, right+1, step)
            step += 1
            
bracket(n)
