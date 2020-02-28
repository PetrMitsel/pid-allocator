# pid-allocator
Replicates the process manager of an operating system programmatically. A process manager is responsible for assigning unique process ids to each process that is running on an operating system. We replicate this by keeping track of the availability of a range of process ids using a bit-map, similar to Linux. When the bitmap is full no more process id’s can be assigned unless a process is terminated and a process id is released. This ensures that all running processes have a unique id. 
#	allocate_map(): 
This method takes no parameters, and returns an integer 1 or -1 representing a success or failure. It is responsible for initializing the bitmap which tracks availability of various process ids.
#	allocate_pid(): 
This method takes no parameters and returns an integer representing the allocated process id, or -1 if the bitmap is full and no process ids are available. It is responsible for keeping track of the index of the bitmap, and keeping track of the last pid assigned. The method assigns ids from the possible range one by one until its assigned an amount of ideas equal to the maximum possible process id. After this occurs, on each new allocation the method will find the first empty bit in the bitmap and allocate the corresponding pid. 
#	release_pid(pid): 
This method takes an integer parameter representing the process id to be released. It returns nothing. The method resets the bit in the bitmap at the index equal to the process id minus an offset of the minimum process id. 

# to run:
    pip install BitMap
    python client.py
