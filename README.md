# WinRAR Password Import/Export Tool

A utility tool for backing up and restoring WinRAR saved passwords. Supports exporting and importing WinRAR password registry entries, making it convenient to restore passwords after system reinstallation or on different computers.

## Features

- **Export Passwords**: Export WinRAR saved passwords as registry files
- **Import Passwords**: Restore WinRAR passwords from backup files
- **Automatic Permission Management**: Automatically detects and requests administrator privileges
- **Cross-Platform Support**: Provides Python scripts and packaged Windows executables
- **Security Warnings**: Detailed explanation of password encryption mechanisms and usage limitations

## System Requirements

- Windows operating system
- Python 3.6+ (if using Python script)
- Administrator privileges (for registry access)

## Quick Start

### Method 1: Using Executable File (Recommended)

1. Download `WinRAR_Password_Manager.exe` from [Releases](https://github.com/EricDasha/WinRAR-PassWord-import-and-export/releases)
2. Double-click to run (administrator privileges required on first run)
3. Follow the menu prompts

### Method 2: Using Python Script

1. Ensure Python 3.6+ is installed
2. Download `WinRAR_Password_Manager.py`
3. Run the script:
   ```bash
   python WinRAR_Password_Manager.py
   ```

## Usage

### Export Passwords

1. Run the program and select option `1`
2. The program will automatically export WinRAR passwords to `WinRAR_Passwords.reg` file
3. Keep this file safe (contains encrypted password data)

### Import Passwords

1. Ensure `WinRAR_Passwords.reg` file is in the same directory
2. Run the program and select option `2`
3. Confirm the import operation
4. Open WinRAR to test if passwords are working

## Important Notes

### Password Encryption Mechanism

WinRAR passwords are **encrypted** and the encryption is related to Windows user accounts:

- **Can be used**: Same computer with the same user account
- **May not work**: Different user accounts or different computers

### Usage Scenarios

- **Supported**: Backup current user's WinRAR passwords
- **Supported**: Restore passwords after system reinstallation (same user account)
- **Not supported**: Migrate passwords across computers (different encryption keys)

### Security Recommendations

- Backup files contain encrypted password data, keep them safe
- Do not share backup files with others
- Test passwords after import to ensure they work

## Building from Source

### Automatic Build (Recommended)

Windows users can directly run:
```bash
build.bat
```

### Manual Build

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build executable:
   ```bash
   pyinstaller --onefile --console --name WinRAR_Password_Manager WinRAR_Password_Manager.py
   ```

3. The executable will be located at `dist\WinRAR_Password_Manager.exe`

For detailed instructions, see [README_BUILD.md](README_BUILD.md)

## Project Structure

```
.
├── WinRAR_Password_Manager.py    # Python main program
├── build_exe.py                  # Build script
├── build.bat                     # Windows one-click build script
├── README.md                     # Project documentation (this file)
├── README_BUILD.md               # Build instructions
└── LICENSE                       # MIT License
```

## Tech Stack

- **Python 3.6+**
- **PyInstaller** (for packaging)
- **Windows Registry API** (via reg.exe)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Issues and Pull Requests are welcome!

## FAQ

### Q: Passwords don't work after import?

A: This is usually because the encryption keys don't match. WinRAR password encryption is related to user accounts, and will only work under the same user account.

### Q: Packaged exe is flagged by antivirus?

A: This is a common false positive with PyInstaller packaged files. You can add it to whitelist or run from source.

### Q: Does it support passwords from other compression software?

A: Currently only WinRAR is supported. Other software (such as 7-Zip, WinZip) use different password storage methods.

## Contact

For questions or suggestions, please submit an [Issue](https://github.com/EricDasha/WinRAR-PassWord-import-and-export/issues).

---

If this project is helpful to you, please give it a Star!
