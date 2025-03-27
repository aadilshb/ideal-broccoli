def shift_coor(coords):
    min_x=min(x for x, y in coords)
    min_y=min(y for x, y in coords)

    shift_x=abs(min_x) if min_x < 0 else 0
    shift_y=abs(min_y) if min_y < 0 else 0

    new_coords=[(x + shift_x, y + shift_y) for x, y in coords]
    return new_coords

coords=[(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
new_coords=shift_coor(coords)

print(coords,"\n\n\n")
print(new_coords)
