import argparse
import markdown2
from pathlib import Path
from html2text import html2text

def convert_md_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding = 'utf-8') as md_file:
            md_content = md_file.read()
            html_content = markdown2.markdown(md_content)
    
        with open(output_file, 'w', encoding = 'utf-8') as html_file:
            html_file.write(html_content)
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    
    except Exception as e:
        print(f"An unexpected error has occurred during Markdown to HTML file conversion.\n{e}")

def convert_html_to_md(input_file, output_file):
    try:
        with open(input_file, 'r', encoding = 'utf-8') as html_file:
            html_content = html_file.read()
            md_content = html2text(html_content)

        with open(output_file, 'w', encoding = 'utf-8') as md_file:
            md_file.write(md_content)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    
    except Exception as e:
        print(f"An unexpected error has occurred during HTML to Markdown file conversion.\n{e}")

def main():
    parser = argparse.ArgumentParser(description = "Convert Markdown to HTML or HTML to Markdown")
    parser.add_argument('input', help = 'Input File')
    parser.add_argument('output', help = 'Output File')
    parser.add_argument('--direction', choices = ['md2html', 'html2md'], default = 'md2html', help = "Conversion direction (default: md2html)")

    args = parser. parse_args()

    if args.direction == 'md2html':
        convert_md_to_html(args.input, args.output)
    elif args.direction == 'html2md':
        convert_html_to_md(args.input, args.output)


if __name__ == "__main__":
    main()
