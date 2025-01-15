print(f"{('Snake','Horse','Goat','Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon')[(y:=__import__('time').localtime().tm_year-2025)%12].upper()}{y+1}")
