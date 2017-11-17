import psutil, subprocess, sys, ctypes, time, getpass, win32gui

chrome_id = 0
chrome_running = False
timer = 0

ctypes.windll.kernel32.SetConsoleTitleW("darkBotLock")

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def chrome():
    global chrome_running, timer, chrome_id
    while 1:
        list = psutil.pids()
        for i in range(0, len(list)):
            try:
                p = psutil.Process(list[i])
                if (p.cmdline()[0].find("chrome.exe") != -1) and chrome_running is False:
                    print("main-block")
                    p.suspend()
                    chrome_id = p
                    password = "aezakmi11"
                    p_try = 0
                    if chrome_running is True:
                        break
                    while chrome_running is False:
                        if p_try == 3:
                            print("3 login attempts failed...")
                            time.sleep(5)
                            ctypes.windll.user32.LockWorkStation()
                            sys.exit()
                        input_s = getpass.getpass()
                        print(input_s)
                        if input_s == password:
                            chrome_id.resume()
                            chrome_running = True
                            mailer = subprocess.Popen('F:\\c_latest\\dev_work\\app_lock v2.1\\mailer.py', shell=True)
                            timer = subprocess.Popen('F:\\c_latest\\dev_work\\app_lock v2.1\\timer.py', shell=True, stdout=subprocess.PIPE)
                        else:
                            p_try = p_try + 1
                            print("Password wrong...")

                elif (p.cmdline()[0].find("chrome.exe") != -1) and chrome_running is True:
                    password = "aezakmi11"
                    if psutil.pid_exists(timer.pid) is False:
                        print("making chrome running false")
                        chrome_running = False
                        chrome_id.suspend()
                        top_windows = []
                        #win32gui.EnumWindows(windowEnumerationHandler, top_windows)
                        #or i in top_windows:
                            #if "darkbotlock" in i[1].lower():
                                #win32gui.ShowWindow(i[0], 5)
                                #win32gui.SetForegroundWindow(i[0])
                                #break
                    if chrome_running is False:
                        print("i am not running")
                    while chrome_running is False:
                        print("Trying for input")
                        if p_try == 3:
                            print("3 login attempts failed...")
                            time.sleep(5)
                            ctypes.windll.user32.LockWorkStation()
                            sys.exit()
                        print("User check")
                        input_s = getpass.getpass()
                        if input_s == password:
                            try:
                                chrome_id.resume()
                                print("Resumed")
                            except:
                                print("failed")
                            chrome_running = True
                            timer = subprocess.Popen('F:\\c_latest\\dev_work\\app_lock v2.1\\timer.py', shell=True)
                        else:
                            p_try = p_try + 1
                            print("Password wrong...")
            except:
                pass

chrome()
