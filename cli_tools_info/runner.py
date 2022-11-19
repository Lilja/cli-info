import re
import shutil
from typing import List
from cli_tools_info.utils import Tool, run_cmd, success, fail
import tabulate


def _process_output_of_cmd(tool: Tool) -> List[str]:
    output = run_cmd(tool)
    if tool.grep_string:
        grep_output = re.search(pattern=tool.grep_string, string=output)
        if grep_output:
            version = grep_output.group(0)
            return success(tool.name, version)
        else:
            return fail(tool.name, "Unable to find version")
    else:
        return success(tool.name, output)


def run(tools: List[Tool]):
    def inner():
        for tool in tools:
            if tool.use_which:
                which_output = shutil.which(tool.name)
                if which_output:
                    yield _process_output_of_cmd(tool)
                else:
                    yield fail(tool.name, "Command not found")
            else:
                yield _process_output_of_cmd(tool)

    print(tabulate.tabulate(tabular_data=[row for row in inner()]))
