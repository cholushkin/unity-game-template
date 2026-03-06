import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ScriptUtils")))
from Core.GitSubmoduleManager.GitSubmoduleManager import GitSubmoduleManager


GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/coding-convention.git", 
    "CodingConvention")
    
GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/gamelib.git", 
    "Unity/Game/Assets/Libs/Gamelib")
    
GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/TinyColor.git", 
    "Unity/Game/Assets/Libs/TinyColor")
    
GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/towergenerator.git", 
    "Unity/Game/Assets/Libs/TowerGenerator")
    
GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/uconsole.git", 
    "Unity/Game/Assets/Libs/uconsole")

GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/umoonsharp.git", 
    "Unity/Game/Assets/Libs/UMoonSharp")

GitSubmoduleManager().add_git_submodule(
    "https://github.com/cholushkin/VersionHistory.git", 
    "Unity/Game/Assets/Libs/VersionHistory")
