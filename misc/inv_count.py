

def inv_count(arr,count_inv=0):
    #defining base cases
    if len(arr)==1:
        return arr,count_inv
    elif len(arr)==2:
        if arr[0]>arr[1]:
            count_inv+=1
            arr[0],arr[1]=arr[1],arr[0]
        return arr,count_inv
    else:#recursion
        arr_i,count_inv=inv_count(arr[:len(arr)/2],count_inv=count_inv)
        arr_k,count_inv=inv_count(arr[len(arr)/2:],count_inv=count_inv)
        #combining sorted arrays
        counter_k=0
        counter=0
        print arr_i
        print arr_k
        for i in range(len(arr_i)):
            while counter_k<len(arr_k) and arr_k[counter_k]<arr_i[i]:
                arr[counter]=arr_k[counter_k]
                print count_inv
                count_inv+=len(arr_i)+counter_k-counter
                print count_inv
                counter_k+=1
                counter+=1
            arr[counter]=arr_i[i]
            counter+=1
        while counter_k<len(arr_k):
            arr[counter]=arr_k[counter_k]
            counter+=1
            counter_k+=1
        return arr,count_inv

print inv_count([7,6,5,4,3,2,1])#inv_count([10,1,12,3,17,2,16,0])
