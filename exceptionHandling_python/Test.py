l=[x for x in range(-10,11)]
Sum=0
Sum1=0
Sum2=0
for x in l:
    if x>0:
        if x%2==0:
            Sum=Sum+x
        else:
            Sum1=Sum1+x
    else:
        Sum2=Sum2+x         
                   
print("the sum of +ve even and odd  and -ve:",Sum)