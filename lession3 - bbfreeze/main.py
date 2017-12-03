import wx
# print("I love you")

if __name__ == '__main__':
	app = wx.App(False)
	frame = wx.Frame(None, -1, 'simple.py')
	frame.Show()
	app.MainLoop()
	# print(wx.version())
