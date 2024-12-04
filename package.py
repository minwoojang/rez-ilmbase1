name = "ilmbase"

version = "2.3.0"

authors = [
    "Industrial Light & Magic"
]

description = \
    """
    Utility libraries from Industrial Light & Magic: Half, Imath, Iex, IlmThread.
    """

requires = [
    "cmake-3+",
    "gcc-11"
]


variants = [['platform-linux', 'arch-x86_64']]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "ilmbase-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.prepend("{root}/lib/pkgconfig")

    # Helper environment variables.
    env.ILMBASE_INCLUDE_PATH.set("{root}/include")
    env.ILMBASE_LIBRARY_PATH.set("{root}/lib")
