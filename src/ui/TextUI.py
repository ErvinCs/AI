from src.controller.GameController import GameControler
from timeit import default_timer as timer


class TextUI:
    def __init__(self):
        self.__con = GameControler("Files\sudoku1.txt")

    def menu(self):
        string = "\t 0.Exit \n"
        string += "\t 1.BFS \n"
        string += "\t 2.GBFS"
        print(string)

    def readCommand(self):
        command = input("Enter command: ").strip()
        return command

    def mainMenu(self):
        print(str(self.__con.getProblem().getInitState()))
        while True:
            self.menu()
            command = self.readCommand()
            if command == '0':
                input("Goodbye.")
                break
            elif command == '1':
                start = timer()
                print(str(self.__con.BFS()))
                end = timer()
                print("RunTime= " + str(end - start) + "\n")
            elif command == '2':
                start = timer()
                print(str(self.__con.GBFS()))
                end = timer()
                print("RunTime= " + str(end - start) + "\n")
            else:
                self.readCommand()


