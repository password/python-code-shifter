#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Fri Sep 24 00:36:00 2010

import wx

# begin wxGlade: extracode
# end wxGlade

abc = u"АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ01234567890,.!?\\\":-_Z"
str_sample = u"ДУФДХФШФТДШЁТДЭШФГШФДЧСЩЭПСФЧ2-ДУПРШФДУЛДОУЁЛШДШФЭУФ-ДЭШФ-ДЁ"
result_sample = u'ЗЧШЗЩШЬШЦЗЬКЦЗ1ЬШЖЬШЗЫХЭ1УХШЫ6БЗЧУФЬШЗЧПЗТЧКПЬЗЬШ1ЧШБЗ1ЬШБЗК'

def shift (string, dict_string, push_length):
 ans = u''
 for string_l in string:
  i = 0
  for dict_string_l in dict_string:
   if string_l == dict_string_l:
    ipush = i + push_length
    new_l = dict_string[ipush % len(dict_string)]
    if new_l == '_':
     ans = ans + ' '
    elif new_l == 'Z':
     ans = ans + '\r\n'
    else:
     ans = ans + new_l
   i = i + 1
 return ans

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.text_ctrl_str = wx.TextCtrl(self, -1, str_sample, style=wx.TE_MULTILINE)
        self.slider_1 = wx.Slider(self, -1, 4, 1, len(abc), style=wx.SL_HORIZONTAL|wx.SL_LABELS)
        self.text_ctrl_result = wx.TextCtrl(self, -1, result_sample, style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.scroll, self.text_ctrl_str)
        self.Bind(wx.EVT_COMMAND_SCROLL, self.scroll, self.slider_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(u"Простой шифр")
        self.SetSize((412, 309))
        self.text_ctrl_str.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_1 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_str, 0, wx.ALL|wx.EXPAND, 3)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_1.Add(self.slider_1, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_2.Add(self.text_ctrl_result, 0, wx.ALL|wx.EXPAND, 3)
        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def scroll(self, event): # wxGlade: MyFrame.<event_handler>
        self.text_ctrl_result.SetValue(shift (self.text_ctrl_str.GetValue(), abc, int(self.slider_1.GetValue())))

# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
