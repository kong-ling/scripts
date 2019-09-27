import win32gui, win32con

win = win32gui.FindWindow(None, u'TmainWindow') # find the program
tid = win32gui.FindWindowEx(win, None, u'Start', None) # find the textbox

#send message
win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, 'hello')

#Chinese
#win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, u'你好'.encode('gbk'))

#send 'Enter'
#win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, 'hello')
win32gui.PostMessage(tid, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
#win32gui.PostMessage(tid, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
