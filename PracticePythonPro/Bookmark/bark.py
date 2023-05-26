import commands
import os
from collections import OrderedDict


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)

    def __str__(self):
        return self.name


def print_options(options):
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choose_option = input("choose an option\n> ")
    while not option_choice_is_valid(choose_option, options):
        print("Invalid choice")
        choose_option = input("choose an option\n> ")
    return options[choose_option.upper()]


def get_user_input(label, required=True):
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_new_bookmark_data():
    return {
        "TITLE": get_user_input("Title"),
        "URL": get_user_input("URL"),
        "NOTES": get_user_input("Notes", required=False),
    }


def get_bookmark_id_for_deletion():  # <6>
    return get_user_input('Enter a bookmark ID to delete')


def clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    print(f"GET OS NAME: {os.name}")
    os.system(clear)


def get_github_import_options():
    return {
        "github_username": get_user_input("Github username"),
        "preserve_timestamps": get_user_input(
            "Preserve timestamps [Y/n]",
            required=False
        ) in {"Y", "y", None},
    }


def get_new_bookmark_info():
    bookmark_id = get_user_input("Enter a bookmark ID to edit")
    field = get_user_input("Choose a value to edit (title, URL, notes)")
    new_value = get_user_input(f"Enter the new value for {field}")
    return {
        "ID": bookmark_id,
        "update": {field: new_value},
    }


def loop():
    clear_screen()

    options = OrderedDict({
        'A': Option('Add a bookmark', commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
        'B': Option('List bookmarks by date', commands.ListBookmarksCommand()),
        'T': Option('List bookmarks by title', commands.ListBookmarksCommand(order_by='title')),
        "E": Option("Edit a bookmark", commands.EditBookmarkCommand(), prep_call=get_new_bookmark_info),
        'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
        "G": Option("Import Github stars", commands.ImportGitHubStarsCommand(), prep_call=get_github_import_options),
        'Q': Option('Quit', commands.QuitCommand()),
    })
    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input('Press ENTER to return to menu')


if __name__ == "__main__":
    commands.CreateBookmarksTableCommand().execute()

    while True:
        loop()
