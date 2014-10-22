__author__ = 'Craig'


class CommandLineInterface:

    def __init__(self):
        pass

    def isDone(self, inputValue=""):
        return inputValue.lower() == "exit"

    def getInput(self):
        return raw_input("Please enter the IP Address to check: ")

    def reportResult(self, count):
        print("Found %d entries." % count)

    def displayError(self, errorMsg):
        print(errorMsg)