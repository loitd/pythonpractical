# bb_setup.py
from bbfreeze import Freezer
includes = []
excludes = []
f = Freezer(distdir="dist", includes=includes, excludes=excludes)
f.use_compression = 1
f.addScript("main.py", gui_only=True)
f()