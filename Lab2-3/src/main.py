from src.UI.EAUI import EAUI
from src.UI.ACOUI import ACOUI
'''
Consider n cubes of known sides’ length si and colors ci . Assemble the highest
pyramid from the cubes in such a way that it has ‘stability’ (there is not a bigger cube
over a smaller one) and there are not two consecutive cubes of the same color.
'''

if __name__ == '__main__':
    while True:
        userInterface = input("Algorithm: ")
        if userInterface == '1':
            ui = EAUI()
            ui.run()
            break
        elif userInterface == '2':
            ui = ACOUI()
            ui.run()
            break
