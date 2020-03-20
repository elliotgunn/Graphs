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


# path already travelled
traversal_path = []

# reverse directions
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# visited
visited = {}

# start exploring
## keep exploring if number of rooms > num of rooms visited so far
while len(visited) < len(room_graph):

    # if current room has not been added to dict
    if player.current_room.id not in visited:
        ## add new room to dict and exits
        # {
        #  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
        #  5: {'n': 0, 's': '?', 'e': '?'}
        # }
        # make sub-dict within visited
        visited[player.current_room.id] = {}
        for exit in player.current_room.get_exits():
            visited[player.current_room.id][exit] = '?'

    more_exits = []
    # start exploring the new exits
    for unvisited in visited[player.current_room.id]:
        if visited[player.current_room.id][unvisited] == '?':
            # ['n', 's']
            more_exits.append(unvisited)

    # case 1: When you reach a dead-end (i.e. a room with no unexplored paths),
    # walk back to the nearest room that does contain an unexplored path.
    # You can find the path to the shortest unexplored room by using BFS
    # for a room with a `'?'` for an exit.




    # case 2:

















# TRAVERSAL TEST
visited_rooms = set()
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
