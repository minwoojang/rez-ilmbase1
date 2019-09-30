name = "ilmbase"

version = "2.2.1"

authors = [
    "Industrial Light & Magic"
]

description = \
    """
    Utility libraries from Industrial Light & Magic: Half, Imath, Iex, IlmThread.
    """

requires = [
    "gcc-6",
    "cmake-3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

#TODO: Use the SHA1 of the archive instead.
uuid = "ilmbase-2.2.1"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
