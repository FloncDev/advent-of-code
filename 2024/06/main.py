from sys import stdin

data = stdin.read()

grid = [[char for char in i] for i in data.split("\n") if i != ""]
gsize = (len(grid[0]), len(grid))

guard_index = data.find("^")
# +1 Because data still has \n
guard = (guard_index % (gsize[0] + 1), guard_index // (gsize[1] + 1))
starting_pos = guard

facing = (0, -1)


def in_grid(x: int, y: int) -> bool:
    return (x >= 0 and x < gsize[0]) and (y >= 0 and y < gsize[1])


visited = set()
dirvisited = {i: set() for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]}

obstacles = set()

while in_grid(*guard):
    visited.add(guard)
    dirvisited[facing].add(guard)

    facing_tile = (guard[0] + facing[0], guard[1] + facing[1])

    if not in_grid(*facing_tile):
        break

    right_facing = (-facing[1], facing[0])

    if grid[facing_tile[1]][facing_tile[0]] == "#":
        facing = right_facing
        continue

    right_tile = (guard[0] + right_facing[0], guard[0] + right_facing[1])

    if right_tile in dirvisited[right_facing] and right_tile != starting_pos:
        obstacles.add(facing_tile)

    else:
        # Check for a tile further on
        vguard = guard
        vfacing = right_facing
        vvisited = set()
        vdirvisited = {i: set() for i in [(1, 0), (-1, 0), (0, 1), (0, -1)]}

        while in_grid(*vguard):
            vfacing_tile = (vguard[0] + vfacing[0], vguard[1] + vfacing[1])

            if not in_grid(*vfacing_tile):
                break

            if vguard in vdirvisited[vfacing]:
                obstacles.add(facing_tile)
                break

            vdirvisited[vfacing].add(vguard)

            if vfacing_tile in dirvisited[vfacing]:
                obstacles.add(facing_tile)
                break

            vright_facing = (-vfacing[1], vfacing[0])

            if grid[vfacing_tile[1]][vfacing_tile[0]] == "#":
                vfacing = vright_facing
                continue

            vguard = vfacing_tile

    grid[guard[1]][guard[0]] = "."
    guard = facing_tile
    grid[guard[1]][guard[0]] = "^"


print(len(visited), len(obstacles))
# 320 too low
# 627 too low
# 4710 too high
# not 1983
