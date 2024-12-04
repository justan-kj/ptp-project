from dungeon_game.area import Area
import random
from dungeon_game.direction import Direction, Position


class MazeBuilder:
    def __init__(self, size, seed):
        self.rows, self.cols = size
        self.maze = None
        self.seed = seed

    def build_maze(self):
        self.initialize_maze()
        self.generate_maze_path()
        return self.maze

    def link_areas(self, area1, area2, direction):
        area1.exits[direction] = True
        area2.exits[direction.opposite] = True
        return area2

    def initialize_maze(self):
        new_maze = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(Area(Position(row,col,self.rows,self.cols)))
            new_maze.append(new_row)
        self.maze = new_maze
        return new_maze

    def generate_maze_path(self):
        rows = len(self.maze)
        cols = len(self.maze[0])
        passages = []
        kruskal_sets = []

        for row_id,row in enumerate(self.maze):
            for col_id,ele in enumerate(row):
                if col_id < cols - 1:
                    passages.append([self.maze[row_id][col_id], self.maze[row_id][col_id +1], Direction.EAST])
                if row_id < rows - 1:
                    passages.append([self.maze[row_id][col_id], self.maze[row_id+1][col_id], Direction.SOUTH])

        random.seed(self.seed)
        random.shuffle(passages)

        while len(passages) > 0:
            current_passage = passages.pop()
            set1 = None
            set2 = None

            for a_set in kruskal_sets:
                if current_passage[0] in a_set:
                    set1 = a_set
                if current_passage[1] in a_set:
                    set2 = a_set

            if set1 == set2 and not set1 is None:
                continue
            self.link_areas(current_passage[0], current_passage[1], current_passage[2])
            if set1 is None and set2 is None:
                kruskal_sets.append({current_passage[0],current_passage[1]})

                continue

            if set1 is None:
                set2.add(current_passage[0])
                continue

            if set2 is None:
                set1.add(current_passage[1])
                continue

            if set1 != set2:
                new_set = set1.union(set2)
                kruskal_sets.remove(set1)
                kruskal_sets.remove(set2)
                kruskal_sets.append(new_set)
        return self.maze





