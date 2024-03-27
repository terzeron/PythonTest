#!/usr/bin/env python


import os
import time
import json
from pathlib import Path


path_prefix = Path("/mnt/data/text")


def get_entries_from_dir(dir_name: str = "", size: int = 0):
    global path_prefix
    result = []
    path = path_prefix / dir_name
    if path.is_dir():
        count = 0
        for entry in path.iterdir():
            if entry.is_file():
                result.append({"key": entry.name, "label": entry.name})
                count = count + 1
                if 0 < size <= count:
                    break
        result.sort(key=lambda x: x["key"])
    else:
        return result, f"can't find '{dir_name}'"
    return result, None


def get_full_dirs():
    global path_prefix
    result = []
    path = path_prefix
    for entry in path.iterdir():
        if entry.is_dir():
            nodes, error = get_entries_from_dir(entry.name)
            result.append({"key": entry.name, "label": entry.name, "nodes": nodes})
        elif entry.is_file():
            result.append({"key": entry.name, "label": entry.name})
    result.sort(key=lambda x: x["key"])
    return result


def get_full_dirs2():
    global path_prefix
    result = []
    path = path_prefix
    for entry in os.scandir(path):
        if entry.is_dir():
            sub_result = []
            for e in os.scandir(entry):
                if e.is_file():
                    sub_result.append({"key": e.name, "label": e.name})
            #sub_result.sort(key=lambda x: x["key"])
            result.append({"key": entry.name, "label": entry.name, "nodes": sub_result})
        elif entry.is_file():
            result.append({"key": entry.name, "label": entry.name})
    result.sort(key=lambda x: x["key"])
    return result
    

for i in range(10):
    start_ts = time.time()    
    result = get_full_dirs()
    print("#1")
    json_str = json.dumps(result)
    print(len(json_str))
    print(time.time() - start_ts)

    start_ts = time.time()
    result = get_full_dirs2()
    print("#2")
    json_str = json.dumps(result)
    print(len(json_str))
    print(time.time() - start_ts)
