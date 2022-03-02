def get_puzzle_input(file_name: str, return_type: type = str):
    data = []
    try:
        with open(f"inputs/{file_name}", "r") as file:
            if return_type != str:
                for line in file:
                    data.append(return_type(line.rstrip("\n")))
            else:
                for line in file:
                    data.append(line.rstrip("\n"))
    except IOError:
        print("input file not found")

    return data
