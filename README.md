# grafana_smscountry_webhook

![Architecture](/assets/img/grafana_sms_webhook_architecture.png)

## Dependencies
* python needs to be installed and added in the ```PATH``` environment variable
* for running the server as a windows background service, then nssm should be installed and added in the ```PATH``` environment variable

## Server Setup Instructions
* create config.json in config folder as per the sample config
* run create_env.bat
* run install_env.bat
* check if server is running using run_server.bat
* If everything is ok, install the server as a windows background service using setup_service.bat
* check if the server is running using services.msc. The name of the service can be seen in setup_service.bat

## Logs locations
* application logs can be seen in app_logs folder
* nssm service logs can be seen in logs folder


## Setup user phone numbers in config.json file
![Persons Phone Number Config](/assets/img/person_config.png)
* Users phone numbers and user groups can be configured in config.json file
* The user group name in config.json will be used in grafana webhook url. For example if we have a user group named scada, we can create a grafana webhook channel with the url ```http://localhost:5000/api/send-sms/scada```

## Setup web hook based sms alerts in grafana
* Create a notification channel of type webhook in grafana
* In grafana webhook settings, mention the webhook url and disable images. 
    * If the webhook server is running on port 5000 of the same machine as grafana and the user group name is ```it```, then the webhook url will be ```http://localhost:5000/api/send-sms/it```
* In the config.json file if we have a user group named scada, we can create another webhook channel with the url ```http://localhost:5000/api/send-sms/scada```

## Notification Channel example
![Notification Channel example](/assets/img/notification_channel_settings.png)

## Alert Settings example
![Alert Settings example](/assets/img/alert_settings_example.png)

