from os import makedirs
from os.path import exists

from typing import Union
from loguru import logger

class FileHelper(object):
    def ensure_directory_exists(self, path: str):
        """
        function to check directory os exist or not
        
        Argss:
            path (_type_): string path
        """
        if not exists(path):
            makedirs(path)
            logger.info(f"Directory created: {path}")
        else:
            logger.info(f"Directory already exists: {path}")


    
    def writetmpfile(self, file_name: str, data: Union[str, bytes]) -> None:
        """ write temporary file

        Args:
            file_name (str): _description_
            data (Union[str, bytes]): _description_
        """
        with open(file_name, "wb" if isinstance(data, bytes) else "w+", encoding='UTF-8') as file:
            file.write(data)