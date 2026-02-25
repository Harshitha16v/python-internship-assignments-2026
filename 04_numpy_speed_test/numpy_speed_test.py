import time
import numpy as np
import matplotlib.pyplot as plt


def test_python_list(n):
    start = time.perf_counter()

    py_list = [i for i in range(n)]
    result = [x * 2 for x in py_list]
    total = sum(result)

    end = time.perf_counter()
    return end - start


def test_numpy_array(n):
    start = time.perf_counter()

    np_array = np.arange(n)
    result = np_array * 2
    total = np.sum(result)

    end = time.perf_counter()
    return end - start


def plot_results(python_time, numpy_time):
    labels = ["Python List", "NumPy Array"]
    times = [python_time, numpy_time]

    plt.figure()
    plt.bar(labels, times)
    plt.xlabel("Method")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Python List vs NumPy Performance Comparison")
    plt.show()


def main():
    N = 1_000_000

    print("NumPy Speed Benchmark (1 Million Elements)\n")

    python_time = test_python_list(N)
    numpy_time = test_numpy_array(N)

    print(f"Python List Time: {python_time:.6f} seconds")
    print(f"NumPy Array Time: {numpy_time:.6f} seconds")

    improvement = ((python_time - numpy_time) / python_time) * 100
    print(f"\nNumPy is approximately {improvement:.2f}% faster than Python list.")

    plot_results(python_time, numpy_time)


if __name__ == "__main__":
    main()