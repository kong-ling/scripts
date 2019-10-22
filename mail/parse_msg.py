import win32com.client

outlook = win32com.client.Dispatch("Outlook.Applicaion").GetNamespace("MAPI")
msg = outlook.OpenSharedItem(r"C:\posv_cv_script-scripts\mail\test.msg")

print(msg.SenderName)
