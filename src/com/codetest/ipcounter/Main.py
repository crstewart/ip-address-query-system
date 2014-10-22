#!/usr/bin/env python

import com.codetest.ipcounter.components.UserInterfaces as UserInterfaces
import com.codetest.ipcounter.components.QueryTools as QueryTools

__author__ = 'Craig'


class IpAddressCounter:
    def __init__(self):
        self.__userInterface = UserInterfaces.CommandLineInterface()
        self.__queryTool = QueryTools.QueryTool("../../../../logs/visitors.log")

    def main(self):
        self.__queryTool.load()
        while True:
            try:
                inputValue = self.__userInterface.getInput()
                if self.__userInterface.isDone(inputValue):
                    return
                count = self.__queryTool.getVisitCountForIpAddress(inputValue)
                self.__userInterface.reportResult(count)
            except AssertionError:
                self.__userInterface.displayError("Encountered an error: The input was not an IP address!")
            except EOFError:
                self.__userInterface.displayError("Program interrupted abnormally.")

if __name__ == "__main__":
    mainObj = IpAddressCounter()
    mainObj.main()