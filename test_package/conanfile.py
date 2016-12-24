from conans import CMake, ConanFile
import os


channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "russelltg")


class DefaultNameConan(ConanFile):
    name="KConfigTest"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "extra-cmake-modules/5.29.0@%s/%s" % (username, channel)

    def build(self):
        #cmake = CMake(self.settings)
        
        #self.run('echo %s' % self.conanfile_directory)
        #self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        #self.run("cmake --build . %s" % cmake.build_config)
        pass
    def test(self):
        pass
    