import sys
import reader

if __name__ == '__main__':
    replay_path = sys.argv[1]
    new_file_name = sys.argv[2] if len(sys.argv) >= 3 else sys.argv[1].replace('.SC2Replay', '.json')

    replay = reader.Sc2Replay(replay_path)
    productions = replay.parse_player_productions(True)
    with open(new_file_name, 'w') as file:
        file.write(productions)
