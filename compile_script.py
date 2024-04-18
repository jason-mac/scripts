# Python script to compile and execute project in current directory
# My first ever Python script
import os
import subprocess
import time
from datetime import datetime

from timedinput import TimeoutOccurred, timedinput


def run_commands():
    subprocess.run(["zsh", "-c", "clang++ -o main *.cpp"])
    subprocess.run(["zsh", "-c", "./main"])


def directory_changed(directory_path, last_modified):
    current_modified = os.stat(directory_path).st_mtime
    if current_modified != last_modified:
        return True, current_modified
    return False, current_modified


def main():
    directory_path = os.getcwd()
    last_modified = os.stat(directory_path).st_mtime
    changed = False
    while True:
        current_datetime = datetime.now()
        formated_time = current_datetime.strftime("%I:%M:%S %p")
        changed, last_modified = directory_changed(directory_path, last_modified)
        if changed:
            print(
                "Changes have been detected. Compile and execute changes in current directory?",
                formated_time,
            )
            try:
                user_input = timedinput(
                    "Enter any key for yes, enter nothing for no (8 second time limit): ",
                    timeout=8,
                    default="",
                )
            except TimeoutOccurred:
                user_input = None
            if user_input:
                print("Attempting to compile and execute current directory now\n")
                run_commands()
                print("\nPython Script resuming now\n")
            if user_input == "":
                print("No input detected. Resuming Python Script", formated_time, "\n")
            if user_input == None:
                print("Time limit reached. Resuming Python Script", formated_time, "\n")
            changed, last_modified = directory_changed(directory_path, last_modified)
            continue
        time.sleep(2)


main()
