
   # swap based algorithm
   ## Intiuition(ascending)
       A1 A2 A3 A4.....
       A1<=A2
    point is Ai shoule be less than or equal to Ai+1

    Then take two pair of elemenet (Ai, Ai+1) compare Ai and Ai+1
     
    If Ai<=Ai+1 (in correct order) move ahead
    else swap(Ai , Ai+1) // bring them to correct order

  #### 3 1 5 0 4
    step 1: (3 1) 5 0 4 => (not in correct order) (swap) 1 3 5 0 4
    step 2: 1 (3 5) 0 4 => (correct order) move ahead
    step 3: 1 3 (5 0) 4 => (not in correct order) (swap) 1 3 0 5 4
    step 4: 1 3 0 (5 4) => (not in correct order) (swap) 1 3 0 4 5

  #### 1 3 0 4 5
    step 1: (1 3) 0 4 5 => (correct order) move ahead
    step 2: 1 (3 0) 4 5 => (not in correct order) (swap) 1 0 3 4 5
    step 3: 1 0 (3 4) 5 => (correct order) move   1 0 3 4 5 

### SHOULD WE GO FOR LAST COMPARISON?
    Ans: No. Because at the end of 1st iteration highest element already in it's correct possition (n-1)th.
         and now 2nd highest element in it's correct place(n-2)th place. Then why should we take an unnecessary
         (n-1)th and (n-2)th comparision.

  #### 1 0 3 4 5
    Step 1: (1 0) 3 4 5 => (not in correct order) (swap) 0 1 3 4 5
    step 2: 0 (1 3) 4 5 => (correct order) move 0 1 3 4 5

  #### 0 1 3 4 5
    Step 1: (0 1) 3 4 5 => (correct order) move 0 1 3 4 5

###  HOW NUMBER OF ITERATION REQUIRED TO PLACE ALL ELEMENT IT'S CORRECT POSITION?
         - In 1st iteration (n-1)th poisition is fixed (highest element)
         - In 2nd iteration (n-2)th poisition is fixed (2nd highest element)
         - In 3rd iteration (n-3)th poisition is fixed (3rd highest element)
         .
         .
         .
         - In ith iteration (n-i)th poisition is fixed (ith element)
         .
         .
         .
         - In (n-1)th iteration (n-(n-1))th = 1st poisition is fixed (2nd element)

### SHOULD WE GO FOR LAST ITERATION?
    Ans: No. At the end of (n-1)th iteration 1st element already in it's correct position
           - (A0 A1) A1 in correct position means A0 <= A1 then A0 also in correct position
    
    Total number of iteration required is (n-1)

#### After 1 iteration we noticed one(bigger element) in right position
         - Total number of swap required to fix the (n-1)th position is (n-1) swap // highest element
         - Total number of swap required to fix the (n-2)th position is (n-2) swap // 2nd highest element
         - Total number of swap required to fix the (n-3)th position is (n-3) swap // 3rd
         .
         .
         .
         - Total number of swap required to fix the (n-i)th position is (n-i) swap // ith element
         .
         .
         - Total number of swap required to fix the 1st position is 1 swap    // 2nd lowest element
         - Total number of swap required to fix the 0th position is 0 swap    // lowest element

### HOW NUMBER OF SWAP REQUIRED TO PLACE ALL ELEMENT IT'S CORRECT POSITION?
           (n-1) + (n-2) + (n-3) + ........+1
           = (n(n-1)/2)

# Program

from typing import List

### Ascending order
def bubble_sort_ascending(array: List[int]):
     # Iterate from 0 to n-1
    for i in range(len(array)):
        #(Ai, Ai+1) compare Ai and Ai+1 from 0 to n-i-2 
        for j in range(0,len(array)-1-i):
            # compare Ai,Ai+1 and if not in correct position then swap
            if array[j] > array[j+1]: # For descending change to '<'
                array[j], array[j+1] = array[j+1], array[j]

def main():
    array = list(map(int, input('Enter the unsorted array: ').split( )))
    bubble_sort_ascending(array=array)
    print(array)

main()