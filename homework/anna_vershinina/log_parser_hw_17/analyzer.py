import argparse
from pathlib import Path


def args_set():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The path for program execution')
    parser.add_argument('-t', '--text', required=True,
                        help='Indicate the text to pass to the program')
    parser.add_argument('-m', '--mode',
                        choices=['all', 'first'], default='all',
                        help='Choose "all" to show all matches or or '
                             '"first" to show the first match'
                        )

    return parser.parse_args()


def search_logs(path, text, mode):
    search_dir = Path(path)

    log_files = list(search_dir.glob("*.log"))
    for file in log_files:
        with file.open('r') as f:
            for line_num, line in enumerate(f, start=1):
                if text in line:
                    words_list = line.strip().split()
                    output_line = line.strip()

                    index = None
                    for i, word in enumerate(words_list):
                        if text.lower() in word.lower():
                            index = i
                            break

                    if index is not None:
                        start = max(0, index - 5)
                        end = min(len(words_list), index + 6)
                        output_line = ' '.join(words_list[start:end])

                    print(
                        f'The searched text "{text}" found in file '
                        f'"{file.name}" on line {line_num}:'
                    )
                    print(f'"{output_line}"')

                    if mode == 'first':
                        print(
                            'Note: Only the first search result is shown '
                            'as the argument first was passed.'
                        )
                        return


def main():
    args = args_set()
    search_logs(args.path, args.text, args.mode)


if __name__ == "__main__":
    main()
