import re


def change_dr(dr, step, arr):
    if dr in ['N', 'E']:
        arr[dr] += step
        return
    dr = 'N' if dr == 'S' else 'E'
    arr[dr] -= step
        
        
def get_ship_coords(ins):
    global ship_cur
    dr, step = ins[0], int(ins[1])
    ins = ins[0] + ins[1]
    if dr in ['L', 'R']:
        if ins in ['R90', 'L270']:
            ind_offset = 1
        else:
            ind_offset = 2 if ins in ['R180', 'L180'] else -1
        ship_cur = dr_list[(dr_list.index(ship_cur) + ind_offset) % len(dr_list)]
    else:
        dr = ship_cur if dr == 'F' else dr
        change_dr(dr, step, ship_drs)
    

def get_waypoint_coords(ins):
    dr, step = ins[0], int(ins[1])
    ins = ins[0] + ins[1]
    if dr == 'F':
        ship_drs['E'] += step * waypoint_drs['E']
        ship_drs['N'] += step * waypoint_drs['N']
    elif ins in ['R90', 'L270']:
        waypoint_drs['E'], waypoint_drs['N'] = waypoint_drs['N'], -waypoint_drs['E']
    elif ins in ['R180', 'L180']:
        waypoint_drs['E'], waypoint_drs['N'] = -waypoint_drs['E'], -waypoint_drs['N']
    elif ins in ['R270', 'L90']:
        waypoint_drs['E'], waypoint_drs['N'] = -waypoint_drs['N'], waypoint_drs['E']
    else:
        change_dr(dr, step, waypoint_drs)


with open('navigation.txt', 'r') as f:
    nav = [re.findall(r'[A-Za-z]|\d+', line.rstrip()) for line in f.readlines()]

ship_cur = 'E'
ship_drs = {'E': 0, 'N': 0}
waypoint_drs = {'E': 10, 'N': 1}
dr_list = ['E', 'S', 'W', 'N']
for i in nav:
    # get_ship_coords(i)
    get_waypoint_coords(i)
print(sum(abs(i) for i in ship_drs.values()))
