import os, json
from editdistance import edit_distance
from subprocess import run
path = os.path

cmd_strings = {}

def prepare_strings():
    global cmd_strings

    for script_folder in os.listdir('./scripts'):
        folder = path.join('scripts', script_folder)

        with open(path.join(folder, 'config.json'), 'r') as config_file:
            config = json.load(config_file)
            for command_string in config['command_strings']:
                cmd_strings[command_string] = config['controller_program'] + ' ' + path.join(folder, config['run_program'])


def process(command):

    highest_command = None
    lowest_dis = None
    for cmd_string in cmd_strings:
        if lowest_dis == None:
            lowest_dis = edit_distance(command, cmd_string)
            highest_command = cmd_string
            continue

        dis = edit_distance(command, cmd_string)
        if dis < lowest_dis:
            highest_command = cmd_string
            lowest_dis = dis
    print(cmd_strings[highest_command])
    completed_process = run(cmd_strings[highest_command], universal_newlines=True, shell=True)
    print(completed_process.stdout)



if __name__ == '__main__':

    command = input()
    prepare_strings()
    process(command)
