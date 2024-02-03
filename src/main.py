from HandMotionRecognizer import HandMotionRecognizer
from DotoolInputOutputController import DotoolInputOutputController

inputOutputController = DotoolInputOutputController()
motionRecognizer = HandMotionRecognizer()

def motionAdapter(xRatio, yRatio):
    inputOutputController.movePointer(xRatio, yRatio)

motionRecognizer.run(motionAdapter)