from dungeon_game.area import Area
import random
from dungeon_game.direction import Direction, Position


def link_areas(area1, area2, direction):
    """
    Given a direction from area1 to area2, opens the exit for area1 and the corresponding opposite exit in area2.
    area1 and area2 are assumed to be adjacent and the direction correctly matches the adjacency.
    :param area1: the first area
    :param area2: the second area adjacent to the first
    :param direction: the direction to link the exits
    :return: area2 for debugging purposes
    """
    area1.exits[direction] = True
    area2.exits[direction.opposite] = True
    return area2


class MazeBuilder:
    """
    A helper class to procedurally generate a maze, an array of Areas with logically consistnet exits.
    """
    def __init__(self, size):
        """
        Initializes the maze builder, taking the size of the maze, and setting up a maze attribute for use across methods.
        :param size: a 2-tuple representing teh rows,columns of the maze
        :return: None
        """
        self.rows, self.cols = size
        self.maze = None

    def build_maze(self):
        """
        Coordinates the various methods to build the maze then outputs the built maze
        :return: The generated maze represented by an array of areas
        """
        self.initialize_maze()
        self.generate_maze_path()
        return self.maze

    def initialize_maze(self):
        """
        Sets up the initial area array with closed off Areas with no exits matching the sizes defined in initialization
        :return: an Array of closed room Areas
        """
        new_maze = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(Area(Position(row, col, self.rows, self.cols)))
            new_maze.append(new_row)
        self.maze = new_maze
        return new_maze

    def generate_maze_path(self):
        """
        Sets up exits between the areas using a somewhat questionable interpretation of the Kruskal algorithm
        :return: returns the maze attribute. Not currently used
        """
        rows = len(self.maze)
        cols = len(self.maze[0])
        passages = []
        kruskal_sets = []

        #A oassage is a list containing area1, area2 and the direction between them.
        # The loop goes through East-West pairs and North-South pair, which should cover all unique ones since W-E and S-N are just mirrored pairs
        for row_id, row in enumerate(self.maze):
            for col_id, ele in enumerate(row):
                if col_id < cols - 1:
                    passages.append([self.maze[row_id][col_id], self.maze[row_id][col_id + 1], Direction.EAST])
                if row_id < rows - 1:
                    passages.append([self.maze[row_id][col_id], self.maze[row_id + 1][col_id], Direction.SOUTH])

        #shuffle the passages to make things random
        random.shuffle(passages)


        while len(passages) > 0:
            current_passage = passages.pop()
            set1 = None
            set2 = None


            #check if either area in the passage is in an existing set
            for a_set in kruskal_sets:
                if current_passage[0] in a_set:
                    set1 = a_set
                if current_passage[1] in a_set:
                    set2 = a_set

            #if they are in teh same set we skip it to avoid cycles
            if set1 == set2 and not set1 is None:
                continue
            #otherwise we create an exit link between the adjacent areas.
            link_areas(current_passage[0], current_passage[1], current_passage[2])

            #if the sets aren't in any current ones we make a new one out of them
            if set1 is None and set2 is None:
                kruskal_sets.append({current_passage[0], current_passage[1]})
                continue

            #otherwise add the setless area to the set of the other area
            if set1 is None:
                set2.add(current_passage[0])
                continue

            if set2 is None:
                set1.add(current_passage[1])
                continue

            #otherwise if both are part of different sets we can join both sets
            if set1 != set2:
                new_set = set1.union(set2)
                kruskal_sets.remove(set1)
                kruskal_sets.remove(set2)
                kruskal_sets.append(new_set)

        return self.maze
