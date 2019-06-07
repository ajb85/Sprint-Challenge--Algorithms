class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # I'm starting with the light on just because it's easier for me to think of
        # the light on as a positive case.  I'm aware I'm using a couple extra lines to
        # turn it on then off again but it doesn't hurt my time efficiency and I think it's
        # more intuitive to users so I'll argue for it :)
        self.set_light_on()
        while self.light_is_on():
            # Initial conditions for the main loop
            self.set_light_off()
            self.swap_items()

            # Begin moving robit arm up the list
            self.sort_right()
            # Then return to initial location
            self.sort_left()

    def sort_right(self):
        # Robot's instructions when its moving to the right (positive index direction)
        while(self.can_move_right()):
            self.move_right()
            # Biggest to the right so only swap if held item is smaller (returns -1)
            # Except at the last index, we want the biggest set down so swap if return 1
            if(self.can_move_right() and self.compare_item() == -1) or (not self.can_move_right() and self-compare_item() == 1):
                self.swap_item()
                self.set_light_on()

    def sort_left(self):
        # Do the same as above, just opposite direction
        while(self.can_move_left()):
            self.move_left()
            if(self.can_move_left() and self.compare_item() == 1) or (not self.can_move_left() and self-compare_item() == -1):
                self.swap_item()
                self.set_light_on()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


# Understand

# I am going to write an algorithm that will sort a list of items based on the robot's abilities.
# However, given the limitations, I won't be able to do anything particularly efficient--or fun :'( 
# The robot is only able to move left or right, swap items, and toggle a light.

# Plan

# Since the robot has no memory and has to pick up an item to compare it, the only algorithm 
# that is going to work with any level of efficiency is a bubble sort. That way I can pick blocks 
# up and carry them to compare and swap when needed.  However, since I can't get the length 
# of the list, I have to do a full iteration each time but I should be able to increase the 
# efficiency by allowing the robot to sort on the way back to the zero position.  The light 
# will be useful in determining if a sort was made or not (so I know when to end).