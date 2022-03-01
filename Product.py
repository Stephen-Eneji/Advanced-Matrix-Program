from main import *
#################
# SCRIPT FOR 2x2 MATRIX
def logicfor2x2():
    # The Location of the characters of the matrix using rows and column #Mat1
    # Matrix 1

    print("Data for Matrix 1")
    m1_row1 = input("Row 1, Col 1: ")
    m1_row2 = input("Row 1, Col 2: ")
    m1_col1 = input("Row 2, Col 1: ")
    m1_col2 = input("Row 2, Col 2: ")

    # The Location of the characters of the matrix using rows and columns #Mat2
    # Matrix 2
    print("Data for Matrix 2")
    m2_row1 = input("Row 1, Col 1: ")
    m2_row2 = input("Row 1, Col 2: ")
    m2_col1 = input("Row 2, Col 1: ")
    m2_col2 = input("Row 2, Col 2: ")

    # Logic
    # MATRIX 1
    m1_row1_num = float(m1_row1)
    m1_row2_num = float(m1_row2)
    m1_col1_num = float(m1_col1)
    m1_col2_num = float(m1_col2)

    # MATRIX 2
    m2_row1_num = float(m2_row1)
    m2_row2_num = float(m2_row2)
    m2_col1_num = float(m2_col1)
    m2_col2_num = float(m2_col2)

    if m1_row1.isdigit():
        print(m1_row1_num * m2_row1_num)

    if m1_row2.isdigit():
        print(m1_row2_num * m2_row2_num)

    if m1_col1.isdigit():
        print(m1_col1_num * m2_col1_num)

    if m2_col2.isdigit():
        print(m1_col2_num * m2_col2_num)
    else:
        print("Enter valid number")


###############
# Script for 2x3 matrix

def logicfor2x3():
    # The Location of the characters of the matrix using rows and column #Mat1
    # Matrix 1
    # Row1
    print("Data for Matrix 1")
    m1_r1c1 = input("Row 1, Col 1: ")
    m1_r1c2 = input("Row 1, Col 2: ")

    # Row2
    m1_r2c1 = input("Row 2, Col 1: ")
    m1_r2c2 = input("Row 2, Col 2: ")

    # Row3
    m1_r3c1 = input("Row 3, Col 1: ")
    m1_r3c2 = input("Row 3, Col 2: ")

    # The Location of the characters of the matrix using rows and columns #Mat2
    print("Data for Matrix 2")
    # Matrix 2
    m2_r1c1 = input("Row 1, Col 1: ")
    m2_r1c2 = input("Row 1, Col 2: ")

    # Row2
    m2_r2c1 = input("Row 2, Col 1: ")
    m2_r2c2 = input("Row 2, Col 2: ")

    # Row3
    m2_r3c1 = input("Row 3, Col 1: ")
    m2_r3c2 = input("Row 3, Col 2: ")

    # Logic

    # MATRIX 1
    m1_r1c1_num = float(m1_r1c1)
    m1_r1c2_num = float(m1_r1c2)

    m1_r2c1_num = float(m1_r2c1)
    m1_r2c2_num = float(m1_r2c2)

    m1_r3c1_num = float(m1_r3c1)
    m1_r3c2_num = float(m1_r3c2)


    # MATRIX 2
    m2_r1c1_num = float(m2_r1c1)
    m2_r1c2_num = float(m2_r1c2)

    m2_r2c1_num = float(m2_r2c1)
    m2_r2c2_num = float(m2_r2c2)

    m2_r3c1_num = float(m2_r3c1)
    m2_r3c2_num = float(m2_r3c2)

    if m1_r1c1.isdigit():
        print(m1_r1c1_num * m2_r1c1_num)

    if m1_r1c2.isdigit():
        print(m1_r1c2_num * m2_r1c2_num)

    # Row2
    if m1_r2c1.isdigit():
        print(m1_r2c1_num * m2_r2c1_num)

    if m1_r2c2.isdigit():
        print(m1_r2c2_num * m2_r2c2_num)

    # Row3
    if m1_r3c1.isdigit():
        print(m1_r3c1_num * m2_r3c1_num)

    if m1_r3c2.isdigit():
        print(m1_r3c2_num * m2_r3c2_num)

    else:
        print("Enter a valid number")


