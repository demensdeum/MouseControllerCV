from HandMotionRecognizer import HandMotionRecognizer
from DotoolInputOutputController import DotoolInputOutputController

motionRecognizer = HandMotionRecognizer()
inputOutputController = DotoolInputOutputController()

def motionAdapter(xRatio, yRatio):
    inputOutputController.movePointer(xRatio, yRatio)

motionRecognizer.run(motionAdapter)