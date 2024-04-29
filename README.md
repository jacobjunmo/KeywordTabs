# KeywordTabs

## Overview
I wrote this code to help my friend who is working in the PR industry. She often needs to monitor news coverage for specific keywords across multiple news websites. KeywordTabs automates this process by allowing users to search for keywords across a list of news websites and open the search results in chronological order in a web browser tab.

## Requirements
- Python environment for Windows
- `chromedriver.exe` in the same folder as the code
- Two text files in the same folder as the code:
  - `oneDepth.txt`: Contains a list of one-depth news websites and target elements
  - `twoDepth.txt`: Contains a list of two-depth news websites and target elements

## Usage
1. Ensure that the `chromedriver.exe` file is located in the same directory as the Python code.
2. Place the text files (`oneDepth.txt` and `twoDepth.txt`) containing the list of news websites in the same directory as the Python code.
3. Execute the Python script.
4. The application will prompt the user to enter a keyword in the UI.
5. Once a keyword is entered, KeywordTabs will open a web browser tab and search for the keyword across the specified news websites in chronological order.

## Note
Note that the code may not work with all websites, as it depends on the structure and accessibility of the web pages.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
