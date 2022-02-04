#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# variant 6

import sys
from solver import interaction as inter
from solver import data_commands as d_com


if __name__ == '__main__':
    trains = []
    while True:
        command = inter.get_command()
        if command == 'exit':
            break

        elif command == 'add':
            trains.append(d_com.add())
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('destination', ''))

        elif command == 'list':
            inter.print_list(trains)

        elif command.startswith('select '):
            d_com.select(command, trains)

        elif command == 'help':
            inter.print_help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
