import argparse
import sys

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

    print(f"Source file path: {args.file1path}")
    print(f"Path to the second file: {args.file2path}")

main()