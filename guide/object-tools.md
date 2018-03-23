# Tools

## Bolt

%figure "Bolt model in Webots."

![Bolt](images/objects/tools/Bolt/model.png)

%end

```
Bolt {
  SFVec3f translation 0 0.0131 0
  SFRotation rotation 0 0 1 0
  SFString name "bolt"
  SFString contactMaterial "default"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/Bolt.proto"

### Bolt Description

A threaded bolt.

## Hammer

%figure "Hammer model in Webots."

![Hammer](images/objects/tools/Hammer/model.png)

%end

```
Hammer {
  SFVec3f translation 0 0.014 0
  SFRotation rotation 0 1 0 0
  SFString name "hammer"
  SFString contactMaterial "default"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/Hammer.proto"

### Hammer Description

A 25cm asymmetric club hammer.

## Nut

%figure "Nut model in Webots."

![Nut](images/objects/tools/Nut/model.png)

%end

```
Nut {
  SFVec3f translation 0 0.004 0
  SFRotation rotation 0 1 0 0
  SFString name "nut"
  SFString contactMaterial "default"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/Nut.proto"

### Nut Description

A hexagonal nut.

## PaintBucket

%figure "PaintBucket model in Webots."

![PaintBucket](images/objects/tools/PaintBucket/model.png)

%end

```
PaintBucket {
  SFVec3f translation 0 0 0
  SFRotation rotation 0 1 0 0
  SFString name "paint bucket"
  SFString contactMaterial "default"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/PaintBucket.proto"

### PaintBucket Description

A 4kg bucket of paint, with HingeJoint-based handle.

## PlatformCart

%figure "PlatformCart model in Webots."

![PlatformCart](images/objects/tools/PlatformCart/model.png)

%end

```
PlatformCart {
  SFVec3f translation 0 0 0
  SFRotation rotation 0 1 0 0
  SFString name "platform cart"
  MFNode slot []
  SFNode physics Physics {}
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/PlatformCart.proto"

### PlatformCart Description

A platform cart with overall dimensions 90Lx50Wx85H cm.

## Screwdriver

%figure "Screwdriver model in Webots."

![Screwdriver](images/objects/tools/Screwdriver/model.png)

%end

```
Screwdriver {
  SFVec3f translation 0 0.012 0
  SFRotation rotation 0 1 0 0
  SFString name "screwdriver"
  SFString contactMaterial "default"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/Screwdriver.proto"

### Screwdriver Description

A Philips screwdriver. The blade and handle are balanced.

## Wrench

%figure "Wrench model in Webots."

![Wrench](images/objects/tools/Wrench/model.png)

%end

```
Wrench {
  SFVec3f translation 0 0 0
  SFRotation rotation 0 1 0 0
  SFString name "wrench"
  SFString contactMaterial "default"
}
```

> **File location**: "WEBOTS\_HOME/projects/objects/factory/tools/protos/Wrench.proto"

### Wrench Description

A 15cm Open-End wrench.
