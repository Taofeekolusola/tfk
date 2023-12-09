class Robot:
    """defines robots that perform certain tasks"""

    count = 0

    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def working(self):
        """Robot at work"""
        print("{} with {} strength is currently at work".format(self.name, self.ability))

        Robot.count += 1

    def stop_working(self):
        """Robot stooped working"""
        print("{} with {} strength is no longer at work".format(self.name, self.ability))

        Robot.count -= 1

    @classmethod
    def robot_at_work(cls):
        """Numbers of robots currently at work"""
        print("There are {:d} robots currently at work".format(cls.count))

rbt = Robot("RBT-320", "1000-MAH")
rbt.working()
rbt.robot_at_work()
rbt1 = Robot("RBT-330", "1500-MAH")
rbt1.working()
rbt1.robot_at_work()
