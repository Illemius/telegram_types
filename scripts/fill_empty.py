from util import scan_files


def main():
    for full_path, _ in scan_files():
        with open(full_path, 'r+') as f:
            if f.read():
                continue
            f.write('{}')


if __name__ == '__main__':
    main()
