# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_shelf_interfaces_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED shelf_interfaces_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(shelf_interfaces_FOUND FALSE)
  elseif(NOT shelf_interfaces_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(shelf_interfaces_FOUND FALSE)
  endif()
  return()
endif()
set(_shelf_interfaces_CONFIG_INCLUDED TRUE)

# output package information
if(NOT shelf_interfaces_FIND_QUIETLY)
  message(STATUS "Found shelf_interfaces: 0.0.0 (${shelf_interfaces_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'shelf_interfaces' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${shelf_interfaces_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(shelf_interfaces_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${shelf_interfaces_DIR}/${_extra}")
endforeach()
