from app.grid.grid import Grid
from app.algorithms.astar import astar

def main():
    grid = Grid(5, 5)
    path = astar(grid, (0,0), (4,4))
    print("Path:", path)

if __name__ == "__main__":
    main()
