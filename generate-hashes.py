import hashlib
import argparse

def generate_md5_hash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def main(input_file):
    try:
        with open(input_file, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return

    for password in passwords:
        password = password.strip()  # Remove leading/trailing whitespace
        md5_hash = generate_md5_hash(password)
        print(f"{md5_hash}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate MD5 hashes for passwords in a file.")
    parser.add_argument("input_file", help="Path to the password file")
    args = parser.parse_args()
    main(args.input_file)

