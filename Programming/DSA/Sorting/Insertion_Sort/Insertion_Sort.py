from typing import List

def inserionSort(array:List[int]):
    #Traverse from 1 to n-1 and assume all element before i(0 to i-1) are sorted.
    count = 0
    for i in range(len(array)):
        # Find the acctual position of ith element
        # compare the element from i-1 until finds it's actual position
        # if arr[j] > arr[i] then swap
        current_value = array[i]
        j = i - 1
        while(j>=0 and array[j]>current_value):
            
            array[j+1] = array[j]
            count += 1
            print('current_value: {} array[j]: {}, count: {}'.format(current_value, array[j],count))
            j -= 1
        j += 1
        array[j] = current_value
    print(array,count, sep= '\n')

def main():
    array = list(map(int,input('Enter the array element: ').split(" ")))
    inserionSort(array= array)

main()