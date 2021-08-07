call nssm.exe install grafana_sms_hook "%cd%\run_server.bat"
call nssm.exe set grafana_sms_hook AppStdout "%cd%\logs\grafana_sms_hook.log"
call nssm.exe set grafana_sms_hook AppStderr "%cd%\logs\grafana_sms_hook.log"
nssm set grafana_sms_hook AppRotateFiles 1
nssm set grafana_sms_hook AppRotateOnline 1
nssm set grafana_sms_hook AppRotateSeconds 86400
nssm set grafana_sms_hook AppRotateBytes 104857600
call sc start grafana_sms_hook
rem call nssm.exe edit grafana_sms_hook