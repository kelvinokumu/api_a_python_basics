def double_loops():
    n = 11
    m = 11
    for i in range(n):
        # print(f"Outer loop {i}")
        for j in range(m):
            # print(f"Inner loop {i*j}")
            pass

    print(f"The final value {i * j}")


if __name__ == '__main__':
    double_loops()