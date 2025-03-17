import os
import shutil
import re

def organize_ibdp_papers(root_dir, target_subjects):
    """
    Organizes IBDP past papers by subject, filtering and moving specified subjects.

    Args:
        root_dir (str): The root directory containing the year folders.
        target_subjects (list): A list of subject names to keep.
    """

    for year in os.listdir(root_dir):
        year_path = os.path.join(root_dir, year)

        if not os.path.isdir(year_path):
            continue

        for session in os.listdir(year_path):
            session_path = os.path.join(year_path, session)
            if not os.path.isdir(session_path):
                continue

            for group in os.listdir(session_path):
                group_path = os.path.join(session_path, group)
                if not os.path.isdir(group_path):
                    continue

                for filename in os.listdir(group_path):
                    filepath = os.path.join(group_path, filename)
                    print(filepath)
                    if not os.path.isfile(filepath):
                        continue

                    if not search(filename.lower(), subjects_to_keep):
                        os.remove(filepath)

                #Remove empty group folders.
                if not os.listdir(group_path):
                    os.rmdir(group_path)
                    print(f"Removed empty directory: {group_path}")
            #Remove empty session folders.
            if not os.listdir(session_path):
                os.rmdir(session_path)
                print(f"Removed empty directory: {session_path}")
        #Remove empty year folders.
        if not os.listdir(year_path):
            os.rmdir(year_path)
            print(f"Removed empty directory: {year_path}")

def search(name, subjectsArray):
    for subject in subjectsArray:
        res = re.search(subject, name)
        if res:
            return True
        
    return False

root_directory = "~/Insert/Path/here"  # Replace with the actual path

# Replace with subjects you want to keep
subjects_to_keep = [
    r"^english\_a\_.*",
    r"^french\_b.*",
    r"^computer\_science(?!.*(french|spanish|german)).*",
    r"^physics(?!.*(french|spanish|german)).*",
    r"^chemistry(?!.*(french|spanish|german)).*",
    r"^mathematics_analysis_and_approaches(?!.*(french|spanish|german)).*",
    r"^math(?!.*(french|spanish|german)).*",
]

if __name__ == "__main__":
    organize_ibdp_papers(root_directory, subjects_to_keep)
