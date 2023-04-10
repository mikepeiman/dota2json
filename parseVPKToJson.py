import os
import shutil
import subprocess

# Set the path to the VPK file and the output folder
# vpk_file = "C:/Program Files (x86)/Steam/steamapps/common/dota 2 beta/game/dota/pak01_dir.vpk"
vpk_file = "C:/webdev/dota2json/vpk/pak01_dir.vpk"
vpk_file2 = "C:\\webdev\\dota2json\\vpk\\pak01_dir.vpk"
vpk_file3 = "C:\webdev\dota2json\\vpk\pak01_dir.vpk"
vpk_file4 = "C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\pak01_dir.vpk"
output_folder = "C:/webdev/dota2json/json"
output_folder2 = "C:\\webdev\\dota2json\\json"
output_folder3 = "C:\webdev\dota2json\json"

# command = 'gcfscape "{}" "{}"'.format(vpk_file, output_folder)
# result = subprocess.run(command, shell=True, text=True, capture_output=True)

# if result.returncode != 0:
#     print("Error:", result.stderr)
# else:
#     print("Success:", result.stdout)


# # source file path
# source = "C:/Program Files (x86)/Steam/steamapps/common/dota 2 beta/game/dota/pak01_dir.vpk"

# # destination file path
# destination = "C:/webdev/dota2json/vpk/pak01_dir.vpk"

# # copy the file
# shutil.copyfile(source, destination)

# verify the file was copied by printing a message
# print(f"File {source} was successfully copied to {destination}")
# print(f"File to open with GCFScape from location {vpk_file} to location {output_folder}")
# print(f"File to open with GCFScape from location {vpk_file} to location {output_folder}")
# print(f"File to open with GCFScape from location {vpk_file3} to location {output_folder3}")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Use GCFScape to extract the hero data files
# print('{vpk_file} {output_folder}')
# print('gcfscape -e "{}" "{}"'.format(vpk_file4, output_folder))
os.system('gcfscape "{}" "{}"'.format(vpk_file, output_folder))
# os.system('gcfscape -e "{}" "{}"'.format(vpk_file2, output_folder2))
# os.system('gcfscape -e "{}" "{}"'.format(vpk_file3, output_folder3))

# Rename the extracted files to have a .txt extension
for filename in os.listdir(output_folder):
    if not filename.endswith(".txt"):
        new_filename = os.path.splitext(filename)[0] + ".txt"
        os.rename(os.path.join(output_folder, filename), os.path.join(output_folder, new_filename))

print("Hero data extraction complete!")

