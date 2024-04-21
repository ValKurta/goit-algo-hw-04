import sys
from pathlib import Path
from colorama import Fore, Back, Style

def dir_content(dir, limit=10):
    """
    The content of a directory with colored output view.
    """
    path = Path(dir)
    print("📦" + path.name)
    inner_dir_content(path, "", Fore.BLACK, limit)

def inner_dir_content(dir, prefix, color, limit):
    limit = limit - 1
    folder_color = Fore.YELLOW  # Color for folders
    file_color = Fore.GREEN  # Color for files

    if limit == 0:
        print(Fore.RED + "(recursion limit reached)" + Style.RESET_ALL)
        return
    
    for item in dir.iterdir():
        if item.is_dir() and item.name != ".git":
            print(folder_color + prefix + "┣ 📂" + item.name)
            inner_dir_content(item, prefix + "┃ ", folder_color, limit)

        else:
            print(file_color + prefix + "┗ 📜" + item.name)
    


if __name__ == "__main__":
    try:
        dir = sys.argv[1]
        dir_content(dir)
    except IndexError:
        print(Fore.RED + "Usage: python hw03.py <directory_path> [limit]" + '\n' + Fore.BLACK + Back.GREEN + "The current dir content for instance:" + Style.RESET_ALL)
        dir_content(".")
