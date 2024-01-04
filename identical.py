def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            # Check if the files are identical
            if lines1 == lines2:
                print("The files are identical.")
            else:
                print("The files differ. Corresponding lines:")
                for line_num, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
                    if line1 != line2:
                        print(f"Line {line_num}:")
                        print(f"File 1: {line1.strip()}")
                        print(f"File 2: {line2.strip()}")
                        print()
    except FileNotFoundError:
        print("Error: One or more files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file1_path = 'programing.txt'
file2_path = 'test.txt'
compare_files(file1_path, file2_path)
