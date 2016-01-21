# PROTO

A PROTO defines a new node type in terms of built-in nodes or other PROTO nodes.
The PROTO interface defines the fields for the PROTO. Once defined, PROTO nodes
may be instantiated in the scene tree exactly like built-in nodes.

## PROTO Definition

### Interface

The PROTO definition defines exactly what the PROTO does in terms of the built-
in nodes or of the instances of other PROTO nodes. Here is the syntax for a
PROTO definition:


```
PROTO protoName [ protoInterface ] { protoBody }
```

The interface is a sequence of field declarations which specify the types, names
and default values for the PROTO's fields. A field declaration has this syntax:


```
field fieldType fieldName defaultValue
```

where `field` is a reserved keyword, `fieldType` is one of: `SFNode, SFColor,
SFFloat, SFInt32, SFString, SFVec2f, SFVec3f, SFRotation, SFBool, MFNode,
MFColor, MFFloat, MFInt32, MFString, MFVec2f` and `MFVec3f`. `fieldName` is a
freely chosen name for this field and `defaultValue` is a literal default value
that depends on `fieldType`.

Here is an example of PROTO definition:


```
PROTO MyProto [
  field SFVec3f    translation   0 0 0
  field SFRotation rotation      0 1 0 0
  field SFColor    color         0.5 0.5 0.5
  field SFNode     physics       NULL
  field MFNode     extensionSlot []
]
{
  Solid {
    ...
  }
}
```

The type of the root node in the body of the PROTO definition (a `Solid` node in
this example) is called the *base type* of the PROTO. The base type determines
where instantiations of the PROTO can be placed in the scene tree. For example,
if the base type of a PROTO is `Material`, then instantiations of the PROTO can
be used wherever a `Material` mode can be used. A PROTO whose base node is
another PROTO is called *derived PROTO*.

### IS Statements

Nodes in the PROTO definition may have their fields associated with the fields
of the PROTO interface. This is accomplished using IS statements in the body of
the node. An IS statement consists of the name of a field from a built-in node
followed by the keyword IS followed by the name of one of the fields of the
PROTO interface:

For example:


```
PROTO Bicycle [
  field SFVec3f    position   0 0 0
  field SFRotation rotation   0 1 0 0
  field SFColor    frameColor 0.5 0.5 0.5
  field SFBool     hasBrakes  TRUE
]
{
  Solid {
    translation IS position
    rotation IS rotation
    ...
    children [
      ...
    ]
    ...
  }
}
```

IS statements may appear inside the PROTO definition wherever fields may appear.
IS statements shall refer to fields defined in the PROTO declaration. Multiple
IS statements for the same field in the PROTO interface declaration is valid.

It is an error for an IS statement to refer to a non-existent interface field.
It is an error if the type of the field being associated does not match the type
declared in the PROTO's interface. For example, it is illegal to associate an
`SFColor` with an `SFVec3f`. It is also illegal to associate a `SFColor` with a
`MFColor` or vice versa. Results are undefined if a field of a node in the PROTO
body is associated with more than one field in the PROTO's interface.

## PROTO Instantiation

Each PROTO instance can be considered to be a complete copy of the PROTO, with
its interface fields and body nodes. PROTO are instantiated using the standard
node syntax, for example:


```
Bicycle {
  position   0 0.5 0
  frameColor 0 0.8 0.8
  hasBrakes  FALSE
}
```

When PROTO instances are read from a ".wbt" file, field values for the fields of
the PROTO interface may be given. If given, the field values are used for all
nodes in the PROTO definition that have IS statements for those fields.

## Example

A complete example of PROTO definition and instantiation is provided here. The
PROTO is called `TwoColorChair`; it defines a simple chair with four legs and a
seating part. For simplicity, this PROTO does not have bounding objects nor
`Physics` nodes. A more complete example of this PROTO named `SimpleChair` is
provided in Webots distribution.

The `TwoColorChair` PROTO allows to specify two colors: one for the legs and one
for the seating surface of the chair. The interface also defines a `translation`
field and a `rotation` field that are associated with the equally named fields
of the PROTO's `Solid` base node. This allows to store the position and
orientation of the PROTO instances.

"TwoColorChair.proto":


