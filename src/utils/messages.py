from random import randint
from app_user.models import CodesModel

class MessagesClass:
    def __init__(self, text, user=None):
        self.__text = text
        self.user = user

    def commends(self):
        dict = {
            '{first_name}': self.first_name(),
            '{last_name}': self.last_name(),
            '{email}': self.email(),
            '{code}': self.code(),
            '{space}': '<br><br>',
        }
        return dict

    def result(self):
        commends = self.commends()
        text = str(self.__text)
        for key in commends.keys():
            if key in text:
                if commends[key] != None:
                    text = text.replace(f'{key}', commends[key])

        return text

    def first_name(self):
        return self.user.first_name if self.user is not None else None

    def last_name(self):
        return self.user.last_name if self.user is not None else None

    def email(self):
        return self.user.email if self.user is not None else None
    def code(self):
        if self.user is not None:
            code = randint(1000,4000)
            CodesModel.objects.filter(user_id=self.user.id).delete()
            CodesModel.objects.create(code=code, user_id=self.user.id)
            return str(code)
        else:
            return None