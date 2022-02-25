#2x2 matrix solver
def userinfo():
    username = input("Enter your name: ")
    print(f"{username}, Welcome to Matrix solverv1.0")
userinfo()

#Matrix 1
m1_row1 = input("Row 1, Col 1: ")
m1_row2 = input("Row 1, Col 2: ")
m1_col1 = input("Row 2, Col 1: ")
m1_col2 = input("Row 2, Col 2: ")

#Matrix 2
m2_row1 = input("Row 1, Col 1: ")
m2_row2 = input("Row 1, Col 2: ")
m2_col1 = input("Row 2, Col 1: ")
m2_col2 = input("Row 2, Col 2: ")

def INPUT_VALIDATIONS():
    #MATRIX 1
    m1_row1_num = float(m1_row1)
    m1_row2_num = float(m1_row2)
    m1_col1_num = float(m1_col1)
    m1_col2_num = float(m1_col2)

    #MATRIX 2
    m2_row1_num = float(m2_row1)
    m2_row2_num = float(m2_row2)
    m2_col1_num = float(m2_col1)
    m2_col2_num = float(m2_col2)

    if m1_row1.isdigit():
        print(m1_row1_num + m2_row1_num)

    if m1_row2.isdigit():
        print(m1_row2_num + m2_row2_num)

    if m1_col1.isdigit():
        print(m1_col1_num + m2_col1_num)

    if m2_col2.isdigit():
        print(m1_col2_num + m2_col2_num)
    else:
        print("Enter 4 number")


INPUT_VALIDATIONS()

'''
#CALCULATION
print(f'Row1Col1 = {m1_row1_num + m2_row1_num}')
print(f'Row2Col1 = {m1_row2_num + m2_row2_num}')
print(f'Row1Col2 = {m2_row1_num + m2_row2_num}')
print(f'Row2Col2 = {m2_row1_num + m2_row2_num}')
'''