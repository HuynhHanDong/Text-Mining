def min_edit_distance(str1, str2, sub_cost, del_cost, insert_cost):
    m, n = len(str1), len(str2)

    # Initialize matrix with dimensions (m+1) x (n+1)
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize first row
    for j in range(n + 1):
        matrix[0][j] = j * insert_cost

    # Initialize first column 
    for i in range(m + 1):
        matrix[i][0] = i * del_cost

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]  # No cost
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j - 1] + sub_cost,  # Substitution
                    matrix[i - 1][j] + del_cost,      # Deletion
                    matrix[i][j - 1] + insert_cost    # Insertion
                )
    return matrix, matrix[m][n]

def print_matrix(str1, str2, matrix):
    m, n = len(str1), len(str2)

    print("Min Edit Distance Matrix:")
    print("  ", "  ".join([" "] + list(str2)))

    for i in range(m + 1):
        row = [str1[i - 1] if i > 0 else " "] + [str(matrix[i][j]) for j in range(n + 1)]
        print("  ".join(row))

def main():
    str1 = "institution"
    str2 = "tuition"
    matrix, min_edit_dist = min_edit_distance(str1, str2, sub_cost=2, del_cost=1, insert_cost=1)
    print_matrix(str1, str2, matrix)
    print("\nMinimum Edit Distance:", min_edit_dist)

if __name__ == "__main__":
    main()