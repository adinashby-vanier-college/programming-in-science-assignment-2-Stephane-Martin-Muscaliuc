# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    maxNum1 = 0
    maxNum2 = 0
    sortedNums = sorted(numbers)
    
    
    maxNum1 = sortedNums[-1]
    
    
    for i in range(len(sortedNums) - 1, -1, -1):
        if sortedNums[i] < maxNum1:
            maxNum2 = sortedNums[i]
            break
        
    
    else:
            return (maxNum1, None)

   
    return (maxNum1, maxNum2)



# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
   
   
    numsUnique = set(numbers)
    
    sortedUniqueNums = sorted(numsUnique)
    
    
    return sortedUniqueNums

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    cumulativeSum = [0] * len(arr)
    sum = 0

    
    for i in range(len(cumulativeSum)):
        
        sum += arr[i]
        cumulativeSum[i] = sum
        print(cumulativeSum[i])
    
    
    return cumulativeSum

cumulative_sum([1, 2, 3, 4])

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])


    trans = []

    
    for cols in range(columns):
        new_row = []

        for i in range(rows):
            new_row.append(0)

        trans.append(new_row)


    for r in range(rows):
        for cols in range(columns):
            trans[cols][r] = matrix[r][cols]


    return trans
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    result = []

    
    for i in range(0, len(lst), step):
        result.append(lst[i])

    
    return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    total = 0

    
    for i in range(len(list1)):
        total = total + (list1[i] * list2[i])

    
    return total

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    r1 = len(matrix1)
    c1 = len(matrix1[0])
    r2 = len(matrix2)
    c2 = len(matrix2[0])

    
    result = []


    for i in range(r1):
        new_r = []
        
        for j in range(c2):
            new_r.append(0)
        
        result.append(new_r)


    for i in range(r1):
        for j in range(c2):
            total = 0

            for k in range(c1):
                total = total + (matrix1[i][k] * matrix2[k][j])
            
            result[i][j] = total


    return result
