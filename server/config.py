import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '11235813213455' 
