import os

last_day = max(int(name.split()[1]) for name in os.listdir() if name.startswith('day '))

os.mkdir(f'day {last_day+1}')

txt = open(f'./day {last_day+1}/day{last_day+1}_input.txt', 'w')
txt.close()

py = open(f'./day {last_day+1}/day{last_day+1}_solutions.py', 'w')
py.close()

print(f'Successfully created {last_day+1} directory')
