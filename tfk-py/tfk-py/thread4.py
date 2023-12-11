import threading
import time

class HotelRooms(threading.Thread):
    availableRooms = 10
    threadLock = threading.Lock()

    def __init__(self, name, roomRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.roomRequest = roomRequest

    def run(self):
        self.threadLock.acquire()
        self.getRoom()
        self.threadLock.release()

    def getRoom(self):
        print("{} tries to get a room at {}".format(self.name, time.strftime("%H:%M:%S", time.gmtime())))

        if HotelRooms.availableRooms - self.roomRequest >= 0:
            HotelRooms.availableRooms -= self.roomRequest
            print(f"New available rooms: {HotelRooms.availableRooms}")
        else:
            print(f"Not enough rooms, the available rooms are: {HotelRooms.availableRooms}")

        time.sleep(1)  # Added parentheses to call the sleep function

# Creating thread objects
thread1 = HotelRooms("Kunle", 5)
thread2 = HotelRooms("Tao", 6)
thread3 = HotelRooms("Lila", 5)

# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Waiting for all threads to finish
thread1.join()
thread2.join()
thread3.join()
