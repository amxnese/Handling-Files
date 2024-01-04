def concatenate_files(file1_path, file2_path, output_file_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            # Concatenate the contents of the two files
            concatenated_content = content1 + '\n' + content2

            # Write the concatenated content to a new file
            with open(output_file_path, 'w') as output_file:
                output_file.write(concatenated_content)

            print(f"Files '{file1_path}' and '{file2_path}' have been concatenated and saved to '{output_file_path}'.")
    except FileNotFoundError:
        print(f"Error: One or more files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file1_path = 'programing.txt'
file2_path = 'test.txt'
output_file_path = 'concatenated.txt'
concatenate_files(file1_path, file2_path, output_file_path)
