## Slot


```
Slot {
  field     SFString type      ""
  vrmlField SFNode   endPoint  NULL
}
```

### Description

`Slot` nodes always works with pairs, only a second `Slot` can be added in the
`endPoint` field of a `Slot` before to be able to add any node in the `endPoint`
field of the second `Slot`. Furthermore, the second `Slot` can be added only if
it has the same `type` as the first one.  The `Slot` node is particularly
usefull with PROTOs, it allows the user to constrain the type of nodes that can
be added in an extension field of the PROTO. Imagine for example that you have
an armed robot in which you can plug different kinds of hands. In order to do so
you will put the hand as an extension field of your robot, you will then be able
to add all the different PROTOs of hand that you have made. But nothing prevent
you to add a PROTO of table in the hand extension field. The `Slot` is made for
preventing this kind of problems. By encapsulating your extension field in a
`Slot` and using the `Slot` node as base node for all your hands PROTOs and
defining the same `type` for the field `Slot` and the PROTO `Slot`, only hands
can be inserted in the extension field. This is illustrated in the `example`
section.

### Field Summary

### Example

If you want to write a proto of a robot called `MyRobot` that accepts only hands
in its field `handExtension`, you have to set the field `handExtension` to be
the `endPoint` of a `Slot`.


```
PROTO MyRobot [
  field SFNode handExtension NULL
]
Robot {
  children [
    Slot {
      type "robotHand"
      endPoint IS handExtension
    }
    ...
  ]
}
```

Then any PROTO of a hand needs to use the `Slot` as base node and the `type` of
this `Slot` should match the one in `MyRobot`.


```
PROTO RobotHand [
]
{
  Slot {
    type "robotHand"
    endPoint Solid {
      ...
    }
  }
}
```

