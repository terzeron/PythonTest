#!/usr/bin/env python

import sys

# 스택의 최소값을 상수 시간에 구하는 방법
# 보조 스택을 이용하여 단조감소하는 순으로 일부 값을 저장해둠
# 스택에서 pop할 때 보조 스택에서 동일한 값을 pop하는 전략임

data = [ 9, 7, 3, 8, 2, 5, 1, 6, 4, 10 ]
minstack = [] 
stack = []

def construct_minstack():
    # data 배열에서 stack은 그대로 복사함
    # data 배열에서 단조감소하는 원소만 minstack에 복사함
    for item in data:
        stack.append(item)
        if len(minstack) == 0 or minstack[-1] > item:
            minstack.append(item)
    print("stack=", stack)
    print("minstack=", minstack)
    print()


def find_min_from_minstack():
    for i in range(len(stack)):
        value = stack.pop()
        print("popped:", value)
        print("stack=", stack)
        if value == minstack[-1]:
            minstack.pop()
        if len(minstack) > 0:
            minvalue = minstack[-1]
        else:
            minvalue = None
        print("min=", minvalue)
        print("minstack=", minstack)
        print()


def main():
    construct_minstack()
    find_min_from_minstack()

    
if __name__ == "__main__":
    sys.exit(main())