###############
# Script for 3x3 matrix
def logicfor3x3():
    # The Location of the characters of the matrix using rows and column #Mat1
    # Matrix 1
    # Row1
    print("Data for Matrix 1")
    m1_r1c1 = input("Row 1, Col 1: ")
    m1_r1c2 = input("Row 1, Col 2: ")
    m1_r1c3 = input("Row 1, Col 3: ")

    # Row2
    m1_r2c1 = input("Row 2, Col 1: ")
    m1_r2c2 = input("Row 2, Col 2: ")
    m1_r2c3 = input("Row 2, Col 3: ")

    # Row3
    m1_r3c1 = input("Row 3, Col 1: ")
    m1_r3c2 = input("Row 3, Col 2: ")
    m1_r3c3 = input("Row 3, Col 3: ")

    # The Location of the characters of the matrix using rows and columns #Mat2
    print("Data for Matrix 2")
    # Matrix 2
    # Row1
    m2_r1c1 = input("Row 1, Col 1: ")
    m2_r1c2 = input("Row 1, Col 2: ")
    m2_r1c3 = input("Row 1, Col 3: ")

    # Row2
    m2_r2c1 = input("Row 2, Col 1: ")
    m2_r2c2 = input("Row 2, Col 2: ")
    m2_r2c3 = input("Row 2, Col 3: ")

    # Row3
    m2_r3c1 = input("Row 3, Col 1: ")
    m2_r3c2 = input("Row 3, Col 2: ")
    m2_r3c3 = input("Row 3, Col 3: ")

    # Logic

    # MATRIX 1
    m1_r1c1_num = float(m1_r1c1)
    m1_r1c2_num = float(m1_r1c2)
    m1_r1c3_num = float(m1_r1c3)

    m1_r2c1_num = float(m1_r2c1)
    m1_r2c2_num = float(m1_r2c2)
    m1_r2c3_num = float(m1_r2c3)

    m1_r3c1_num = float(m1_r3c1)
    m1_r3c2_num = float(m1_r3c2)
    m1_r3c3_num = float(m1_r3c3)

    # MATRIX 2
    m2_r1c1_num = float(m2_r1c1)
    m2_r1c2_num = float(m2_r1c2)
    m2_r1c3_num = float(m2_r1c3)

    m2_r2c1_num = float(m2_r2c1)
    m2_r2c2_num = float(m2_r2c2)
    m2_r2c3_num = float(m2_r2c3)

    m2_r3c1_num = float(m2_r3c1)
    m2_r3c2_num = float(m2_r3c2)
    m2_r3c3_num = float(m2_r3c3)

    if m1_r1c1.isdigit():
        print(m1_r1c1_num * m2_r1c1_num)

    if m1_r1c2.isdigit():
        print(m1_r1c2_num * m2_r1c2_num)

    if m1_r1c3.isdigit():
        print(m1_r1c3_num * m2_r1c3_num)

    # Row2
    if m1_r2c1.isdigit():
        print(m1_r2c1_num * m2_r2c1_num)

    if m1_r2c2.isdigit():
        print(m1_r2c2_num * m2_r2c2_num)

    if m1_r2c3.isdigit():
        print(m1_r2c3_num * m2_r2c3_num)

    # Row3
    if m1_r3c1.isdigit():
        print(m1_r3c1_num * m2_r3c1_num)

    if m1_r3c2.isdigit():
        print(m1_r3c1_num * m2_r3c1_num)

    if m1_r3c3.isdigit():
        print(m1_r3c3_num * m2_r3c3_num)

    else:
        print("Enter a valid number")


###############
# Script for 3x2 matrix
def logicfor3x2():
    # The Location of the characters of the matrix using rows and column #Mat1
    # Matrix 1
    # Row1
    print("Data for Matrix 1")
    m1_r1c1 = input("Row 1, Col 1: ")
    m1_r1c2 = input("Row 1, Col 2: ")
    m1_r1c3 = input("Row 1, Col 3: ")

    # Row2
    m1_r2c1 = input("Row 2, Col 1: ")
    m1_r2c2 = input("Row 2, Col 2: ")
    m1_r2c3 = input("Row 2, Col 3: ")

    # The Location of the characters of the matrix using rows and columns #Mat2
    print("Data for Matrix 2")
    # Matrix 2
    # Row1
    m2_r1c1 = input("Row 1, Col 1: ")
    m2_r1c2 = input("Row 1, Col 2: ")
    m2_r1c3 = input("Row 1, Col 3: ")

    # Row2
    m2_r2c1 = input("Row 2, Col 1: ")
    m2_r2c2 = input("Row 2, Col 2: ")
    m2_r2c3 = input("Row 2, Col 3: ")

    # Logic

    # MATRIX 1
    m1_r1c1_num = float(m1_r1c1)
    m1_r1c2_num = float(m1_r1c2)
    m1_r1c3_num = float(m1_r1c3)

    m1_r2c1_num = float(m1_r2c1)
    m1_r2c2_num = float(m1_r2c2)
    m1_r2c3_num = float(m1_r2c3)

    # MATRIX 2
    m2_r1c1_num = float(m2_r1c1)
    m2_r1c2_num = float(m2_r1c2)
    m2_r1c3_num = float(m2_r1c3)

    m2_r2c1_num = float(m2_r2c1)
    m2_r2c2_num = float(m2_r2c2)
    m2_r2c3_num = float(m2_r2c3)


    if m1_r1c1.isdigit():
        print(m1_r1c1_num * m2_r1c1_num)

    if m1_r1c2.isdigit():
        print(m1_r1c2_num * m2_r1c2_num)

    if m1_r1c3.isdigit():
        print(m1_r1c3_num * m2_r1c3_num)

    # Row2
    if m1_r2c1.isdigit():
        print(m1_r2c1_num * m2_r2c1_num)

    if m1_r2c2.isdigit():
        print(m1_r2c2_num * m2_r2c2_num)

    if m1_r2c3.isdigit():
        print(m1_r2c3_num * m2_r2c3_num)

    else:
        print("Enter a valid number")


# Logic to get user input and run either code 1 or two based on it

int_matrixTypeselector = int(matrixTypeselector)


def conditionsfortype():
    if int_matrixTypeselector == 1:
        return logicfor2x2()
    elif int_matrixTypeselector == 2:
        return logicfor2x3()
    elif int_matrixTypeselector == 3:
        return logicfor3x3()
    elif int_matrixTypeselector == 4:
        return
    else:
        print("Input 1 or 2")


conditionsfortype()