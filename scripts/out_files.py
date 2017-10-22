from util import scan_files


def main():
    print('## Files')
    for _, file_name in scan_files():
        part_name = file_name.rpartition('.')[0]
        print(f"### {part_name}")
        print(f"File: `res/{file_name}`", end='\n\n')
        print(f"Sender: <N/A>", end='\n\n')
        print(f"Update object with {part_name} field.", end='\n\n')


if __name__ == '__main__':
    main()
