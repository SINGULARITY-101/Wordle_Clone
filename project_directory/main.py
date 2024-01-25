import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")

print(username, password, sep = "\n")
