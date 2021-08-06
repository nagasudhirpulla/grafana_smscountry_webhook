from flask import Flask, request
from waitress import serve

from src.config.appConfig import loadAppConfig
from src.logs.loggerFactory import getFileLogger
from src.services.smsSender import SmsApi

# get application config
appConf = loadAppConfig()

# setup logging based on application config
backUpCount = appConf["backUpCount"]
fileRollingHrs = appConf["fileRollingHrs"]
logFilePath = appConf["logFilePath"]
logger = getFileLogger(
    "app_logger", logFilePath, backUpCount, fileRollingHrs)

# create webhook server
app = Flask(__name__)
app.secret_key = appConf['flaskSecret']
app.logger = logger

# initialize sms api sender with required parameters from application config
smsApi = SmsApi(appConf["smsUsername"], appConf["smsPassword"],
                appConf["persons"], appConf["groups"])


@app.route('/')
def index():
    # end point for testing the webhook
    return 'Hello, World!'


@app.route('/api/send-sms/<grpName>', methods=['POST'])
def sendSms(grpName: str):
    # api end point to send sms
    msgJson = request.json
    alertMsg = msgJson["message"]
    alertState = msgJson["state"].capitalize()
    smsStr = "[{0}] {1}".format(alertState, alertMsg)
    isSuccess = smsApi.sendSmsToGroup(grpName, smsStr)
    # logger.log(smsStr)
    return isSuccess


if __name__ == '__main__':
    serverMode: str = appConf['mode']
    if serverMode.lower() == 'd':
        app.run(host=appConf["flaskHost"], port=int(
            appConf["flaskPort"]), debug=True)
    else:
        serve(app, host=appConf["flaskHost"], port=int(
            appConf["flaskPort"]), threads=1)
