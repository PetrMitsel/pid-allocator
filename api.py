from bitmap import BitMap


class PidManager:
    # Minimum pid in range
    MIN_PID = 300
    # Maximum pid in range
    MAX_PID = 5000
    # Class variable keeps track of current pid
    pid_counter = 0
    # Class variable keeps track of index in bit_map
    bit_index = 0
    # BitMap has a size equal to the range of pids
    bit_map = BitMap(MAX_PID - MIN_PID)

    def allocate_map(self):
        # checks if a map exists
        if self.bit_map is not None:
            self.pid_counter = self.MIN_PID
            self.bit_index = 0
            return 1
        else:
            return -1

    def allocate_pid(self):
        # check against empty bitmap
        if self.bit_map is not None:
            # this case will trigger when the pid_counter goes out of the range of pids
            if self.pid_counter > self.MAX_PID:
                # Set to -1, if not overwritten in the loop, method will return -1
                pid = -1
                # this loop finds the first empty bit in the bitmap
                for i in range(self.MIN_PID, self.MAX_PID):
                    # checks if the bit at position i-MIN_PID is 'off'
                    # i must be offset by MIN_PID because index of bitmap does not correspond to pid range directly
                    if not self.bit_map.test(i - self.MIN_PID):
                        # turns on the bit at i-MIN_PID
                        self.bit_map.set(i - self.MIN_PID)
                        # the pid to be allocated will be the index i at this point in the loop
                        pid = i
                        break
                return pid
            # this case will trigger for the first n<MAX_PID allocations
            else:
                # the pid to be allocated will be the value of the pid_counter at this point
                pid = self.pid_counter
                # turns on the bit at bit_index
                self.bit_map.set(self.bit_index)
                # increments bit_index to write to next index in bit_map on next iteration
                self.bit_index += 1
                # increments pid_counter to allocate next pid on next iteration
                self.pid_counter += 1
                return pid

    def release_pid(self, pid):
        # turns 'off' the bit at pid with an offset of MIN_PID
        # releasing pid '300' will turn off bit 300-300, or 0
        self.bit_map.reset(pid - self.MIN_PID)
