import wmi, time
ip = 'xxx.xx.xx.xx.xxx'
username = "user"
password = "password"
SW_SHOWNORMAL = 1
from socket import *
print "Establishing connection to %s" %ip
c = wmi.WMI(ip, user=username, password=password)
process_startup = c.win32_ProcessStratup.new()
process_startup.ShowWindow = SW_SHOWNORMAL
process_id, result = c.Win32_Process.Create(CommandLine="C:\User\Administrator\Desktop\runIOX_auto.bat,ProcessStratupInformation=process_startup")
if result == 0:
    print "Process strated successfully: %d" % process_id
else:
    raise RuntimeError, "Problem creating process: %d" % result
