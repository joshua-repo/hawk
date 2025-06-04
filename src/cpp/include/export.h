#pragma once

// Export macros for building shared libraries
#ifdef _WIN32
    #ifdef HAWK_BUILDING_DLL
        #define HAWK_API __declspec(dllexport)
    #elif defined(HAWK_USING_DLL)
        #define HAWK_API __declspec(dllimport)
    #else
        #define HAWK_API
    #endif
#else
    #define HAWK_API __attribute__((visibility("default")))
#endif