# ADD TAB_COMPONENT IN NODE PAGES

## FROM

\[C\+\+\]\(.*\) \[Java\]\(.*\) \[Python\]\(.*\) \[MATLAB\]\(.*\) \[ROS\]\(.*\)\n*```c(.*|\n)*?```

## TO

%tab-component

%tab "C"

```c
$1
```

%tab-end

%tab "C++"

```cpp
#include "<webots/TODO.hpp>`"

namespace webots {
  class TODO : public Device {
    // ...
  }
}
```

%tab-end

%tab "Python"

```python
from controller import TODO

class TODO (Device):
    # ...
```

%tab-end

%tab "Java"

```java
import com.cyberbotics.webots.controller.TODO;

public class TODO extends Device {
  // ...
}
```

%tab-end

%tab "MATLAB"

```matlab
% TODO
```

%tab-end

%tab "ROS"

| name | service/topic | data type | data type definition |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

%tab-end

%end
