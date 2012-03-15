from watchdog.events import FileSystemEventHandler

class SubBoxMonitor(FileSystemEventHandler):
    #Custom EventHandler
    def catch_all_handler(self, event):
        print "catch all handler"

    def on_moved(self, event):
        tipo_evento = "tipo evento: %s \n" % (event.event_type)
        src_path    = "percorso src:  %s \n" % (event.src_path)
        dest_path   = "percorso dest: %s \n" % (event.dest_path)
        is_dir      = event.is_directory
        
        print tipo_evento
        print src_path
        print dest_path
        
        if is_dir == True:
            print "e una cartella \n"
        else:
            print "non e una cartella \n"
        
    def on_created(self, event):
        tipo_evento = "tipo evento: %s \n" % (event.event_type)
        src_path    = "percorso src:  %s \n" % (event.src_path)
        is_dir      = event.is_directory
        
        print tipo_evento
        print src_path
        
        if is_dir == True:
            print "e una cartella \n"
        else:
            print "non e una cartella \n"

    def on_deleted(self, event):
        tipo_evento = "tipo evento: %s \n" % (event.event_type)
        src_path    = "percorso src:  %s \n" % (event.src_path)
        is_dir      = event.is_directory
        
        print tipo_evento
        print src_path
        
        if is_dir == True:
            print "e una cartella \n"
        else:
            print "non e una cartella \n"

    def on_modified(self, event):
        tipo_evento = "tipo evento: %s \n" % (event.event_type)
        src_path    = "percorso src:  %s \n" % (event.src_path)
        is_dir      = event.is_directory
        
        print tipo_evento
        print src_path
        
        if is_dir == True:
            print "e una cartella \n"
        else:
            print "non e una cartella \n"