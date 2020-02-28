from api import PidManager
import random


def main():
    # open a file to write to
    output_file = open("output.txt", "w")
    # Instantiate pidManager object
    pidManager = PidManager()
    output_file.write("Allocating Map:" + "\n")
    print("Allocating Map:" + "\n")
    if pidManager.allocate_map() == -1:
        output_file.write("allocate_map failed" + "\n")
        print("allocate_map failed" + "\n")
    else:
        output_file.write("allocate_map success" + "\n")
        print("allocate_map success" + "\n")
    output_file.write("Allocating pids:" + "\n")
    print("Allocating pids:" + "\n")
    # allocate ids in full range
    # 50 extra to demonstrate release_pid once index is over MAX_PID
    for i in range(pidManager.MIN_PID, (pidManager.MAX_PID) + 50):
        # attempt to allocate a pid
        pid = pidManager.allocate_pid()
        # a return of -1 indicates a full bitmap
        if pid != -1:
            output_file.write("Allocated pid: ")
            print("Allocated pid: ")
            output_file.write(str(pid) + "\n")
            print(str(pid) + "\n")
        else:
            output_file.write("Bitmap is full, no pids available" + "\n")
            print("Bitmap is full, no pids available" + "\n")
        if i > 5000:
            # after assigning over 5000 pids we start releasing them at random
            # the released id should be allocated on the next iteration of the loop
            rand_pid = random.randint(300, 5000)
            output_file.write("Releasing pid: ")
            print("Releasing pid: ")
            output_file.write(str(rand_pid) + "\n")
            print(str(rand_pid) + "\n")
            pidManager.release_pid(rand_pid)
    output_file.close()


if __name__ == "__main__":
    main()
