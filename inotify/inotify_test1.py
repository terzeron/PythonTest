#!/usr/bin/env python

import inotify.adapters

def _main():
    i = inotify.adapters.InotifyTree("/mnt/data/text")
    print("ready")
    
    for event in i.event_gen():
        if not event:
            continue
        _, type_names, path, filename = event
        if type_names[0] in ("IN_CLOSE_WRITE", "IN_DELETE", "IN_MOVED_TO"):
            print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(path, filename, type_names))


if __name__ == '__main__':
    _main()
