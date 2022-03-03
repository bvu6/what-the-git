#!/usr/bin/env python3
# Made By Thicc Juice
# What The Git!
from PyQt5.QtWidgets import QMainWindow


class git_manager:
    def __init__(self):
        self.add = False
        self.commit = False
        self.push = False
        self.lastMove = -1
        self.branch = 'main'
        self.file_add_list = []
        self.chbase = QMainWindow

        self.cmd = ''
        self.file_dict = {}
        self.number_files_changed = 0

        self.new_cmd = "\nuser@what-the-git repo_folder % "
        self.cmd_not_found = "\nwtg_shell: command not found or supported: "
        self.git_cmd_not_found = "\nwhat_the_git: 'test' is not a git command that is supported."
        self.git_enter_valid_cmd = "\nwhat_the_git: please enter a valid git command"
        self.git_add_error = "\nNothing specified. nothing added\nhint: Maybe you wanted to say 'git add .'?"
        self.file_not_found = "\nwhat_the_git: 'test' file does not exist!"
        self.commit_msg = "\n[main] test\n x file(s) changed"
        self.push_msg = "\nEnumerating objects: done.\nCounting objects: 100%, done.\nDelta compression using up to " \
                        "10 threads\nCompressing objects: 100%, done.\nWriting objects: 100%, done.\nremote: " \
                        "Resolving deltas: 100%, done.\nTo https://github.com/wtg/what_the_git\n   62e827a..4b1d808  " \
                        "main -> main "

        self.up_to_date = "\nEverything already up-to-date"
        self.commit_no_changes = f"\nOn branch {self.branch}\nYour branch is up to date with 'origin/{self.branch}'." \
                                 f"\n\nnothing to commit, working tree clean"
        self.commit_error = "\nerror: please enter 'git commit -m \"msg\"' to make a commit"
        self.push_error = "\nerror: please enter 'git push' to push all your changes"

    # generate output string for console to display
    def generate_output(self, output):
        return self.cmd + output + self.new_cmd

    # handle commands entered by the user
    def handle_commands(self, chbase, cmd, file_dict):
        self.file_dict = file_dict
        self.cmd = cmd
        self.chbase = chbase

        # check for blank and empty string
        if not cmd or cmd.isspace():
            return self.new_cmd  # returns output for console to display

        cmd_list = cmd.split()

        if cmd_list[0] == 'git':
            if len(cmd_list) == 1:
                return self.generate_output(self.git_enter_valid_cmd)

            cmd_list.pop(0)  # remove "git" from list

            if cmd_list[0] == 'add':
                return self.git_add_cmd(cmd_list)

            elif cmd_list[0] == 'commit':
                return self.git_commit_cmd(cmd_list)

            elif cmd_list[0] == 'push':
                return self.git_push_cmd(cmd_list)

            else:
                output = self.git_cmd_not_found
                output = output.replace('test', cmd_list[0])
                return self.generate_output(output)

        # return empty string if no specifications are met
        return self.generate_output(self.cmd_not_found + cmd)

    def check_move(self, card_type):
        # if self.lastMove == card_type - 1:
        #     self.lastMove = card_type
        #     return True
        print("Last", self.lastMove, "type", card_type)
        if card_type == 0:
            self.lastMove = card_type
            return True

        elif card_type == 1 and self.lastMove == card_type - 1:
            self.lastMove = card_type
            self.commit = True
            return True

        elif card_type == 2 and self.commit:
            self.git_reset_flags()
            return True

        else:
            print("Invalid move")
            return False

    def modify_file_status(self, file):
        if self.file_dict[file].get_file_modified_status():
            print(f'modify init pass file {self.file_dict[file].get_file_modified_status()}')
            print(f'modify init pass add {self.add}')
            self.file_dict[file].set_file_modified_status_false()

            if file not in self.file_add_list:
                self.number_files_changed += 1
                self.file_add_list.append(file)

            self.add = True

            if 1 in self.chbase.task_done_list:
                self.chbase.set_task_done(2)

    def git_add_cmd(self, cmd_list):
        cmd_list.pop(0)  # remove "add" from list

        if len(cmd_list) == 0:
            return self.generate_output(self.git_add_error)

        # check cmd from the end
        cmd_list.reverse()

        # iterate through files in list and check what has been modified
        for file in cmd_list:

            # add all modified files
            if file == '.' or file == '*':
                for f in self.file_dict.keys():
                    self.modify_file_status(f)

            # add specified file if exists
            elif file in self.file_dict.keys():
                self.modify_file_status(file)

            # file not found
            else:
                output = self.file_not_found
                output = output.replace('test', file)
                return self.generate_output(output)

            return self.generate_output('')

    def git_commit_cmd(self, cmd_list):
        msg = ''
        cmd_list.pop(0)  # remove "commit" from list

        # check for valid git add command
        if len(cmd_list) < 2 or cmd_list[0] != '-m':
            return self.generate_output(self.commit_error)

        cmd_list.pop(0)  # remove "-m" from list

        # concatenate msg
        for cmd in cmd_list:
            msg = msg + cmd + ' '

        msg = msg.strip()
        if len(msg) < 2 or msg[0] != "\"" or msg[-1] != "\"":
            print('err2')
            print(msg)
            return self.generate_output(self.commit_error)

        # commit only if user has added files
        if not self.add:
            return self.generate_output(self.commit_no_changes)

        # perform git commit
        output = self.commit_msg
        output = output.replace('x', str(self.number_files_changed))
        self.add = False
        self.file_add_list.clear()
        self.number_files_changed = 0
        self.commit = True

        if 2 in self.chbase.task_done_list:
            self.chbase.set_task_done(3)

        return self.generate_output(output)

    def git_push_cmd(self, cmd_list):
        cmd_list.pop(0)  # remove "push" from list

        # check for valid git push command
        if len(cmd_list) > 0:
            return self.generate_output(self.push_error)

        # push only is user has committed
        if self.commit:
            self.commit = False

            if 3 in self.chbase.task_done_list:
                self.chbase.set_task_done(4)

            return self.generate_output(self.push_msg)

        # if user has not committed, indicate that everything is up-to-date
        return self.generate_output(self.up_to_date)
