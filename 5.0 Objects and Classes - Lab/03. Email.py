class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


email_collection = []
emails = [x.split() for x in iter(input, 'Stop')]
send_emails = [int(x) for x in input().split(', ')]

for e, s, m in emails:
    email = Email(e, s, m)
    email_collection.append(email)

[email_collection[x].send() for x in send_emails]
[print(email.get_info()) for email in email_collection]
