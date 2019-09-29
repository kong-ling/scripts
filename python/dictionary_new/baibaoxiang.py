# -*- coding: utf-8 -*-
# -*- coding: cp936 -*-
'''MainWindow类完成最简单的编辑功能，添加一个主菜单，两个子菜单（about和exit）'''
import wx

class MainWindow(wx.Frame):
  '''定义一个窗口类'''
  def __init__(self, parent, title):
    wx.Frame.__init__(self, parent, title=title, size=(300, 300))
    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

    self.start = wx.TextCtrl(self, style=wx.TE_MULTILINE)
    self.searchLabel = wx.StaticText(self, -1, 'input your criteria:')

    self.setupMenuBar()
    self.Show(True)

  def setupMenuBar(self):
    self.CreateStatusBar()

    menubar = wx.MenuBar()
    menufile = wx.Menu()

    mnuabout = menufile.Append(wx.ID_ABOUT, '&About', 'about this shit')
    mnuexit = menufile.Append(wx.ID_EXIT, 'E&xit', 'end program')

    menubar.Append(menufile, '&File')

    #事件绑定
    self.Bind(wx.EVT_MENU, self.onAbout, mnuabout)
    self.Bind(wx.EVT_MENU, self.onExit, mnuexit)

    self.SetMenuBar(menubar)

  def onAbout(self, evt):
      '''点击about的事件响应'''
      dlg = wx.MessageDialog(self, 'This is to assit your studay', 'Author: Ling', wx.OK)
      dlg.ShowModal()
      dlg.Destroy()

  def onExit(self, evt):
      '''点击退出'''
      self.Close(True)
app = wx.App(False)
frame = MainWindow(None, 'baishitong')
app.MainLoop() #循环监听事件
