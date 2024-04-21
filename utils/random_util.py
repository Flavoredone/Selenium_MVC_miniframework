#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
import string


class RandomUtil(object):
    def __init__(self, password=''):
        self.password = password

    def generate_password(self, length):
        self.password = random.sample(string.ascii_letters, length-2)
        self.password.append(random.choice('абвгдАБВГД'))
        self.password.append(str(random.randint(1, 9)))

        random.shuffle(self.password)
        print(''.join(self.password), ' - password')
        return ''.join(self.password)

    def generate_mail(self, length=4):
        mail = random.sample(string.ascii_letters, length)
        mail.append(random.choice(self.password))
        print(''.join(mail), ' - mail')
        return ''.join(mail)

    @staticmethod
    def generate_domain(length=4):
        domain = random.sample(string.ascii_letters, length)
        print(''.join(domain), ' - domain')
        return ''.join(domain)
