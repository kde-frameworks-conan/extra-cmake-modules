#/usr/bin/python3

from conan.packager import ConanMultiPackager
import platform


if __name__ == "__main__":
    builder = ConanMultiPackager(visual_runtimes=["MT", "MD"])
    
    builder.builds.append({})
    
    builder.run()
