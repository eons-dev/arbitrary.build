import os
import logging
from ebbs import Builder
from ebbs import OtherBuildError

class arbitrary(Builder):
    def __init__(this, name="Publisher"):
        super().__init__(name)

        this.requiredKWArgs.append("commands")

        this.supportedProjectTypes = [] #all

    # Required Builder method. See that class for details.
    def Build(this):
        for command in this.commands:
            this.RunCommand(command)