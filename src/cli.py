import curses
import os
import termios
import sys
import tty

class CursesMenu:
    def __init__(self):
        self.options = []
        self.selected_option = 0
        self.window = None

    def display_menu(self):
        self.window = curses.initscr()
        curses.curs_set(0)  # Hide cursor
        self.window.clear()
        self.window.refresh()
        self.window.keypad(True)  # Enable arrow key navigation

        self.options = [d for d in os.listdir() if os.path.isdir(d)]

        while True:
            self.window.clear()

            # Display options
            for i, option in enumerate(self.options):
                if i == self.selected_option:
                    self.window.addstr(i, 0, f"> {option}", curses.A_BOLD)
                else:
                    self.window.addstr(i, 0, f"  {option}")

            self.window.refresh()

            key = self.window.getch()

            if key == curses.KEY_UP and self.selected_option > 0:
                self.selected_option -= 1
            elif key == curses.KEY_DOWN and self.selected_option < len(self.options) - 1:
                self.selected_option += 1
            elif key == 10:  # Enter key
                return self.options[self.selected_option]  # Return the selected option

    def close_menu(self):
        if self.window:
            curses.endwin()

def main():
    try:
        curses_menu = CursesMenu()
        directory_path = curses_menu.display_menu()
        curses_menu.close_menu()
    except:
        directory_path = os.path.expanduser("~")  # Use os.path.expanduser to get user home directory

    # Rest of your code goes here
    image_paths = check_images_in_directory(directory_path)
    if image_paths:
        print("Image files in the directory:")
        for image_path in image_paths:
            print(image_path)
        dictionary = {image_path: predict_step([image_path]) for image_path in image_paths}
        print(dictionary)
    else:
        print("No image files found in the directory.")

if __name__ == "__main__":
    main()
