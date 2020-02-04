#
import logging
import os
import json
from pathlib import Path


def basedir():
    return os.path.join(str(Path.home()), '.mfl')

def fullpath(relative_path):
    return os.path.join(basedir(), relative_path)

def mkdir(relative_path):
    try:
        os.makedirs(
            fullpath(relative_path)
        )
    except OSError:
        logging.error("failed to create directory: %s" % (relative_path))
    else:
        logging.debug("successfully created directory: %s" % (relative_path))

def dump_json(relative_path, filename, data):
    dir_path = fullpath(relative_path)
    file_path = os.path.join(dir_path, filename)
    mkdir(dir_path)
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file)
            return true
    except:
        logging.error("failed to write data to file: %s" % (file_path))
    else:
        logging.debug("successfully written to file: %s" % (file_path))
        return false

def read_json(relative_path, filename):
    file_path = os.path.join(fullpath(relative_path), filename)
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except:
        logging.error("failed read data from file: %s" % (file_path))
    else:
        logging.debug("successfully read from file: %s" % (file_path))
    return {}
