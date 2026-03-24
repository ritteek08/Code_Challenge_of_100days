# Simple Digital Clock Program in Python
import time

def digital_clock():
    print("Digital Clock - Press Ctrl+C to stop\n")
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(current_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nClock stopped! Goodbye!")

if __name__ == "__main__":
    digital_clock()