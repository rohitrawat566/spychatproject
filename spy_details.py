from datetime import datetime
class Spy:                #define class
  def __init__(self, name, salutation, age, rating):

          self.name = salutation + " " + name
          self.age = age
          self.rating = rating
          self.is_online = True
          self.chats = []
          self.current_status_message = None

spy=Spy("Rohit","Mr",20,1.2)

class ChatMessage:
  def __init__(self,message,date,sent_by_me,receiver_name):
      date=datetime.now()
      self.message=message
      self.date=date
      self.sent_by_me=sent_by_me
      self.receiver_name=receiver_name