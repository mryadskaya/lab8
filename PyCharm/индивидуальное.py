#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    championship_1 =tuple(map(int, input().split()))
    championship_2 =tuple(map(int, input().split()))

    total_goals = 0

    for goals in championship_1:
        total_goals += goals

    for goals in championship_2:
        total_goals += goals

    print("Общее количество мячей, забитых командой в двух чемпионатах:",
          total_goals)
