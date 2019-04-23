from conans import ConanFile, CMake, tools
import os, platform

imgui_version = os.getenv('IMGUI_VERSION', '0.0')
imgui_commit = os.getenv('IMGUI_COMMIT', '')

class IMGUIConan(ConanFile):
    name = "imgui"
    license = "MIT"
    url = "https://github.com/BentouDev/conan-imgui"
    version = imgui_version
    commit = imgui_commit

    description = "Bloat-free Immediate Mode Graphical User interface for C++ with minimal dependencies"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = ["CMakeLists.txt","imgui-source/*"]

    options = {"shared" : [True, False], "fPIC" : [True, False], "build_type": ["Release", "Debug", "RelWithDebInfo", "MinSizeRel"]}
    default_options = "build_type=MinSizeRel", "shared=False", "fPIC=True"

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def package_id(self):
        self.info.include_build_settings()
        self.info.settings.compiler
        self.info.settings.arch
        self.info.settings.build_type

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake
    
    def build(self):
        # Workaround for conan choosing cmake embedded in Visual Studio
        if platform.system() == "Windows" and 'AZURE' in os.environ:
            cmake_path = '"C:\\Program Files\\CMake\\bin\\cmake.exe"'
            print (' [DEBUG] Forcing CMake : ' + cmake_path)
            os.environ['CONAN_CMAKE_PROGRAM'] = cmake_path

        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
        self.copy(pattern="LICENSE.txt", dst="licenses", src="imgui-source")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
