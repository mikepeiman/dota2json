import vpk
import os

vpk_file_path = "C:/webdev/dota2json/vpk/pak01_dir.vpk"
output_folder = "C:/webdev/dota2json/json"

# Specify the path of the file you want to extract within the VPK
file_to_extract = "scripts/npc/npc_heroes.txt"

# Read VPK
# archive = vpk.open(vpk_file_path)
archive = vpk.open("C:/webdev/dota2json/vpk/pak01_dir.vpk")

# Get the specific file
# pakfile = archive.get_file(file_to_extract)
# pakfile = archive.get_file("scripts/npc/npc_heroes.txt")
pakfile = archive["scripts/npc/npc_heroes.txt"]
pakfile.save("{output_folder}/npc_heroes.txt")

if pakfile:
    file_content = pakfile.read()

    # Save the content to the output folder without additional subfolders
    output_file_name = os.path.basename(file_to_extract)
    output_file_path = f"{output_folder}/{output_file_name}"

    with open(output_file_path, "wb") as output_file:
        output_file.write(file_content)

    print(f"File '{file_to_extract}' has been extracted to '{output_file_path}'.")
else:
    print(f"File '{file_to_extract}' not found in the VPK archive.")
