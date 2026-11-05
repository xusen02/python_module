#!/usr/bin/env python3

def ft_harvest_total():
    day_1 = int(input("Day 1 harvest: "))
    day_2 = int(input("Day 2 harvest: "))
    day_3 = int(input("Day 3 harvest: "))
    total_hrvt = day_1 + day_2 + day_3
    print(f"Total harvest: {total_hrvt}")


if __name__ == "__main__":
    ft_harvest_total()
