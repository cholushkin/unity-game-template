import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ScriptUtils")))
from Core.PromptContextCollector.PromptContextCollector import PromptContextCollector

PromptContextCollector(
    directories=[],
    files=[
      ".gitmodules", # git submodules
      "Unity/Game/Packages/manifest.json",  # UPM
      "Unity/Game/Assets/packages.config"  # NuGet
    ],
    includes=[],
    ignores=[],
    template_path="UserScriptsCoding/TextTemplates/MakePromptWriteProjectDependenciesTemplate.txt",  # Relative to project root
    template_vars={"additional_subdirectories": ""}, # todo: get directory listing here
    output_path="UserScriptsCoding/Outputs/PromptWriteProjectDependencies.txt"
).run()