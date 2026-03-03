# 5. You are given a string S consisting of lowercase English letters. A duplicate 
# removal consists of choosing two adjacent and equal letters and removing 
# them. We repeatedly make duplicate removals on S until we no longer can. 
# Write a program to return the final string after all such duplicate removals have 
# been made.  
# Input: s = abbaca 
# Output: ca 
# Explanation:  
# For example, in "abbaca" we could remove "bb" since the 
# letters are adjacent and equal, and this is the only possible 
# move.  The result of this move is that the string is "aaca", 
# of which only "aa" is possible, so the final string is "ca".

x='bbaaccacdddef'
l1=[]

def finalString():
    global x
    for  i in range(len(x)-1):
        print('i',i)
        if x[i] == x[i+1]:
            l1.append(i)
            l1.append(i+2)
    print(l1)
    
    if len(l1) > 0 :
        x=x[:l1[0]] +x [l1[1]:]
    return l1

while(True):
  
    z=finalString()
    print(z) 

    def is_Empty():
        if len(z) == 0:
            return True
        else:
            return False

    print(x)
    
    while(z):
        print("hii")
        l1.clear()
        finalString()
    
    
    break

print(x)        


        