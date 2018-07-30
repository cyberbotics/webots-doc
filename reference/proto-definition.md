## PROTO Definition

### Interface

The PROTO definition defines exactly what the PROTO does in terms of the built-in nodes or of the instances of other PROTO nodes.
Here is the syntax for a PROTO definition:

```
PROTO protoName [ protoInterface ] { protoBody }
```

The interface is a sequence of field declarations which specify the types, names and default values for the PROTO's fields.
A field declaration has the following syntax:

```
field fieldType fieldName defaultValue
```

`field` is a reserved keyword, `fieldType` is one of: `SFNode, SFColor, SFFloat, SFInt32, SFString, SFVec2f, SFVec3f, SFRotation, SFBool, MFNode, MFColor, MFFloat, MFInt32, MFString, MFVec2f` and `MFVec3f`.
`fieldName` is a freely chosen name for this field and `defaultValue` is a literal default value that depends on `fieldType`.

Here is an example of PROTO definition:

```
PROTO MyProto [
  field SFVec3f    translation   0 0 0
  field SFRotation rotation      0 1 0 0
  field SFString   name          "my proto"
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

The type of the root node in the body of the PROTO definition (a [Solid](solid.md) node in this example) is called the *base type* of the PROTO.
The base type determines where instantiations of the PROTO can be placed in the scene tree.
For example, if the base type of a PROTO is [Material](material.md), then instantiations of the PROTO can be used wherever a [Material](material.md) mode can be used.
A PROTO whose base node is another PROTO is called *derived PROTO*.

### Field Value Restriction

If a field should have only a limited set of possible values, it is possible to specify them directly in the PROTO definition just after the field type like this:
```
PROTO MyProto [
  field SFVec3f                             translation   0 0 0
  field SFRotation                          rotation      0 1 0 0
  field SFString                            name          "my proto"
  field SFColor{0 0 0, 0.5 0.5 0.5, 1 1 1}  color         0.5 0.5 0.5
  field SFNode                              physics       NULL
  field MFNode{Solid{}, Transform{}}        extensionSlot []
]
```

In this example, the `color` field value can only be `0 0 0`, `0.5 0.5 0.5` or `1 1 1` and the `extensionSlot` field can only accept [Solid](../reference/solid.md) and [Transform](../reference/transform.md) nodes.

### IS Statements

Nodes in the PROTO definition may have their fields associated with the fields of the PROTO interface.
This is accomplished using IS statements in the body of the node.
An IS statement consists in the name of a field from a built-in node followed by the keyword IS followed by the name of one of the fields of the PROTO interface:

For example:

```
PROTO Bicycle [
  field SFVec3f    position   0 0 0
  field SFRotation rotation   0 1 0 0
  field SFString   name       "bicycle"
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
IS statements shall refer to fields defined in the PROTO declaration.
Multiple IS statements for the same field in the PROTO interface declaration is valid but it is discouraged to use fields containing [Solid](solid.md) or [Joint](joint.md) nodes multiple times.
This is because the system assumes that all the instances of a PROTO field are identical to work correctly but this cannot be guaranteed for these nodes given that due to internal changes or controller program instructions the instances' state could diverge.

An interface field that is not linked to an internal PROTO field with an IS may produce a warning when parsed.
This warning can be suppressed when declaring an interface field by using the `unconnectedField` keyword instead of `field` in the declaration.
This is useful when the value of an interface field is used to 'store' relevant data that a `Supervisor` controller may wish to access, such as the speed limit for a stretch of road, or an object's radioactivity.

It is an error for an IS statement to refer to a non-existent interface field.
It is an error if the type of the field being associated does not match the type declared in the PROTO's interface.
For example, it is illegal to associate an `SFColor` with an `SFVec3f`.
It is also illegal to associate a `SFColor` with a `MFColor` or vice versa.
Results are undefined if a field of a node in the PROTO body is associated with more than one field in the PROTO's interface.
