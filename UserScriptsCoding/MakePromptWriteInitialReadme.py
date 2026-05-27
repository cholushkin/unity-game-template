import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ScriptUtils")))
from Core.PromptContextCollector.PromptContextCollector import PromptContextCollector

PromptContextCollector(
    files=[],
    directories=["Documentation"],  # Wildcards and folders
    includes=["*.cs", "*.md"],
    ignores=[],
    template_path="UserScriptsCoding/TextTemplates/MakePromptWriteInitialReadmeTemplate.txt",  # Relative to project root
    template_vars={"project_name": "Prototype", "project_short_description": "Game prototype"},
    output_path="UserScriptsCoding/Outputs/PromptWriteInitialReadme.txt"
).run()