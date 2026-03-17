import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../ScriptUtils")))
from Core.GitSubmoduleManager.GitSubmoduleManager import GitSubmoduleManager


GitSubmoduleManager().force_update_all_submodules()