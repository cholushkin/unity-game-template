# Unity Project Dependency Analysis

## Introduction

Managing dependencies effectively is critical to building robust, maintainable, and scalable Unity projects. Large-scale projects, particularly those leveraging advanced asynchronous execution models, modern user interface frameworks, and decoupled architectural patterns, rely on multi-channel dependency streams to integrate engine systems, industry-standard .NET libraries, and custom reusable toolsets.

This project structures its dependency workflows across four specialized pipelines:

1. **Git Submodules:** Facilitates seamless sharing of internal core packages, utility repositories, and structural design configurations across multiple independent game projects.
2. **Unity Package Manager (UPM):** Delivers official engine features, essential editor interfaces, and direct integration with cutting-edge open-source tools via remote Git URLs.
3. **NuGet Packages (via NuGetForUnity):** Bridges the environment with ecosystem-standard .NET libraries, ensuring zero-allocation operations, data structures, and standard logging abstractions are native to the runtime environment.
4. **Manually Tracked Source Libraries:** Utilized explicitly for highly stable third-party utilities that deploy assets or specific localized files directly into the project directory hierarchy.

---

## Dependencies Table

| Source | Dependency Name | Version | URL | Notes |
| --- | --- | --- | --- | --- |
| **Git Submodule** | ScriptUtils | — | [Link](https://github.com/cholushkin/script-utils.git) | Internal development automation and script tools. |
| **Git Submodule** | Gamelib | — | [Link](https://github.com/cholushkin/gamelib.git) | Core collection of shared algorithmic and structural elements. |
| **Git Submodule** | TinyColor | — | [Link](https://github.com/cholushkin/TinyColor.git) | Palette generation, manipulation, and runtime color management. |
| **Git Submodule** | TowerGenerator | — | [Link](https://github.com/cholushkin/towergenerator.git) | Procedural grid layout and chunk topology builder module. |
| **Git Submodule** | uconsole | — | [Link](https://github.com/cholushkin/uconsole.git) | Integrated runtime console shell and command handling hook. |
| **Git Submodule** | UMoonSharp | — | [Link](https://github.com/cholushkin/umoonsharp.git) | Embedded Lua compiler and scripting environment wrapper. |
| **Git Submodule** | VersionHistory | — | [Link](https://github.com/cholushkin/VersionHistory.git) | Local layout modification tracking and asset log subsystem. |
| **Git Submodule** | DevConventions | — | [Link](https://github.com/cholushkin/dev-conventions.git) | Quality controls and architectural documentation configurations. |
| **Git Submodule** | CVB | — | [Link](https://github.com/cholushkin/CVB.git) | Context-View-Broker architectural pattern framework. |
| **Package Manager** | com.annulusgames.alchemy | Git | [Link](https://github.com/annulusgames/Alchemy.git?path=/Alchemy/Assets/Alchemy) | Attributes layout engine and serialized inspector modifications. |
| **Package Manager** | com.annulusgames.lit-motion | Git | [Link](https://github.com/annulusgames/LitMotion.git?path=src/LitMotion/Assets/LitMotion) | High-performance, low-allocation functional animation tool. |
| **Package Manager** | com.cysharp.csprojmodifier | Git | [Link](https://github.com/Cysharp/CsprojModifier.git?path=src/CsprojModifier/Assets/CsprojModifier) | Dynamic editor configuration builder for external compilers. |
| **Package Manager** | com.cysharp.r3 | Git | [Link](https://github.com/Cysharp/R3.git?path=src/R3.Unity/Assets/R3.Unity) | Next-generation reactive extensions framework designed for Unity. |
| **Package Manager** | com.cysharp.unitask | Git | [Link](https://github.com/Cysharp/UniTask.git?path=src/UniTask/Assets/Plugins/UniTask) | Allocation-free structured async/await runtime integration. |
| **Package Manager** | com.cysharp.zlogger | Git | [Link](https://github.com/Cysharp/ZLogger.git?path=src/ZLogger.Unity/Assets/ZLogger.Unity) | High-speed logging architecture linked to text endpoints. |
| **Package Manager** | com.github-glitchenzo.nugetforunity | Git | [Link](https://github.com/GlitchEnzo/NuGetForUnity.git?path=/src/NuGetForUnity) | Direct assembly package management inside the active project pipeline. |
| **Package Manager** | com.mischief.markdownviewer | Git | [Link](https://github.com/gwaredd/UnityMarkdownViewer.git) | Local markdown layout display extension inside the inspector. |
| **Package Manager** | com.unity.ai.navigation | 2.0.12 | — | Official pathfinding computation components. |
| **Package Manager** | com.unity.collab-proxy | 2.12.4 | — | Multi-user asset streaming and cloud synchronization connector. |
| **Package Manager** | com.unity.ide.rider | 3.0.40 | — | Rider IDE connection handler. |
| **Package Manager** | com.unity.ide.visualstudio | 2.0.27 | — | Visual Studio assembly connection builder. |
| **Package Manager** | com.unity.inputsystem | 1.19.0 | — | Action-based unified user hardware input processing. |
| **Package Manager** | com.unity.multiplayer.center | 1.0.1 | — | Centralized server validation dashboard. |
| **Package Manager** | com.unity.render-pipelines.universal | 17.4.0 | — | Scriptable Universal Render Pipeline package. |
| **Package Manager** | com.unity.test-framework | 1.6.0 | — | Embedded automation engine test runner context. |
| **Package Manager** | com.unity.timeline | 1.8.12 | — | Multi-track sequencing tool. |
| **Package Manager** | com.unity.ugui | 2.0.0 | — | Traditional canvas Canvas/EventSystem user interfaces. |
| **Package Manager** | com.unity.visualscripting | 1.9.11 | — | Flow graph logical building blocks editor. |
| **Package Manager** | jp.hadashikick.vitalrouter.unity | 2.2.0 | [Link](https://github.com/hadashiA/VitalRouter.git?path=/src/VitalRouter.Unity/Assets/VitalRouter#2.2.0) | High-speed, zero-allocation custom message routing pipeline. |
| **Package Manager** | *com.unity.modules.** | 1.0.0 | — | Native modular engine components (Physics, Audio, Particles, Animation, UI Elements, VectorGraphics, etc.). |
| **NuGet Package** | Microsoft.Bcl.AsyncInterfaces | 8.0.0 | — | Standard async service mapping primitives. |
| **NuGet Package** | Microsoft.Bcl.TimeProvider | 8.0.0 | — | Clock and time measurement abstraction libraries. |
| **NuGet Package** | Microsoft.Extensions.DependencyInjection | 8.0.0 | — | Modern decoupled IoC container architectures. |
| **NuGet Package** | Microsoft.Extensions.DependencyInjection.Abstractions | 8.0.0 | — | Shared interfaces for service definition containers. |
| **NuGet Package** | Microsoft.Extensions.Logging | 8.0.0 | — | Structured logging pipeline integration base. |
| **NuGet Package** | Microsoft.Extensions.Logging.Abstractions | 8.0.0 | — | Common structural extensions for external logs. |
| **NuGet Package** | Microsoft.Extensions.Options | 8.0.0 | — | Dynamic programmatic configuration framework pattern. |
| **NuGet Package** | Microsoft.Extensions.Primitives | 8.0.0 | — | Shared low-level data parsing string structures. |
| **NuGet Package** | ObservableCollections | 3.3.4 | — | Performance-optimized data mutation callback arrays. |
| **NuGet Package** | R3 | 1.3.1 | — | Fundamental assembly layer for the reactive streaming matrix. |
| **NuGet Package** | System.Collections.Immutable | 8.0.0 | — | Thread-safe, unmodifiable collection definitions. |
| **NuGet Package** | System.ComponentModel.Annotations | 5.0.0 | — | Meta-attribute validation layer hooks. |
| **NuGet Package** | System.Diagnostics.DiagnosticSource | 8.0.0 | — | Dynamic performance metrics monitoring primitives. |
| **NuGet Package** | System.Text.Encodings.Web | 8.0.0 | — | Sanitized text string processing mechanics. |
| **NuGet Package** | System.Text.Json | 8.0.5 | — | Zero-allocation structural text deserialization utility. |
| **NuGet Package** | System.Threading.Channels | 8.0.0 | — | Multi-threaded producer-consumer message pipelines. |
| **NuGet Package** | Utf8StringInterpolation | 1.3.1 | — | Fast string allocations avoiding reference garbage collection. |
| **NuGet Package** | VitalRouter | 2.2.0 | — | Shared runtime interface assemblies for message routing. |
| **NuGet Package** | ZLogger | 2.5.10 | — | High-performance formatting core logger architecture. |
| **Manual Library** | DOTween | — | — | External programmatic animation engine managed within `Assets/Libs/DOTween`. |

---

## Notes

* **Asynchronous & Reactive System Alignment:** The framework exhibits a highly intentional architecture focused on zero-allocation asynchronous data transformation and message parsing. By pairing **R3**, **UniTask**, and **VitalRouter** via the package manager with matching core assemblies via NuGet, runtime conflicts are minimized while establishing a seamless event-driven state model.
* **NuGet System Version Cohesion:** The project strictly enforces standard versioning across its underlying .NET dependencies, pinning critical extensions to version `8.0.0`. This maintains absolute compilation parity within Unity's modern Mono or IL2CPP compilation steps and guarantees thread execution primitives remain fully deterministic.
* **Architecture Isolation via Git Submodules:** Custom architecture logic (such as the **CVB** framework layer and the core **Gamelib**) is managed using submodules mapped directly within `Assets/Libs/`. This isolates third-party code integration entirely from direct repository commits and streamlines tool updates across development environments.
* **Manual Dependency Encapsulation:** **DOTween** stands out as the singular third-party asset dropped manually into the system file layout without relying on an external configuration manifest file entry. To maintain project hygiene and stable dependency resolution, this package should be safely isolated with standalone, manually defined assembly definitions (`.asmdef`) to keep compilation domains fully decoupled from fluid git modifications.