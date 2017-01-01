from conans import CMake, ConanFile
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "russelltg")


class DefaultNameConan(ConanFile):
    name="QtBaseTest"
    requires = "extra-cmake-modules/5.29.0@%s/%s" % (username, channel)
    settings = "os", "arch", "compiler", "build_type"
    generators="cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run("cmake {} {}".format(self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . {}".format(cmake.build_config))
    
    def test(self):
        self.run("./bin/qtbasetest")
    
