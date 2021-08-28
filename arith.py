def lots_of_math():
    print(1 + 1)
    a = 1 + 1
    print(a)
    print(a == 1 + 1)
    print(a != 1 + 1)
    print(not (a != 1 + 1))
    print(1 < 2 and 3 < 4)
    print(1 < 2 or 3 > 4)
    print(1 < a <= 3)


def some_string_ops():
    s = "Hello World!!!"
    print(s)
    s1 = "Hello"
    s2 = "World"
    s = s1 + " " + s2 + "!!!"
    print(s)
    print(s1[0])
    print(s1[0:2])
    print(s1[:2])
    print(s1[1:])
    print(len(s1))
    name = "Reiko"
    print("Hello " + name)
    print(f"Hello {name} (with {len(name)} characters)")


def conditional():
    a = 0
    b = True
    if a < 5:
        print("You tell the truth")
    else:
        print("You dont tell the truth")
    print("truth" if True else "liar")
    if True:
        print("truth")
    else:
        print("liar")


def some_listing():
    first_list = [1, 2, True, 'banana', 3.4]
    second_list = []
    second_list.append(1)
    second_list.append(2)
    second_list.append(True)
    second_list.append(first_list)
    print(second_list)
    print(second_list[0])
    print(second_list[-1])
    print(second_list[-2] == second_list[1])
    print(second_list[-3] == second_list[0])

    l1 = second_list[3]
    print(l1[0])
    print((second_list[3])[0])
    print(second_list[3][0])


def some_dictionaries():
    empty_dict = {}
    filled_dict = {"one": 1, "two": 2, "three": 3}
    print(filled_dict)
    print(filled_dict["one"])
    print(filled_dict.get("one"))

    if "four" not in filled_dict:
        print("Not found")
    if not ("four" in filled_dict):
        print("Not found")

    print("Default value access in dictionaries")
    print(filled_dict.get("one", -1))
    print(filled_dict.get("five", -1))
    print(filled_dict['five'])
    print("Ozgur's Question")

    if "three" in filled_dict:
        print("Found found -1 ")
    if "3" in filled_dict:
        print("Found found -2")
    if 3 in filled_dict:
        print("Found found -3 ")

    print(filled_dict["one"] + filled_dict["two"])


def for1():
    for i in range(10):
        print(i)
    l = ['apple', 'banana', 'orange']
    for fruit in l:
        print(fruit)
    filled_dict = {"one": 1, "two": 2, "three": 3}
    for k in filled_dict:
        print(k)
    for k in filled_dict.keys():
        print(k)
    for k in filled_dict.values():
        print(k)
    s = "Hello World"
    for c in s:
        print(c)


def for2():
    s = "Hello World"
    chars = []
    for c in s:
        if 'a' <= c <= 'l' or 'A' <= c <= 'L':
            chars.append(c)
    print(chars)
    chars = [c for c in s if 'a' <= c <= 'l' or 'A' <= c <= 'L']
    print(chars)
    chars = dict((c, i) for i, c in enumerate(s) if 'a' <= c <= 'l' or 'A' <= c <= 'L')
    print(chars)


def some_stupid_cool_things():
    a = 1
    b = 2
    dummy = a
    a = b
    b = dummy
    a, b = b, a


if __name__ == '__main__':
    pass
