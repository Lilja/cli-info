import os
from typing import Optional
from dataclasses import dataclass
import asyncio

ESC = "\033["
RED = "1;31"
BLUE = "1;34"
CYAN = "1;36"
GREEN = "32"
RESET = "0;0"
BOLD = "1"
UNDERLINE = "4"
ANSI_EXIT_CHAR = "m"
RESET = ESC + "0;0" + ANSI_EXIT_CHAR
CHECKMARK = "✅"
CROSS = "❌"


@dataclass
class Tool:
    name: str
    args: str
    use_which: bool = True
    pipe_stderr_to_stdout: bool = False
    grep_string: Optional[str] = None
    wrap_with_fish: bool = False


def color(*items):
    return ESC + ";".join(items) + ANSI_EXIT_CHAR


async def run_cmd(tool: Tool) -> str:
    cmd = " ".join(
        [
            'fish -c "' if tool.wrap_with_fish else "",
            tool.name,
            tool.args,
            '"' if tool.wrap_with_fish else "",
            "2>&1" if tool.pipe_stderr_to_stdout else "",
        ]
    )
    proc = await asyncio.subprocess.create_subprocess_shell(
        cmd=cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    if stderr:
        return stderr.decode("utf-8")
    if stdout:
        return stdout.decode("utf-8")

    raise Exception("no stderr or stdout: " + tool.name)



def success(msg1, msg2):
    return [CHECKMARK + " " + color(GREEN, BOLD) + msg1 + RESET, msg2]


def fail(msg1, msg2):
    return [CROSS + " " + color(RED, BOLD) + msg1 + RESET, msg2]
