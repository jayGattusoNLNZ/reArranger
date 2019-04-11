import os
import sys

descriptor = """This is a tool that creates a replca of a given file structure in a new location. All the files are empty/zero copies. It is a useful and fast way of making a very portable copy of a file system to help arrangement planning and other analysis"""


def main(argv=None):

	if argv:
		source_root = argv[0]
		output_folder = argv[1]
		file_list_file = argv[2]
	else:	
    ### edit here for text file file listing
    ### assumes / expects newline delimited utf-8 encoded
    ### 
		source_root = r"c:"
		output_folder = "junk"
		file_list_file = "my_file_list.txt"

	file_list = []

	folder_counter = 0
	files_counter = 0

	with open(file_list_file, encoding="utf8" ) as data:
		my_files = data.read().split("\n")
  
	for my_file in my_files:
		my_file_path, my_file_name = my_file.rsplit(os.sep, 1)
		new_file_path = my_file.replace(source_root, output_folder)
		folder_counter += 1
		try:
			os.makedirs(new_s)
		except FileExistsError:
			pass
		new_f = os.path.join(new_file_path, my_file_name)
		with open(new_f, 'wb') as data:
			files_counter +=1


print (f'Copying from "{input_folder}"')
print (f'To "{output_folder}"')
print (f"Made {folder_counter} folders ")
print (f"Made {files_counter} folders ")


if __name__ == '__main__':
	main(sys.argv[1:])
