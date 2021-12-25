###
# Logging from multiple threads is as simple as normal process
# To differentiate the logs  generated from each thread, threadName can be used
# Below example shows the logging from the main thread and another one more thread
###
import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from thread 2')
        time.sleep(0.5)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(threadName)s - %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main thread')
            time.sleep(1.0)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

if __name__ == '__main__':
    main()
