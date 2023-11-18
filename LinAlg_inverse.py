def main():
    matrix = input_square_matrix()
    if len(matrix) == 1:
        if matrix[0] == 0:
            raise ValueError("\nThe matrix you put in isn't invertible, it is singular!") 

        else:
            print("\nYour matrix has the size 1x1\n")

            inverse = []
            inverse = 1/matrix[0]
            print("The inverse of your matrix is:")
            print(f"[{inverse}]")

    else:
        size_matrix = len(matrix)
        check_matrix(matrix, size_matrix)


        identity_matrix = get_identity_matrix(size_matrix)
   
    
        augumented_matrix = add_matrices(matrix, identity_matrix)
 

        new_augumented_matrix = gauss_elimination(augumented_matrix, size_matrix)



        inverse = get_inverse(new_augumented_matrix, size_matrix)
        print("The inverse of your matrix is:")
        print(inverse)




def input_square_matrix():
    input_matrix = input("\nEnter a square matrix as a nested list (make a list for every row): ")
    matrix = eval(input_matrix)
    return matrix

def calculate_determinant(matrix, size_matrix):
    if size_matrix == 1:
        return matrix[0][0]

    determinant = 0
    for col in range(size_matrix):
        cofactor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        determinant += ((-1) ** col) * matrix[0][col] * calculate_determinant(cofactor, size_matrix - 1)
        
    return determinant


def check_matrix(matrix, size_matrix):

    if len(matrix) != len(matrix[0]):
        raise ValueError("\nThe matrix you put in isn't a square matrix!")
    
    for row in matrix:
        if len(row) != size_matrix:
            raise ValueError("\nThe matrix you put in hasn't the same number of values in each row!")
        

    else:
        print(f"\nYour matrix has the size {size_matrix}x{size_matrix}\n")

    determinant = calculate_determinant(matrix, size_matrix)
    if determinant == 0:
        raise ValueError("\nThe matrix you put in isn't invertible, it is singular!")




def get_identity_matrix(size_matrix):
    identity_matrix = []
    
    for i in range(size_matrix):
        row = [] 
        for j in range(size_matrix):
            if i == j: 
                row.append(1)
            else:
                row.append(0)
        
        identity_matrix.append(row)
       
    return identity_matrix


def add_matrices(matrix, identity_matrix):
    augumented_matrix = [row_matrix + row_identity_matrix for row_matrix, row_identity_matrix in zip(matrix, identity_matrix)]

    return augumented_matrix

def gauss_elimination(augmented_matrix, size_matrix):
    new_augumented_matrix = [row[:] for row in augmented_matrix]

    for i in range(size_matrix):
        # Normalize the pivot row
        pivot_element = new_augumented_matrix[i][i]
        if pivot_element != 1:
            new_augumented_matrix[i] = [element / pivot_element for element in new_augumented_matrix[i]]

        # Eliminate other rows for the current column
        for j in range(size_matrix):
            if j != i:
                factor = new_augumented_matrix[j][i]
                new_augumented_matrix[j] = [element - factor * new_augumented_matrix[i][index] for index, element in enumerate(new_augumented_matrix[j])]

    return new_augumented_matrix


def get_inverse(new_augumented_matrix, size_matrix):
    inverse = [row[size_matrix:] for row in new_augumented_matrix]
    return inverse


        


if __name__ == "__main__":
    main()