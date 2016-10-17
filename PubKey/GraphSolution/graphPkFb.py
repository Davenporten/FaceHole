import facebook
import urllib
import urlparse
import subprocess
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Logging in is just for testing
# Enter your own name and password

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = ''
FACEBOOK_APP_SECRET = ''
#FACEBOOK_PROFILE_ID = 'XXXXXX'
ACCESS_TOKEN = ''

graph = facebook.GraphAPI(ACCESS_TOKEN, version='2.2')
prof = graph.get_object('me')
print prof

ID = prof["id"]
EMAIL = prof["email"]


