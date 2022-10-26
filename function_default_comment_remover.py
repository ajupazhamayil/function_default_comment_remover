'''
Input:
 * @param string $projectId The ID of your Google Cloud Platform project.
 * @param string $accessId Access ID for an inactive HMAC key.
 */
function foo($projectId, $accessId)
{
    // $projectId = 'my-project-id';
    // $accessId = 'GOOG0234230X00';

    $storage = new StorageClient();

Output:
 * @param string $projectId The ID of your Google Cloud Platform project.
 * @param string $accessId Access ID for an inactive HMAC key.
 */
function foo($projectId, $accessId)
{

    $storage = new StorageClient();
'''

import sys
import os
import fileinput

number_of_file_changed = 0


def get_file_paths(path):
    php_files = []
    # Get all the file names ends with php
    for file in os.listdir(path):
        if file.endswith('.php'):
            php_files.append(os.path.join(path, file))
    return php_files


def process_file(path):
    global number_of_file_changed
    param_start = '@param '
    args = []
    comment = '// '
    equal_symbol = ' = '
    file_changed = 0

    for line in fileinput.input(path, inplace=1):
        if param_start in line:
            # example for param in comment:
            # * @param string $bucketName The name of your Cloud Storage bucket.
            param = line.split(param_start)[1].split(' ')[0:2]
            # expect '// $bucketName' in the line
            args.append(comment + param[1])
        # line to be removed looks like this '// $bucketName = '
        if not line.strip().split(equal_symbol)[0] in args:
            if file_changed == 1:
                number_of_file_changed += 1
                file_changed = 2
                # skip the empty line just below the arg default comment
                continue
            sys.stdout.write(line)
        elif file_changed == 0:
            file_changed = 1


# Run like python filename.py path_to_php_file_directory
if __name__ == "__main__":
    file_paths = get_file_paths(sys.argv[1])
    print("Started processing the following files: \n", file_paths)
    print("Number of files is : \n", len(file_paths))
    for file in file_paths:
        process_file(file)
        print("Completed processing ", file, end="\n")
    print("Total number of files changed = " + str(number_of_file_changed))
