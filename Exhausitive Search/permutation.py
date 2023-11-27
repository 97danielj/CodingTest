# 순열 탐색
# 순열을 활용하여 모든 경우의 수를 탐색하는 방법입니다.
# 1. swap 배열을 이용한 순열
    # 장점: 쉽게 구현
    # 단점: 큰 데이터셋에 비효율적



# 1.
class Permutation():
    # permute: 순열의 로직을 수행합니다.
    def permute(self, arr, k):
        for i in range(k, len(arr)):
            self.swap(arr, i, k)
            self.permute(arr, k+1)
            self.swap(arr, k, i)

        if (k == len(arr)-1):
            print(arr)

    # swap: 배열의 요소 값을 Swap 합니다.
    def swap(self, arr, i, j):
        """

        :param arr: 배열
        :param i: 현재 인덱스
        :param j: 바꿀 인덱스
        :return:
        """
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp


def main():
    arr = [1, 2, 3, 4]
    p = Permutation()

    p.permute(arr, 0)



if __name__ == '__main__':
    main()