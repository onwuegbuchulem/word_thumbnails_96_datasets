import os
import random
import shutil

def split_and_save_data(input_folder, test_size=0.2, random_seed=42):
    # List all files in the input folder
    files = os.listdir(input_folder)
    
    # Set a seed for reproducibility
    random.seed(random_seed)

    # Shuffle the list of files
    random.shuffle(files)

    # Calculate the number of files for the test set
    num_test_files = int(test_size * len(files))

    # Split the files into train and test sets
    train_files = files[num_test_files:]
    test_files = files[:num_test_files]

    # Create output folders if they don't exist
    output_train_folder = "output_train"
    output_test_folder = "output_test"

    os.makedirs(output_train_folder, exist_ok=True)
    os.makedirs(output_test_folder, exist_ok=True)

    # Move files to the corresponding folders
    for file in train_files:
        source_path = os.path.join(input_folder, file)
        dest_path = os.path.join(output_train_folder, file)
        shutil.copy(source_path, dest_path)

    for file in test_files:
        source_path = os.path.join(input_folder, file)
        dest_path = os.path.join(output_test_folder, file)
        shutil.copy(source_path, dest_path)

    return output_train_folder, output_test_folder

if __name__ == "__main__":
    input_folder = "CenturyGothic"  # Replace with the path to your data folder

    output_train_folder, output_test_folder = split_and_save_data(input_folder)

    print(f"Train data saved to: {output_train_folder}")
    print(f"Test data saved to: {output_test_folder}")
