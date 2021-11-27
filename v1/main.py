"""
# 1. 문자열 덧셈 계산기 구현
- '3+4+5' 를 입력하면 int 형으로 결과를 반환한다.
- '3+' 처럼 처리할 수 없는 경우 0을 반환한다.
"""


def string_calculator(input_string: str) -> int:
    digit_list = input_string.split('-')
    print("2번테스트:" + str(digit_list), type(digit_list))  # test method

    print("3번테스트:", end="")  # test method

    int_list = []
    for digit in digit_list:
        int_list.append(int(digit))

    print(int_list, type(int_list))

    print("4번테스트:", end="")  # test method

    y = int_list[0] + int_list[1] + int_list[2] + int_list[3]

    summary = 0
    for x in int_list:
        summary += x
    print(summary)

    return summary

# git test

def main():
    # input_string = input("입력하세요 : ")
    answer = string_calculator("1+2+3+4")  # 메인 시작

    print(f"답은 {answer} 입니다")


# if : 이 스크립트 파일(main.py)을 직접 실행한 경우 True.
if __name__ == '__main__':
    main()
