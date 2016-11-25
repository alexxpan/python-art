# Startup file for the NodeBox OS X application

# PyObjC requires the startup file to be in the root folder.
# This just imports everything from the nodebox.gui.mac module
# and works from there

from nodebox.gui.mac import *

if __name__ == "__main__":
    AppHelper.runEventLoop()
