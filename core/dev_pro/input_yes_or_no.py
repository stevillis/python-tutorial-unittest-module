"""Gets user input methods"""


def get_answer_yes_or_no():
    """Get user input 'yes' or 'no'"""
    user_input = ''
    while user_input not in {'yes', 'no'}:
        user_input = input('Type "yes" or "no": ').lower()
    return user_input


def execute():
    """Execute the module until user types 'yes'"""
    while True:
        print('Do you want to stop program execution?')
        user_input = get_answer_yes_or_no()
        if user_input == 'yes':
            break


if __name__ == '__main__':
    execute()
    print('Program execution stopped.')
