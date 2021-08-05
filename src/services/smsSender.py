import urllib
import urllib.request
import urllib.parse
from typing import Dict, List


class SmsApi:
    username: str = ""
    password: str = ""
    persons: Dict[str, str] = {}
    groups: Dict[str, List[str]] = {}

    def __init__(self, username: str, password: str, persons: Dict[str, str], groups: Dict[str, List[str]]):
        self.username = username
        self.password = password

        # validate and filter persons data
        for prsn in persons:
            phNum = persons[prsn]
            if not isinstance(phNum, str):
                persons.pop(prsn)

        # validate and filter groups data
        for grpName in groups:
            grpPersons = [x for x in groups[grpName] if x in persons]
            groups[grpName] = grpPersons

        self.persons = persons
        self.groups = groups

    def SendSms(self, mobilenumber: str, message: str) -> str:
        """send sms via api
        Args:
            mobilenumber (str): mobile number
            message (str): message body
        Returns:
            str: status after message sending
        """
        url = "http://www.smscountry.com/smscwebservice_bulk.aspx"
        values = {'user': self.username,
                  'passwd': self.password,
                  'message': message,
                  'mobilenumber': mobilenumber,
                  'mtype': 'N',
                  'DR': 'Y'
                  }
        data = urllib.parse.urlencode(values)
        dataStr = data.encode('utf-8')
        request = urllib.request.Request(url, dataStr)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')

    def sendSmsToGroup(self, grpName: str, message: str) -> bool:
        # check the group name
        if grpName in self.groups:
            return False
        grpPersons = self.groups[grpName]
        for prsn in grpPersons:
            phNum = self.persons[prsn]
            _ = self.SendSms(phNum, message)
        return True
