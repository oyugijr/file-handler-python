# File Read & Write 🖋️  

This Python script reads a file, modifies its content, and writes the modified version to a new file. It also includes error handling to manage cases where the file doesn't exist or can't be read.  

## Features  
- Reads a user-specified text file.  
- Converts the content to uppercase (modification step).  
- Writes the modified content to a new file prefixed with `modified_`.  
- Handles errors gracefully, such as file not found or permission issues.  

## How to Use  
1. Run the script:  
   ```bash
   python file_modifier.py
   ```
2. Enter the filename when prompted.  
3. If the file exists, a modified version will be created with a `modified_` prefix.  
4. If the file is missing or unreadable, the script will display an error message.  

## Example  
### Original File (`example.txt`)  
```
Hello, world!
Python is great.
```
### After Running the Script  
Creates `modified_example.txt`:  
```
HELLO, WORLD!
PYTHON IS GREAT.
```

## Error Handling  
- If the file doesn't exist:  
  ```
  Error: File not found. Please check the filename and try again.
  ```
- If the file is unreadable:  
  ```
  Error: Unable to read the file. Check permissions or file format.
  ```

## Requirements  
- Python 3.x  

## License  
This project is open-source under the MIT License.