```
# A two-color chair

PROTO TwoColorChair [
  field SFVec3f    translation       0 0.91 0
  field SFRotation rotation          0 1 0 0
  field SFColor    legColor          1 1 0
  field SFColor    seatColor         1 0.65 0 
  field SFNode     seatGeometry      NULL 
  field MFNode     seatExtensionSlot []       ]
{
  Solid {
    translation IS translation
    rotation IS rotation
    children [
      Transform {
        translation 0 0 -0.27
        children IS seatExtensionSlot
      }
      Transform {
        translation 0 -0.35 0
        children [
          Shape {
            appearance Appearance {
              material Material { diffuseColor IS seatColor }
            }
            geometry IS seatGeometry
          }
        ]
      }
      Transform {
        translation 0.25 -0.65 -0.23
        children [
          DEF LEG_SHAPE Shape {
            appearance Appearance {
              material Material { diffuseColor IS legColor }
            }
            geometry Box { size 0.075 0.52 0.075 }
          }
        ]
      }
      Transform {
        translation -0.25 -0.65 -0.23
        children [ USE LEG_SHAPE ]
      }
      Transform {
        translation 0.25 -0.65 0.2
        children [ USE LEG_SHAPE ]
      }
      Transform {
        translation -0.25 -0.65 0.2
        children [ USE LEG_SHAPE ]
      }
    ]
  }
}
```

As you can observe in this example, it is perfectly valid to have several IS
statement for one interface field (`seatColor`), as long as the types match. It
is also possible to use IS statements inside a defined (DEF) node and then to
reuse (USE) that node. This is done here with the `diffuseColor IS legColor`
statement placed inside the `DEF LEG_SHAPE Shape` node which is then reused
(USE) several times below.

The "ProtoInstantiationExample.wbt" file below exemplifies the instantiation of
this PROTO. PROTO nodes are instantiated using the regular node syntax. Fields
with the default value can be omitted. Fields which value differ from the
default must be specified.

"TwoChairs.wbt":


```
#VRML_SIM V6.0 utf8

WorldInfo {
}
Viewpoint {
  orientation 0.628082 0.772958 0.089714 5.69177
  position -0.805359 1.75254 2.75772
}
Background {
  skyColor [
    0.4 0.7 1
  ]
}
DirectionalLight {
  direction -0.3 -1 -0.5
  castShadows TRUE
}
TwoColorChair {
  seatGeometry Cylinder {
    height 0.075
    radius 0.38
  }
}
TwoColorChair {
  translation 1.2 0.91 0
  seatColor 0.564706 0.933333 0.564706
  seatGeometry Box { size 0.6 0.075 0.52 }
  seatExtensionSlot [
    Shape {
      appearance Appearance {
        material Material { diffuseColor 0.564706 0.933333 0.564706}
      }
      geometry Box { size 0.6 0.67 0.0275 }
    }
  ]
}

```

The "TwoChairs.wbt" file once loaded by Webots appears as shown in .

As you can observe in this example, defining MFNode fields in the PROTO
interface allows to reuse the same model for slightly different objects or
robots. Extenstion slots like `seatExtensionSlot` field could, for example, be
used to add additional devices to a base robot without needing to copy the robot
definition or creating a new PROTO.

![Two instances of the TwoColorChair PROTO in Webots](png/two_chairs_v7-2-0.png)
**Two instances of the TwoColorChair PROTO in Webots**

## Procedural PROTO nodes

The expressive power of PROTO nodes can be significantly improved by extending
them using a scripting language. In this way, the PROTO node may contain
constants, mathematic expressions, loops, conditional expressions, randomness,
and so on.

### Scripting language

The used scripting language is `Lua`. Introducing and learning Lua is outside
the scope of this document. Please refer to the `Lua documentation` for
complementary information.

### Template Engine

A template engine is used to evaluate the PROTO according to the fields values
of the PROTO, before being loaded in Webots. The template engine used is `slt2`
(under the MIT license).

### Programming Facts

### Example


```

#VRML_SIM V8.1.0 utf8

PROTO SimpleStairs [
  field SFVec3f    translation 0 0 0
  field SFRotation rotation    0 1 0 0
  field SFInt32    nSteps      10
  field SFVec3f    stepSize    0.2 0.2 0.8
  field SFNode     appearance  NULL
]
{
  # template statements can be used from here
  %{
    -- a template statement can be written on several lines
    if fields.nSteps.value lt 1 then
      print('nSteps should be strictly positive')
    end
    
    -- print the path to this proto
    print(context.proto)
    
    if fields.stepSize.value ~= fields.stepSize.defaultValue then
      print('The step size used is not the default one')
    end

    -- print the first texture url of the ImageTexture node
    -- inside the Appearance node
    if fields.appearance.value and fields.appearance.value.fields.texture.value then
      -- The following test is true: fields.appearance.value.fields.texture.value.node_name == "ImageTexture"
      print (fields.appearance.value.fields.texture.value.url[0])
    end
  }%
  Solid {
    translation IS translation
    rotation IS rotation
    children [
      DEF SIMPLE_STAIRS_GROUP Group {
        children [
        %{ for i = 0, (fields.nSteps.value - 1) do }%
          %{ x = i * fields.stepSize.value.x }%
          %{ y = i * fields.stepSize.value.y + fields.stepSize.value.y / 2 }%
            Transform {
              translation %{=x}% %{=y}% 0
              children [
                Shape {
                  appearance IS appearance
                  geometry Box {
                    size IS stepSize
                  }
                }
              ]
            }
          %{ end }%
        ]
      }
    ]
    boundingObject USE SIMPLE_STAIRS_GROUP
  }
  # template statements can be used up to there
}
     
```

