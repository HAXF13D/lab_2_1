#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from module import individual_func as indiv

if __name__ == "__main__":
    replacer = indiv(
        "Уважаемый %F%, %N%! Вы делаете работу по замыканиям функций."
    )
    print(replacer('Vladimir', 'Shalnev'))
    print(replacer('Dinis', 'Proverkovich'))
    replacer = indiv("Уважаемый %F%, %N%!")
    print(replacer('Nestikus', 'Dimov'))
