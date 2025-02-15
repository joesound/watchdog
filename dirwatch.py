# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
from queue import Queue
from threading import Thread 


class OnMyWatch:
	# Set the directory on watch
	watchDirectory = "D:\sideproject\watchdgo"

	def __init__(self, q):
		self.observer = Observer()
		self.q = q

	def run(self):
		event_handler = Handler(self.q)
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()


class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None

		elif event.event_type == 'created':
			# Event is created, you can process it now
			print("Watchdog received created event - % s." % event.src_path)
			data = event.src_path
			# data = "新增資料夾"
			# payload = {'data': data}
			response = requests.post('http://127.0.0.1:5000/api/dirupdate', data=data)
			# response = requests.post('https://line-app-test.onrender.com/api/test', data=data)
			print("reply", response.text)


		elif event.event_type == 'modified':
			# Event is modified, you can process it now
			print("Watchdog received modified event - % s." % event.src_path)
			

if __name__ == '__main__':

	watchdog_queue = Queue()
	watch = OnMyWatch(watchdog_queue)
	watch.run()
	
