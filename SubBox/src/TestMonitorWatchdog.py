import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
import logging

logging.basicConfig(level=logging.DEBUG)

conta = 0

class MyEventHandler(FileSystemEventHandler):
    def catch_all_handler(self, event):
        #if event.src_path.find("/.DS_Store") == -1:
        logging.debug(event)
        #print 1
        

    def on_moved(self, event):
        self.catch_all_handler(event)
        #logging.debug(event)
        #print 1

    def on_created(self, event):
        self.catch_all_handler(event)
        #logging.debug(event)
        #print 1

    def on_deleted(self, event):
        self.catch_all_handler(event)
        #logging.debug(event)
        #print 1

    def on_modified(self, event):
        self.catch_all_handler(event)
        #logging.debug(event)
        #print 1

if __name__ == "__main__":
    path = "/Users/paganotti/SubBox"
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    '''
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    '''
    observer.join()
  