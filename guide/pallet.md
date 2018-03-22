# Pallet

## WoodenPallet

%figure "WoodenPallet"

![WoodenPallet-image](images/objects/pallet/WoodenPallet/model.png)

%end

```
WoodenPallet {
  SFVec3f    translation    0 0 0
  SFRotation rotation       0 1 0 0
  SFString   name           "wooden pallet"
  SFVec3f    size           0.8 0.14 1.2
  SFInt32    lathNumber     6
  SFFloat    lathWidth      0.08
  SFFloat    mass           0
  SFBool     boundingObject TRUE
  SFBool     locked         FALSE
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/pallet/protos/WoodenPallet.proto"

### Description

Simple and configurable wooden pallet.

## WoodenPalletStack

%figure "WoodenPalletStack"

![WoodenPalletStack-image](images/objects/pallet/WoodenPalletStack/model.png)

%end

```
WoodenPalletStack {
  SFVec3f    translation              0 0 0
  SFRotation rotation                 0 1 0 0
  SFString   name                     "wooden pallet stack"
  SFInt32    palletNumber             8
  SFVec3f    palletSize               0.8 0.14 1.2
  SFInt32    palletLathNumber         6
  SFFloat    palletLathWidth          0.08
  SFFloat    lateralMisalignment      0.1
  SFFloat    longitudinalMisalignment 0.05
  SFFloat    palletMass               0
  SFBool     boundingObject           TRUE
  SFBool     locked                   FALSE
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/pallet/protos/WoodenPalletStack.proto"

### Description

Simple and configurable wooden pallet stack

