import yaml
import argparse


# generates students list
def generate(args):
    # collect students info from members file
    data = {}
    with open(args.members, 'r', encoding='latin-1') as f:
        # id, lastname, name, email, rol
        first = True
        for line in f:
            # ignore first line
            if first:
                first = False
                continue
            # strip whitespace
            line = line.strip()
            # ignore blank lines
            if line == '':
                continue
            line = line.split(',')
            rol = line[-1].strip('"').lower()
            line = line[:-1]
            # only students
            if (rol == 'alumno'):
                id, lastname, name, email = line
                id = id.strip('"')
                email = email.strip('"')
                data[id] = email
    # save output file
    with open(args.output, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Students List Generator')
    parser.add_argument('--members', '-m', type=str, help='members.csv file from GES', required=True)
    parser.add_argument('--output', '-o', type=str, help='output yaml file', default='out.yml')
    args = parser.parse_args()
    generate(args)
