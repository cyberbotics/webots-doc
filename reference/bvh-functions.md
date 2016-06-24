# BVH Functions

The Biovision Hierarchy animation file format (.bvh) was developed to capture and distribute motion capture data, typically of humans performing actions such as walking, running, etc.
This file format was developed by the Biovision company (now defunct).
There are several freely available human motion capture data resources in BVH format, which can be used for making animations.
This BVH utility is provided to enable reading BVH files and animate human models defined as [Skin](#skin) node in Webots.

The BVH files define a skeleton in the form of hierarchy of bones, and a time series of joint angles for each joint in the skeleton. Note that this skeleton is not necessarily the same as the skeleton associated with a Webots [Skin](#skin) node, since they come from different sources.
This library provides functions to adapt and re-target BVH motion data to Webots [Skin](#skin).


## Sections
- [BVH Utility Functions](bvh.md)
