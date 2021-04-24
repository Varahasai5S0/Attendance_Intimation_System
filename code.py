import os
import smtplib   
import csv 
import xlrd
from datetime import date
from twilio.rest import Client 
from twilio.twiml.voice_response import VoiceResponse 


loc = ("path of file")#location of excel file 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0) 
for i in range(sheet.rows):
    if sheet.cell_value(i,5)=='Absent': 
        receiver_email_id=sheet.cell_value(i,4)
        receiver_number=int(sheet.cell(i,3))
        message='Your child '+sheet.cell_value(0,1)+' '+str(sheet.cell_value(0,2))+'was absent on today '+date.today()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls() 
        sender_email_id='A-----' #sender mail id 
        sender_email_id_password='XXXXXXX' #sender password id
        s.login("sender_email_id", "sender_email_id_password")
        s.sendmail("sender_email_id", "receiver_email_id", message)
        s.quit() 
        AccountSid='-----' #Account Sid of Twilio account 
        Auth_Token='-----' #Authorization token of twilio account
        client = Client("AccountSid", 'Auth_Token')

        call = client.calls.create(
                                twiml='<Response><Say>message</Say></Response>',
                                to='receiver_number',
                                from_='sender_number'
                            )
        message=client.messages.create(
                                to='receiver_number',
                                from='sender_number',
                                body=message
                            )
        print(call.sid)  

        ''' make neccesary changes before executing code like 
            account_sid,auth_token,mailid and about the phone numbers which should be verified 
            with prior to before they use.
        '''
            
