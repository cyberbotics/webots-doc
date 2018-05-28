# ADD TAB_COMPONENT IN NODE PAGES

## FROM

\[C\+\+\]\(.*\) \[Java\]\(.*\) \[Python\]\(.*\) \[MATLAB\]\(.*\) \[ROS\]\(.*\)\n*(```c?(.*|\n)*?```)

## TO

%tab-component

%tab "C"

$1

%tab-end

%tab "C++"

```cpp
#include <webots/CLASS_NAME.hpp>

namespace webots {
  class CLASS_NAME : public Device {
    // ...
  }
}
```

%tab-end

%tab "Python"

```python
from controller import CLASS_NAME

class CLASS_NAME (Device):
    # ...
```

%tab-end

%tab "Java"

```java
import com.cyberbotics.webots.controller.CLASS_NAME;

public class CLASS_NAME extends Device {
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
