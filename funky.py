import time


def full_name(name, surname, middle=""):
    if middle == "":
        return f"{name} {surname}"
    else:
        return f"{name} {middle} {surname}"


from functools import lru_cache as cache


@cache
def factorial(n):
    time.sleep(0.00625)
    if n in [0, 1]:
        return 1
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    t0 = time.time()

    factorial(400)
    factorial(401)

    t1 = time.time()

    print(f"Elapsed duration in many factorial is {t1 - t0} sec")
    print(factorial.cache_info())
