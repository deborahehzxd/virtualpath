# VirtualPath

VirtualPath is a Python program designed to repair common issues with the Windows search function, enhancing file and folder searching capabilities on your system.

## Features

- Restarts the Windows Search service to resolve potential issues.
- Rebuilds the Windows Search index to ensure up-to-date file and folder information.
- Verifies critical directories are included in the search path.

## Requirements

- Windows operating system.
- Python 3.x.
- Administrative privileges to run the script.

## Installation

1. Clone this repository or download the `VirtualPath.py` file.
2. Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. Open a command prompt with administrative privileges.
2. Navigate to the directory containing `VirtualPath.py`.
3. Run the script with Python:

    ```bash
    python VirtualPath.py
    ```

4. Follow the on-screen instructions.

## Logging

The script logs its operations to a file named `VirtualPath.log` in the same directory. This log file can be used to diagnose any issues that occur during the script's execution.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.