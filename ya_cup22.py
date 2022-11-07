def subset_sum(W, N, M):
    if sum(W) < M:
        return [1]*M
    else:
        prev = [ii for ii in range(M + 1)]
        curr = [ii for ii in range(M + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if j < W[i - 1]:
                    curr[j] = prev[j]
                if j >= W[i - 1]:
                    curr[j] = min(prev[j], prev[j - W[i - 1]])
            prev = curr
            curr = [ii for ii in range(M + 1)]
        return prev


def get_and_transform_input():
    input_m = int(input())  # значение, до которого (включительно) мы проверяем числа
    input_w = list(map(int, input().split(' ')))  # веса гирек
    sum_of_w = sum(input_w)
    input_m += sum_of_w
    double_w = []
    double_w.extend(input_w)
    double_w.extend(input_w)
    input_n = len(input_w)*2
    return sum_of_w, double_w, input_n, input_m


if __name__ == "__main__":
    s_o_w, w, n, m = get_and_transform_input()
    result = subset_sum(w, n, m)
    ind = 0
    # так как мы добавили в к m сумму w, нас интересуют только числа в конце списка
    if all(item == 0 for item in result[s_o_w:]):
        print('Yes')
    else:
        print('No')
