# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.utils.translation import gettext as _
#
# from config import settings
#
# from .functions import create_otp_code
#
# # import redis
# import json


# class Redis:
#     """
#     manage user keys on redis
#     """
#     cache = redis.StrictRedis(
#         decode_responses=True,
#         host=settings.Redis_host,
#         port=settings.Redis_port,
#         db=settings.Redis_db
#     )  # config redis system cache
#     expire_times = {
#         "otp_code": 300,  # 5Min
#         "forget_password": 900,  # 15Min
#     }
#
#     def __init__(self, mobile, key):  # For the key to be unique, we use the user's email to access the key and a string for the key to be unique and clear.
#         self.key = mobile + key
#
#     def set_value(self, value):  # Set a value on the key in Redis
#         self.cache.set(self.key, value)
#
#     def set_json_value(self, value):  # Set a value on the key in Redis when data is dict or json
#         self.set_value(json.dumps(value))
#
#     def set_status_value(self, value):  # Set a bool value on the key in redis
#         self.set_value(str(value))
#
#     def create_and_set_otp_key(self, length=5):
#         otp_code = create_otp_code(length)
#         self.set_value(otp_code)
#         self.set_expire(self.expire_times['otp_code'])
#         return otp_code
#
#     def get_value(self):  # Returns the internal value of the key
#         if self.cache.exists(self.key):
#             return self.cache.get(self.key)
#         else:
#             return None
#
#     def get_json_value(self):  # Returns the json value of the key
#         try:
#             return json.loads(self.get_value())
#         except TypeError:
#             return None
#
#     def get_status_value(self):  # Returns the True or False status value of the key
#         the_value = self.get_value()
#         if the_value is not None and str(the_value).upper() == "TRUE":
#             return True
#         else:
#             return False
#
#     def set_expire(self, time=300):  # Set a time for the key to expire (time is in seconds)
#         self.cache.expire(self.key, time)
#
#     def get_expire(self):  # Returns the number of seconds remaining before the key expires
#         return self.cache.ttl(self.key)
#
#     def validate(self, user_value):  # Takes an input value and checks to see if it is the same as the value inside the key
#         user_value = str(user_value)
#         if self.cache.exists(self.key):
#             redis_value = self.cache.get(self.key)
#             if redis_value == user_value:
#                 return True
#             else:
#                 return False
#         else:
#             return None
#
#     def exists(self):  # Checks if the key is there or not
#         return self.cache.exists(self.key) == 1
#
#     def delete(self):  # Remove the key from Redis
#         return self.cache.delete(self.key)

#
# class ManageMailService:
#     subjects = {
#         "activate_account": _("Active Your Account"),
#         "forget_password": _("Forget Your Account Password")
#     }
#
#     def __init__(self, receiver_email):
#         self.receiver_email = receiver_email
#
#     def send_email_to_user(self, subject, content):
#         target_email = self.receiver_email
#         html_content = render_to_string(
#             "email/email.html",
#             {
#                 "content": content
#             }
#         )
#         text_content = strip_tags(html_content)
#         email = EmailMultiAlternatives(
#             subject,
#             text_content,
#             settings.EMAIL_HOST_USER,
#             [target_email]
#         )
#         email.attach_alternative(html_content, 'text/html')
#         email.send()
#         return True
#
#     def send_otp_code(self, title):
#         redis_management = Redis(self.receiver_email, f'{title}_otp_code')
#         otp_code = redis_management.create_and_set_otp_key()
#         content = {
#             "title": title,
#             "otp_code": otp_code
#         }
#         self.send_email_to_user(self.subjects[title], content)
#         return otp_code
