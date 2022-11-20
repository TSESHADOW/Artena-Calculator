import interface
import calculations
import image_process

if __name__ == "__main__":
    #hide = image_process.win32gui.GetForegroundWindow()
    #image_process.win32gui.ShowWindow(hide , win32con.SW_HIDE)
    
    root = interface.tk.Tk()
    app = interface.Application(root)
    
    root.mainloop()
