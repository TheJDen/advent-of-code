import itertools

def part1(directions, distances, colors):
    x = y = 0
    perimeter = set()
    for direction, distance_str, color in zip(directions, distances, colors):
        distance = int(distance_str)
        if direction == 'R':
            for i in range(x, x + distance + 1):
                perimeter.add((i, y))
            x += distance
        elif direction == 'L':
            for i in range(x - distance, x):
                perimeter.add((i, y))
            x -= distance
        elif direction == 'U':
            for j in range(y, y + distance + 1):
                perimeter.add((x, j))
            y += distance
        elif direction == 'D':
            for j in range(y - distance, y + 1):
                perimeter.add((x, j))
            y -= distance
    volume = 0
    visited = set()
    frontier = [(1, 1)]
    while frontier:
        next_frontier = []
        for i, j in frontier:
            visited.add((i, j))
            volume += 1
            if (i, j) in perimeter:
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    if (i + di, j + dj) in visited or (i + di, j + dj) not in perimeter:
                        continue
                    next_frontier.append((i + di, j + dj))
                    visited.add((i + di, j + dj))
            else:
                for di, dj in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 0)):
                    if (i + di, j + dj) in visited:
                        continue
                    next_frontier.append((i + di, j + dj))
                    visited.add((i + di, j + dj))

        frontier = next_frontier
    return volume
      
    

def part2(directions, distances, colors):
    x = y = 0
    points = [(0, 0)]
    for color in colors:
        distance = int(color[2:7], 16)
        if color[-2] == '0':
            x += distance
        elif color[-2] == '2':
            x -= distance
        elif color[-2] == '3':
            y += distance
        elif color[-2] == '1':
            y -= distance
        points.append((x, y))
    twice_area = 0
    perimeter = 0
    for (x1, y1), (x2, y2) in itertools.pairwise(reversed(points)):
        twice_area += (x1 * y2 - x2 * y1)
        perimeter += max(abs(y2 - y1), abs(x2 - x1))
    return (twice_area  - perimeter + 2) // 2 + perimeter
    
    

def parse_input(lines):
    directions, distances, colors = [], [], []
    for line in lines:
        direction, distance, color = line.split()
        directions.append(direction)
        distances.append(distance)
        colors.append(color)
    return directions, distances, colors

def main():
    with open("input.txt") as f:
        directions, distances, colors = parse_input([line.rstrip() for line in f])
    #print(part1(directions, distances, colors))
    print(part2(directions, distances, colors))


if __name__ == "__main__":
    main()