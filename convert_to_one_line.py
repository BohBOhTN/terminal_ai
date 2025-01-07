import sys

def convert_to_single_line(input_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            single_line_content = content.replace('\n', ' ').replace('\r', '')
            print(single_line_content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file.txt>")
    else:
        input_file = sys.argv[1]
        convert_to_single_line(input_file)
