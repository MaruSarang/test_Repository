def input_x():
    # 사용자가 값을 입력하면, 배열로 반환함.
    abc = input("값을 입력하세요 : ")

    return abc


def list_out(receive_string):
    test_array = []
    for stupid in receive_string:
        test_array.append(int(stupid))

    # 숫자(123) 문자열로 받은 후, 배열로 바꿈
    # 그 배열을 int형 배열로 반환.
    return test_array


def array_to_sum(int_array) -> int:
    summary = 0
    for x in int_array:
        summary = summary + x
    # 입력값으로 int형 배열을 받아서, 추출하고 그걸 서로 더한값을 int형으로 반환해줌.
    return summary


def string_calculator(input_str:str):
    # 스트링 계산기
    output_array: list = list_out(input_str)
    int_result: int = array_to_sum(output_array)
    return int_result


def main():
    # 스트링 계산기
    # 출력 : 10 : int, 모든 수의 합
    result: int = string_calculator("1234")
    print(result)


if __name__ == '__main__':
    main()
    # print(main())

"""

- '3+4+5' 를 입력하면 int 형으로 결과를 반환한다.
- '3+' 처럼 처리할 수 없는 경우 0을 반환한다.

1. 계산 기능이 가능해야 한다. (입력값을 받음)
2. 계산을 해서 int형으로 반환해야 한다.
3. 계산이 불가능하면 0을 반환해야 한다.



"""
