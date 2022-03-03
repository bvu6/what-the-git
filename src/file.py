#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

class file:
    def __init__(self, name):
        self.file_name = name
        self.file_modified_status = False

    def get_file_modified_status(self):
        return self.file_modified_status

    def toggle_file_modified_status(self):
        self.file_modified_status = not self.file_modified_status


def main():
    return


if __name__ == "__main__":
    main()
