# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
from queue import Queue


class OnMyWatch:
	# Set the directory on watch
	watchDirectory = "D:\sideproject\watchdgo"

	def __init__(self):
		self.observer = Observer()
	
	def run(self):
		
		event_handler = Handler()
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
		self.observer.start()
		try:
			while True:
				while not event_handler.event_q.empty():
					data, ts = event_handler.event_q.get()
					response = requests.post('http://127.0.0.1:5000/api/dirupdate', data=data)
					print(response.text)	
				time.sleep(1)
		except:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.event_q = Queue()

    # @staticmethod
    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
            data = event.src_path
            self.event_q.put((data, time.time()))


if __name__ == '__main__':

	watch = OnMyWatch()
	watch.run()
	
