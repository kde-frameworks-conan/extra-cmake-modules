#/usr/bin/python3

from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager()
    
    builder.add()
    
    builder.run()
