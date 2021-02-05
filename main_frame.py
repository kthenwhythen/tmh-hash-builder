import wx
import mouse
import time
import threading
from scan import Scan
from items import Items


class MainFrame(wx.Frame):
    def __init__(self):
        style = (wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR | wx.SIMPLE_BORDER)
        super().__init__(None, title='TMH database builder', size=(300, 54), style=style)
        self.panel = wx.Panel(self)
        self.SetTransparent(220)
        self.SetBackgroundColour("black")

        self.previous_item_hash = None
        self.items = Items()
        # self.item = pandas.DataFrame()
        # self.item_state = "No item"
        self.item_hash = ""

        self.current_item_position = 0
        self.items_names_len = len(self.items.item_names)

        self.name_text = wx.StaticText(self.panel, label="")
        self.hash_text = wx.StaticText(self.panel, label="")

        self.init_ui()

        self.thread_is_on = False
        self.set_update_frame(True)
        self.Show(True)

    def set_update_frame(self, thread_is_on):
        self.thread_is_on = thread_is_on
        if self.thread_is_on:
            thread = threading.Thread(target=self.update_frame)
            thread.start()

    def update_frame(self):
        while self.thread_is_on:
            time.sleep(0.005)

            # Update position
            pos_x, pos_y = mouse.get_position()
            wx.CallAfter(self.Move, wx.Point(pos_x + 10, pos_y + 20))

            # Auto scan (hitting performance)
            self.scan_item()

            # Update item info
            if self.previous_item_hash is not self.item_hash or \
                    self.item_hash is None and self.previous_item_hash is not None:
                self.previous_item_hash = self.item_hash
                self.update_ui()

    def init_ui(self):
        hbox = wx.BoxSizer()
        fb = wx.FlexGridSizer(2, 1, 6, 6)
        self.name_text = wx.StaticText(self.panel, label="TMH hash creator")
        self.name_text.SetForegroundColour((160, 160, 170))
        self.hash_text = wx.StaticText(self.panel, label="Select item")
        self.hash_text.SetForegroundColour((160, 160, 170))
        fb.AddMany([self.name_text, self.hash_text])
        hbox.Add(fb, proportion=1, flag=wx.EXPAND | wx.ALL, border=6)
        self.panel.SetSizer(hbox)
        self.Layout()

    def update_ui(self):
        if self.items.data.at[self.current_item_position, 'Hash EN'] == 'No hash':
            self.name_text.SetForegroundColour((255, 160, 170))
        elif self.items.data.at[self.current_item_position, 'Hash EN'] != 'None':
            self.name_text.SetForegroundColour((160, 255, 170))
        else:
            self.name_text.SetForegroundColour((160, 160, 170))
        self.name_text.SetLabel(self.items.item_names[self.current_item_position])
        if self.item_hash:
            self.hash_text.SetForegroundColour((160, 160, 170))
            self.hash_text.SetLabel(self.item_hash)
            if self.item_hash == self.items.data.at[self.current_item_position, 'Hash EN'] and 'None' != self.items.data.at[self.current_item_position, 'Hash EN']:
                self.hash_text.SetForegroundColour((160, 255, 170))
                self.hash_text.SetLabel(self.item_hash)
        else:
            self.hash_text.SetForegroundColour((160, 160, 170))
            self.hash_text.SetLabel('None')

    def scan_item(self):
        self.item_hash = Scan().item_hash

    def next_item(self):
        if self.current_item_position < self.items_names_len - 1:
            self.current_item_position += 1
            self.name_text.SetLabel('')
            self.hash_text.SetLabel('')
            self.update_ui()

    def prev_item(self):
        if self.current_item_position > 0:
            self.current_item_position -= 1
            self.hash_text.SetLabel('')
            self.update_ui()

    def item_name(self):
        return self.items.item_names[self.current_item_position]

    def set_hash_to_item(self):
        if self.item_hash:
            self.items.data.at[self.current_item_position, 'Hash EN'] = self.item_hash
            self.hash_text.SetLabel('')
            self.name_text.SetLabel('')

    def set_no_hash_to_item(self):
        self.items.data.at[self.current_item_position, 'Hash EN'] = 'No hash'
        self.hash_text.SetLabel('')
        self.name_text.SetLabel('')
        self.update_ui()

    def save(self):
        self.items.save_data()

    def search_first_no_hash_item(self):
        for item_pos in range(self.items_names_len):
            if self.items.data.at[item_pos, 'Hash EN'] == 'None':
                self.current_item_position = item_pos
                break
        self.hash_text.SetLabel('')
        self.update_ui()

    def search_last_no_hash_item(self):
        for item_pos in reversed(range(self.items_names_len)):
            if self.items.data.at[item_pos, 'Hash EN'] == 'None':
                self.current_item_position = item_pos
                break
        self.hash_text.SetLabel('')
        self.update_ui()
