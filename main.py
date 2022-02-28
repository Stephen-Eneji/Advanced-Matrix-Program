# import kivy module
# import kivy
# from kivy.app import App
# from kivy.uix.button import Button
# # this restrict the kivy version i.e
# # below this kivy version you cannot
# # use the app or software
# kivy.require("1.9.1")


# class in which we are creating the button
# class ButtonApp(App):
#
#     def build(self):
#         btn = Button(text="Push Me !")
#         return btn


# creating the object root for ButtonApp() class
# root = ButtonApp()
# root.run()

# WRITING A PROGRAM THAT SUM 2X2 MATRIX

print("WELCOME TO MATRIPSY")

selectioninput = input(f"Input {1} for 2x2 matrix or {2} for 3x3 matrix: ")
#Script for 2x2 matrix

def logicfor2x2(self):
# The Location of the characters of the matrix using rows and column #Mat1
# Matrix 1
    m1_row1 = input("Row 1, Col 1: ")
    m1_row2 = input("Row 1, Col 2: ")
    m1_col1 = input("Row 2, Col 1: ")
    m1_col2 = input("Row 2, Col 2: ")

    # The Location of the characters of the matrix using rows and columns #Mat2
    # Matrix 2
    m2_row1 = input("Row 1, Col 1: ")
    m2_row2 = input("Row 1, Col 2: ")
    m2_col1 = input("Row 2, Col 1: ")
    m2_col2 = input("Row 2, Col 2: ")

    # Logic
    def input_validation():

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
            print(m1_row1_num + m2_row1_num)

        if m1_row2.isdigit():
            print(m1_row2_num + m2_row2_num)

        if m1_col1.isdigit():
            print(m1_col1_num + m2_col1_num)

        if m2_col2.isdigit():
            print(m1_col2_num + m2_col2_num)
        else:
            print("Enter 4 number")

    input_validation()

    logicfor2x2(1)



#Script for 3x3 matrix
def logicfor3x3(self):
    # The Location of the characters of the matrix using rows and column #Mat1

    # Matrix 1
    #Row1
    m1_r1c1 = input("Row 1, Col 1: ")
    m1_r1c2 = input("Row 1, Col 2: ")
    m1_r1c3 = input("Row 1, Col 3: ")

    #Row2
    m1_r2c1 = input("Row 2, Col 1: ")
    m1_r2c2 = input("Row 2, Col 2: ")
    m1_r2c3 = input("Row 2, Col 3: ")

    #Row3
    m1_r3c1 = input("Row 3, Col 1: ")
    m1_r3c2 = input("Row 3, Col 2: ")
    m1_r3c3 = input("Row 3, Col 3: ")


    # The Location of the characters of the matrix using rows and columns #Mat2
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
    def input_validation_3():
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
            print(m1_r1c1_num + m2_r1c1_num)

        if m1_r1c2.isdigit():
            print(m1_r1c2_num + m2_r1c2_num)

        if m1_r1c3.isdigit():
            print(m1_r1c3_num + m2_r1c3_num)

        #Row2
        if m1_r2c1.isdigit():
            print(m1_r2c1_num + m2_r2c1_num)

        if m1_r2c2.isdigit():
            print(m1_r2c1_num + m2_r2c1_num)

        if m1_r2c3.isdigit():
            print(m1_r2c3_num + m2_r2c3_num)

        #Row3
        if m1_r3c1.isdigit():
            print(m1_r3c1_num + m2_r3c1_num)

        if m1_r3c2.isdigit():
            print(m1_r3c1_num + m2_r3c1_num)

        if m1_r3c3.isdigit():
            print(m1_r3c3_num + m2_r3c3_num)

        else:
            print("Enter 6 number")

    input_validation_3()
logicfor3x3(2)


def matrixtypeselection():
    if selectioninput == 1:
        print(logicfor2x2)
    elif selectioninput == 2:
        print(logicfor3x3)

matrixtypeselection()