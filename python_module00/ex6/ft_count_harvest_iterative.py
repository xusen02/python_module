#!/usr/bin/env python3

def ft_count_harvest_iterative():
    loop_day = int(input("Days until harvest: "))
    for day in range(1, loop_day + 1):
        print(f"Days {day}")
    print("Harvest time!")


if __name__ == "__main__":
    ft_count_harvest_iterative()