## Using PROTO nodes with the Scene Tree

Several PROTO examples are packaged with Webots. Instances of these PROTO nodes
can be added to the simulation with the Scene Tree buttons. Note that currently
the Scene Tree allows the instantiation but not the definition of PROTO nodes.
PROTO definitions must be created or modified manually in ".proto" files.

### PROTO Directories

In order to make a PROTO available to Webots, the complete PROTO definition must
be placed in a ".proto" file. Each ".proto" file can contain the definition for
only one PROTO, and each file must be saved under the name
lt*PROTOName*gt".proto", where *PROTOName* is the name of the PROTO as specified
after the PROTO keyword (case-sensitive). For example the above `TwoColorChair`
PROTO must be saved in a file name "TwoColorChair.proto".

The ".proto" file should be placed in the "protos" subdirectory of the current
project directory. By definition, the current project directory is the parent
directory of the "worlds" directory that contains the currently opened ".wbt"
file. The  shows where ".proto" files are stored in a project directory.

![PROTO directory in a project directory structure](png/protos_directory_structure.png)
**PROTO directory in a project directory structure**

Note that inside the "protos" directory, the number of subdirectories and their
names is free. The user can assign directory names for practical classification
reasons; but the names do not influence how PROTO files are searched. The whole
subdirectory tree is always searched recursively.

In addition to the current project directory, Webots does also manage a
*default* project directory. This directory is structurally similar to the
current project directory (see above) but it is located inside Webots
distribution. In the default project directory there is also a "protos"
subdirectory that provides Webots standard PROTO nodes. These standard PROTO
nodes should normally not be modified by the user. Note that ".proto" files will
be searched first in the current project directory and then in the default
project directory.

### Add a Node Dialog

If a PROTO is saved in a file with proper name and location, it should become
visible in the `Add a node` dialog that can be invoked from the `Scene Tree`. In
the dialog, the PROTO nodes are organized using the same directory hierarchy
found in the project's and Webots's "protos" folders. However this dialog shows
a PROTO only if its *base type* is suitable for the chosen insertion point. For
example, a PROTO whose base type is `Material` cannot be inserted in a
`boundingObject` field. In  you can see how the `TwoColorChair` PROTO appears in
the dialog. Note that, the dialog's text pane is automatically filled with any
comment placed at the beginning of the ".proto" file.

![Adding an instance of the TwoColorChair PROTO](png/add_proto.png)
**Adding an instance of the TwoColorChair PROTO**

Icons can be used to better illustrate PROTO nodes. A PROTO icon must be stored
in a 128 x 128 pixels ".png" file. The file name must correspond to that of the
PROTO plus the ".png" extension and it must be stored in the "icons"
subdirectory of the "protos" directory (see ). Note that it is possible to
create the ".png" files directly with Webots's menu `File > Take Screenshot...`.
Then the image should be cropped or resized to 128 x 128 pixels using an image
editor.

### Using PROTO Instances

If you hit the `Add` button, the PROTO instance is added to the `Scene Tree`. In
the `Scene Tree`, PROTO instances are represented with a different color than
built-in nodes (see ). PROTO fields can be manipulated exactly like built-in
node fields.

![Scene Tree with two instances of the TwoColorChair PROTO](png/scene_tree_with_protos.png)
**Scene Tree with two instances of the TwoColorChair PROTO**

## PROTO Scoping Rules

PROTO names must be unique: defining a PROTO with the same name as another PROTO
or a built-in node type is an error. A ".proto" file can contain only one PROTO
definition. A PROTO node can be defined in terms of other PROTO nodes. However,
instantiation of a PROTO inside its own definition is not permitted (i.e.,
recursive PROTO are illegal). An IS statement refers to a field in the interface
of the same PROTO, in the same file. Fields declared in the interface can be
passed to sub-PROTO nodes using IS statements.

