## C++ version of the libraries

If needed, it is possible to write the controller in C++ too. Indeed a C++
version of the [driver](driver-library.md#driver-library) and
[car](car-library.md#car-library) libraries are provided, they work the same way
as the C versions of the libraries (except that the `init` and `cleaup`
functions are called automatically from the constructor/destructor of the
[Driver](cpp-libraries.md#cppdriver) and [Car](cpp-libraries.md#cppcar))
classes. The methods names are very similar to the names of the C functions.

