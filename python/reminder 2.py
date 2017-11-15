import threading
import time
from twilio.rest import Client

account_sid = "AC4083a8eec202a05d3fef049eef96e6b4"
auth_token  = "d54180f23031bae9b883540852d457aa"
#MONDAY
def f():
    
	client = Client(account_sid, auth_token)
	message = client.messages.create(
    to="+919879106332", 
    from_="+12672823021 ",
    body="YOUR MONDAY TIME TABLE\n\
	9-11	ASD B2052\n\
				WS B1041\n\
				DC B2015\n\
				IRS B2011\n\
				BDA B2014\n\
	11-12	CC B203\n\
	12-1	AI B203\n\
	2-4	IWM(A3) B1043\n\
		IWM(A2) B1044\n\
		CC(A1)  B2012\n\
		OSL(A4) B2015\n\
	")
	#threading.Timer(60,f).start()
	print(message.sid)
#TUESDAY
"""
def f():
	client = Client(account_sid, auth_token)
	message = client.messages.create(
    to="+919879106332", 
    from_="+12244791958 ",
    body="9-11	IRS(E13) B1044\n\
				ASD(E8) B2052\n\
				ASD(E7) B2051\n\
				DC B2015\n\
				BDA B2014\n\
				IRS(E12) B2053\n\
		  11-12 CC B203\n\
		  12-1 AI B203\n\
		  2-3 ASD D303\n\
		      BDA B204\n\
			  WS A208A\n\
			  DC B203\n\
			  IRS D304\n\
		  3-4 IWM B203\n\
		  5-6 AI(T2) B203\n\")
	#threading.Timer(60,f).start()
	print(message.sid)
#WEDNESDAY
def f():
	client = Client(account_sid, auth_token)
	message = client.messages.create(
    to="+918347743890", 
    from_="+12244791958 ",
    body="9-11	MP(A4) B2012\n\
				IWM B1042\n\
				OSL B1061\n\
				MP(A2) B2011\n\
		  11-12 OB B203\n\
		  12-1 IWM B203\n\
		  2-4 ELECTIVE\n\")
	#threading.Timer(60,f).start()
	print(message.sid)
#THURSDAY
def f():
	client = Client(account_sid, auth_token)
	message = client.messages.create(
    to="+918347743890", 
    from_="+12244791958 ",
    body="9-10	OB B203\n\		 
		  10-11 ASD D303\n\
		        BDA B204\n\
			    WS A208A\n\
			    DC B203\n\
			    IRS D304\n\
		  11-1 MP(A3) B2015\n\
			   OSL B2014\n\
			   CC B2012\n\
			   MP(A2) B1062\n\
		  2-3 AI B203\n\
		  3-4 ELECTIVE\n\")
	#threading.Timer(60,f).start()
	print(message.sid)
#FRIDAY
def f():
	client = Client(account_sid, auth_token)
	message = client.messages.create(
    to="+918347743890", 
    from_="+12244791958 ",
    body="9-11	MP B2017\n\
				IWM B2015\n\
				CC B2012\n\
				OSL B1061\n\
		  11-12 CC B203\n\
		  12-1 AI(T1) B203\n\
			   AI(T3) B213\n\
		  2-3 IWM B203\n\
		  3-4 ASD D303\n\
		        BDA B204\n\
			    WS A208A\n\
			    DC B203\n\
			    IRS D304\n\
		  4-6 MP(A4) B1062\n\
			  MP(A3) B2015\n\
			  CC     B2012\n\
			  MP(A1) B1061\n\")
	#threading.Timer(60,f).start()
	print(message.sid)

"""
while(1):
    f()
    time.sleep(120)
#f()