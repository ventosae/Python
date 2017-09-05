from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5c35fbdeb6cf1156702e3687be217931"
# Your Auth Token from twilio.com/console
auth_token  = "943b7636e72d0b50fcf98ff80829a49c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447746721193", 
    from_="+447514970876",
    body="Hello from Jhoshua. Im still here bitch!")

print(message.sid)
