#!/usr/bin/env python


import sys
import os
from pathlib import Path
import tempfile
import shutil
import zipfile
from mobi.kindleunpack import unpackBook


def main():
    infile = Path(sys.argv[1])
    temp_dir_path = Path(tempfile.mkdtemp(None, None, None))

    print(infile, temp_dir_path)
    unpackBook(infile.name, str(temp_dir_path))

    filename = infile.name
    basename = infile.stem
    epub_filepath = temp_dir_path / "mobi8" / (basename + ".epub")
    pdf_filepath = temp_dir_path / (basename + ".001.pdf")
    html_filepath = temp_dir_path / "mobi7" / "book.html"

    if os.path.exists(epub_filepath):
        shutil.copyfile(epub_filepath, basename + ".epub")
        # 바이너리 다운로드
    elif os.path.exists(pdf_filepath):
        shutil.copyfile(pdf_filepath, basename + ".pdf")
    elif os.path.exists(html_filepath):
        os.rename(temp_dir_path / "mobi7", temp_dir_path / "OEBPS")
        with open(temp_dir_path / "mimetype", "w", encoding="utf-8") as outfile:
            outfile.write("application/epub+zip")
        os.mkdir(temp_dir_path / "META-INF")
        with open(temp_dir_path / "META-INF" / "container.xml", "w", encoding="utf-8") as outfile:
            outfile.write('''<?xml version='1.0' encoding='utf-8'?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
    <rootfiles>
        <rootfile media-type="application/oebps-package+xml" full-path="OEBPS/content.opf"/>
    </rootfiles>
</container>''')
        with zipfile.ZipFile(basename + ".epub", "w") as zip:
            os.chdir(temp_dir_path)
            zip.write("mimetype")
            zip.write("META-INF/container.xml")
            for root, dirs, files in os.walk("OEBPS"):
                for file in files:
                    zip.write(os.path.join(root, file))

    shutil.rmtree(temp_dir_path)


if __name__ == '__main__':
    sys.exit(main())
