#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import List

#   https://drive.google.com/drive/folders/1cZ1eLdnvKhSnTTWN0nnztHVqnrwLN2CB

@dataclass(frozen=True)
class People:
    birthday: List[int]
    br: List[int]


@dataclass
class Man:
    soul: List[People] = field(default_factory=lambda: [])

    def add(self, birthday, br):
        self.soul.append(
            People(
                birthday=birthday,
                br=br
            )
        )


if __name__ == '__main__':
    birthday = list(map(int, input("Введите числа: ").split(" ")))
    br = list(map(int, input("Введитеdfsaf: ").split(" ")))
    num = birthday.append("Ширма")
    for i in birthday:
        print(i)
