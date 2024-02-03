from InputOutputController import InputOutputController
import subprocess

class DotoolInputOutputController(InputOutputController):

    def __init__(self):
        self.dotool = subprocess.Popen("dotool", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    def movePointer(self, xRatio, yRatio):
        xRatio = xRatio * 4
        yRatio = yRatio * 4
        command = f"mouseto {xRatio} {yRatio}\n"
        self.dotool.stdin.write(command.encode())
        self.dotool.stdin.flush()        
