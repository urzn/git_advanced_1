from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """    
    Determines if a number is even and return an even list. 
    
    Args:        
        int_list: A list of integer.   
        
    Returns:   
        A list of even integers.    
    """    
    # TODO: Implement even_list  
    
    nums=len(int_list)
    ev_list=[]
    i=0
    while (i<nums):
        if (int_list[i]%2==0):
            ev_list.append(int_list[i])
            i+=1
        else:
            i+=1
        continue    
    return ev_list        


# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:    
    """    
    Computes the sum of the squares of all even numbers in a list of integers.    
    Args:        
        even_int_list: A list of even integers.   
    Returns:       
        The sum of the squares of all even numbers in the list.  
    """   
    # TODO: Implement sum_of_squares_of_even  
    num=len(even_int_list)
    i=0
    sum=0
    while(i<num):
        sum+=even_int_list[i]*even_int_list[i]
        i+=1
    return sum


# Main function
def main():  
    # Example list 
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
    even_int_list = even_list(int_list)    
    output = sum_of_squares_of_even(even_int_list)  
    print(output)
    
    
# Boilerplate code
if __name__ == "__main__":   
    main()