# PHP commented function param example value remover

This repository helps to remove the commented example function param values in the repository.

example PR output of this repo: https://github.com/GoogleCloudPlatform/php-docs-samples/pull/1715

# How to use this script

Run `python function_param_example_comment_remover.py path_to_directory`
where `path_to_directory` is the path to the php files' directory

# Requirements
The `python3` script expects proper `@param` comments for all the variables in the function signature.

eg:
```
 /*
 * @param string $projectId The ID of your Google Cloud Platform project.
 * @param string $accessId Access ID for an inactive HMAC key.
 */
function foo($projectId, $accessId)
{
    // $projectId = 'my-project-id';
    // $accessId = 'GOOG0234230X00';

```

# Input and Output example

```
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
```


**Feel free to raise any issues/suggestions in the repository**
