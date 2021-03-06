#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Thu Apr 23 16:37:30 2015
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade
import urllib
import subprocess
import webbrowser
# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Team 4 - Web Server"), style=wx.ALIGN_CENTRE)
        self.btnStart = wx.Button(self, wx.ID_ANY, _("Start"))
        self.btnStop = wx.Button(self, wx.ID_ANY, _("Stop"))
        self.btnRestart = wx.Button(self, wx.ID_ANY, _("Restart"))
        self.btnWindow = wx.Button(self, wx.ID_ANY, _("Open Window"))
        self.btnExit = wx.Button(self, wx.ID_ANY, _("Exit"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        self.Bind(wx.EVT_BUTTON, self.startApache, self.btnStart)
        self.Bind(wx.EVT_BUTTON, self.stopApache, self.btnStop)
        self.Bind(wx.EVT_BUTTON, self.restartApache, self.btnRestart)
        self.Bind(wx.EVT_BUTTON, self.exitApp, self.btnExit)
        self.Bind(wx.EVT_BUTTON, self.openBrowser, self.btnWindow)

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame_1"))
        self.SetSize((300, 100))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.label_1, 0, wx.EXPAND, 0)
        sizer_2.Add(self.btnStart, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.btnStop, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.btnRestart, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.btnWindow, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.btnExit, 0, 0, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade


    def startApache(self, event):
        subprocess.call("sudo service apache2 start", shell=True)
        self.openBrowser(event)
    def stopApache(self, event):
        subprocess.call("sudo service apache2 stop", shell=True)
    def restartApache(self, event):
        subprocess.call("sudo service apache2 restart", shell=True)
        self.openBrowser(event)
    def exitApp(self, event):
        self.stopApache(event)
        app.Exit()
    def openBrowser(self, event):
        # command = "cmd /c start firefox http://localhost --new-window"
        # subprocess.Popen(command, shell=True)
        webbrowser.open('http://localhost', new=1)

# end of class MyFrame
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()