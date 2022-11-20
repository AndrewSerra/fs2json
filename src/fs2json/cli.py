#!/usr/bin/python3
from argparse import ArgumentParser
from pathlib import Path
from datetime import datetime
from typing import Union
import json

def get_default_dir_dict() -> dict:
    return { "files": [], "dirs": {} }

def create_output_file(outfile: str) -> Path:
    path = Path(outfile)

    if not path.is_absolute():
        path = path.resolve()

    if path.is_dir():
        raise IsADirectoryError("Output file given is a directory.")

    if check_existence(path):
        path_of_existing = path.cwd().resolve()
        path = Path(f"{path_of_existing}/{path.stem}-{datetime.now().isoformat()}.json")
        
    path.touch()
    return path
        
def check_existence(path: Union[str, Path]) -> bool:
    return Path(path).exists() if isinstance(path, str) else path.exists() 

def create_json(path: str) -> dict:
    if not check_existence(path):
        raise Exception("Path does not exist.")

    def get_fs_object(path: Path):
        fs = get_default_dir_dict()
        dir_items = path.glob('./*')

        for item in dir_items:
            item = Path(item)

            if item.is_dir():
                fs["dirs"][item.parts[-1]] = get_fs_object(item.absolute())
            else:
                fs["files"].append(item.name)
        return fs

    return get_fs_object(Path(path).resolve())
                
def create_parser(parser: ArgumentParser):
    parser.add_argument('path', help="Path to start mapping to json")
    parser.add_argument('-o', '--out-file')

if __name__ == '__main__':
    parser = ArgumentParser(
        prog="fs2json",
        description="A command-line tool to convert a directory to a json format"
    )
    create_parser(parser)
    args = parser.parse_args()
    converted_obj = create_json(args.path)
    output_file = args.out_file

    if output_file is None:
        current_dir = Path().resolve()
        output_file = f"{current_dir.parts[-1]}-tree-output.json".lower()
    
    file = create_output_file(output_file)
    with open(file, "w") as outfile:
        json.dump(converted_obj, outfile)
