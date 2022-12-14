# cli-tools-info

[![asciicast](https://asciinema.org/a/WUtnWUkMnrm5NyQ0Gi0c1CaHu.svg)](https://asciinema.org/a/WUtnWUkMnrm5NyQ0Gi0c1CaHu)

An overview of you cli tools, if they are installed and what version they are on.

## Usage
* `pip install cli-tools-info`

* Create a python file that has the following contents

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

* Run your file, likely: `./file`. You should get an output of the tool you are using depending on if it's installed or not.

## Requirements
* python>=3.8(runs asycncio)

### `run`-options
* `tools: List[Tool]`
* `headers: bool`, whether to use headers in the table formatted list
* `table_fmt: Optional[str] = "simple"`, what table formatting to send to `tabulate`. See `tablefmt` in `tabulate`. Default `simple`.

### Creator's `cli-info` file
[link](https://github.com/Lilja/dotfiles/blob/master/bin/cli-info)

## Showcase of usage/workflow in vim
[![asciicast](https://asciinema.org/a/538827.svg)](https://asciinema.org/a/538827)
