# Write your solution here
# You can test your function by calling it within the following block
def hash_square(length):
    for _ in range(length):
        print("#" * length)
if __name__ == "__main__":
    hash_square(3)
    print()
    hash_square(5)