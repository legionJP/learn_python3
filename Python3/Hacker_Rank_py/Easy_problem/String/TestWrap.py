import textwrap
def wrap(string, max_width):
    wrapped_text = textwrap.fill(string, max_width)
    return wrapped_text


def wrap(string, max_width):
    list_str = []
    for i in range(0, len(string) , max_width):
        list_str.append(string[i:i+max_width])
    return '\n \n'.join(list_str)



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

