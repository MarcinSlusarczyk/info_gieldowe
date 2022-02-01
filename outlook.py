import win32com.client as client

outlook = client.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)

# RESPONDER DATA
message.to = "marcink442@gmail.com"
message.subject = "Przykładowy tytuł"
message.body = "jakaś przykładowa treść"

message.display()