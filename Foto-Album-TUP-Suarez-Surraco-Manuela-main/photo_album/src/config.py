import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///photo_album.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
    