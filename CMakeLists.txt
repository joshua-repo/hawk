cmake_minimum_required(VERSION 3.12)
project(hawk-minimal)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE Debug)  # Enable debug symbols

include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.12.0  # or latest stable
)
FetchContent_MakeAvailable(pybind11)

FetchContent_Declare(
  CLI11
  GIT_REPOSITORY https://github.com/CLIUtils/CLI11.git
  GIT_TAG        v2.4.2
)
FetchContent_MakeAvailable(CLI11)

FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG        v1.13.0
)
FetchContent_MakeAvailable(spdlog)

# Core library
add_library(hawk_core_lib
    src/cpp/lib/portfolio.cpp
    src/cpp/lib/trade.cpp
)

target_include_directories(hawk_core_lib PUBLIC src/cpp/include)
target_compile_options(hawk_core_lib PRIVATE -g -O0)  # Debug flags

# Python bindings
pybind11_add_module(hawk_core 
    src/cpp/bindings/python_bindings.cpp
    src/cpp/lib/portfolio.cpp
    src/cpp/lib/trade.cpp
)

target_include_directories(hawk_core PRIVATE src/cpp/include)
target_compile_definitions(hawk_core PRIVATE VERSION_INFO="1.0.0")
target_compile_options(hawk_core PRIVATE -g -O0)  # Debug flags

# Optional: Create a simple C++ test executable for debugging
add_executable(hawk_portfolio_cli
    src/cpp/test/hawk_test.cpp
)
target_link_libraries(hawk_portfolio_cli PRIVATE hawk_core_lib CLI11::CLI11 spdlog::spdlog)
target_include_directories(hawk_portfolio_cli PRIVATE src/cpp/include)

