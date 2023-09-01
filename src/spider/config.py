from pathlib import Path
from os.path import join

class Config(object):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent #agar file selain koding tidak masuk ke src
    TEMP_DIR = join(BASE_DIR, "temp")
    LOGDIR = join(BASE_DIR, "log")

class DevConfig(Config):
    pass
