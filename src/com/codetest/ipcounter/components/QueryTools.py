import re

__author__ = 'Craig'


class QueryTool:

    def __init__(self, logLocation="../../../../../logs/visitors.log"):
        self.__logLocation = logLocation
        self.__mappedValues = {}

    def load(self):
        logfile = open(self.__logLocation, "r")
        for ipAddress in logfile:
            self.__addToMap(ipAddress.strip(" \t\n\r"))

    def getVisitCountForIpAddress(self, ipAddress):
        self.__validateIpAddress(ipAddress)
        if ipAddress in self.__mappedValues:
            return self.__mappedValues[ipAddress]

        return 0

    def __addToMap(self, ipAddress):
        if ipAddress in self.__mappedValues:
            self.__mappedValues[ipAddress] += 1
        else:
            self.__mappedValues[ipAddress] = 1

    def __validateIpAddress(self, ipAddress):
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ipAddress):
            raise AssertionError
