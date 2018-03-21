## PROTO Design Guidelines

When creating your own PROTO nodes, we recommend that you follow these guidelines so that your new PROTO nodes will be well designed, easy-to-use and consistent with the existing PROTO nodes provided in Webots.

### Naming

The naming of a PROTO node is important and should be precise and explicit. Therefore, you should avoid abbreviations, numbers and vague terminology when naming a PROTO node. For example `SmallWoodenChair` is better than `SmallChair`, which is better than `Chair`, which is better than `Chair7`. PROTO names should use upper camel case, e.g., each word should begin with a capital letter with no intervening spaces.

### Recommended Fields for Object PROTO Nodes

#### translation and rotation

PROTO nodes are usually meant to represent real world objects, that can be placed at different locations and orientations in the world. Therefore a PROTO node should expose at least a `translation` and a `rotation` field to allow the users to move and rotate the object easily. The default value for the translation should be preferably the origin (0, 0, 0) and should correspond to the object in a normal position, e.g., laying on the floor rather than sinking into the floor. That means the origin of an object should not be at its 3D geometrical center, but rather in the middle of the surface in contact with the floor. The rotation axis should be already well positioned, e.g., usually vertical, so that when you rotate a building for example, you should simply change the angle value to have it rotate along its vertical axis.

#### enableBoundingObject

Bounding objects are used for collision detection. If you believe that an object won't collide with anything, it is convenient to be able to turn off collision detection to save computation time. Providing a PROTO node with a `enableBoundingObject` boolean field deserves this purpose. For example, in a scenario where a small robot is running on a table top in a living room, all the objects outside of the range of the robot, like the sofa, chairs, chandelier, TV set, etc. will never collide with the robot and hence could have their collision detection disabled. However, in some other scenarios, we want that the robot can collide with a chair, because the robot is running on the floor. Therefore such objects should have a `enableBoundingObject` field exposed to allow the users to decide whether they want to enable collision detection, depending on the specific simulation scenario.

#### enablePhysics

Because sometimes, we want to simulate the physical motion of an object and sometimes we want to save computation time by not simulating the physics of the object, it is good also to add a `enablePhysics` boolean field that allows the user to enable or disable physics simulation for an object. For example, a box may be meant to be moveable by a robot or may be glued to the floor or so heavy that it won't move. In that case, it is nice to be able to specify if we want to simulate the physical motion of that object or not. Not simulating the physics saves computation time and increase the stability of the simulation. However, some objects are not meant to move during a simulation. This includes buildings, traffic signs, trees, mailboxes, etc. Therefore such objects should not contain a `Physics` node and obviously should not expose a `enablePhysics` field.

#### Other Fields

In PROTO nodes that correspond to real world objects, it is not recommend to add fields such as `mass` or `scale`. This is because in real life, you cannot change the mass or the size of an object. And we don't want to encourage users of the PROTO nodes to do so, as it may lead to numerical instabilities. Some exceptions however exist. For example, it may be convenient to add a `size` field to a Matryoshka doll PROTO. Nevertheless, such a `size` field should be limited to a minimal and a maximal size or to a limited range of integer values. Therefore it could be either a floating point or an integer value.

For some PROTO nodes, it could be useful to expose a `color` field. For example, a car or a color pencil PROTO node could have a `color` field exposed. However, that should be limited to objects that are available in different colors. For example, it should not be used for a fire hydrant (usually always red) or a fork (usually always metallic grey). The `color` field may be specified as a `Color` node if any color is available or as a string (if only a limited number of colors is available for that object).

Depending on the object, a number of texture fields may be useful. For example a painting PROTO node could have the painting specified in a `picture` field and the frame texture specified in a `frame` field.

Generally, the number of exposed fields should be minimal in order to guarantee that the resulting object will be realistic and correspond to the original idea of the PROTO node. Also, floating point and integer values should be generally constrained between a minimum and a maximum value to ensure a realistic and stable result.

### Example

Here is a simple example of a good PROTO declaration:

```
ColorPencil {
  SFFloat    translation          0 0 0
  SFRotation rotation             0 1 0 0
  SFBool     enablePhysics        TRUE
  SFBool     enableBoundingObject TRUE
  SFColor    color                1 0 0     # defaults to red
  SFFloat    size                 0.2       # range in [0.02, 0.2]
}
```
