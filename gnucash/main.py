import json
import os


def get_dir():
    """ get this file's directory """
    return os.path.dirname(os.path.realpath(__file__))


def read(file):
    """ Load JSON data from file """
    with open(get_dir() + file) as in_file:
        return json.load(in_file)


def clean(acc):
    """ Eliminate unnecessary properties """
    new = {
        "id": acc['id'],
        "name": acc['name'],
        "account_type": acc['account_type'].title(),
    }

    if not acc['is_group']:
        new["account_number"] = acc['account_number']
    else:
        new['is_group'] = 1

    if acc['description']:
        new['description'] = acc['description']

    return new


def walk(acc, skr):
    """ Recursively walk tree and add children """
    children = get_children(acc['id'], skr)
    if children:
        acc['children'] = children
        for child in acc['children']:
            walk(child, skr)
    return acc


def get_children(acc_id, skr):
    """ Return all child accounts for a given ID """
    return [clean(acc) for acc in skr if acc['parent'] == acc_id]


def write(file, data):
    """ Write JSON data to file """
    with open(get_dir() + file, 'w') as out_file:
        json.dump(data, out_file, indent=4)


def main():
    skr = read('/gnucash_skr04_array.json')
    root = clean(skr[0])
    tree = walk(root, skr)
    write('/gnucash_skr04_nested.json', tree)


if __name__ == '__main__':
    main()
