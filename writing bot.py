pages1, lines1, pages2, lines2, read_speed, write_speed, time = map(int, (input() for i in range(7)))
total_lines1 = pages1 * lines1
total_time = total_lines1 // read_speed
if total_time < time:
    lines = (time - total_time) * write_speed
    page = lines // lines2
    line = lines % lines2
    if line == 0:
        line = lines2
    print("{} {} {}".format("WRITE", page, line))
else:
    lines = time * read_speed
    page = lines // lines1
    line = lines % lines1
    if line == 0:
        line = lines1
    print("{} {} {}".format("READ", page, line))
