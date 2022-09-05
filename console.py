#!/usr/bin/python3
"""
A custom console module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    custom console
    """

    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
