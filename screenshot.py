# If there are any issues, there might be a missing wx dependency.
# pip install wheel, pip install wxpython worked for me, but here are some things to try if you run into any issues:
# https://stackoverflow.com/questions/32284938/how-to-properly-install-wxpython

import wx
app = wx.App()  # Need to create an App instance before doing anything

# Inspired by: https://stackoverflow.com/a/10089645/4954277
def takeScreenshot():
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem  # Release bitmap
    bmp.SaveFile('screenshot.png', wx.BITMAP_TYPE_PNG)
    return 'screenshot.png'

