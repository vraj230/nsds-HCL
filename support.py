import os
import psutil

def modify(line):
    #print(line)
    line_lst = []
    line_str = ''
    j = 0
    while line[j] != '\n':
        if line[j] == ' ':
            line_lst.append(line_str)
            line_str = ''
        line_str += line[j]
        j += 1
    line_lst.append(line_str)
    return line_lst


def get_process():

    output = os.popen('ps aux')
    lst = output.readlines()
    #print(lst)

    new_lst = []

    user_lst = []
    PID = []
    cpu = []
    mem = []
    vsz = []
    rss = []
    tt = []
    stat = []
    started = []
    time = []
    #command = []
    p_name = []
    #new_str = ""
    i = 0
    #for i in lst:
    for i in range(1, len(lst)):
        list = modify(lst[i])
        num = 0
        for j in list:
            if num == 0 and j != ' ':
                user_lst.append(j)
                num += 1
            elif num == 1 and j != ' ':
                PID.append(j)
                num += 1
            elif num == 2 and j != ' ':
                cpu.append(j)
                num += 1
            elif num == 3 and j != ' ':
                mem.append(j)
                num += 1
            elif num == 4 and j != ' ':
                vsz.append(j)
                num += 1
            elif num == 5 and j != ' ':
                rss.append(j)
                num += 1
            elif num == 6 and j != ' ':
                tt.append(j)
                num += 1
            elif num == 7 and j != ' ':
                stat.append(j)
                num += 1
            elif num ==8 and j != ' ':
                started.append(j)
                num += 1
            elif num == 9 and j != ' ':
                time.append(j)
                num += 1

            # if you need command implement this
            #elif num == 10 and j != ' ':
            #    command.append(j)

    #print(user_lst)

    for item in PID:
        #print(item)
        process = psutil.Process(int(item))
        name = process.name()
        p_name.append(name)

    #print(p_name)

    json_lst = []
    for num in range(0, len(user_lst)):
        dct = {}
        dct['user'] = user_lst[num]
        dct['pid'] = PID[num]
        dct['p_name'] = p_name[num]
        dct['cpu'] = cpu[num]
        dct['mem'] = mem[num]
        dct['vsz'] = vsz[num]
        dct['rss'] = rss[num]
        dct['tt'] = tt[num]
        dct['stat'] = stat[num]
        dct['started'] = started[num]
        dct['time'] = time[num]

        json_lst.append(dct)

    return (json_lst)