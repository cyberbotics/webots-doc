# Introduction

This manual contains the specification of the nodes and fields of the ".wbt"
world description language used in Webots. It also specifies the functions
available to operate on these nodes from controller programs.

The Webots nodes and APIs are open specifications which can be freely reused
without authorization from Cyberbotics. The Webots API can be freely ported and
adapted to operate on any robotics platform using the remote-control and/or the
cross-compilation frameworks. Cyberbotics offers support to help developers
implementing the Webots API on real robots. This benefits to the robotics
community by improving interoperability between different robotics applications.

## Nodes and Functions

### Nodes

Webots nodes listed in this reference are described using standard VRML syntax.
Principally, Webots uses a subset of the VRML97 nodes and fields, but it also
defines additional nodes and fields specific to robotic definitions. For
example, the Webots `WorldInfo` and `Sphere` nodes have additional fields with
respect to VRML97.

### Functions

This manual covers all the functions of the controller API, necessary to program
robots. The C prototypes of these functions are described under the *SYNOPSIS*
tag. The prototypes for the other languages are available through hyperlinks or
directly in . The language-related particularities mentioned under the label
called *C++ Note, Java Note, Python Note, Matlab Note*, etc.

## ODE: Open Dynamics Engine

Webots relies on ODE, the Open Dynamics Engine, for physics simulation. Hence,
some Webots parameters, structures or concepts refer to ODE. The Webots
documentation does not, however, duplicate or replace the ODE documentation.
Hence, it is recommended to consult the ODE documentation to understand these
parameters, structures or concepts. This ODE documentation is available online
from the `ODE web site`.

