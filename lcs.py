import argparse

def search_string_in_file(file_name, search_string):
    encodings_to_try = ['utf-8', 'latin-1', 'iso-8859-1', 'windows-1252']

    for encoding in encodings_to_try:
        try:
            with open(file_name, 'r', encoding=encoding, errors='replace') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_string in line:
                        print(f"{line.strip()}")
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            break
        except Exception as e:
            print(f"Error with encoding '{encoding}': {e}")
            continue
        else:
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a string in a file.")
    parser.add_argument("-f", "--file", required=True, help="File to read")
    parser.add_argument("-s", "--string", required=True, help="String to search")
    args = parser.parse_args()

    search_string_in_file(args.file, args.string)
