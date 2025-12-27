MOD = 1000000007

n, q = map(int, input().split())

matrix = []

def mul_main_diag(sub_matrix):
    res = 1
    for i in range(len(sub_matrix)):
        res *= sub_matrix[i][i]
        res = ((res % MOD) + MOD) % MOD
    return res

def mul_sub_diag(sub_matrix):
    res = 1
    for i in range(len(sub_matrix)):
        res *= sub_matrix[i][len(sub_matrix) - 1 - i] 
        res = ((res % MOD) + MOD) % MOD
    return res

def f(sub_matrix):
    res = mul_main_diag(sub_matrix) - mul_sub_diag(sub_matrix)
    res = ((res % MOD) + MOD) % MOD
    return res

def guazi(matrixB, matrixC):
    res = f(matrixB) * f(matrixC)
    res = ((res % MOD) + MOD) % MOD
    return res

def get_remaining_matrix(matrix, row_to_be_deleted, col_to_be_deleted):
    return [
        [matrix[i][j] for j in range(len(matrix[i])) if j not in col_to_be_deleted]
        for i in range(len(matrix)) if i not in row_to_be_deleted
    ]

def get_deleting_cross_matrix(matrix, row_to_be_deleted, col_to_be_deleted):
    return [
        [matrix[i][j] for j in range(len(matrix[i])) if j in col_to_be_deleted]
        for i in range(len(matrix)) if i in row_to_be_deleted
    ]




# =============================


def compute_f_B(row_to_be_deleted, col_to_be_deleted):
    selected_rows = [i for i in range(len(matrix)) if i not in row_to_be_deleted]
    selected_cols = [j for j in range(len(matrix[0])) if j not in col_to_be_deleted]

    if not selected_rows or not selected_cols:
        return 0

    res_main = 1
    res_sub = 1

    for i in range(len(selected_rows)):
        res_main *= matrix[selected_rows[i]][selected_cols[i]]
        res_sub *= matrix[selected_rows[i]][selected_cols[len(selected_cols) - 1 - i]]

        res_main = ((res_main % MOD) + MOD) % MOD
        res_sub = ((res_sub % MOD) + MOD) % MOD

    return (((res_main - res_sub) % MOD) + MOD) % MOD


def compute_f_C(row_to_be_deleted, col_to_be_deleted):
    selected_rows = row_to_be_deleted
    selected_cols = col_to_be_deleted

    if not selected_rows or not selected_cols:
        return 0

    res_main = 1
    res_sub = 1

    for i in range(len(selected_rows)):
        res_main *= matrix[selected_rows[i]][selected_cols[i]]
        res_sub *= matrix[selected_rows[i]][selected_cols[len(selected_cols) - 1 - i]]

        res_main = ((res_main % MOD) + MOD) % MOD
        res_sub = ((res_sub % MOD) + MOD) % MOD

    return (((res_main - res_sub) % MOD) + MOD) % MOD





for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for _ in range(q):
    temp = list(map(int, input().split()))
    k = temp[0]
    row_to_be_deleted = temp[1:k+1]
    col_to_be_deleted = temp[k+1:]
    row_to_be_deleted = [r - 1 for r in row_to_be_deleted]
    col_to_be_deleted = [c - 1 for c in col_to_be_deleted]

    # # print("row_to_be_deleted:", row_to_be_deleted)
    # # print("col_to_be_deleted:", col_to_be_deleted)

    # B = get_remaining_matrix(matrix, row_to_be_deleted, col_to_be_deleted)
    # C = get_deleting_cross_matrix(matrix, row_to_be_deleted, col_to_be_deleted)

    # # print(">>>")
    # # print(B)
    # # print(">>>")
    # # print(C)

    # # print(">>>")
    # print(guazi(B, C))

    res = compute_f_B(row_to_be_deleted, col_to_be_deleted) * compute_f_C(row_to_be_deleted, col_to_be_deleted)
    res = ((res % MOD) + MOD) % MOD
    print(res)
    