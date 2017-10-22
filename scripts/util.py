import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
WORK_DIR = os.path.dirname(SCRIPTS_DIR)
SOURCE_DIR = os.path.join(WORK_DIR, 'res')


def scan_files():
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.json'):
            yield os.path.join(SOURCE_DIR, filename), filename
