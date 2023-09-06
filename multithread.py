from threading import Thread, Event, Lock
import socket
import ssl
import time

host = "localhost"
#host = "api.ipify.org"


# Protocol control variable: 0 for HTTP, 1 for HTTPS
use_https = 0

# Define the request string based on the protocol
if use_https:
    req = "GET /rc1.php?amt=1 HTTP/1.1\r\n"
else:
    req = "GET /rc1.php?amt=1 HTTP/1.1\r\n"
req = req + "Host: " + host + "\r\n\r\n"

class myThread(Thread):
    def __init__(self, ID, name, finished_event, responses):
        Thread.__init__(self)
        self.threadID = ID
        self.name = name
        self.finished_event = finished_event
        self.responses = responses
        self.lock = Lock()  # Lock to synchronize access to responses

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if use_https:
            ssl_context = ssl.create_default_context()
            s = ssl_context.wrap_socket(s, server_hostname=host)
        s.connect((host, 443 if use_https else 80))
        s.send(req.encode('utf-8'))

        response_data = b""
        s.settimeout(5)  # Set a 5-second timeout for recv

        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response_data += chunk
            except socket.timeout:
                break

        response_length = len(response_data)

        with self.lock:
            self.responses[self.threadID] = response_data  # Store response in array

        s.close()
        self.finished_event.set()  # Signal that this thread has finished

threads = []
finished_event = Event()
print("[*] Starting.. setting threads..")

responses = {}  # Dictionary to store responses with thread ID as keys

start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Record script's start timestamp

for i in range(1, 101):
    thread = myThread(i, "", finished_event, responses)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.finished_event.wait()

# Sleep to wait for some threads
print("\n[*] Sleeping 3 seconds to wait for some threads..")
time.sleep(3)

end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Record script's end timestamp

print("\n[*] Writing responses to files..")

# Write responses to files
for thread_id, response_data in responses.items():
    filename = f"response_{thread_id}.txt"
    print("[.] writing file : " + filename)
    with open(filename, "wb") as file:
        file.write(response_data)

print("\n[*] All requests were sent successfully")
print(f"Script Start Time: {start_time}")
print(f"Script End Time: {end_time}")
