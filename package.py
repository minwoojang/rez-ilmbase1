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
    "gcc-6+",
    "cmake-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "ilmbase-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")

    # Helper environment variables.
    env.ILMBASE_INCLUDE_PATH.set("{root}/include")
    env.ILMBASE_LIBRARY_PATH.set("{root}/lib")
