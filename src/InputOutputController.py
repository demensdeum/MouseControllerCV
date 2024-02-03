from abc import abstractmethod

class InputOutputController:

    @abstractmethod
    def movePointer(xRatio, yRatio):
        pass