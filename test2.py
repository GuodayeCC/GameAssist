from pymouse import PyMouse
import win32gui
from PIL import ImageGrab

mouse = PyMouse()

# wdname = "编程 - 记事本"
#
# hwnd = win32gui.FindWindow(0, wdname)
# if hwnd:
#     win32gui.SetForegroundWindow(hwnd)
#     image = ImageGrab.grab((363, 275, 1270, 929))
#     image.show()
#     mouse.click(int(12/5*4), int(12/5*4))
# else:
#     print("not found!!!")


# mouse.click(int(12 / 5 * 4), int(12 / 5 * 4))
