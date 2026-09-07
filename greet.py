import sys


def greet(name):
    return f"Hello, {name}! Welcome to your first pull request."


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
