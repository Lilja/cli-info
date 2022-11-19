import re
import shutil
from typing import List, Optional
from cli_tools_info.utils import Tool, run_cmd, success, fail
import tabulate
import asyncio


async def _process_output_of_cmd(tool: Tool) -> List[str]:
    output = await run_cmd(tool)
    if tool.grep_string:
        grep_output = re.search(pattern=tool.grep_string, string=output)
        if grep_output:
            version = grep_output.group(0)
            return success(tool.name, version)
        else:
            return fail(tool.name, "Unable to find version")
    else:
        return success(tool.name, output)


async def _async_run(tools: List[Tool], headers: bool, table_fmt: Optional[str]):
    async def inner(tool: Tool):
        if tool.use_which:
            which_output = shutil.which(tool.name)
            if which_output:
                return await _process_output_of_cmd(tool)
            else:
                return fail(tool.name, "Command not found")
        else:
            return await _process_output_of_cmd(tool)

    data = await asyncio.gather(*[inner(x) for x in tools])
    if headers:
        tab_headers = ["CLI", "version"]
    else:
        tab_headers = []
    if not table_fmt:
        table_fmt = "simple"
    print(tabulate.tabulate(tabular_data=data, headers=tab_headers, tablefmt=table_fmt))


def run(tools: List[Tool], headers: bool = False, table_fmt: Optional[str] = None):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_async_run(tools=tools, headers=headers, table_fmt=table_fmt))
    loop.close()
