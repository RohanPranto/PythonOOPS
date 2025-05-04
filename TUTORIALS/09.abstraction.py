'''
Abstraction is the concept of hiding complex internal details and showing only the necessary features to the user.

You press a button like "Volume Up" or "Power" on a remote — you don't need to know how it sends signals or how the TV processes them internally. You just use the simple interface (the buttons) to perform actions.
'''
class EmailService:
    def _connect(self):
        print("Connecting to email server...")

    def _authentication(self):
        print("Authenticating...")

    def _disconnect(self):
        print("Disconnecting from the server...")

    def send_email(self):
        self._connect()
        self._authentication()
        print("Sending email...")
        self._disconnect()

# User only calls a single simple method — internal details are abstracted
email=EmailService() 
email.send_email()


'''
Abstraction hides the internal logic of how things work and only exposes what is necessary. In your case, the user just calls send_email() and doesn't need to know the details of connecting/authenticating/disconnecting.
_______________________________________________________________________
|
|🔎Without Abstraction (BAD Example):
|
|     |   email = EmailService()
|     |   email._connect()
|     |   email._authentication()
|     |   print("Sending email...")
|     |   email._disconnect()
|
| 1.Here, the user has to manually handle all the steps.
| 2.They are exposed to internal implementation.
| 3.This violates abstraction — it's not user-friendly and error-prone.
_______________________________________________________________________
|
|🔍With Abstraction (Your GOOD Example):
|
|     |   email = EmailService()
|     |   email.send_email()
|     |   Now the user just calls send_email().
|
| All internal operations (_connect(), _authentication(), _disconnect()) are hidden.
| This is abstraction — only essential features are exposed.
'''