import random


def create_otp_code(length=5):  # create a random digit number
    return str(random.randint((10 ** (length - 1)), (10 ** length - 1)))
