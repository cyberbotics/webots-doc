## Supervisor

Derived from `Robot`.


```
Supervisor {
  # no additional fields
}
```

### Description

A `Supervisor` is a special kind of `Robot` which is specially designed to
control the simulation. A `Supervisor` has access to extra functions that are
not available to a regular `Robot`. If a `Supervisor` contains devices then the
`Supervisor` controller can use them. Webots PRO is required to use the
`Supervisor` node.

### Supervisor Functions

As for a regular `Robot` controller, the `wb_robot_init()`, `wb_robot_step()`,
etc. functions must be used in a `Supervisor` controller.

