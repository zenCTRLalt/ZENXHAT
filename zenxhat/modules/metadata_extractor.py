"""
Metadata Extraction Module
"""

import os
from pathlib import Path
try:
    import exifread
except ImportError:
    exifread = None

from PIL import Image
from PIL.ExifTags import TAGS
from zenxhat.core.logger import setup_logger

logger = setup_logger(__name__)


class MetadataExtractor:
    """Extract metadata from images and documents"""

    def __init__(self):
        self.logger = logger

    def extract_image_metadata(self, image_path: str) -> dict:
        """Extract EXIF data from images"""
        if not os.path.exists(image_path):
            self.logger.error(f"File not found: {image_path}")
            return {"error": "File not found"}

        try:
            metadata = {"file_path": image_path, "exif_data": {}}

            # Using PIL
            image = Image.open(image_path)
            exif_data = image.getexif()

            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                # Convert bytes to string if needed
                if isinstance(value, bytes):
                    try:
                        value = value.decode("utf-8", errors="ignore")
                    except:
                        value = str(value)
                metadata["exif_data"][tag_name] = str(value)

            # Basic image info
            metadata["image_info"] = {
                "format": image.format,
                "size": image.size,
                "mode": image.mode,
            }

            self.logger.info(f"Extracted metadata from {image_path}")
            return metadata

        except Exception as e:
            self.logger.error(f"Metadata extraction failed: {str(e)}")
            return {"error": str(e)}

    def extract_pdf_metadata(self, pdf_path: str) -> dict:
        """Extract metadata from PDF files"""
        if not os.path.exists(pdf_path):
            return {"error": "File not found"}

        try:
            # Basic file metadata
            file_stat = os.stat(pdf_path)
            metadata = {
                "file_path": pdf_path,
                "file_size": file_stat.st_size,
                "creation_time": file_stat.st_ctime,
                "modification_time": file_stat.st_mtime,
            }

            self.logger.info(f"Extracted metadata from {pdf_path}")
            return metadata

        except Exception as e:
            self.logger.error(f"PDF metadata extraction failed: {str(e)}")
            return {"error": str(e)}

    def extract_file_metadata(self, file_path: str) -> dict:
        """Extract generic file metadata"""
        if not os.path.exists(file_path):
            return {"error": "File not found"}

        try:
            file_stat = os.stat(file_path)
            metadata = {
                "file_path": file_path,
                "file_name": os.path.basename(file_path),
                "file_size": file_stat.st_size,
                "creation_time": file_stat.st_ctime,
                "modification_time": file_stat.st_mtime,
                "access_time": file_stat.st_atime,
                "is_file": os.path.isfile(file_path),
                "is_directory": os.path.isdir(file_path),
            }

            return metadata

        except Exception as e:
            self.logger.error(f"File metadata extraction failed: {str(e)}")
            return {"error": str(e)}
