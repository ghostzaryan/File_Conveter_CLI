# Markdown-To-HTML and HTML-To-Markdown Converter
This is CLI tool I designed which will seamlessly convert Markdown files to HTML and vice-versa

## Installation
1) Clone the repository to your local machine:\
`git clone https://github.com/ghostzaryan/File_Conveter_CLI`

2) Navigate to the project directory:\
`cd {directory_name}`

3) Install the required dependancies:\
`pip install -r requirements.txt`


## Usage
### Markdown to HTML Conversion
To use the tool, write the following statement in the terminal:\
`python main.py input.md output.html --direction md2html`


Replace the `input.md` with the input file in Markdown format and `output.html` with the output file where the HTML content is to be stored.

### HTML to Markdown Conversion
The method is similar, except the direction and order of input\
`python main.py input.html output.md --direction html2md`


### Options
There are 2 options available for the `--direction` argument which are:
1) `--direction md2html` for Markdown to HTML Conversion (Default)
2) `--direction html2md` for HTML to Markdown Conversion


## Example
For Markdown to HTML Conversion\
`python main.py "...\sample.md" "...\sample.html" --direction md2html`

Similarly, for HTML to Markdown Conversion\
`python main.py "...\sample.html" "...\sample.md" --direction html2md`
