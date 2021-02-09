from wx import App
from main_frame import MainFrame
import keyboard


# Options
hash_lang = 'RU'  # Available choices: 'EN', 'RU'


# App initialization
app = App()
main_frame = MainFrame(hash_lang)


# Listener
keyboard.add_hotkey('F1', lambda: main_frame.prev_item())
keyboard.add_hotkey('F2', lambda: main_frame.next_item())
keyboard.add_hotkey('F3', lambda: main_frame.search_first_no_hash_item())
keyboard.add_hotkey('F4', lambda: main_frame.search_last_no_hash_item())

keyboard.add_hotkey('F5', lambda: keyboard.write(main_frame.item_name()))
keyboard.add_hotkey('F6', lambda: main_frame.set_hash_to_item())
keyboard.add_hotkey('F7', lambda: main_frame.set_no_hash_to_item())
keyboard.add_hotkey('F8', lambda: main_frame.save())


app.MainLoop()
