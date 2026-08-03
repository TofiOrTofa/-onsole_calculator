#!/usr/bin/env -S python3 -u
"""console colculator"""

from modules.calc_pkg import nodes
from modules import menu

def main() -> None:

    result = ""
    while not result:
        nodes.terminal_clear()
        result = menu.print_menu()
        try:
            if len(result) > 1:
                menu.Menu[result[0]](result[1])
            else:
                menu.Menu[result[0]]()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
