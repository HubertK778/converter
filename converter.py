import argparse
import sys
import os
import json
from pathlib import Path

def loadSourceFile(sourcePath, sourceExtension):
    try:
        with open(sourcePath, 'r', encoding='utf-8') as sourceFile:
            content = sourceFile.read()

            if sourceExtension == '.json':
                content = json.loads(content)
                return content
    except json.JSONDecodeError as error:
        print(f"Error: Invalid JSON format in {sourcePath}.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found - {sourcePath}.")
        sys.exit(1)

def convertToFile(sourceContent, targetPath, targetExtension):
    try:
        with open(targetPath, 'w', encoding='utf-8') as targetFile:
            if targetExtension == '.json':
                json.dump(sourceContent, targetFile)
    except Exception as error:
        print(f"Error: Could not write to {targetPath}. {error}")
        sys.exit(1)

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
    sourceExtension = Path(sourcePath).suffix.lower()
    
    sourceContent = loadSourceFile(sourcePath, sourceExtension)

    targetPath = args.file2path
    targetExtension = Path(targetPath).suffix.lower()
    convertToFile(sourceContent, targetPath, targetExtension)

main()