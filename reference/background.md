## Background

```
Background {
  MFString backUrl   [ ]          # list of Image URLs
  MFString bottomUrl [ ]          # list of Image URLs
  MFString frontUrl  [ ]          # list of Image URLs
  MFString leftUrl   [ ]          # list of Image URLs
  MFString rightUrl  [ ]          # list of Image URLs
  MFString topUrl    [ ]          # list of Image URLs
  MFColor  skyColor  [ 0 0 0 ]    # any color
}
```

The [Background](#background) node defines the background used for rendering the 3D world.
The `skyColor` field defines the red, green and blue components of this color.
Only the three first float values of the `skyColor` field are used.

The `backUrl`, `bottomUrl`, `frontUrl`, `leftUrl`, `rightUrl`, and `topUrl` fields specify a set of images that define a background panorama, between the ground/sky backdrop and the world's geometry.
The panorama consists of six images, each of which is mapped onto the faces of an infinitely large cube centered in the local coordinate system.
The images are applied individually to each face of the cube; the entire image goes on each face.
On the front, back, right, and left faces of the cube, when viewed from the inside with the Y-axis up, the texture is mapped onto each face with the same orientation as the if image was displayed normally in 2D.
On the top face of the cube, when viewed from the inside looking up along the +Y axis with the +Z axis as the view up direction, the texture is mapped onto the face with the same orientation as the if image was displayed normally in 2D.
On the bottom face of the box, when viewed from the inside down the -Y axis with the -Z axis as the view up direction, the texture is mapped onto the face with the same orientation as the if image was displayed normally in 2D.
