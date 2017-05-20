# -*- coding: utf-8 -*-
from facebook import loginAndPost
import time

# configure username and password for facebook here
# also configure gmail send

def mine():
    username = ""
    password = ""

    loginAndPost(username, password)

mine()