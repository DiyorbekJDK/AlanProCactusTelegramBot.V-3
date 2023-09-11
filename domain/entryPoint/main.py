from pathlib import Path
import sys

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from domain.mainCode.all_code import allCode


##############################
# Entry point of python code #
##############################

def main():
    print("Bot started")
    allCode()


if __name__ == '__main__':
    main()
