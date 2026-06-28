import argparse
import sys
import os
import json

def main():
    parser = argparse.ArgumentParser(
        description="Skrypt przyjmujący dwie ścieżki do plików jako argumenty."
    )

    parser.add_argument(
        "file1path", 
        type=str, 
        help="Source file path"
    )
    
    parser.add_argument(
        "file2path", 
        type=str, 
        help="Path to the second file"
    )

    args = parser.parse_args()

    sourcePath = args.file1path

    try:
        with open(sourcePath, 'r', encoding='utf-8') as sourceFile:
            _, fileExtension = os.path.splitext(sourcePath)
            content = sourceFile.read()

            if fileExtension.lower() == '.json':
                content = json.loads(content)
    except json.JSONDecodeError as error:
        print(f"Error: Invalid JSON format in {sourcePath}.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found - {sourcePath}.")
        sys.exit(1)
main()