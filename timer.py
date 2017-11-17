import time, sys
mins = 0

def timer():
    global mins
    while mins!=1:
        time.sleep(60)
        mins += 1
    sys.exit(0)

timer()
