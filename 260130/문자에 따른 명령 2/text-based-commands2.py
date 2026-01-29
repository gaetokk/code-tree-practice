dirs = input()

# Please write your code here.

def rotate_R(dir_num):    
    # rotate direction
    if dir_num == 0:
        dir_num = 1
    elif dir_num == 1:
        dir_num = 2
    elif dir_num == 2:
        dir_num = 3
    else:
        dir_num = 0
    return dir_num

def rotate_L(dir_num):    
    # rotate direction
    if dir_num == 0:
        dir_num = 3
    elif dir_num == 1:
        dir_num = 0
    elif dir_num == 2:
        dir_num = 1
    else:
        dir_num = 2
    return dir_num

dir_num = 3 
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for mov in dirs:
    if mov == 'L':
        dir_num = rotate_L(dir_num)
    elif mov == 'R':
        dir_num = rotate_R(dir_num)
    elif mov == 'F':
        # move
        nx, ny = x + dx[dir_num], y + dy[dir_num]

print(nx, ny)
