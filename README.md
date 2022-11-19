# cli-tools-info

[![asciicast](https://asciinema.org/a/WUtnWUkMnrm5NyQ0Gi0c1CaHu.svg)](https://asciinema.org/a/WUtnWUkMnrm5NyQ0Gi0c1CaHu)

An overview of you cli tools, if they are installed and what version they are on.

## Usage
Create a python file that has the following contents
```python
#!/usr/bin/env python
from cli_tools_info import (
    Tool,
    LONG,
    VERSION_WITH_THREE_NUMBERS_AND_DOTS,
    run,
)

tools = [
    Tool(name="nvim", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
]
run(tools)
```

Run your file, likely: `./file`. You should get an output of the tool you are using depending on if it's installed or not.
