# Basic utilities

import uuid
import os
# import logging as logger
# logger_dir = os.path.join(os.getcwd(), "logs")
# if not os.path.exists(logger_dir): os.makedirs(logger_dir)
# logger_file = os.path.join(logger_dir, "debug.log")
# logger.basicConfig(filename=logger_file, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def get_ID():
    try:
        ID = str(uuid.uuid1().int >> 64)
        print (ID, type(ID), '<<<<< ID')
        return ID
    except Exception as err:
        pass

