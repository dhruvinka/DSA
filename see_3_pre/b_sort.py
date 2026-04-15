
def sort():
        arr=[("Nash", "ILV641",78.79,"Male"),
            ("Ainsley", "DYY371", 40.96, "Female"),
            ("Hedda", "LDB343", 55.29, "Male"),
            ("Shafira", "UBW126", 61.47, "Female"),
            ("Camilla", "HMM604", 89.26, "Female"),
            ("Sydney", "GFJ647", 59.50, "Female"),
            ("Acton", "YQQ138", 65.87, "Male"),
            ("Coby", "JPH342", -44.05, "Male")]
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][2] < arr[j][2]:
                    arr[i],arr[j]=arr[j],arr[i]
        for i in arr:
            print(i)

        with open('sort.txt','w') as f:
            for i in arr:
                f.write(str(i)+'\n')

sort()  