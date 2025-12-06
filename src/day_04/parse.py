import os

class Item:
    # represents an item in a 2D grid
    def __init__(self, x: int, y: int, value: str):
        self.x: int = x
        self.y: int = y
        self.type: str = value
        self.can_be_visited: bool = False
    
    def check_accessible(self, neighbors: list["Item"]) -> bool:
        count = 0
        for neighbor in neighbors:
            if neighbor.type == "@":
                count += 1
        return count < 4


class Grid:
    # represents a 2D grid of items
    # want to be able to easily determine neighbors of a given item
    def __init__(self, grid_list: list[str]):
        self.grid_list: list[str] = grid_list
        self.height: int = len(grid_list)
        self.width: int = len(grid_list[0]) if self.height > 0 else 0
        self.items: list[Item] = self.populate_grid()
    
    def populate_grid(self) -> list[Item]:
        items: list[Item] = []
        for y, row_str in enumerate(self.grid_list):
            item: list[Item] = [Item(x, y, char) for x, char in enumerate(row_str)]
            items.extend(item)
        return items
    
    def get_item_neighbors(self, item: Item) -> list[Item]:
        neighbors: list[Item] = []
        directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]  # left, right, up, down, left-up, right-up, left-down, right-down
        for dx, dy in directions:
            nx, ny = item.x + dx, item.y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor = next((i for i in self.items if i.x == nx and i.y == ny), None)
                if neighbor:
                    neighbors.append(neighbor)
        return neighbors
    
    def get_obstacles(self) -> list[Item]:
        for item in self.items:
            if not item.check_accessible(self.get_item_neighbors(item)):
                item.can_be_visited = False
            else:
                if item.type == "@":
                    item.can_be_visited = True
        return self.items

    def count_accessible_items(self) -> int:
        count = 0
        for item in self.items:
            if item.can_be_visited:
                count += 1
        return count
    
    def print_accessible_grid(self) -> None:
        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                item = next(i for i in self.items if i.x == x and i.y == y)
                if item.can_be_visited:
                    row_str += item.type
                else:
                    row_str += "."
            print(row_str)

def parse_file_to_list_str(file_path: str) -> list[str]:
    # get absolute path from relative path
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r') as file:
        input_list = file.read().strip().split('\n')
    return input_list

def create_grid_from_input_list(input_list: list[str]) -> Grid:
    grid = Grid(input_list)
    return grid
