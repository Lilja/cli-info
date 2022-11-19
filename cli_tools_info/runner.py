import re
import shutil
from typing import List
from cli_tools_info.utils import Tool, run_cmd, success, fail

def _process_output_of_cmd(tool: Tool):
    output = run_cmd(tool)
    if tool.grep_string:
        grep_output = re.search(pattern=tool.grep_string, string=output)
        if grep_output:
            version = grep_output.group(0)
            success(tool.name, version)
    else:
        success(tool.name, output)


def run(tools: List[Tool]):
    for tool in tools:
        if tool.use_which:
            x = shutil.which(tool.name)
            if x:
                _process_output_of_cmd(tool)
            else:
                fail(tool.name, "not found")
        else:
            _process_output_of_cmd(tool)
