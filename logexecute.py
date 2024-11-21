import subprocess
import tkinter as tk
from threading import Thread, Event

StopEvent = Event()
root = tk.Tk()
root.withdraw()

def run_command():
    
    alert_window = tk.Toplevel(root)
    alert_window.title("正在截取logs")
    alert_label = tk.Label(alert_window, text="截取中")
    alert_label.pack(padx=100, pady=100)
    
    process = subprocess.run(["THE COMMAND TO GET DEVICE LOG"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
    for line in process.stdout:
        if "Done!" in line: 
            process.stdout.close()
            break
    
    print(process.stdout)

    alert_window.destroy()
    
    success_window = tk.Toplevel(root)
    success_window.title("成功")
    success_label = tk.Label(success_window, text="截取logs成功！")
    success_label.pack(padx=100, pady=100)
    
    StopEvent.set()
    
def checkstatus():
    if StopEvent.is_set():
        root.quit()
    else:
        root.after(1000, checkstatus)
        
        
thread = Thread(target=run_command)
thread.start()
checkstatus()

root.mainloop()
        
