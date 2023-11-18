def main():
    matrix = input_square_matrix()
    right_hand_side_vector = input_right_hand_side_vector(matrix)

    # makes something special if it is a 1x1 matrix
    if len(matrix) == 1:
        if matrix[0] == 0:
            raise ValueError("\nThe matrix you put in isn't invertible, it is singular!") 

        else:
            print("\nYour matrix has the size 1x1\n")

            inverse = []
            inverse = 1/matrix[0]
            print("The inverse of your matrix is:")
            print(f"[{inverse}]")

    # if it isn't a 1x1 matrix it performs the following path
    else:
        size_matrix = len(matrix)
        check_matrix(matrix, size_matrix)
        identity_matrix = get_identity_matrix(size_matrix)
        augumented_matrix = add_matrices(matrix, identity_matrix)
        new_augumented_matrix = gauss_elimination(augumented_matrix, size_matrix)
        inverse = get_inverse(new_augumented_matrix, size_matrix)
        result = solve_linear_equations(inverse, right_hand_side_vector)
        print(result)


# gets a square matrix as an input
def input_square_matrix():
    input_matrix = input("\nEnter a square matrix as a nested list (make a list for every row): ")
    matrix = eval(input_matrix)
    return matrix


# gets a right-hand vector as an input, and also checks if it is the right size 
# for the provided matrix
def input_right_hand_side_vector(matrix):
    right_hand_side_vector = input("\nEnter a right-hand side vector as a list: ")
    right_hand_side_vector = eval(right_hand_side_vector)
    if len(right_hand_side_vector) != len(matrix[0]):
        raise ValueError("Vector doesn't have the right amount of elements for the type of matrix!")
    return right_hand_side_vector


# calculates the determinant to later see if the matrix is invertible
def calculate_determinant(matrix, size_matrix):
    if size_matrix == 1:
        return matrix[0][0]
    determinant = 0
    for col in range(size_matrix):
        cofactor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        determinant += ((-1) ** col) * matrix[0][col] * calculate_determinant(cofactor, size_matrix - 1)
    return determinant


# checks if the provided matrix is a square matrix, then prints out which size 
# of matrix it is and thenchecks if the determinant, calculated in the function
# before is = 0 if any of these things are wron it rasies an error
def check_matrix(matrix, size_matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("\nThe matrix you put in isn't a square matrix!")
    for row in matrix:
        if len(row) != size_matrix:
            raise ValueError("\nThe matrix you put in hasn't the same number of values in each row!")    
    determinant = calculate_determinant(matrix, size_matrix)
    if determinant == 0:
        raise ValueError("\nThe matrix you put in isn't invertible, it is singular!")


# makes an identity matrix that has the exact same size as the matrix the user provided
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


# combines the two matrices (the one of the input and the identity matrix)
def add_matrices(matrix, identity_matrix):
    augumented_matrix = [row_matrix + row_identity_matrix for row_matrix, row_identity_matrix in zip(matrix, identity_matrix)]
    return augumented_matrix


# performs the gauss elimination, with the augmented matrix, 
def gauss_elimination(augmented_matrix, size_matrix):
    new_augumented_matrix = [row[:] for row in augmented_matrix]
    for i in range(size_matrix):
        # normalize the pivot row
        pivot_element = new_augumented_matrix[i][i]
        if pivot_element != 1:
            new_augumented_matrix[i] = [element / pivot_element for element in new_augumented_matrix[i]]

        # eliminate other rows for the current column
        for j in range(size_matrix):
            if j != i:
                factor = new_augumented_matrix[j][i]
                new_augumented_matrix[j] = [element - factor * new_augumented_matrix[i][index] for index, element in enumerate(new_augumented_matrix[j])]
    return new_augumented_matrix


# the gauss_algorithm provides a new matrix, of which we can erase the 
# left part so we have only the invers left
def get_inverse(new_augumented_matrix, size_matrix):
    inverse = [row[size_matrix:] for row in new_augumented_matrix]
    return inverse


# solves the linear equation Ax = b, it multiplies A^-1 * b
def solve_linear_equations(inverse, right_hand_side_vector):
    result = [0] * len(right_hand_side_vector)
    for i in range(len(inverse)):
        for j in range(len(right_hand_side_vector)):
            result[i] += inverse[i][j] * right_hand_side_vector[j]
    return result


if __name__ == "__main__":
    main()