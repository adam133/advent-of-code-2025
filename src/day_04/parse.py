import os

class Item:
    # represents an item in a 2D grid
    def __init__(self, x: int, y: int, value: str):
        self.x: int = x
        self.y: int = y
        self.type: str = value
        self.accessible: bool = False
        self.neighbors: list[Item] = []
    
    def is_accessible(self, neighbors: list["Item"]) -> bool:
        count = 0
        if self.type == ".":
            self.accessible = False
            return False
        for neighbor in neighbors:
            if neighbor.type == "@":
                count += 1
        if count < 4 and self.type == "@":
            self.accessible = True
            return True
        else:
            self.accessible = False
            return False

class Grid:
    # represents a 2D grid of items
    # want to be able to easily determine neighbors of a given item
    def __init__(self, grid_list: list[str]):
        self.grid_list: list[str] = grid_list
        self.height: int = len(grid_list)
        self.width: int = len(grid_list[0]) if self.height > 0 else 0
        self.items: list[Item] = self.populate_grid()
        self._item_map: dict[tuple[int, int], Item] = {(item.x, item.y): item for item in self.items}
    
    def populate_grid(self) -> list[Item]:
        items: list[Item] = []
        for y, row_str in enumerate(self.grid_list):
            item: list[Item] = [Item(x, y, char) for x, char in enumerate(row_str)]
            items.extend(item)
        return items
    
    def get_item_neighbors(self, item: Item) -> list[Item]:
        if item.neighbors:
            return item.neighbors
        neighbors: list[Item] = []
        directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        for dx, dy in directions:
            nx, ny = item.x + dx, item.y + dy
            if (nx, ny) in self._item_map:
                neighbors.append(self._item_map[(nx, ny)])
        item.neighbors = neighbors
        return neighbors
    
    def get_obstacles(self) -> list[Item]:
        for item in self.items:
            item.is_accessible(self.get_item_neighbors(item))
        return self.items

    def count_accessible_items(self) -> int:
        count = 0
        for item in self.items:
            if item.accessible:
                count += 1
        return count
    
    def print_accessible_grid(self) -> None:
        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                item = next(i for i in self.items if i.x == x and i.y == y)
                row_str += item.type
            print(row_str)
    
    def remove_accessible_items(self) -> int:
        removed_count = 0
        for item in self.items:
            if item.accessible:
                self.update_item_type(item, ".")
                removed_count += 1
        return removed_count
    
    def update_item_type(self, item: Item, new_type: str) -> None:
        item.type = new_type
        if new_type == ".":
            item.accessible = False
        # item.is_accessible(self.get_item_neighbors(item))
        # for neighbor in self.get_item_neighbors(item):
        #     neighbor.is_accessible(self.get_item_neighbors(neighbor))

def parse_file_to_list_str(file_path: str) -> list[str]:
    # get absolute path from relative path
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r') as file:
        input_list = file.read().strip().split('\n')
    return input_list

def create_grid_from_input_list(input_list: list[str]) -> Grid:
    grid = Grid(input_list)
    return grid
