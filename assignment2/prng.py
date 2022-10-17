import time
import random

def main():
    while True:
        time.sleep(1)
        f_read = open('prng-service.txt', 'r', encoding="utf-8")
        if f_read.readline() == "run":
            rand_num = random.randint(1, 10)
            with open('prng-service.txt', 'w', encoding="utf-8") as f:
                f.write(str(rand_num))
        else:
            f_read.close()

if __name__ == "__main__":
    main()