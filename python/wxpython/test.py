import wx
class Frame(wx.Frame):  # 定义一个 wx.Frame的子类，以便我们更容量控制框架的内容和外观
        """ Frame class that displays an image."""
        def __init__(self, image, parent=None, id=-1,
                     pos=wx.DefaultPosition,
                     title='Hello, wxPython!'):  # 给我们的框架的构造器增加一个图像参数。这个值通过我们的应用程序
                                                                                                # 类在创建一个框架的实例时提供
            """Create a Frame instance and display image."""  # 用 wx.StaticBitmap控件来显示这个图像，它要求一个位图
            temp = image.ConvertToBitmap()
            size = temp.GetWidth(), temp.GetHeight()
            wx.Frame.__init__(self, parent, id, title, pos, size)
            self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
class App(wx.App):  # 定义一个带有 OnInit()方法的 wx.App的子类
        """Application class."""
        def OnInit(self):  # 使用与 hello.py在同一目录下的名为 wxPython.jpg的文件创建了一个图像对象
            image = wx.Image('wxPython.jpg', wx.BITMAP_TYPE_JPEG)
            self.frame = Frame(image)
            self.frame.Show()
            self.SetTopWindow(self.frame)
            return True
def main():  # main()函数创建一个应用程序的实例并启动wxPython的事件循环
        app = App()
        app.MainLoop()
if __name__ == '__main__':
        main()
