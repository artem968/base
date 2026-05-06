import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some strings or files.")

    # 'nargs="?"' makes the positional argument optional
    # 'default=None' allows us to check if the user provided it
    parser.add_argument("input_string", nargs="?", default="default_string", 
                        help="The default positional string")

    parser.add_argument("--file", type=str, 
                        help="A file path that overrides the default string")

    args = parser.parse_args()

    # Priority Logic: Use --file if provided, otherwise use the positional/default
    final_value = args.file if args.file else args.input_string

    print(f"Final value being used: {final_value}")

if __name__ == "__main__":
    main()
