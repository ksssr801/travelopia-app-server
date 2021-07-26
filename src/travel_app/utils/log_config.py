import os
import time
import sys
import linecache
# from log_rollover_handler import create_log_handler

main_log_file = 'debug.log'
curr_time = time.ctime()

def log_info(message='',file_name=''):
    final_log_msg = time.ctime() + ' : INFO : ' + message + '\n'
    cwd = os.getcwd()
    dir_path = cwd + '/logs'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    log_file = ''
    if file_name:
        log_file = file_name
    else:
        log_file = main_log_file

    file_path = os.path.join(dir_path, log_file)

    file_ptr = open(file_path, 'a')
    file_ptr.write(final_log_msg)
    file_ptr.close()

def log_exception(log_file_name=''):
    log_file = ''
    if log_file_name:
        log_file = log_file_name
    else:
        log_file = main_log_file
    final_log_msg = construct_log_error_message()
    cwd = os.getcwd()
    dir_path = cwd + '/logs'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = os.path.join(dir_path, log_file)
    file_ptr = open(file_path, 'a')
    file_ptr.write(final_log_msg)
    file_ptr.close()

def construct_log_error_message():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    log_message = 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    new_log_msg = time.ctime() + ' : ' + log_message + '\n'
    return new_log_msg
