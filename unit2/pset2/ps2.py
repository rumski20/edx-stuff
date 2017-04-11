# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be greater than zero.")
        self.width = width
        self.height = height
        self.tiles = self.populate_tiles(self.width, self.height)

    def populate_tiles(self, w, h):
        """
        Populate tile space for room
        :param w: width (integer)
        :param h: height (integer)
        :return: returns dictionary of tile space for room in the format
        (x, y) : <clean?> (True/False)
        """
        d = {}
        # loop through x axis
        for x in range(w):
            # loop through y axis
            for y in range(h):
                # create dict entry from x,y coord
                d[(x, y)] = 'dirty'
        return d
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = math.floor(pos.getX())
        y = math.floor(pos.getY())
        if (x, y) not in self.tiles.keys():
            raise ValueError("That position is not in this room!")
        self.tiles[(x, y)] = 'cleaned'

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m, n) not in self.tiles.keys():
            raise ValueError("That tile is not in this room!")
        return True if self.tiles[(m, n)] == 'cleaned' else False

    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len([v for k, v in self.tiles.items() if v == 'cleaned'])

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(
            random.uniform(0, self.width),
            random.uniform(0, self.height)
        )

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return True if (math.floor(pos.getX()), math.floor(pos.getY())) \
                       in self.tiles.keys() else False

# === Testing problem 1
# print('=====================================')
# print('Testing problem 1: Rectangular Room')
# room = RectangularRoom(5,5)
# print('This room is {0} tiles in size'.format(room.getNumTiles()))
# # loop through and clean random tiles
# for i in range(5):
#     randpos = room.getRandomPosition()
#     room.cleanTileAtPosition(randpos)
#     print('Cleaning tile at {} \n Number of cleaned tiles: {}'
#           .format(randpos, room.getNumCleanedTiles()))
#
# print(room.tiles)



# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # set random initial direction
        self.direction = self.get_new_direction()
        self.room = room
        # set random initial position (in the room)
        self.position = room.getRandomPosition()
        # clean initial position
        self.room.cleanTileAtPosition(self.position)
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError("Robot's speed must be greater than zero")

    def get_new_direction(self):
        """
        get random direction (angle) between 0 and 360
        :return: integer
        """
        return random.randint(0, 360)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # get new position based on current speed and heading
        new_position = self.position.getNewPosition(self.direction, self.speed)

        # check if new position is in the room
        # and clean tile if it is
        if self.room.isPositionInRoom(new_position):
            self.position = new_position
            self.room.cleanTileAtPosition(self.position)

        # otherwise just change direction
        else:
            self.direction = self.get_new_direction()



# Uncomment this line to see your implementation of StandardRobot in action!
# testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runAnimation(num_robots, speed, width, height, min_coverage, robot_type,
                 delay=0.2):
    """
    Runs animation of the simulation using Tk!

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    # animated version
    # DON'T use with more than one trial
    anim = ps2_visualize.RobotVisualization(num_robots, width, height, delay)
    room = RectangularRoom(width, height)
    pct_cleaned = 0
    timer = 0
    # get robo army
    robots = [robot_type(room, speed) for r in range(num_robots)]
    # clean the room until minimum coverage is reached
    while pct_cleaned <= min_coverage:

        # animate bots
        anim.update(room, robots)

        # loop through number of robots and execute a single step
        for robot in robots:
            robot.updatePositionAndClean()

        timer += 1
        pct_cleaned = room.getNumCleanedTiles() / room.getNumTiles()

    # animation complete
    anim.done()


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """

    times = []
    # loop through trials
    for t in range(num_trials):
        room = RectangularRoom(width, height)
        pct_cleaned = 0
        timer = 0
        # get robo army
        robots = [robot_type(room, speed) for r in range(num_robots)]
        # clean the room until minimum coverage is reached
        while pct_cleaned <= min_coverage:

            # loop through number of robots and execute a single step
            for robot in robots:
                robot.updatePositionAndClean()

            timer += 1
            pct_cleaned = room.getNumCleanedTiles() / room.getNumTiles()

        # add time to times
        times.append(timer)
        # print('Trial {0}: {1}'.format(t, timer))

    # return average time it took to clean room
    return sum(times) / len(times)



# Uncomment this line to see how much your simulation takes on average
# print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))
# print(runAnimation(10, 1.0, 50, 50, 0.75, StandardRobot, 0.01))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # get new position based on current speed and heading
        new_position = self.position.getNewPosition(self.direction, self.speed)

        # check if new position is in the room
        # and clean tile if it is
        if self.room.isPositionInRoom(new_position):
            self.position = new_position
            self.room.cleanTileAtPosition(self.position)

        # otherwise just change direction
        else:
            self.direction = self.get_new_direction()

        # set new random direction
        self.direction = self.get_new_direction()

# print(runAnimation(1, 3.0, 10, 10, 0.75, RandomWalkRobot, 0.1))


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()


def showPlot3(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    speeds = [1, 3, 5]
    for s in speeds:
        num_robot_range = range(1, 11)
        times1 = []
        times2 = []
        for num_robots in num_robot_range:
            print("Plotting", num_robots, "robots with speed of {"
                                          "}...".format(s))
            times1.append(runSimulation(num_robots, s, 20, 20, 0.8, 20,
                                        StandardRobot))
            times2.append(runSimulation(num_robots, s, 20, 20, 0.8, 20,
                                        RandomWalkRobot))
        pylab.plot(num_robot_range, times1)
        pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
# showPlot1('Number of Robots by Time it Takes to Clean Room',
#           'Number of Robots', 'Time')

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
# showPlot2('Time it takes to clean the room by aspect ratio', 'Aspect Ratio',
#           'Time-Steps')

showPlot3('Number of Robots by Time it Takes to Clean Room', 'Number of '
                                                             'Robots', 'Time')
