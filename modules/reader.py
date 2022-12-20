
class FileType:
    HTML = 'html'
    TEXT = 'txt'
    IMAGE = 'jpg'

COMMON_ROUTES = {
    "html": "/pages",
    "files": "/files",
    "images": "/images"
}

def read_file_as_string(*, file_name: str = "index", file_type: str = FileType.HTML) -> str:
    try:
        file_to_open_type = COMMON_ROUTES[file_type]
        file = open(f'.{file_to_open_type}/{file_name}.{file_type}', mode="r+")
        return file.read()
    except IOError:
        raise IOError("Error opening file")