from functools import reduce
def f(inputs):
    turn_shift = {'L':(1j,0), 'R':(-1j,0), 'S':(1,1)}
    dir, pos = reduce(lambda dir_pos, turn_shift:
                        (dir_pos[0]*turn_shift[0], 
                         dir_pos[1]+turn_shift[1]*dir_pos[0]),
                      map(turn_shift.__getitem__, inputs.upper()),
                      (1, 0))
    x = pos == 0 if dir == 1 else 2*(1 - dir*(dir+1)).real
    print(x and 'Loop detected! %i cycle(s) to complete loop'%x or 'No loop detected!')