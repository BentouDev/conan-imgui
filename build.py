#!/bin/python3
import sys
sys.path.insert(0, './conan-base')
import build_base

build_base.DEBUG_MODE = False
build_base.PACKAGE_NAME = 'imgui'
build_base.GIT_DIR = "imgui-source"
build_base.ENV_PREFIX = "IMGUI"
build_base.STABLE_IN_GIT = True

build_base.username = "bentoudev"

if __name__ == '__main__':
    build_base.StartBuild()