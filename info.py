from cli_info.utils import Tool
from cli_info.versions import (
    LONG,
    SHORT,
    VERSION_WITH_THREE_NUMBERS_AND_DOTS,
    VERSION_WITH_V_PREFIX,
)

tools = [
    Tool(name="nvim", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(
        name="rust-analyzer", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS
    ),
    Tool(
        name="vue-language-server",
        args=LONG,
        grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS,
    ),
    Tool(
        name="typescript-language-server",
        args=LONG,
        grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS,
    ),
    Tool(name="pyright", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="black", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="yarn", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="tldr", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="curl", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="fd", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="jq", args=LONG),
    Tool(name="fzf", args=LONG),
    Tool(name="git", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="ssh", args=SHORT, pipe_stderr_to_stdout=True),
    Tool(name="fish", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="bat", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="rg", args=LONG, grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS),
    Tool(name="exa", args=LONG, grep_string=VERSION_WITH_V_PREFIX),
    Tool(
        name="fisher",
        args=LONG,
        use_which=False,
        wrap_with_fish=True,
        grep_string=VERSION_WITH_THREE_NUMBERS_AND_DOTS,
    ),
]

