from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
#------------------------------------------------------------------------------#
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
#------------------------------------------------------------------------------#


def bfs(visited_rooms):
        """
        Return a path containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # modify the BFS code

        # make a queue
        queue = Queue()

        # make a set for visited
        visited = set()

        # enqueue a path to the starting_vertex
        # ['5']
        queue.enqueue([player.current_room.id])

        # while the queue isn't empty:
        while queue.size() > 0:
            # dequeue the next path
            current_path = queue.dequeue()
            # last room (node) is the last thing in the path
            last_room = current_path[-1]

            # instead of searching for a target vertext, search for exit '?'
            # If an exit has been explored, you can put it in your BFS queue like normal.

            if last_room not in visited:
                visited.add(last_room)

                for exit in visited_rooms[last_room]:
                    if visited_rooms[last_room][exit_direction] == '?':
                        return current_path
                    # if it's not a ? but a direction, it has been explored
                    # so add to the queue as normal
                    else:
                        # copy path
                        copy = list(current_path)
                        # BFS will return the path as a list of room IDs.
                        # You will need to convert this to a list of n/s/e/w
                        # directions before you can add it to your traversal path.
                        copy.append(visited_rooms[last_room][exit])
                        queue.enqueue(copy)
            return path

# path already travelled
traversal_path = []

# reverse directions
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# visited rooms
visited_rooms = {}

# start exploring
## keep exploring if number of rooms > num of rooms visited so far
while len(visited_rooms) < len(room_graph):

    # if current room has not been added to dict
    if player.current_room.id not in visited_rooms:
        ## add new room to dict and exits
        # {
        #  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
        #  5: {'n': 0, 's': '?', 'e': '?'}
        # }
        # make sub-dict within visited
        visited_rooms[player.current_room.id] = {}
        for exit in player.current_room.get_exits():
            visited_rooms[player.current_room.id][exit] = '?'

    more_exits = []
    # start exploring the new exits
    for unvisited in visited_rooms[player.current_room.id]:
        if visited_rooms[player.current_room.id][unvisited] == '?':
            # ['n', 's']
            more_exits.append(unvisited)

    # case 1: When you reach a dead-end (i.e. a room with no unexplored paths),
    # walk back to the nearest room that does contain an unexplored path.
    # You can find the path to the shortest unexplored room by using BFS
    # for a room with a `'?'` for an exit.
    if len(more_exits) == 0:
        path = bfs(visited_rooms)
    # as you make your way back, you need to track the directions by appending
    # to traversal_path



    # case 2: pick a random exit from more_exits
    else:
        next_exit = random.choice(more_exits)
        traversal_path.append(next_exit)





player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
