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

from Sum import *
from Difference import *
from Product import *

# MATRIX Logic
print("WELCOME TO MATRIPSY")

matrixTypeselector = input("Input 1 = 2x2 Matrix, 2 = 2x3 Matrix, 3 = 3x3 matrix, 4 = 3x2 Matrix: ")
operationSelector = input("1 FOR SUM, 2 FOR DIFFERENCE, 3 FOR PRODUCT")

def operationSelection():
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