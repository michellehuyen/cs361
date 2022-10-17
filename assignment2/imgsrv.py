import time

def main():
    while True:
        time.sleep(1)
        f = open('image-service.txt', 'r', encoding="utf-8")
        try_read = f.read()
        try:
            x = int(try_read)
        except:
            f.close()
            continue

        if x > 5:
            mod = x%5
        with open('image-service.txt', 'w', encoding="utf-8") as f_write:
            if mod == 1 or int(try_read) == 1:
                f_write.write('/Users/michellenguyen/cs361/assignment2/img/1.jpeg')
            elif mod == 2 or int(try_read) == 2:
                f_write.write('/Users/michellenguyen/cs361/assignment2/img/2.jpeg')
            elif mod == 3 or int(try_read) == 3:
                f_write.write('/Users/michellenguyen/cs361/assignment2/img/3.jpeg')
            elif mod == 4 or int(try_read) == 4:
                f_write.write('/Users/michellenguyen/cs361/assignment2/img/4.jpeg')
            else:
                f_write.write('/Users/michellenguyen/cs361/assignment2/img/5.jpeg')

            f.close()

if __name__ == "__main__":
    main()