#   Subject:Character Encodings
#   Homework: Write a program that expects as arguments any number of pathname of UTF-8 encoded files, and indicates
#   the mean number of bytes per character in the content of each one.
import sys


def avg_byte_per_ch(path):
    try:
        with open(path, 'rb') as file:
            data = file.read()
            num_bytes = len(data)
            num_chars = len(data.decode('utf-8'))
            avg_bytes_per_ch = num_bytes / num_chars
            return avg_bytes_per_ch
    except FileNotFoundError:
        print(f"Error:File couldn't be found at: {path}")
        return None
    except Exception as e:
        print(f"Error: {e} at the following: {path} ")
        return None


if len(sys.argv) < 2:
    print("Please pass the arguments as following: python3 main.py file1 file2 ...")
    sys.exit(1)

file_paths = sys.argv[1:]
for file_path in file_paths:
    mean_bytes = avg_byte_per_ch(file_path)
    if mean_bytes is not None:
        print(f"Mean bytes per character in the following path {file_path} is: {mean_bytes:.3f}")
