
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(list_of_orbits):
    s = [pi * a * b for a, b in list_of_orbits if a != b]
    return list_of_orbits[s.index(max(s))]

print(find_farthest_orbit(orbits))