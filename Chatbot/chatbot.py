import wx
import wikipedia


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(1000, 700))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(panel, -1, "Response")

        hbox2.Add(l1, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t2 = wx.TextCtrl(panel, size=(1000, 600), style=wx.TE_MULTILINE)

        hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        vbox.Add(hbox2)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        l1 = wx.StaticText(panel, -1, "Requests")

        hbox1.Add(l1, 0, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1 = wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER, size=(1000, 20))

        hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        self.t1.SetFocus()
        self.t1.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        vbox.Add(hbox1)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()
        self.Fit()
    def OnEnter(self, event):
        ques = self.t1.GetValue()
        ques = ques.lower()

        try:
            self.t1.Clear()
            self.t2.AppendText("Request>> ")
            self.t2.AppendText('\n')
            self.t2.AppendText(ques)
            self.t2.AppendText('\n')
            self.t2.AppendText('\n')
            self.t2.AppendText("Response>> ")
            self.t2.AppendText('\n')
            self.t2.AppendText(str(wikipedia.summary(ques, sentences=2)))
            self.t2.AppendText('\n')
            self.t2.AppendText('\n')
        except:
            self.t2.AppendText("I don't know")
            self.t2.AppendText('\n')
            self.t2.AppendText('\n')
            print( "I don't know")

app = wx.App()
Mywin(None, 'TextCtrl demo')
app.MainLoop()