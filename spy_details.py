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
  def __init__(self,message,sent_by_me):
    self.message=message
    self.time=datetime.now()
    self.sent_by_me=sent_by_me