## Plugin Setup

You can add a new plugin, or edit the existing plugin, by using the menu `Tools
> Edit Physics Plugin`. After a physics plugin was created it must be associated
with the current ".wbt" file. This can be done in the Scene Tree: the
`WorldInfo` node has a field called `physics` which indicates the name of the
physics plugin associated with the current world. Select the `WorldInfo.physics`
field, then hit the `Select...` button. A dialog pops-up and lets you choose one
of the plugins available in the current project. Choose a plugin in the dialog
and then save the ".wbt" file.

Note that the `WorldInfo.physics` string specifies the name of the plugin source
and binary files without extension. The extension will be added by Webots
depending on the platform: it will be ".so" (Linux), ".dll" (Windows) or
".dylib" (Mac OS X) for the binary file. For example, this `WorldInfo` node:


```
WorldInfo {
  ...
  physics "my_physics"
  ...
}
```

specifies that the plugin binary file is expected to be at the location
"my_project/plugins/physics/my_physics/my_physics[.dll|.dylib|.so]" (actual
extension depending on the platform) and that the plugin source file should be
located in "my_project/plugins/physics/my_physics/my_physics[.c|.cpp]". If
Webots does not find the file there, it will also look in the
"WEBOTS_HOME/resources/projects/plugins" and
"WEBOTS_MODULES_PATH/projects/default/plugins" directories.

