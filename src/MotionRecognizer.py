from abc import abstractmethod

class MotionRecognizer:

    @abstractmethod
    def run(self, motionHandler):
        pass