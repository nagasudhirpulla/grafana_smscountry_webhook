import unittest
from src.services.smsSender import SmsApi
from src.config.appConfig import loadAppConfig


class TestSmsSender(unittest.TestCase):

    def test_run(self) -> None:
        """tests the function that sends sms
        """
        appConf = loadAppConfig()
        smsApi = SmsApi(appConf["smsUsername"], appConf["smsPassword"],
                        appConf["persons"], appConf["groups"])
        resp: bool = smsApi.sendSmsToGroup(
            'it', '[Alerting] CCTV uptime notification')
        self.assertTrue(resp == True)
