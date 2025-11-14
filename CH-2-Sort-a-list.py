"""
2. Sort a list
Create a function in Python that accepts two parameters. 
The first will be a list of numbers. 
The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. 
If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.

"""

def sort_a_list(list_to_be_rearranged, sorting_order):
  
    if sorting_order == 'asc':
        for i in range(len(list_to_be_rearranged)):
            if i == len(list_to_be_rearranged) - 1:
                break
            while list_to_be_rearranged[i] > list_to_be_rearranged[i+1]:              
                list_to_be_rearranged[i], list_to_be_rearranged[i + 1] = list_to_be_rearranged[i+1], list_to_be_rearranged[i]
                print(list_to_be_rearranged)
    
    print(list_to_be_rearranged)
        
      




sort_a_list([1, 2, 3, 6, 9, 8, 0, -3 ], 'asc')



            

