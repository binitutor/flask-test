import os
import os.path

def root_path():
    src_path = os.path.dirname(__file__)
    root_path = os.path.dirname(src_path)
    return root_path

def data_path():
    return os.path.join(root_path(), 'data') + os.sep

def config_path():
    return os.path.join(root_path(), 'src', 'config') + os.sep

def sql_path():
    return os.path.join(root_path(), 'src', 'sql') + os.sep

def req_file_path():
    return os.path.join(root_path(), 'doc', 'dev') + os.sep

def report_path():
    return os.path.join(root_path(), 'report') + os.sep

def mapping_path():
    return os.path.join(root_path(), 'data', 'all_mapping_files') + os.sep

def custom_report_path():
    return os.path.join(root_path(), 'custom_report') + os.sep


