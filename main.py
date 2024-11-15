from linked_list import LinkedList
from my_deque import Deque


def main():
    text = LinkedList()

    with open("Problems solution/Problem 7/input.txt", "r") as f:
        for line in f:
            text.append(line)

    reversed_text = Deque()

    for line in text:
        reversed_text.append_left(line)

    revers_text = ""
    for line in reversed_text:
        revers_text += line

    print(revers_text)

    with open("Problems solution/Problem 7/output.txt", "w") as f:
        f.write(revers_text)

if __name__ == "__main__":
    main()
