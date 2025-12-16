from random import randint
from tile import Tile, plains, forest, pines, mountain, water


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.map_data: list[list[Tile]]

        self.generate_map()
        self.generate_patch(forest, 2, 5, 7)
        self.generate_patch(pines, 2, 2, 5)
        self.generate_patch(mountain, 3, 5, 7)
        # Ensure patch size does not exceed map dimensions
        max_patch_size = min(10, self.width - 2, self.height - 2)
        min_patch_size = min(8, max_patch_size)
        if max_patch_size >= 2:
            self.generate_patch(water, 1, min_patch_size, max_patch_size)

    def generate_map(self) -> None:
        self.map_data = [[plains for _ in range(self.width)] for _ in range(self.height)]

    def generate_patch(
            self,
            tile: Tile,
            num_patches: int,
            min_size: int,
            max_size: int,
            irregular: bool = True
    ) -> None:
        for _ in range(num_patches):
            # Ensure patch size fits within map
            patch_max_width = min(max_size, self.width - 2)
            patch_max_height = min(max_size, self.height - 2)
            patch_min_width = min(min_size, patch_max_width)
            patch_min_height = min(min_size, patch_max_height)
            if patch_max_width < 1 or patch_max_height < 1:
                continue
            width = randint(patch_min_width, patch_max_width)
            height = randint(patch_min_height, patch_max_height)
            if self.width - width - 1 < 1 or self.height - height - 1 < 1:
                continue
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular and self.width - max_size > 3:
                init_start_x = randint(3, self.width - max_size)
            else:
                init_start_x = start_x

            for i in range(height):
                if irregular and self.width - max_size > 3:
                    width = randint(int(0.7 * max_size), patch_max_width)
                    start_x = init_start_x - randint(0, 2)
                    start_x = max(1, min(start_x, self.width - width - 1))
                for j in range(width):
                    if 0 <= start_y + i < self.height and 0 <= start_x + j < self.width:
                        self.map_data[start_y + i][start_x + j] = tile

    def display_map(self) -> None:
        frame = "x" + self.width * "=" + "x"
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            print("|" + "".join(row_tiles) + "|")
        print(frame)

