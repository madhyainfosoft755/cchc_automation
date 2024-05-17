import random
import string


class Random:
    def __init__(self):
        pass

    def generate_random_email(self):
        # Random email address generate karne ke liye
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
        username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        domain = random.choice(domains)
        email = username + '@' + domain
        return email

    def generate_random_mobile_number(self):
        # Generate a random 10-digit mobile number
        mobile_number = '0'  # Assuming country code starts with 0
        for _ in range(9):
            digit = random.randint(0, 9)
            mobile_number += str(digit)
        return mobile_number