A ".proto" file establishes a DEF/USE name scope separate from the rest of the
scene tree and separate from any other PROTO definition. Nodes given a name by a
DEF construct inside the PROTO may not be referenced in a USE construct outside
of the PROTO's scope. Nodes given a name by a DEF construct outside the PROTO
scope may not be referenced in a USE construct inside the PROTO scope.

In case of derived PROTO nodes, it is allowed to declare in the interface a
field with the same name as a base PROTO field only if it is not associated with
any other field than the homonymous base PROTO field. This means that it is
possible to use the derived field in template statements without restrictions,
but if it used in a IS statement then the two identifiers before and after the
IS keyword have to match. If the derived field has a unique name then no
restrictions apply.

## PROTO hidden fields

Regular PROTO fields let you change, save and restore, chosen characteristics of
your model. In constrast, PROTO encapsulation prevent field values which are not
accessible through PROTO fields, but which may change during simulation, from
being saved and subsequently restored. Still, this is not true for all field
values, since Webots save for you hidden PROTO fields which are bound to change
over simulation time. Namely the `translation` and `rotation` fields of `Solid`
nodes as well as the `position` fields of `Joint` nodes are saved as hidden
PROTO fields in the field scope of every top-level PROTO. In case of `solid
merging`, note that hidden `translation` and `rotation` fields are saved only
for the `Solid` placed at the top of the solid assembly.

As in the case of non-PROTO objects, initial velocities of physical subparts of
a PROTO are saved and can be subsequently restored when reloading your world
file. Like the other hidden fields, velocities are saved in the field scope of
every top-level PROTO.

Each hidden field appends an index to its name which encodes the location of the
`Solid` to which it belongs inside the tree hierarchy rooted at the the PROTO
node. This index corresponds is the depth-first pre-order traversal index of the
`Solid` in this tree. If a hidden field corresponds to the `position` of
`Joint`, an additional index is appended to its name, namely the index of the
`Joint` in the list of `Joint` nodes originating from the `Solid` sorted by
means of pre-order traversal. As an example, we display below an excerpt of
"projects/robots/pioneer/pioneer3at/worlds/pioneer3at.wbt" when saved after one
simulation step. ` DEF PIONEER_3AT Pioneer3at { hidden position_0_0 -2.88177e-07
hidden position_0_1 -4.63679e-07 hidden position_0_2 -3.16282e-07 hidden
position_0_3 -4.91785e-07 hidden linearVelocity_0 -0.00425142 -0.0284347
0.0036279 hidden angularVelocity_0 0.0198558 -9.38102e-07 0.0232653 hidden
translation_2 -0.197 4.04034e-06 0.1331 hidden rotation_2 -0.013043 0.00500952
0.999902 -2.88177e-07 hidden linearVelocity_2 -0.00255659 -0.0214607 0.00218164
hidden angularVelocity_2 0.0198598 -9.84272e-07 0.0232733 hidden translation_3
0.197 7.85063e-06 0.1331 hidden rotation_3 -0.00949932 0.00367208 0.999948
-4.63679e-07 hidden linearVelocity_3 -0.00255694 -0.0330774 0.00218161 hidden
angularVelocity_3 0.0198623 -9.92987e-07 0.0232782 hidden translation_4 -0.197
4.64107e-06 -0.1331 hidden rotation_4 -0.011884 0.0045545 0.999919 -3.16282e-07
hidden linearVelocity_4 -0.00255674 -0.0232922 0.00218172 hidden
angularVelocity_4 0.0198602 -9.84272e-07 0.0232741 hidden translation_5 0.197
8.45135e-06 -0.1331 hidden rotation_5 -0.00895643 0.00345587 0.999954
-4.91785e-07 hidden linearVelocity_5 -0.0025571 -0.0349089 0.00218169 hidden
angularVelocity_5 0.0198627 -9.92987e-07 0.023279 translation 2.61431 0.109092
18.5514 rotation -0.000449526 1 0.000227141 -2.66435 controller
"obstacle_avoidance_with_lidar" extensionSlot [ SickLms291 { translation 0 0.24
-0.136 pixelSize 0 } ] ` The names of the first six hidden fields all contain 0
as primary index, which is the index of the `Pioneer3at` PROTO itself. The
additional secondary indices for the four hidden `position` fields correspond to
the four `HingeJoint` nodes used for the wheels and numbered by means of pre-
order traversal. There is no hidden field associated the `Solid` node with index
1, namely the `SickLms291` PROTO, since its relative position and orientation
are kept fixed during simulation. The indices ranging from 2 to 5 correspond to
the four `Solid` wheels of the `Pioneer3at`.

