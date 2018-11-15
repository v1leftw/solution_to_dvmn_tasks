import robot_api
import re


def run_robot(commands, room_map):
    command_deltas = {
        'DOWN': (1, 0),
        'LEFT': (0, -1),
        'UP': (-1, 0),
        'RIGHT': (0, 1),
    }
    print(type(commands))
    current_position = robot_api.get_robot_position()
    movement_history = [current_position]
    for command in commands:
        delta = command_deltas[command]
        new_position = (
            current_position[0] + delta[0], current_position[1] + delta[1]
        )
        if is_wall(new_position, room_map):
            continue
        movement_history.append(new_position)
        robot_api.send_delta_to_engine(delta)
        current_position = new_position
    return movement_history


def is_wall(position, ascii_map):
    map_array = turn_ascii_map_into_array(ascii_map)
    return map_array[position[0]][position[1]] == '|'


def print_map(movement_history, room_map):
    if not movement_history:
        print(room_map)
        return
    footprint_positions = movement_history[:-1]
    robot_position = movement_history[-1]
    map_with_footprints = get_map_with_footprints(
        footprint_positions,
        room_map
    )
    map_with_footprints_and_robot = get_map_with_robot(
        robot_position,
        map_with_footprints
    )
    print(map_with_footprints_and_robot)


def get_map_with_footprints(movement_history, room_map):
    footprint_mark = '·'
    return add_symbol_to_ascii_map(
        ascii_map=room_map,
        symbol=footprint_mark,
        points=movement_history
    )


def get_map_with_robot(robot_position, room_map):
    robot_mark = '◆'
    return add_symbol_to_ascii_map(
        ascii_map=room_map,
        symbol=robot_mark,
        points=[robot_position]
    )


def add_symbol_to_ascii_map(ascii_map, symbol, points):
    map_array = turn_ascii_map_into_array(ascii_map)
    for point_x, point_y in points:
        map_array[point_x][point_y] = symbol
    return turn_array_into_ascii_map(map_array)


def turn_ascii_map_into_array(ascii_map):
    return [
        list(map_line)
        for map_line in ascii_map.split('\n') if map_line.strip()]


def turn_array_into_ascii_map(map_array):
    return '\n'.join([''.join(map_line) for map_line in map_array])


# robot programs. Contains movement dictionaries for robot
# _______________________________

go_to_new_room = [
    'RIGHT'
]

room_one = [
    *[*['DOWN'] * 4, 'RIGHT', *['UP'] * 4, 'RIGHT', ] * 2
]

room_two = [
    *['DOWN'] * 4,
    'RIGHT',
    *['UP'] * 4,
    'RIGHT',
    *['DOWN'] * 4,
    'RIGHT',
]

room_three = [
    *['RIGHT', 'UP', 'LEFT', 'UP'] * 2, *['RIGHT'] * 2
]

room_four = [
    *['DOWN'] * 4,
]

room_five = [
    'RIGHT',
    *['UP'] * 4,
    'RIGHT',
    *['DOWN'] * 4,
    'RIGHT',
    *['UP'] * 4,
]


# _____________________________


def normalize_map(_map):
    """cause ' ' == '|' (width equal), but '█' != ' ' (width not equal)
     so map outputs in broken format (for user's view).
    In this function we fix that"""
    return re.sub(r'█', '|', _map)


def clean_all_rooms():
    all_rooms_movement = [
        *room_one,
        *go_to_new_room,
        *room_two,
        *go_to_new_room,
        *room_three,
        *go_to_new_room,
        *room_four,
        *go_to_new_room,
        *room_five
    ]
    return all_rooms_movement


if __name__ == '__main__':
    room = robot_api.get_room_map()
    robot_movement_history = run_robot(
        commands=clean_all_rooms(),
        room_map=room)
    print_map(robot_movement_history, normalize_map(room))
