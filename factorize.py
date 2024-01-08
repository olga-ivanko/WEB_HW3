import time
import multiprocessing


def factorize(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def factorize_sync(numbers):
    result = []
    for num in numbers:
        result.append(factorize(num))
    return result


def factorize_parallel(numbers):
    with multiprocessing.Pool(processes= multiprocessing.cpu_count()) as pool:
        result = pool.map(factorize, numbers)
    return result


if __name__ == "__main__":
    test_numbers = [99999, 10651060, 256222558]

    #синхронне виконання
    start_time_sync = time.time()
    result_sync = factorize_sync(test_numbers)
    end_time_sync = time.time()
    print(f"Synchronous execution time: {end_time_sync - start_time_sync} seconds")
    print("Synchronous result:", result_sync)

    #паралельні процеси
    start_time_parallel = time.time()
    result_parallel = factorize_parallel(test_numbers)
    end_time_parallel = time.time()
    print(f"Parallel execution time: {end_time_parallel - start_time_parallel} seconds")
    print("Parallel result:", result_parallel)
