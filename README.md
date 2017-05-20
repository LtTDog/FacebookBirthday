# facebookBirthday

## Use this at your own risk.  I'm not responsible if you get your account locked or it post happy birthday in a ton of places. Or anything else.

I created this to save some time posting happy birthday to people on facebook, also since I don't always login everyday.

I use the gecko driver mainly because I was having issues trying phantomjs where it wasn't logging in properly.  Not sure what the issue for this is probably not keeping cookies for the login or maybe facebook blocked it.  This mainly runs on a computer I use for a server so I don't really mind it poping a window for a couple of mins.  If you figure this out let me know.

### Main Requirements
* Python 3
* [Selenium] (http://selenium-python.readthedocs.io/)
* [Gecko Driver] (https://github.com/mozilla/geckodriver/releases)

### Setup
1. Configure facebook username and password in main.py
2. If you want it to send you an email everytime it runs configure the email and app password in gmailsend.py

Just run main.py with something like cron everyday