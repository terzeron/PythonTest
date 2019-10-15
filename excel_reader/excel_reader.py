#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import sys
import os
import glob
import xlrd


def read_excel_file(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    worksheet1 = workbook.sheet_by_index(0)
    num_rows = worksheet1.nrows

    for row_num in range(num_rows):
        row = worksheet1.row_values(row_num)
        print(row)


def main():
    work_dir = os.environ["HOME"] + "/Downloads"
    print(work_dir)
    os.chdir(work_dir)
    for file in glob.glob("*_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].xls"):
        print(file)
        read_excel_file(file)


if __name__ == "__main__":
    sys.exit(main())