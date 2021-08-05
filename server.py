from flask import Flask, request
from waitress import serve

from src.config.appConfig import loadAppConfig
from src.logs.loggerFactory import getFileLogger

appConf = loadAppConfig()

backUpCount = appConf["backUpCount"]
fileRollingHrs = appConf["fileRollingHrs"]
logFilePath = appConf["logFilePath"]
logger = getFileLogger(
    "app_logger", logFilePath, backUpCount, fileRollingHrs)


app = Flask(__name__)
app.secret_key = appConf['flaskSecret']
app.logger = logger


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/api/send-sms/<grpName>', methods=['POST'])
def sendSms(grpName: str):
    msgJson = request.json
    alertMsg = msgJson["message"]
    alertState = msgJson["state"].capitalize()
    smsStr = "[{0}] {1}".format(alertState, alertMsg)
    # logger.log(smsStr)
    return smsStr


if __name__ == '__main__':
    serverMode: str = appConf['mode']
    if serverMode.lower() == 'd':
        app.run(host=appConf["flaskHost"], port=int(
            appConf["flaskPort"]), debug=True)
    else:
        serve(app, host=appConf["flaskHost"], port=int(
            appConf["flaskPort"]), threads=1)
