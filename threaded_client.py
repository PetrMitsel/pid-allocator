from api import PidManager
import random
import threading
import time


class processThread(threading.Thread):
    def __init__(self, threadID, name, pidManager, output_file):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.pidManager = pidManager
        self.output_file = output_file

    def run(self):
        print("Starting " + self.name + "\n")
        thread_function(self.name, self.pidManager, self.output_file)
        print("Exiting " + self.name + "\n")


def main():
    threads = []
    pidManager = PidManager()
    output_file = open("output.txt", "w")

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
    for i in range(0, 100):
        threads.append(processThread(i, f"thread {i}", pidManager, output_file))
        threads[i].start()


def thread_function(threadname, pidManager, output_file):

    pid = pidManager.allocate_pid()

    output_file.write("Allocated pid: " + str(pid) + " in " + threadname + "\n")
    print("Allocated pid: " + str(pid) + " in " + threadname + "\n")
    rand_time = random.randint(0, 100)
    output_file.write(
        "Sleeping for: " + str(rand_time) + " seconds" + " in " + threadname + "\n"
    )
    print("Sleeping for: " + str(rand_time) + " seconds" + " in " + threadname + "\n")
    time.sleep(rand_time)
    output_file.write("Releasing pid: " + str(pid) + " in " + threadname + "\n")
    print("Releasing pid: " + str(pid) + " in " + threadname + "\n")
    pidManager.release_pid(pid)


if __name__ == "__main__":
    main()
