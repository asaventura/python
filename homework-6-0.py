import time
import sys
import threading


class TrafficLight(threading.Thread):
    def __init__(self):
        super().__init__()
        self.__colors = [("Red", 7), ("Yellow", 2), ("Green", 10)]

    def run(self):
        n = 0
        while n <= len(self.__colors) - 1:
            color = self.__colors[n]
            for remaining in range(color[1], 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write(f"{color[0]} {remaining}")
                sys.stdout.flush()
                time.sleep(1)
            n += 1


traffic_light_1 = TrafficLight()
traffic_light_1.start()
