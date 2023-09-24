def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


def hello_command(args, contacts):
    return 'How can I help you?'


def exit_command(args, contacts):
    return 'Good bye!'


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(args, contacts):
    if not args:
        return 'You need to type username'
    else:
        if len(args) == 1:
            return 'You need to type phone number'
        name, phone = args
        if name and name in contacts.keys():
            contacts[name] = phone
            return 'Contact added.'


def get_all(args, contacts):
    return contacts


def get_phone(args, contacts):
    name = args
    if name:
        return contacts[name[0]]
    return 'You need to point out username, please!'


def unknown_command(args, contacts):
    return 'Unknown command'


COMMAND_HANDLER = {
    hello_command: ['hello', 'hi', 'привет'],
    exit_command: ['exit', 'bye', 'close'],
    add_contact: ['add', '+', 'добавить'],
    change_contact: ['change', 'поменять'],
    get_phone: ['phone', 'телефон'],
    get_all: ['all', 'все', 'всё']
}


def parser(user_input: str):
    for cmd, words in COMMAND_HANDLER.items():
        for word in words:
            if user_input.startswith(word):
                return cmd, user_input[len(word):].split()
    return unknown_command, []


def main():
    print('Welcome to the assistant bot!')

    contacts = {}
    while True:
        user_input = input('Enter a command: ')
        cmd, data = parser(user_input)
        print(cmd(data, contacts))
        if cmd == exit_command:
            break


if __name__ == '__main__':
    main()