#!/usr/bin/env python3

def ft_count_harvest_recursive():
    loop_day = int(input("Days until harvest: "))
    day = 1

    def count(day):
        if day > loop_day:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)
    count(day)


if __name__ == "__main__":
    ft_count_harvest_recursive()
