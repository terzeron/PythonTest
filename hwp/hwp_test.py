#!/usr/bin/env python

import sys
from libhwp import HWPReader

hwp = HWPReader(sys.argv[1])

import pprint
import inspect
#pprint.pprint(hwp)
#pprint.pprint(inspect.getmembers(hwp))
#pprint.pprint(inspect.getmembers(hwp.sections))
for section in hwp.sections:
    #pprint.pprint(inspect.getmembers(section))
    for paragraph in section.paragraphs:
        #pprint.pprint(inspect.getmembers(paragraph))
        for char in paragraph.chars:
            print(chr(char.code), end="")
sys.exit(0)

# 모든 문단 출력 (표, 캡션 포함)
for paragraph in hwp.find_all('paragraph'):
    print(paragraph)

# 표 내용 출력 (표 안의 표 포함)
for table in hwp.find_all('table'):
    for cell in table.cells:
        for paragraph in cell.paragraphs:
            print(paragraph)

# 표 내용 출력 (표 안의 표 무시)
for table in hwp.find_all('table', recursive=False):
    for cell in table.cells:
        for paragraph in cell.paragraphs:
            print(paragraph)

# 표 안의 표 내용 출력 방법 2
for table in hwp.find_all('table'):
    for cell in table.cells:
        for paragraph in cell.paragraphs:
            print(paragraph)

            # paragraph에서도 recursive 하게 찾을 수 있다
            for p in paragraph.find_all('paragraph'):
                print(p)

# 수식 내용 출력
for equation in hwp.find_all('equation'):
    print(equation.script)  # eg. f(x)= logx+sinx

# 문서에 사용된 파일 저장
for file in hwp.bin_data:
    with open(file.name, 'wb') as f:
        f.write(file.data)
