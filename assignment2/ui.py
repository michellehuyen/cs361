import time

def main():
    while True:
        choice = int(input("Enter 1 to generate new image\nEnter 2 to exit\nEnter a number: "))
        if choice == 1:
            prng = open('prng-service.txt', 'w', encoding="utf-8")
            time.sleep(2)
            prng.write("run")
            prng.close()
            time.sleep(5)
            
            prng_read = open('prng-service.txt', 'r', encoding="utf-8")
            prng_num = int(prng_read.read())
            prng_read.close()
            
            with open('image-service.txt', 'w', encoding="utf-8") as img_write:
                img_write.write(str(prng_num))
            time.sleep(5)
            with open('image-service.txt', 'r', encoding="utf-8") as img_read:
                print(img_read.read())

        elif choice == 2:
            return
        else:
            print("unknown option")
        

if __name__ == "__main__":
    main()
