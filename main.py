from wx import App
from main_frame import MainFrame
import keyboard
import mouse
import time
import random


def auto_hash_builder():
    for item in range(main_frame.items_names_len):
        # Open flea market
        time.sleep(0.1)
        mouse.move(1249, 1064, duration=0.1)
        time.sleep(0.1)
        mouse.click()
        time.sleep(0.1)

        # Click on search input
        mouse.move(68, 118, duration=random.random())
        time.sleep(0.1)
        mouse.click()
        time.sleep(0.1)

        # Write item name in search
        keyboard.write(main_frame.item_name())
        time.sleep(2)

        # Click on search result
        mouse.move(119, 165, duration=random.random())
        time.sleep(0.1)
        mouse.click()
        time.sleep(0.1)

        # Move to item for scan and wait
        mouse.move(911, 319, duration=0.1)
        time.sleep(2)

        main_frame.set_hash_to_item()
        time.sleep(0.1)

        # Escape to main menu to clean search input
        mouse.move(1249, 1064, duration=0.1)
        time.sleep(0.1)
        mouse.click()
        time.sleep(0.1)
        time.sleep(random.randint(1, 3))

        # Next item
        main_frame.next_item()
    main_frame.save()


app = App()
main_frame = MainFrame()

# Options
hash_lang = 'EN'

# Listener
keyboard.add_hotkey('F1', lambda: main_frame.prev_item())
keyboard.add_hotkey('F2', lambda: main_frame.next_item())
keyboard.add_hotkey('F3', lambda: main_frame.search_first_no_hash_item())
keyboard.add_hotkey('F4', lambda: main_frame.search_last_no_hash_item())

keyboard.add_hotkey('F5', lambda: keyboard.write(main_frame.item_name()))
keyboard.add_hotkey('F6', lambda: main_frame.set_hash_to_item())
keyboard.add_hotkey('F7', lambda: main_frame.set_no_hash_to_item())
keyboard.add_hotkey('F8', lambda: main_frame.save())

# Experimental
keyboard.add_hotkey('F10', lambda: auto_hash_builder())

app.MainLoop()
