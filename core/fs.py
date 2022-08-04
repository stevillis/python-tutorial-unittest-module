"""File system module"""

from subprocess import check_output


def print_contents_of_cwd():
    """Prints content from current directory"""
    return check_output('dir', shell=True).split()


if __name__ == '__main__':
    print(print_contents_of_cwd())
