import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ScriptUtils")))
from Core.PromptContextCollector.PromptContextCollector import PromptContextCollector

PromptContextCollector(
    directories=[
        "Unity/Game/Assets/Libs/uconsole"
        ],  # Wildcards and folders
    includes=["*.cs"],
    files=[],
    ignores=[],    
    output_path="UserScriptsCoding/Outputs/UconsoleState.txt"
).run()