# 15. The file system crawler keeps a log each time some user performs a change 
# folder operation.  
# The operations are described below: 
# ● "../" : Move to the parent folder of the current folder. (If you are already 
# in the main folder, remain in the same folder). 
# ● "./" : Remain in the same folder. 
# ● "x/" : Move to the child folder named x (This folder is guaranteed to 
# always exist).


# logs = ["d1/","../","../","../"]
# logs = ["d1/","../","../","../"] 
logs = ["d1/","d2/","./","d3/","../","d31/"] 
count=0
for i in logs:
    if len(i.split("..")) == 2 :
        if count == 0:
            continue
        else:
            count-=1
    elif len(i.split(".")) == 2:
        continue
    else:
        count+=1
print(count)
    

    

