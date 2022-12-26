from datetime import datetime, timedelta
import sys
import math
import argparse

parser = argparse.ArgumentParser(description='Pomodoro helper')

parser.add_argument('-no-break', dest='no_break', action='store_true', default=True, help='whether you are taking breaks')
parser.add_argument('-no-short-break', dest='no_short_break', default=False, action='store_true', help='whether you are taking short breaks')
parser.add_argument('-no-long-break', dest='no_long_break', default=False, action='store_true', help='whether you are taking long breaks')
parser.add_argument('-p', dest='pomodoros', type=int, default=16, help='how many pomodoros you have left')
parser.add_argument('-m', dest='partial', type=int, default=0, help='how many minutes of current pomodoro left')

args = parser.parse_args()

now = datetime.now()
pomodoros = args.pomodoros
short_brk_count = pomodoros - 1
long_brk_count = short_brk_count // 4
short_brk_minutes = 0 if args.no_short_break else 5 * short_brk_count
long_brk_duration = 15 if args.no_short_break else 10
long_brk_minutes = 0 if args.no_long_break else long_brk_duration * long_brk_count
brk_minutes = 0 if args.no_break else (short_brk_minutes + long_brk_minutes)

minutes = (pomodoros * 25) + args.partial + brk_minutes
eta = now + timedelta(minutes=minutes)
print(eta.strftime('%Y-%m-%d %I:%M %p'))
