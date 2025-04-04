[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Tutorials
Building MCP with LLMs
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Tutorials
# Building MCP with LLMs
Speed up your MCP development using LLMs such as Claude!
This guide will help you use LLMs to help you build custom Model Context Protocol (MCP) servers and clients. We’ll be focusing on Claude for this tutorial, but you can do this with any frontier LLM.
## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#preparing-the-documentation)
Preparing the documentation
Before starting, gather the necessary documentation to help Claude understand MCP:
  1. Visit <https://modelcontextprotocol.io/llms-full.txt> and copy the full documentation text
  2. Navigate to either the [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) or [Python SDK repository](https://github.com/modelcontextprotocol/python-sdk)
  3. Copy the README files and other relevant documentation
  4. Paste these documents into your conversation with Claude


## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#describing-your-server)
Describing your server
Once you’ve provided the documentation, clearly describe to Claude what kind of server you want to build. Be specific about:
  * What resources your server will expose
  * What tools it will provide
  * Any prompts it should offer
  * What external systems it needs to interact with


For example:
Copy
```
Build an MCP server that:
- Connects to my company's PostgreSQL database
- Exposes table schemas as resources
- Provides tools for running read-only SQL queries
- Includes prompts for common data analysis tasks

```

## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#working-with-claude)
Working with Claude
When working with Claude on MCP servers:
  1. Start with the core functionality first, then iterate to add more features
  2. Ask Claude to explain any parts of the code you don’t understand
  3. Request modifications or improvements as needed
  4. Have Claude help you test the server and handle edge cases


Claude can help implement all the key MCP features:
  * Resource management and exposure
  * Tool definitions and implementations
  * Prompt templates and handlers
  * Error handling and logging
  * Connection and transport setup


## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#best-practices)
Best practices
When building MCP servers with Claude:
  * Break down complex servers into smaller pieces
  * Test each component thoroughly before moving on
  * Keep security in mind - validate inputs and limit access appropriately
  * Document your code well for future maintenance
  * Follow MCP protocol specifications carefully


## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#next-steps)
Next steps
After Claude helps you build your server:
  1. Review the generated code carefully
  2. Test the server with the MCP Inspector tool
  3. Connect it to Claude.app or other MCP clients
  4. Iterate based on real usage and feedback


Remember that Claude can help you modify and improve your server as requirements change over time.
Need more guidance? Just ask Claude specific questions about implementing MCP features or troubleshooting issues that arise.
Was this page helpful?
YesNo
[Example Clients](https://modelcontextprotocol.io/clients)[Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Preparing the documentation](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#preparing-the-documentation)
  * [Describing your server](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#describing-your-server)
  * [Working with Claude](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#working-with-claude)
  * [Best practices](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#best-practices)
  * [Next steps](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#next-steps)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Get Started
Example Clients
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Get Started
# Example Clients
A list of applications that support MCP integrations
This page provides an overview of applications that support the Model Context Protocol (MCP). Each client may support different MCP features, allowing for varying levels of integration with MCP servers.
## 
[​](https://modelcontextprotocol.io/clients#feature-support-matrix)
Feature support matrix
Client| [Resources](https://modelcontextprotocol.io/docs/concepts/resources)| [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)| [Tools](https://modelcontextprotocol.io/docs/concepts/tools)| [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)| Roots| Notes  
---|---|---|---|---|---|---  
[Claude Desktop App](https://claude.ai/download)| ✅| ✅| ✅| ❌| ❌| Full support for all MCP features  
[Claude Code](https://claude.ai/code)| ❌| ✅| ✅| ❌| ❌| Supports prompts and tools  
[5ire](https://github.com/nanbingxyz/5ire)| ❌| ❌| ✅| ❌| ❌| Supports tools.  
[BeeAI Framework](https://i-am-bee.github.io/beeai-framework)| ❌| ❌| ✅| ❌| ❌| Supports tools in agentic workflows.  
[Cline](https://github.com/cline/cline)| ✅| ❌| ✅| ❌| ❌| Supports tools and resources.  
[Continue](https://github.com/continuedev/continue)| ✅| ✅| ✅| ❌| ❌| Full support for all MCP features  
[Copilot-MCP](https://github.com/VikashLoomba/copilot-mcp)| ✅| ❌| ✅| ❌| ❌| Supports tools and resources.  
[Cursor](https://cursor.com)| ❌| ❌| ✅| ❌| ❌| Supports tools.  
[Emacs Mcp](https://github.com/lizqwerscott/mcp.el)| ❌| ❌| ✅| ❌| ❌| Supports tools in Emacs.  
[fast-agent](https://github.com/evalstate/fast-agent)| ✅| ✅| ✅| ✅| ✅| Full multimodal MCP support, with end-to-end tests  
[Genkit](https://github.com/firebase/genkit)| ⚠️| ✅| ✅| ❌| ❌| Supports resource list and lookup through tools.  
[GenAIScript](https://microsoft.github.io/genaiscript/reference/scripts/mcp-tools/)| ❌| ❌| ✅| ❌| ❌| Supports tools.  
[Goose](https://block.github.io/goose/docs/goose-architecture/#interoperability-with-extensions)| ❌| ❌| ✅| ❌| ❌| Supports tools.  
[LibreChat](https://github.com/danny-avila/LibreChat)| ❌| ❌| ✅| ❌| ❌| Supports tools for Agents  
[mcp-agent](https://github.com/lastmile-ai/mcp-agent)| ❌| ❌| ✅| ⚠️| ❌| Supports tools, server connection management, and agent workflows.  
[Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp)| ❌| ❌| ✅| ❌| ❌| Supports tools  
[oterm](https://github.com/ggozad/oterm)| ❌| ✅| ✅| ❌| ❌| Supports tools and prompts.| [Roo Code](https://roocode.com)| ✅| ❌| ✅| ❌| ❌| Supports tools and resources.  
[Sourcegraph Cody](https://sourcegraph.com/cody)| ✅| ❌| ❌| ❌| ❌| Supports resources through OpenCTX  
[Superinterface](https://superinterface.ai)| ❌| ❌| ✅| ❌| ❌| Supports tools  
[TheiaAI/TheiaIDE](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/)| ❌| ❌| ✅| ❌| ❌| Supports tools for Agents in Theia AI and the AI-powered Theia IDE  
[Windsurf Editor](https://codeium.com/windsurf)| ❌| ❌| ✅| ❌| ❌| Supports tools with AI Flow for collaborative development.  
[Witsy](https://github.com/nbonamy/witsy)| ❌| ❌| ✅| ❌| ❌| Supports tools in Witsy.  
[Zed](https://zed.dev)| ❌| ✅| ❌| ❌| ❌| Prompts appear as slash commands  
[SpinAI](https://spinai.dev)| ❌| ❌| ✅| ❌| ❌| Supports tools for Typescript AI Agents  
[OpenSumi](https://github.com/opensumi/core)| ❌| ❌| ✅| ❌| ❌| Supports tools in OpenSumi  
[Daydreams Agents](https://github.com/daydreamsai/daydreams)| ✅| ✅| ✅| ❌| ❌| Support for drop in Servers to Daydreams agents  
[Apify MCP Tester](https://apify.com/jiri.spilka/tester-mcp-client)| ❌| ❌| ✅| ❌| ❌| Supports tools  
## 
[​](https://modelcontextprotocol.io/clients#client-details)
Client details
### 
[​](https://modelcontextprotocol.io/clients#claude-desktop-app)
Claude Desktop App
The Claude desktop application provides comprehensive support for MCP, enabling deep integration with local tools and data sources.
**Key features:**
  * Full support for resources, allowing attachment of local files and data
  * Support for prompt templates
  * Tool integration for executing commands and scripts
  * Local server connections for enhanced privacy and security


> ⓘ Note: The Claude.ai web application does not currently support MCP. MCP features are only available in the desktop application.
### 
[​](https://modelcontextprotocol.io/clients#claude-code)
Claude Code
Claude Code is an interactive agentic coding tool from Anthropic that helps you code faster through natural language commands. It supports MCP integration for prompts and tools, and also functions as an MCP server to integrate with other clients.
**Key features:**
  * Tool and prompt support for MCP servers
  * Offers its own tools through an MCP server for integrating with other MCP clients


### 
[​](https://modelcontextprotocol.io/clients#5ire)
5ire
[5ire](https://github.com/nanbingxyz/5ire) is an open source cross-platform desktop AI assistant that supports tools through MCP servers.
**Key features:**
  * Built-in MCP servers can be quickly enabled and disabled.
  * Users can add more servers by modifying the configuration file.
  * It is open-source and user-friendly, suitable for beginners.
  * Future support for MCP will be continuously improved.


### 
[​](https://modelcontextprotocol.io/clients#beeai-framework)
BeeAI Framework
[BeeAI Framework](https://i-am-bee.github.io/beeai-framework) is an open-source framework for building, deploying, and serving powerful agentic workflows at scale. The framework includes the **MCP Tool** , a native feature that simplifies the integration of MCP servers into agentic workflows.
**Key features:**
  * Seamlessly incorporate MCP tools into agentic workflows.
  * Quickly instantiate framework-native tools from connected MCP client(s).
  * Planned future support for agentic MCP capabilities.


**Learn more:**
  * [Example of using MCP tools in agentic workflow](https://i-am-bee.github.io/beeai-framework/#/typescript/tools?id=using-the-mcptool-class)


### 
[​](https://modelcontextprotocol.io/clients#cline)
Cline
[Cline](https://github.com/cline/cline) is an autonomous coding agent in VS Code that edits files, runs commands, uses a browser, and more–with your permission at each step.
**Key features:**
  * Create and add tools through natural language (e.g. “add a tool that searches the web”)
  * Share custom MCP servers Cline creates with others via the `~/Documents/Cline/MCP` directory
  * Displays configured MCP servers along with their tools, resources, and any error logs


### 
[​](https://modelcontextprotocol.io/clients#continue)
Continue
[Continue](https://github.com/continuedev/continue) is an open-source AI code assistant, with built-in support for all MCP features.
**Key features**
  * Type ”@” to mention MCP resources
  * Prompt templates surface as slash commands
  * Use both built-in and MCP tools directly in chat
  * Supports VS Code and JetBrains IDEs, with any LLM


### 
[​](https://modelcontextprotocol.io/clients#cursor)
Cursor
[Cursor](https://docs.cursor.com/advanced/model-context-protocol) is an AI code editor.
**Key Features** :
  * Support for MCP tools in Cursor Composer
  * Support for both STDIO and SSE


### 
[​](https://modelcontextprotocol.io/clients#emacs-mcp)
Emacs Mcp
[Emacs Mcp](https://github.com/lizqwerscott/mcp.el) is an Emacs client designed to interface with MCP servers, enabling seamless connections and interactions. It provides MCP tool invocation support for AI plugins like [gptel](https://github.com/karthink/gptel) and [llm](https://github.com/ahyatt/llm), adhering to Emacs’ standard tool invocation format. This integration enhances the functionality of AI tools within the Emacs ecosystem.
**Key features:**
  * Provides MCP tool support for Emacs.


### 
[​](https://modelcontextprotocol.io/clients#fast-agent)
fast-agent
[fast-agent](https://github.com/evalstate/fast-agent) is a Python Agent framework, with simple declarative support for creating Agents and Workflows, with full multi-modal support for Anthropic and OpenAI models.
**Key features:**
  * PDF and Image support, based on MCP Native types
  * Interactive front-end to develop and diagnose Agent applications, including passthrough and playback simulators
  * Built in support for “Building Effective Agents” workflows.
  * Deploy Agents as MCP Servers


### 
[​](https://modelcontextprotocol.io/clients#genkit)
Genkit
[Genkit](https://github.com/firebase/genkit) is a cross-language SDK for building and integrating GenAI features into applications. The [genkitx-mcp](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) plugin enables consuming MCP servers as a client or creating MCP servers from Genkit tools and prompts.
**Key features:**
  * Client support for tools and prompts (resources partially supported)
  * Rich discovery with support in Genkit’s Dev UI playground
  * Seamless interoperability with Genkit’s existing tools and prompts
  * Works across a wide variety of GenAI models from top providers


### 
[​](https://modelcontextprotocol.io/clients#genaiscript)
GenAIScript
Programmatically assemble prompts for LLMs using [GenAIScript](https://microsoft.github.io/genaiscript/) (in JavaScript). Orchestrate LLMs, tools, and data in JavaScript.
**Key features:**
  * JavaScript toolbox to work with prompts
  * Abstraction to make it easy and productive
  * Seamless Visual Studio Code integration


### 
[​](https://modelcontextprotocol.io/clients#goose)
Goose
[Goose](https://github.com/block/goose) is an open source AI agent that supercharges your software development by automating coding tasks.
**Key features:**
  * Expose MCP functionality to Goose through tools.
  * MCPs can be installed directly via the [extensions directory](https://block.github.io/goose/v1/extensions/), CLI, or UI.
  * Goose allows you to extend its functionality by [building your own MCP servers](https://block.github.io/goose/docs/tutorials/custom-extensions).
  * Includes built-in tools for development, web scraping, automation, memory, and integrations with JetBrains and Google Drive.


### 
[​](https://modelcontextprotocol.io/clients#librechat)
LibreChat
[LibreChat](https://github.com/danny-avila/LibreChat) is an open-source, customizable AI chat UI that supports multiple AI providers, now including MCP integration.
**Key features:**
  * Extend current tool ecosystem, including [Code Interpreter](https://www.librechat.ai/docs/features/code_interpreter) and Image generation tools, through MCP servers
  * Add tools to customizable [Agents](https://www.librechat.ai/docs/features/agents), using a variety of LLMs from top providers
  * Open-source and self-hostable, with secure multi-user support
  * Future roadmap includes expanded MCP feature support


### 
[​](https://modelcontextprotocol.io/clients#mcp-agent)
mcp-agent
[mcp-agent](https://github.com/lastmile-ai/mcp-agent) is a simple, composable framework to build agents using Model Context Protocol.
**Key features:**
  * Automatic connection management of MCP servers.
  * Expose tools from multiple servers to an LLM.
  * Implements every pattern defined in [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents).
  * Supports workflow pause/resume signals, such as waiting for human feedback.


### 
[​](https://modelcontextprotocol.io/clients#microsoft-copilot-studio)
Microsoft Copilot Studio
[Microsoft Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp) is a robust SaaS platform designed for building custom AI-driven applications and intelligent agents, empowering developers to create, deploy, and manage sophisticated AI solutions.
**Key features:**
  * Support for MCP tools
  * Extend Copilot Studio agents with MCP servers
  * Leveraging Microsoft unified, governed, and secure API management solutions


### 
[​](https://modelcontextprotocol.io/clients#oterm)
oterm
[oterm](https://github.com/ggozad/oterm) is a terminal client for Ollama allowing users to create chats/agents.
**Key features:**
  * Support for multiple fully customizable chat sessions with Ollama connected with tools.
  * Support for MCP tools.


### 
[​](https://modelcontextprotocol.io/clients#roo-code)
Roo Code
[Roo Code](https://roocode.com) enables AI coding assistance via MCP.
**Key features:**
  * Support for MCP tools and resources
  * Integration with development workflows
  * Extensible AI capabilities


### 
[​](https://modelcontextprotocol.io/clients#sourcegraph-cody)
Sourcegraph Cody
[Cody](https://openctx.org/docs/providers/modelcontextprotocol) is Sourcegraph’s AI coding assistant, which implements MCP through OpenCTX.
**Key features:**
  * Support for MCP resources
  * Integration with Sourcegraph’s code intelligence
  * Uses OpenCTX as an abstraction layer
  * Future support planned for additional MCP features


### 
[​](https://modelcontextprotocol.io/clients#spinai)
SpinAI
[SpinAI](https://spinai.dev) is an open-source TypeScript framework for building observable AI agents. The framework provides native MCP compatibility, allowing agents to seamlessly integrate with MCP servers and tools.
**Key features:**
  * Built-in MCP compatibility for AI agents
  * Open-source TypeScript framework
  * Observable agent architecture
  * Native support for MCP tools integration


### 
[​](https://modelcontextprotocol.io/clients#superinterface)
Superinterface
[Superinterface](https://superinterface.ai) is AI infrastructure and a developer platform to build in-app AI assistants with support for MCP, interactive components, client-side function calling and more.
**Key features:**
  * Use tools from MCP servers in assistants embedded via React components or script tags
  * SSE transport support
  * Use any AI model from any AI provider (OpenAI, Anthropic, Ollama, others)


### 
[​](https://modelcontextprotocol.io/clients#theiaai%2Ftheiaide)
TheiaAI/TheiaIDE
[Theia AI](https://eclipsesource.com/blogs/2024/10/07/introducing-theia-ai/) is a framework for building AI-enhanced tools and IDEs. The [AI-powered Theia IDE](https://eclipsesource.com/blogs/2024/10/08/introducting-ai-theia-ide/) is an open and flexible development environment built on Theia AI.
**Key features:**
  * **Tool Integration** : Theia AI enables AI agents, including those in the Theia IDE, to utilize MCP servers for seamless tool interaction.
  * **Customizable Prompts** : The Theia IDE allows users to define and adapt prompts, dynamically integrating MCP servers for tailored workflows.
  * **Custom agents** : The Theia IDE supports creating custom agents that leverage MCP capabilities, enabling users to design dedicated workflows on the fly.


Theia AI and Theia IDE’s MCP integration provide users with flexibility, making them powerful platforms for exploring and adapting MCP.
**Learn more:**
  * [Theia IDE and Theia AI MCP Announcement](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/)
  * [Download the AI-powered Theia IDE](https://theia-ide.org/)


### 
[​](https://modelcontextprotocol.io/clients#windsurf-editor)
Windsurf Editor
[Windsurf Editor](https://codeium.com/windsurf) is an agentic IDE that combines AI assistance with developer workflows. It features an innovative AI Flow system that enables both collaborative and independent AI interactions while maintaining developer control.
**Key features:**
  * Revolutionary AI Flow paradigm for human-AI collaboration
  * Intelligent code generation and understanding
  * Rich development tools with multi-model support


### 
[​](https://modelcontextprotocol.io/clients#witsy)
Witsy
[Witsy](https://github.com/nbonamy/witsy) is an AI desktop assistant, supoorting Anthropic models and MCP servers as LLM tools.
**Key features:**
  * Multiple MCP servers support
  * Tool integration for executing commands and scripts
  * Local server connections for enhanced privacy and security
  * Easy-install from Smithery.ai
  * Open-source, available for macOS, Windows and Linux


### 
[​](https://modelcontextprotocol.io/clients#zed)
Zed
[Zed](https://zed.dev/docs/assistant/model-context-protocol) is a high-performance code editor with built-in MCP support, focusing on prompt templates and tool integration.
**Key features:**
  * Prompt templates surface as slash commands in the editor
  * Tool integration for enhanced coding workflows
  * Tight integration with editor features and workspace context
  * Does not support MCP resources


### 
[​](https://modelcontextprotocol.io/clients#opensumi)
OpenSumi
[OpenSumi](https://github.com/opensumi/core) is a framework helps you quickly build AI Native IDE products.
**Key features:**
  * Supports MCP tools in OpenSumi
  * Supports built-in IDE MCP servers and custom MCP servers


### 
[​](https://modelcontextprotocol.io/clients#daydreams)
Daydreams
[Daydreams](https://github.com/daydreamsai/daydreams) is a generative agent framework for executing anything onchain
**Key features:**
  * Supports MCP Servers in config
  * Exposes MCP Client


### 
[​](https://modelcontextprotocol.io/clients#apify-mcp-tester)
Apify MCP Tester
[Apify MCP Tester](https://github.com/apify/tester-mcp-client) is an open-source client that connects to any MCP server using Server-Sent Events (SSE). It is a standalone Apify Actor designed for testing MCP servers over SSE, with support for Authorization headers. It uses plain JavaScript (old-school style) and is hosted on Apify, allowing you to run it without any setup.
**Key features:**
  * Connects to any MCP server via SSE.
  * Works with the [Apify MCP Server](https://apify.com/apify/actors-mcp-server) to interact with one or more Apify [Actors](https://apify.com/store).
  * Dynamically utilizes tools based on context and user queries (if supported by the server).


## 
[​](https://modelcontextprotocol.io/clients#adding-mcp-support-to-your-application)
Adding MCP support to your application
If you’ve added MCP support to your application, we encourage you to submit a pull request to add it to this list. MCP integration can provide your users with powerful contextual AI capabilities and make your application part of the growing MCP ecosystem.
Benefits of adding MCP support:
  * Enable users to bring their own context and tools
  * Join a growing ecosystem of interoperable AI applications
  * Provide users with flexible integration options
  * Support local-first AI workflows


To get started with implementing MCP in your application, check out our [Python](https://github.com/modelcontextprotocol/python-sdk) or [TypeScript SDK Documentation](https://github.com/modelcontextprotocol/typescript-sdk)
## 
[​](https://modelcontextprotocol.io/clients#updates-and-corrections)
Updates and corrections
This list is maintained by the community. If you notice any inaccuracies or would like to update information about MCP support in your application, please submit a pull request or [open an issue in our documentation repository](https://github.com/modelcontextprotocol/docs/issues).
Was this page helpful?
YesNo
[Example Servers](https://modelcontextprotocol.io/examples)[Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Feature support matrix](https://modelcontextprotocol.io/clients#feature-support-matrix)
  * [Client details](https://modelcontextprotocol.io/clients#client-details)
  * [Claude Desktop App](https://modelcontextprotocol.io/clients#claude-desktop-app)
  * [Claude Code](https://modelcontextprotocol.io/clients#claude-code)
  * [5ire](https://modelcontextprotocol.io/clients#5ire)
  * [BeeAI Framework](https://modelcontextprotocol.io/clients#beeai-framework)
  * [Cline](https://modelcontextprotocol.io/clients#cline)
  * [Continue](https://modelcontextprotocol.io/clients#continue)
  * [Cursor](https://modelcontextprotocol.io/clients#cursor)
  * [Emacs Mcp](https://modelcontextprotocol.io/clients#emacs-mcp)
  * [fast-agent](https://modelcontextprotocol.io/clients#fast-agent)
  * [Genkit](https://modelcontextprotocol.io/clients#genkit)
  * [GenAIScript](https://modelcontextprotocol.io/clients#genaiscript)
  * [Goose](https://modelcontextprotocol.io/clients#goose)
  * [LibreChat](https://modelcontextprotocol.io/clients#librechat)
  * [mcp-agent](https://modelcontextprotocol.io/clients#mcp-agent)
  * [Microsoft Copilot Studio](https://modelcontextprotocol.io/clients#microsoft-copilot-studio)
  * [oterm](https://modelcontextprotocol.io/clients#oterm)
  * [Roo Code](https://modelcontextprotocol.io/clients#roo-code)
  * [Sourcegraph Cody](https://modelcontextprotocol.io/clients#sourcegraph-cody)
  * [SpinAI](https://modelcontextprotocol.io/clients#spinai)
  * [Superinterface](https://modelcontextprotocol.io/clients#superinterface)
  * [TheiaAI/TheiaIDE](https://modelcontextprotocol.io/clients#theiaai%2Ftheiaide)
  * [Windsurf Editor](https://modelcontextprotocol.io/clients#windsurf-editor)
  * [Witsy](https://modelcontextprotocol.io/clients#witsy)
  * [Zed](https://modelcontextprotocol.io/clients#zed)
  * [OpenSumi](https://modelcontextprotocol.io/clients#opensumi)
  * [Daydreams](https://modelcontextprotocol.io/clients#daydreams)
  * [Apify MCP Tester](https://modelcontextprotocol.io/clients#apify-mcp-tester)
  * [Adding MCP support to your application](https://modelcontextprotocol.io/clients#adding-mcp-support-to-your-application)
  * [Updates and corrections](https://modelcontextprotocol.io/clients#updates-and-corrections)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Development
Contributing
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Development
# Contributing
How to participate in Model Context Protocol development
We welcome contributions from the community! Please review our [contributing guidelines](https://github.com/modelcontextprotocol/.github/blob/main/CONTRIBUTING.md) for details on how to submit changes.
All contributors must adhere to our [Code of Conduct](https://github.com/modelcontextprotocol/.github/blob/main/CODE_OF_CONDUCT.md).
For questions and discussions, please use [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions).
Was this page helpful?
YesNo
[Roadmap](https://modelcontextprotocol.io/development/roadmap)
[github](https://github.com/modelcontextprotocol)
[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Development
Roadmap
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Development
# Roadmap
Our plans for evolving Model Context Protocol (H1 2025)
The Model Context Protocol is rapidly evolving. This page outlines our current thinking on key priorities and future direction for **the first half of 2025** , though these may change significantly as the project develops.
The ideas presented here are not commitments—we may solve these challenges differently than described, or some may not materialize at all. This is also not an _exhaustive_ list; we may incorporate work that isn’t mentioned here.
We encourage community participation! Each section links to relevant discussions where you can learn more and contribute your thoughts.
## 
[​](https://modelcontextprotocol.io/development/roadmap#remote-mcp-support)
Remote MCP Support
Our top priority is improving [remote MCP connections](https://github.com/modelcontextprotocol/specification/discussions/112), allowing clients to securely connect to MCP servers over the internet. Key initiatives include:
  * [**Authentication & Authorization**](https://github.com/modelcontextprotocol/specification/discussions/64): Adding standardized auth capabilities, particularly focused on OAuth 2.0 support.
  * [**Service Discovery**](https://github.com/modelcontextprotocol/specification/discussions/69): Defining how clients can discover and connect to remote MCP servers.
  * [**Stateless Operations**](https://github.com/modelcontextprotocol/specification/discussions/102): Thinking about whether MCP could encompass serverless environments too, where they will need to be mostly stateless.


## 
[​](https://modelcontextprotocol.io/development/roadmap#reference-implementations)
Reference Implementations
To help developers build with MCP, we want to offer documentation for:
  * **Client Examples** : Comprehensive reference client implementation(s), demonstrating all protocol features
  * **Protocol Drafting** : Streamlined process for proposing and incorporating new protocol features


## 
[​](https://modelcontextprotocol.io/development/roadmap#distribution-%26-discovery)
Distribution & Discovery
Looking ahead, we’re exploring ways to make MCP servers more accessible. Some areas we may investigate include:
  * **Package Management** : Standardized packaging format for MCP servers
  * **Installation Tools** : Simplified server installation across MCP clients
  * **Sandboxing** : Improved security through server isolation
  * **Server Registry** : A common directory for discovering available MCP servers


## 
[​](https://modelcontextprotocol.io/development/roadmap#agent-support)
Agent Support
We’re expanding MCP’s capabilities for [complex agentic workflows](https://github.com/modelcontextprotocol/specification/discussions/111), particularly focusing on:
  * [**Hierarchical Agent Systems**](https://github.com/modelcontextprotocol/specification/discussions/94): Improved support for trees of agents through namespacing and topology awareness.
  * [**Interactive Workflows**](https://github.com/modelcontextprotocol/specification/issues/97): Better handling of user permissions and information requests across agent hierarchies, and ways to send output to users instead of models.
  * [**Streaming Results**](https://github.com/modelcontextprotocol/specification/issues/117): Real-time updates from long-running agent operations.


## 
[​](https://modelcontextprotocol.io/development/roadmap#broader-ecosystem)
Broader Ecosystem
We’re also invested in:
  * **Community-Led Standards Development** : Fostering a collaborative ecosystem where all AI providers can help shape MCP as an open standard through equal participation and shared governance, ensuring it meets the needs of diverse AI applications and use cases.
  * [**Additional Modalities**](https://github.com/modelcontextprotocol/specification/discussions/88): Expanding beyond text to support audio, video, and other formats.
  * [**Standardization**] Considering standardization through a standardization body.


## 
[​](https://modelcontextprotocol.io/development/roadmap#get-involved)
Get Involved
We welcome community participation in shaping MCP’s future. Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to join the conversation and contribute your ideas.
Was this page helpful?
YesNo
[What's New](https://modelcontextprotocol.io/development/updates)[Contributing](https://modelcontextprotocol.io/development/contributing)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Remote MCP Support](https://modelcontextprotocol.io/development/roadmap#remote-mcp-support)
  * [Reference Implementations](https://modelcontextprotocol.io/development/roadmap#reference-implementations)
  * [Distribution & Discovery](https://modelcontextprotocol.io/development/roadmap#distribution-%26-discovery)
  * [Agent Support](https://modelcontextprotocol.io/development/roadmap#agent-support)
  * [Broader Ecosystem](https://modelcontextprotocol.io/development/roadmap#broader-ecosystem)
  * [Get Involved](https://modelcontextprotocol.io/development/roadmap#get-involved)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Development
What's New
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Development
# What's New
The latest updates and improvements to MCP
[​](https://modelcontextprotocol.io/development/updates#2025-03-26)
2025-03-26
Kotlin SDK 0.4.0 released
  * Fix issues and cleanup API
  * Added binary compatibility tracking to avoid breaking changes
  * Drop jdk requirements to JDK8
  * Added Claude Desktop integration with sample
  * The full changelog can be found here: <https://github.com/modelcontextprotocol/kotlin-sdk/releases/tag/0.4.0>


[​](https://modelcontextprotocol.io/development/updates#2025-03-26-2)
2025-03-26
Java SDK 0.8.1 released
  * Version [0.8.1](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.1) of the MCP Java SDK has been released, providing important bug fixes.


[​](https://modelcontextprotocol.io/development/updates#2025-03-24)
2025-03-24
C# SDK released
  * We are exited to announce the availability of the MCP [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk/) developed by [Peder Holdgaard Pedersen](http://github.com/PederHP) and Microsoft. This joins our growing list of supported languages. The C# SDK is also available as [NuGet package](https://www.nuget.org/packages/ModelContextProtocol)
  * Python SDK 1.5.0 was released with multiple fixes and improvements.


[​](https://modelcontextprotocol.io/development/updates#2025-03-21)
2025-03-21
Java SDK 0.8.0 released
  * Version [0.8.0](https://github.com/modelcontextprotocol/java-sdk/releases/tag/v0.8.0) of the MCP Java SDK has been released, delivering important session management improvements and bug fixes.


[​](https://modelcontextprotocol.io/development/updates#2025-03-10)
2025-03-10
Typescript SDK release
  * Typescript SDK 1.7.0 was released with multiple fixes and improvements.


[​](https://modelcontextprotocol.io/development/updates#2025-02-14)
2025-02-14
Java SDK released
  * We’re excited to announce that the Java SDK developed by Spring AI at VMware Tanzu is now the official [Java SDK](https://github.com/modelcontextprotocol/java-sdk) for MCP. This joins our existing Kotlin SDK in our growing list of supported languages. The Spring AI team will maintain the SDK as an integral part of the Model Context Protocol organization. We’re thrilled to welcome them to the MCP community!


[​](https://modelcontextprotocol.io/development/updates#2025-01-27)
2025-01-27
Python SDK 1.2.1
  * Version [1.2.1](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.2.1) of the MCP Python SDK has been released, delivering important stability improvements and bug fixes.


[​](https://modelcontextprotocol.io/development/updates#2025-01-18)
2025-01-18
SDK and Server Improvements
  * Simplified, express-like API in the [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
  * Added 8 new clients to the [clients page](https://modelcontextprotocol.io/clients)


[​](https://modelcontextprotocol.io/development/updates#2025-01-03)
2025-01-03
SDK and Server Improvements
  * FastMCP API in the [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  * Dockerized MCP servers in the [servers repo](https://github.com/modelcontextprotocol/servers)


[​](https://modelcontextprotocol.io/development/updates#2024-12-21)
2024-12-21
Kotlin SDK released
  * Jetbrains released a Kotlin SDK for MCP!
  * For a sample MCP Kotlin server, check out [this repository](https://github.com/modelcontextprotocol/kotlin-sdk/tree/main/samples/kotlin-mcp-server)


Was this page helpful?
YesNo
[Transports](https://modelcontextprotocol.io/docs/concepts/transports)[Roadmap](https://modelcontextprotocol.io/development/roadmap)
[github](https://github.com/modelcontextprotocol)
On this page
  * [2025-03-26](https://modelcontextprotocol.io/development/updates#2025-03-26)
  * [2025-03-26](https://modelcontextprotocol.io/development/updates#2025-03-26-2)
  * [2025-03-24](https://modelcontextprotocol.io/development/updates#2025-03-24)
  * [2025-03-21](https://modelcontextprotocol.io/development/updates#2025-03-21)
  * [2025-03-10](https://modelcontextprotocol.io/development/updates#2025-03-10)
  * [2025-02-14](https://modelcontextprotocol.io/development/updates#2025-02-14)
  * [2025-01-27](https://modelcontextprotocol.io/development/updates#2025-01-27)
  * [2025-01-18](https://modelcontextprotocol.io/development/updates#2025-01-18)
  * [2025-01-03](https://modelcontextprotocol.io/development/updates#2025-01-03)
  * [2024-12-21](https://modelcontextprotocol.io/development/updates#2024-12-21)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Core architecture
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Core architecture
Understand how MCP connects clients, servers, and LLMs
The Model Context Protocol (MCP) is built on a flexible, extensible architecture that enables seamless communication between LLM applications and integrations. This document covers the core architectural components and concepts.
## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#overview)
Overview
MCP follows a client-server architecture where:
  * **Hosts** are LLM applications (like Claude Desktop or IDEs) that initiate connections
  * **Clients** maintain 1:1 connections with servers, inside the host application
  * **Servers** provide context, tools, and prompts to clients


Server Process
Server Process
Host
Transport Layer
Transport Layer
MCP Client
MCP Client
MCP Server
MCP Server
## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#core-components)
Core components
### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#protocol-layer)
Protocol layer
The protocol layer handles message framing, request/response linking, and high-level communication patterns.
  * TypeScript
  * Python


Copy
```
class Protocol<Request, Notification, Result> {
  // Handle incoming requests
  setRequestHandler<T>(schema: T, handler: (request: T, extra: RequestHandlerExtra) => Promise<Result>): void
  // Handle incoming notifications
  setNotificationHandler<T>(schema: T, handler: (notification: T) => Promise<void>): void
  // Send requests and await responses
  request<T>(request: Request, schema: T, options?: RequestOptions): Promise<T>
  // Send one-way notifications
  notification(notification: Notification): Promise<void>
}

```

Key classes include:
  * `Protocol`
  * `Client`
  * `Server`


### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#transport-layer)
Transport layer
The transport layer handles the actual communication between clients and servers. MCP supports multiple transport mechanisms:
  1. **Stdio transport**
     * Uses standard input/output for communication
     * Ideal for local processes
  2. **HTTP with SSE transport**
     * Uses Server-Sent Events for server-to-client messages
     * HTTP POST for client-to-server messages


All transports use [JSON-RPC](https://www.jsonrpc.org/) 2.0 to exchange messages. See the [specification](https://spec.modelcontextprotocol.io) for detailed information about the Model Context Protocol message format.
### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#message-types)
Message types
MCP has these main types of messages:
  1. **Requests** expect a response from the other side:
Copy
```
interface Request {
 method: string;
 params?: { ... };
}

```

  2. **Results** are successful responses to requests:
Copy
```
interface Result {
 [key: string]: unknown;
}

```

  3. **Errors** indicate that a request failed:
Copy
```
interface Error {
 code: number;
 message: string;
 data?: unknown;
}

```

  4. **Notifications** are one-way messages that don’t expect a response:
Copy
```
interface Notification {
 method: string;
 params?: { ... };
}

```



## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#connection-lifecycle)
Connection lifecycle
### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#1-initialization)
1. Initialization
ServerClientServerClientConnection ready for useinitialize requestinitialize responseinitialized notification
  1. Client sends `initialize` request with protocol version and capabilities
  2. Server responds with its protocol version and capabilities
  3. Client sends `initialized` notification as acknowledgment
  4. Normal message exchange begins


### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#2-message-exchange)
2. Message exchange
After initialization, the following patterns are supported:
  * **Request-Response** : Client or server sends requests, the other responds
  * **Notifications** : Either party sends one-way messages


### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#3-termination)
3. Termination
Either party can terminate the connection:
  * Clean shutdown via `close()`
  * Transport disconnection
  * Error conditions


## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#error-handling)
Error handling
MCP defines these standard error codes:
Copy
```
enum ErrorCode {
 // Standard JSON-RPC error codes
 ParseError = -32700,
 InvalidRequest = -32600,
 MethodNotFound = -32601,
 InvalidParams = -32602,
 InternalError = -32603
}

```

SDKs and applications can define their own error codes above -32000.
Errors are propagated through:
  * Error responses to requests
  * Error events on transports
  * Protocol-level error handlers


## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#implementation-example)
Implementation example
Here’s a basic example of implementing an MCP server:
  * TypeScript
  * Python


Copy
```
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
const server = new Server({
 name: "example-server",
 version: "1.0.0"
}, {
 capabilities: {
  resources: {}
 }
});
// Handle requests
server.setRequestHandler(ListResourcesRequestSchema, async () => {
 return {
  resources: [
   {
    uri: "example://resource",
    name: "Example Resource"
   }
  ]
 };
});
// Connect transport
const transport = new StdioServerTransport();
await server.connect(transport);

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#best-practices)
Best practices
### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#transport-selection)
Transport selection
  1. **Local communication**
     * Use stdio transport for local processes
     * Efficient for same-machine communication
     * Simple process management
  2. **Remote communication**
     * Use SSE for scenarios requiring HTTP compatibility
     * Consider security implications including authentication and authorization


### 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#message-handling)
Message handling
  1. **Request processing**
     * Validate inputs thoroughly
     * Use type-safe schemas
     * Handle errors gracefully
     * Implement timeouts
  2. **Progress reporting**
     * Use progress tokens for long operations
     * Report progress incrementally
     * Include total progress when known
  3. **Error management**
     * Use appropriate error codes
     * Include helpful error messages
     * Clean up resources on errors


## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#security-considerations)
Security considerations
  1. **Transport security**
     * Use TLS for remote connections
     * Validate connection origins
     * Implement authentication when needed
  2. **Message validation**
     * Validate all incoming messages
     * Sanitize inputs
     * Check message size limits
     * Verify JSON-RPC format
  3. **Resource protection**
     * Implement access controls
     * Validate resource paths
     * Monitor resource usage
     * Rate limit requests
  4. **Error handling**
     * Don’t leak sensitive information
     * Log security-relevant errors
     * Implement proper cleanup
     * Handle DoS scenarios


## 
[​](https://modelcontextprotocol.io/docs/concepts/architecture#debugging-and-monitoring)
Debugging and monitoring
  1. **Logging**
     * Log protocol events
     * Track message flow
     * Monitor performance
     * Record errors
  2. **Diagnostics**
     * Implement health checks
     * Monitor connection state
     * Track resource usage
     * Profile performance
  3. **Testing**
     * Test different transports
     * Verify error handling
     * Check edge cases
     * Load test servers


Was this page helpful?
YesNo
[Inspector](https://modelcontextprotocol.io/docs/tools/inspector)[Resources](https://modelcontextprotocol.io/docs/concepts/resources)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Overview](https://modelcontextprotocol.io/docs/concepts/architecture#overview)
  * [Core components](https://modelcontextprotocol.io/docs/concepts/architecture#core-components)
  * [Protocol layer](https://modelcontextprotocol.io/docs/concepts/architecture#protocol-layer)
  * [Transport layer](https://modelcontextprotocol.io/docs/concepts/architecture#transport-layer)
  * [Message types](https://modelcontextprotocol.io/docs/concepts/architecture#message-types)
  * [Connection lifecycle](https://modelcontextprotocol.io/docs/concepts/architecture#connection-lifecycle)
  * [1. Initialization](https://modelcontextprotocol.io/docs/concepts/architecture#1-initialization)
  * [2. Message exchange](https://modelcontextprotocol.io/docs/concepts/architecture#2-message-exchange)
  * [3. Termination](https://modelcontextprotocol.io/docs/concepts/architecture#3-termination)
  * [Error handling](https://modelcontextprotocol.io/docs/concepts/architecture#error-handling)
  * [Implementation example](https://modelcontextprotocol.io/docs/concepts/architecture#implementation-example)
  * [Best practices](https://modelcontextprotocol.io/docs/concepts/architecture#best-practices)
  * [Transport selection](https://modelcontextprotocol.io/docs/concepts/architecture#transport-selection)
  * [Message handling](https://modelcontextprotocol.io/docs/concepts/architecture#message-handling)
  * [Security considerations](https://modelcontextprotocol.io/docs/concepts/architecture#security-considerations)
  * [Debugging and monitoring](https://modelcontextprotocol.io/docs/concepts/architecture#debugging-and-monitoring)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Prompts
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Prompts
Create reusable prompt templates and workflows
Prompts enable servers to define reusable prompt templates and workflows that clients can easily surface to users and LLMs. They provide a powerful way to standardize and share common LLM interactions.
Prompts are designed to be **user-controlled** , meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use.
## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#overview)
Overview
Prompts in MCP are predefined templates that can:
  * Accept dynamic arguments
  * Include context from resources
  * Chain multiple interactions
  * Guide specific workflows
  * Surface as UI elements (like slash commands)


## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#prompt-structure)
Prompt structure
Each prompt is defined with:
Copy
```
{
 name: string;       // Unique identifier for the prompt
 description?: string;   // Human-readable description
 arguments?: [       // Optional list of arguments
  {
   name: string;     // Argument identifier
   description?: string; // Argument description
   required?: boolean;  // Whether argument is required
  }
 ]
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#discovering-prompts)
Discovering prompts
Clients can discover available prompts through the `prompts/list` endpoint:
Copy
```
// Request
{
 method: "prompts/list"
}
// Response
{
 prompts: [
  {
   name: "analyze-code",
   description: "Analyze code for potential improvements",
   arguments: [
    {
     name: "language",
     description: "Programming language",
     required: true
    }
   ]
  }
 ]
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#using-prompts)
Using prompts
To use a prompt, clients make a `prompts/get` request:
Copy
```
// Request
{
 method: "prompts/get",
 params: {
  name: "analyze-code",
  arguments: {
   language: "python"
  }
 }
}
// Response
{
 description: "Analyze Python code for potential improvements",
 messages: [
  {
   role: "user",
   content: {
    type: "text",
    text: "Please analyze the following Python code for potential improvements:\n\n```python\ndef calculate_sum(numbers):\n  total = 0\n  for num in numbers:\n    total = total + num\n  return total\n\nresult = calculate_sum([1, 2, 3, 4, 5])\nprint(result)\n```"
   }
  }
 ]
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#dynamic-prompts)
Dynamic prompts
Prompts can be dynamic and include:
### 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#embedded-resource-context)
Embedded resource context
Copy
```
{
 "name": "analyze-project",
 "description": "Analyze project logs and code",
 "arguments": [
  {
   "name": "timeframe",
   "description": "Time period to analyze logs",
   "required": true
  },
  {
   "name": "fileUri",
   "description": "URI of code file to review",
   "required": true
  }
 ]
}

```

When handling the `prompts/get` request:
Copy
```
{
 "messages": [
  {
   "role": "user",
   "content": {
    "type": "text",
    "text": "Analyze these system logs and the code file for any issues:"
   }
  },
  {
   "role": "user",
   "content": {
    "type": "resource",
    "resource": {
     "uri": "logs://recent?timeframe=1h",
     "text": "[2024-03-14 15:32:11] ERROR: Connection timeout in network.py:127\n[2024-03-14 15:32:15] WARN: Retrying connection (attempt 2/3)\n[2024-03-14 15:32:20] ERROR: Max retries exceeded",
     "mimeType": "text/plain"
    }
   }
  },
  {
   "role": "user",
   "content": {
    "type": "resource",
    "resource": {
     "uri": "file:///path/to/code.py",
     "text": "def connect_to_service(timeout=30):\n  retries = 3\n  for attempt in range(retries):\n    try:\n      return establish_connection(timeout)\n    except TimeoutError:\n      if attempt == retries - 1:\n        raise\n      time.sleep(5)\n\ndef establish_connection(timeout):\n  # Connection implementation\n  pass",
     "mimeType": "text/x-python"
    }
   }
  }
 ]
}

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#multi-step-workflows)
Multi-step workflows
Copy
```
const debugWorkflow = {
 name: "debug-error",
 async getMessages(error: string) {
  return [
   {
    role: "user",
    content: {
     type: "text",
     text: `Here's an error I'm seeing: ${error}`
    }
   },
   {
    role: "assistant",
    content: {
     type: "text",
     text: "I'll help analyze this error. What have you tried so far?"
    }
   },
   {
    role: "user",
    content: {
     type: "text",
     text: "I've tried restarting the service, but the error persists."
    }
   }
  ];
 }
};

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#example-implementation)
Example implementation
Here’s a complete example of implementing prompts in an MCP server:
  * TypeScript
  * Python


Copy
```
import { Server } from "@modelcontextprotocol/sdk/server";
import {
 ListPromptsRequestSchema,
 GetPromptRequestSchema
} from "@modelcontextprotocol/sdk/types";
const PROMPTS = {
 "git-commit": {
  name: "git-commit",
  description: "Generate a Git commit message",
  arguments: [
   {
    name: "changes",
    description: "Git diff or description of changes",
    required: true
   }
  ]
 },
 "explain-code": {
  name: "explain-code",
  description: "Explain how code works",
  arguments: [
   {
    name: "code",
    description: "Code to explain",
    required: true
   },
   {
    name: "language",
    description: "Programming language",
    required: false
   }
  ]
 }
};
const server = new Server({
 name: "example-prompts-server",
 version: "1.0.0"
}, {
 capabilities: {
  prompts: {}
 }
});
// List available prompts
server.setRequestHandler(ListPromptsRequestSchema, async () => {
 return {
  prompts: Object.values(PROMPTS)
 };
});
// Get specific prompt
server.setRequestHandler(GetPromptRequestSchema, async (request) => {
 const prompt = PROMPTS[request.params.name];
 if (!prompt) {
  throw new Error(`Prompt not found: ${request.params.name}`);
 }
 if (request.params.name === "git-commit") {
  return {
   messages: [
    {
     role: "user",
     content: {
      type: "text",
      text: `Generate a concise but descriptive commit message for these changes:\n\n${request.params.arguments?.changes}`
     }
    }
   ]
  };
 }
 if (request.params.name === "explain-code") {
  const language = request.params.arguments?.language || "Unknown";
  return {
   messages: [
    {
     role: "user",
     content: {
      type: "text",
      text: `Explain how this ${language} code works:\n\n${request.params.arguments?.code}`
     }
    }
   ]
  };
 }
 throw new Error("Prompt implementation not found");
});

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#best-practices)
Best practices
When implementing prompts:
  1. Use clear, descriptive prompt names
  2. Provide detailed descriptions for prompts and arguments
  3. Validate all required arguments
  4. Handle missing arguments gracefully
  5. Consider versioning for prompt templates
  6. Cache dynamic content when appropriate
  7. Implement error handling
  8. Document expected argument formats
  9. Consider prompt composability
  10. Test prompts with various inputs


## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#ui-integration)
UI integration
Prompts can be surfaced in client UIs as:
  * Slash commands
  * Quick actions
  * Context menu items
  * Command palette entries
  * Guided workflows
  * Interactive forms


## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#updates-and-changes)
Updates and changes
Servers can notify clients about prompt changes:
  1. Server capability: `prompts.listChanged`
  2. Notification: `notifications/prompts/list_changed`
  3. Client re-fetches prompt list


## 
[​](https://modelcontextprotocol.io/docs/concepts/prompts#security-considerations)
Security considerations
When implementing prompts:
  * Validate all arguments
  * Sanitize user input
  * Consider rate limiting
  * Implement access controls
  * Audit prompt usage
  * Handle sensitive data appropriately
  * Validate generated content
  * Implement timeouts
  * Consider prompt injection risks
  * Document security requirements


Was this page helpful?
YesNo
[Resources](https://modelcontextprotocol.io/docs/concepts/resources)[Tools](https://modelcontextprotocol.io/docs/concepts/tools)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Overview](https://modelcontextprotocol.io/docs/concepts/prompts#overview)
  * [Prompt structure](https://modelcontextprotocol.io/docs/concepts/prompts#prompt-structure)
  * [Discovering prompts](https://modelcontextprotocol.io/docs/concepts/prompts#discovering-prompts)
  * [Using prompts](https://modelcontextprotocol.io/docs/concepts/prompts#using-prompts)
  * [Dynamic prompts](https://modelcontextprotocol.io/docs/concepts/prompts#dynamic-prompts)
  * [Embedded resource context](https://modelcontextprotocol.io/docs/concepts/prompts#embedded-resource-context)
  * [Multi-step workflows](https://modelcontextprotocol.io/docs/concepts/prompts#multi-step-workflows)
  * [Example implementation](https://modelcontextprotocol.io/docs/concepts/prompts#example-implementation)
  * [Best practices](https://modelcontextprotocol.io/docs/concepts/prompts#best-practices)
  * [UI integration](https://modelcontextprotocol.io/docs/concepts/prompts#ui-integration)
  * [Updates and changes](https://modelcontextprotocol.io/docs/concepts/prompts#updates-and-changes)
  * [Security considerations](https://modelcontextprotocol.io/docs/concepts/prompts#security-considerations)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Resources
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Resources
Expose data and content from your servers to LLMs
Resources are a core primitive in the Model Context Protocol (MCP) that allow servers to expose data and content that can be read by clients and used as context for LLM interactions.
Resources are designed to be **application-controlled** , meaning that the client application can decide how and when they should be used. Different MCP clients may handle resources differently. For example:
  * Claude Desktop currently requires users to explicitly select resources before they can be used
  * Other clients might automatically select resources based on heuristics
  * Some implementations may even allow the AI model itself to determine which resources to use


Server authors should be prepared to handle any of these interaction patterns when implementing resource support. In order to expose data to models automatically, server authors should use a **model-controlled** primitive such as [Tools](https://modelcontextprotocol.io/docs/concepts/tools).
## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#overview)
Overview
Resources represent any kind of data that an MCP server wants to make available to clients. This can include:
  * File contents
  * Database records
  * API responses
  * Live system data
  * Screenshots and images
  * Log files
  * And more


Each resource is identified by a unique URI and can contain either text or binary data.
## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#resource-uris)
Resource URIs
Resources are identified using URIs that follow this format:
Copy
```
[protocol]://[host]/[path]

```

For example:
  * `file:///home/user/documents/report.pdf`
  * `postgres://database/customers/schema`
  * `screen://localhost/display1`


The protocol and path structure is defined by the MCP server implementation. Servers can define their own custom URI schemes.
## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#resource-types)
Resource types
Resources can contain two types of content:
### 
[​](https://modelcontextprotocol.io/docs/concepts/resources#text-resources)
Text resources
Text resources contain UTF-8 encoded text data. These are suitable for:
  * Source code
  * Configuration files
  * Log files
  * JSON/XML data
  * Plain text


### 
[​](https://modelcontextprotocol.io/docs/concepts/resources#binary-resources)
Binary resources
Binary resources contain raw binary data encoded in base64. These are suitable for:
  * Images
  * PDFs
  * Audio files
  * Video files
  * Other non-text formats


## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#resource-discovery)
Resource discovery
Clients can discover available resources through two main methods:
### 
[​](https://modelcontextprotocol.io/docs/concepts/resources#direct-resources)
Direct resources
Servers expose a list of concrete resources via the `resources/list` endpoint. Each resource includes:
Copy
```
{
 uri: string;      // Unique identifier for the resource
 name: string;     // Human-readable name
 description?: string; // Optional description
 mimeType?: string;   // Optional MIME type
}

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/resources#resource-templates)
Resource templates
For dynamic resources, servers can expose [URI templates](https://datatracker.ietf.org/doc/html/rfc6570) that clients can use to construct valid resource URIs:
Copy
```
{
 uriTemplate: string;  // URI template following RFC 6570
 name: string;     // Human-readable name for this type
 description?: string; // Optional description
 mimeType?: string;   // Optional MIME type for all matching resources
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#reading-resources)
Reading resources
To read a resource, clients make a `resources/read` request with the resource URI.
The server responds with a list of resource contents:
Copy
```
{
 contents: [
  {
   uri: string;    // The URI of the resource
   mimeType?: string; // Optional MIME type
   // One of:
   text?: string;   // For text resources
   blob?: string;   // For binary resources (base64 encoded)
  }
 ]
}

```

Servers may return multiple resources in response to one `resources/read` request. This could be used, for example, to return a list of files inside a directory when the directory is read.
## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#resource-updates)
Resource updates
MCP supports real-time updates for resources through two mechanisms:
### 
[​](https://modelcontextprotocol.io/docs/concepts/resources#list-changes)
List changes
Servers can notify clients when their list of available resources changes via the `notifications/resources/list_changed` notification.
### 
[​](https://modelcontextprotocol.io/docs/concepts/resources#content-changes)
Content changes
Clients can subscribe to updates for specific resources:
  1. Client sends `resources/subscribe` with resource URI
  2. Server sends `notifications/resources/updated` when the resource changes
  3. Client can fetch latest content with `resources/read`
  4. Client can unsubscribe with `resources/unsubscribe`


## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#example-implementation)
Example implementation
Here’s a simple example of implementing resource support in an MCP server:
  * TypeScript
  * Python


Copy
```
const server = new Server({
 name: "example-server",
 version: "1.0.0"
}, {
 capabilities: {
  resources: {}
 }
});
// List available resources
server.setRequestHandler(ListResourcesRequestSchema, async () => {
 return {
  resources: [
   {
    uri: "file:///logs/app.log",
    name: "Application Logs",
    mimeType: "text/plain"
   }
  ]
 };
});
// Read resource contents
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
 const uri = request.params.uri;
 if (uri === "file:///logs/app.log") {
  const logContents = await readLogFile();
  return {
   contents: [
    {
     uri,
     mimeType: "text/plain",
     text: logContents
    }
   ]
  };
 }
 throw new Error("Resource not found");
});

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#best-practices)
Best practices
When implementing resource support:
  1. Use clear, descriptive resource names and URIs
  2. Include helpful descriptions to guide LLM understanding
  3. Set appropriate MIME types when known
  4. Implement resource templates for dynamic content
  5. Use subscriptions for frequently changing resources
  6. Handle errors gracefully with clear error messages
  7. Consider pagination for large resource lists
  8. Cache resource contents when appropriate
  9. Validate URIs before processing
  10. Document your custom URI schemes


## 
[​](https://modelcontextprotocol.io/docs/concepts/resources#security-considerations)
Security considerations
When exposing resources:
  * Validate all resource URIs
  * Implement appropriate access controls
  * Sanitize file paths to prevent directory traversal
  * Be cautious with binary data handling
  * Consider rate limiting for resource reads
  * Audit resource access
  * Encrypt sensitive data in transit
  * Validate MIME types
  * Implement timeouts for long-running reads
  * Handle resource cleanup appropriately


Was this page helpful?
YesNo
[Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)[Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Overview](https://modelcontextprotocol.io/docs/concepts/resources#overview)
  * [Resource URIs](https://modelcontextprotocol.io/docs/concepts/resources#resource-uris)
  * [Resource types](https://modelcontextprotocol.io/docs/concepts/resources#resource-types)
  * [Text resources](https://modelcontextprotocol.io/docs/concepts/resources#text-resources)
  * [Binary resources](https://modelcontextprotocol.io/docs/concepts/resources#binary-resources)
  * [Resource discovery](https://modelcontextprotocol.io/docs/concepts/resources#resource-discovery)
  * [Direct resources](https://modelcontextprotocol.io/docs/concepts/resources#direct-resources)
  * [Resource templates](https://modelcontextprotocol.io/docs/concepts/resources#resource-templates)
  * [Reading resources](https://modelcontextprotocol.io/docs/concepts/resources#reading-resources)
  * [Resource updates](https://modelcontextprotocol.io/docs/concepts/resources#resource-updates)
  * [List changes](https://modelcontextprotocol.io/docs/concepts/resources#list-changes)
  * [Content changes](https://modelcontextprotocol.io/docs/concepts/resources#content-changes)
  * [Example implementation](https://modelcontextprotocol.io/docs/concepts/resources#example-implementation)
  * [Best practices](https://modelcontextprotocol.io/docs/concepts/resources#best-practices)
  * [Security considerations](https://modelcontextprotocol.io/docs/concepts/resources#security-considerations)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Roots
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Roots
Understanding roots in MCP
Roots are a concept in MCP that define the boundaries where servers can operate. They provide a way for clients to inform servers about relevant resources and their locations.
## 
[​](https://modelcontextprotocol.io/docs/concepts/roots#what-are-roots%3F)
What are Roots?
A root is a URI that a client suggests a server should focus on. When a client connects to a server, it declares which roots the server should work with. While primarily used for filesystem paths, roots can be any valid URI including HTTP URLs.
For example, roots could be:
Copy
```
file:///home/user/projects/myapp
https://api.example.com/v1

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/roots#why-use-roots%3F)
Why Use Roots?
Roots serve several important purposes:
  1. **Guidance** : They inform servers about relevant resources and locations
  2. **Clarity** : Roots make it clear which resources are part of your workspace
  3. **Organization** : Multiple roots let you work with different resources simultaneously


## 
[​](https://modelcontextprotocol.io/docs/concepts/roots#how-roots-work)
How Roots Work
When a client supports roots, it:
  1. Declares the `roots` capability during connection
  2. Provides a list of suggested roots to the server
  3. Notifies the server when roots change (if supported)


While roots are informational and not strictly enforcing, servers should:
  1. Respect the provided roots
  2. Use root URIs to locate and access resources
  3. Prioritize operations within root boundaries


## 
[​](https://modelcontextprotocol.io/docs/concepts/roots#common-use-cases)
Common Use Cases
Roots are commonly used to define:
  * Project directories
  * Repository locations
  * API endpoints
  * Configuration locations
  * Resource boundaries


## 
[​](https://modelcontextprotocol.io/docs/concepts/roots#best-practices)
Best Practices
When working with roots:
  1. Only suggest necessary resources
  2. Use clear, descriptive names for roots
  3. Monitor root accessibility
  4. Handle root changes gracefully


## 
[​](https://modelcontextprotocol.io/docs/concepts/roots#example)
Example
Here’s how a typical MCP client might expose roots:
Copy
```
{
 "roots": [
  {
   "uri": "file:///home/user/projects/frontend",
   "name": "Frontend Repository"
  },
  {
   "uri": "https://api.example.com/v1",
   "name": "API Endpoint"
  }
 ]
}

```

This configuration suggests the server focus on both a local repository and an API endpoint while keeping them logically separated.
Was this page helpful?
YesNo
[Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)[Transports](https://modelcontextprotocol.io/docs/concepts/transports)
[github](https://github.com/modelcontextprotocol)
On this page
  * [What are Roots?](https://modelcontextprotocol.io/docs/concepts/roots#what-are-roots%3F)
  * [Why Use Roots?](https://modelcontextprotocol.io/docs/concepts/roots#why-use-roots%3F)
  * [How Roots Work](https://modelcontextprotocol.io/docs/concepts/roots#how-roots-work)
  * [Common Use Cases](https://modelcontextprotocol.io/docs/concepts/roots#common-use-cases)
  * [Best Practices](https://modelcontextprotocol.io/docs/concepts/roots#best-practices)
  * [Example](https://modelcontextprotocol.io/docs/concepts/roots#example)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Sampling
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Sampling
Let your servers request completions from LLMs
Sampling is a powerful MCP feature that allows servers to request LLM completions through the client, enabling sophisticated agentic behaviors while maintaining security and privacy.
This feature of MCP is not yet supported in the Claude Desktop client.
## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#how-sampling-works)
How sampling works
The sampling flow follows these steps:
  1. Server sends a `sampling/createMessage` request to the client
  2. Client reviews the request and can modify it
  3. Client samples from an LLM
  4. Client reviews the completion
  5. Client returns the result to the server


This human-in-the-loop design ensures users maintain control over what the LLM sees and generates.
## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#message-format)
Message format
Sampling requests use a standardized message format:
Copy
```
{
 messages: [
  {
   role: "user" | "assistant",
   content: {
    type: "text" | "image",
    // For text:
    text?: string,
    // For images:
    data?: string,       // base64 encoded
    mimeType?: string
   }
  }
 ],
 modelPreferences?: {
  hints?: [{
   name?: string        // Suggested model name/family
  }],
  costPriority?: number,     // 0-1, importance of minimizing cost
  speedPriority?: number,    // 0-1, importance of low latency
  intelligencePriority?: number // 0-1, importance of capabilities
 },
 systemPrompt?: string,
 includeContext?: "none" | "thisServer" | "allServers",
 temperature?: number,
 maxTokens: number,
 stopSequences?: string[],
 metadata?: Record<string, unknown>
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#request-parameters)
Request parameters
### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#messages)
Messages
The `messages` array contains the conversation history to send to the LLM. Each message has:
  * `role`: Either “user” or “assistant”
  * `content`: The message content, which can be: 
    * Text content with a `text` field
    * Image content with `data` (base64) and `mimeType` fields


### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#model-preferences)
Model preferences
The `modelPreferences` object allows servers to specify their model selection preferences:
  * `hints`: Array of model name suggestions that clients can use to select an appropriate model:
    * `name`: String that can match full or partial model names (e.g. “claude-3”, “sonnet”)
    * Clients may map hints to equivalent models from different providers
    * Multiple hints are evaluated in preference order
  * Priority values (0-1 normalized):
    * `costPriority`: Importance of minimizing costs
    * `speedPriority`: Importance of low latency response
    * `intelligencePriority`: Importance of advanced model capabilities


Clients make the final model selection based on these preferences and their available models.
### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#system-prompt)
System prompt
An optional `systemPrompt` field allows servers to request a specific system prompt. The client may modify or ignore this.
### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#context-inclusion)
Context inclusion
The `includeContext` parameter specifies what MCP context to include:
  * `"none"`: No additional context
  * `"thisServer"`: Include context from the requesting server
  * `"allServers"`: Include context from all connected MCP servers


The client controls what context is actually included.
### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#sampling-parameters)
Sampling parameters
Fine-tune the LLM sampling with:
  * `temperature`: Controls randomness (0.0 to 1.0)
  * `maxTokens`: Maximum tokens to generate
  * `stopSequences`: Array of sequences that stop generation
  * `metadata`: Additional provider-specific parameters


## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#response-format)
Response format
The client returns a completion result:
Copy
```
{
 model: string, // Name of the model used
 stopReason?: "endTurn" | "stopSequence" | "maxTokens" | string,
 role: "user" | "assistant",
 content: {
  type: "text" | "image",
  text?: string,
  data?: string,
  mimeType?: string
 }
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#example-request)
Example request
Here’s an example of requesting sampling from a client:
Copy
```
{
 "method": "sampling/createMessage",
 "params": {
  "messages": [
   {
    "role": "user",
    "content": {
     "type": "text",
     "text": "What files are in the current directory?"
    }
   }
  ],
  "systemPrompt": "You are a helpful file system assistant.",
  "includeContext": "thisServer",
  "maxTokens": 100
 }
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#best-practices)
Best practices
When implementing sampling:
  1. Always provide clear, well-structured prompts
  2. Handle both text and image content appropriately
  3. Set reasonable token limits
  4. Include relevant context through `includeContext`
  5. Validate responses before using them
  6. Handle errors gracefully
  7. Consider rate limiting sampling requests
  8. Document expected sampling behavior
  9. Test with various model parameters
  10. Monitor sampling costs


## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#human-in-the-loop-controls)
Human in the loop controls
Sampling is designed with human oversight in mind:
### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#for-prompts)
For prompts
  * Clients should show users the proposed prompt
  * Users should be able to modify or reject prompts
  * System prompts can be filtered or modified
  * Context inclusion is controlled by the client


### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#for-completions)
For completions
  * Clients should show users the completion
  * Users should be able to modify or reject completions
  * Clients can filter or modify completions
  * Users control which model is used


## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#security-considerations)
Security considerations
When implementing sampling:
  * Validate all message content
  * Sanitize sensitive information
  * Implement appropriate rate limits
  * Monitor sampling usage
  * Encrypt data in transit
  * Handle user data privacy
  * Audit sampling requests
  * Control cost exposure
  * Implement timeouts
  * Handle model errors gracefully


## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#common-patterns)
Common patterns
### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#agentic-workflows)
Agentic workflows
Sampling enables agentic patterns like:
  * Reading and analyzing resources
  * Making decisions based on context
  * Generating structured data
  * Handling multi-step tasks
  * Providing interactive assistance


### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#context-management)
Context management
Best practices for context:
  * Request minimal necessary context
  * Structure context clearly
  * Handle context size limits
  * Update context as needed
  * Clean up stale context


### 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#error-handling)
Error handling
Robust error handling should:
  * Catch sampling failures
  * Handle timeout errors
  * Manage rate limits
  * Validate responses
  * Provide fallback behaviors
  * Log errors appropriately


## 
[​](https://modelcontextprotocol.io/docs/concepts/sampling#limitations)
Limitations
Be aware of these limitations:
  * Sampling depends on client capabilities
  * Users control sampling behavior
  * Context size has limits
  * Rate limits may apply
  * Costs should be considered
  * Model availability varies
  * Response times vary
  * Not all content types supported


Was this page helpful?
YesNo
[Tools](https://modelcontextprotocol.io/docs/concepts/tools)[Roots](https://modelcontextprotocol.io/docs/concepts/roots)
[github](https://github.com/modelcontextprotocol)
On this page
  * [How sampling works](https://modelcontextprotocol.io/docs/concepts/sampling#how-sampling-works)
  * [Message format](https://modelcontextprotocol.io/docs/concepts/sampling#message-format)
  * [Request parameters](https://modelcontextprotocol.io/docs/concepts/sampling#request-parameters)
  * [Messages](https://modelcontextprotocol.io/docs/concepts/sampling#messages)
  * [Model preferences](https://modelcontextprotocol.io/docs/concepts/sampling#model-preferences)
  * [System prompt](https://modelcontextprotocol.io/docs/concepts/sampling#system-prompt)
  * [Context inclusion](https://modelcontextprotocol.io/docs/concepts/sampling#context-inclusion)
  * [Sampling parameters](https://modelcontextprotocol.io/docs/concepts/sampling#sampling-parameters)
  * [Response format](https://modelcontextprotocol.io/docs/concepts/sampling#response-format)
  * [Example request](https://modelcontextprotocol.io/docs/concepts/sampling#example-request)
  * [Best practices](https://modelcontextprotocol.io/docs/concepts/sampling#best-practices)
  * [Human in the loop controls](https://modelcontextprotocol.io/docs/concepts/sampling#human-in-the-loop-controls)
  * [For prompts](https://modelcontextprotocol.io/docs/concepts/sampling#for-prompts)
  * [For completions](https://modelcontextprotocol.io/docs/concepts/sampling#for-completions)
  * [Security considerations](https://modelcontextprotocol.io/docs/concepts/sampling#security-considerations)
  * [Common patterns](https://modelcontextprotocol.io/docs/concepts/sampling#common-patterns)
  * [Agentic workflows](https://modelcontextprotocol.io/docs/concepts/sampling#agentic-workflows)
  * [Context management](https://modelcontextprotocol.io/docs/concepts/sampling#context-management)
  * [Error handling](https://modelcontextprotocol.io/docs/concepts/sampling#error-handling)
  * [Limitations](https://modelcontextprotocol.io/docs/concepts/sampling#limitations)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Tools
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Tools
Enable LLMs to perform actions through your server
Tools are a powerful primitive in the Model Context Protocol (MCP) that enable servers to expose executable functionality to clients. Through tools, LLMs can interact with external systems, perform computations, and take actions in the real world.
Tools are designed to be **model-controlled** , meaning that tools are exposed from servers to clients with the intention of the AI model being able to automatically invoke them (with a human in the loop to grant approval).
## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#overview)
Overview
Tools in MCP allow servers to expose executable functions that can be invoked by clients and used by LLMs to perform actions. Key aspects of tools include:
  * **Discovery** : Clients can list available tools through the `tools/list` endpoint
  * **Invocation** : Tools are called using the `tools/call` endpoint, where servers perform the requested operation and return results
  * **Flexibility** : Tools can range from simple calculations to complex API interactions


Like [resources](https://modelcontextprotocol.io/docs/concepts/resources), tools are identified by unique names and can include descriptions to guide their usage. However, unlike resources, tools represent dynamic operations that can modify state or interact with external systems.
## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#tool-definition-structure)
Tool definition structure
Each tool is defined with the following structure:
Copy
```
{
 name: string;     // Unique identifier for the tool
 description?: string; // Human-readable description
 inputSchema: {     // JSON Schema for the tool's parameters
  type: "object",
  properties: { ... } // Tool-specific parameters
 }
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#implementing-tools)
Implementing tools
Here’s an example of implementing a basic tool in an MCP server:
  * TypeScript
  * Python


Copy
```
const server = new Server({
 name: "example-server",
 version: "1.0.0"
}, {
 capabilities: {
  tools: {}
 }
});
// Define available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
 return {
  tools: [{
   name: "calculate_sum",
   description: "Add two numbers together",
   inputSchema: {
    type: "object",
    properties: {
     a: { type: "number" },
     b: { type: "number" }
    },
    required: ["a", "b"]
   }
  }]
 };
});
// Handle tool execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
 if (request.params.name === "calculate_sum") {
  const { a, b } = request.params.arguments;
  return {
   content: [
    {
     type: "text",
     text: String(a + b)
    }
   ]
  };
 }
 throw new Error("Tool not found");
});

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#example-tool-patterns)
Example tool patterns
Here are some examples of types of tools that a server could provide:
### 
[​](https://modelcontextprotocol.io/docs/concepts/tools#system-operations)
System operations
Tools that interact with the local system:
Copy
```
{
 name: "execute_command",
 description: "Run a shell command",
 inputSchema: {
  type: "object",
  properties: {
   command: { type: "string" },
   args: { type: "array", items: { type: "string" } }
  }
 }
}

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/tools#api-integrations)
API integrations
Tools that wrap external APIs:
Copy
```
{
 name: "github_create_issue",
 description: "Create a GitHub issue",
 inputSchema: {
  type: "object",
  properties: {
   title: { type: "string" },
   body: { type: "string" },
   labels: { type: "array", items: { type: "string" } }
  }
 }
}

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/tools#data-processing)
Data processing
Tools that transform or analyze data:
Copy
```
{
 name: "analyze_csv",
 description: "Analyze a CSV file",
 inputSchema: {
  type: "object",
  properties: {
   filepath: { type: "string" },
   operations: {
    type: "array",
    items: {
     enum: ["sum", "average", "count"]
    }
   }
  }
 }
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#best-practices)
Best practices
When implementing tools:
  1. Provide clear, descriptive names and descriptions
  2. Use detailed JSON Schema definitions for parameters
  3. Include examples in tool descriptions to demonstrate how the model should use them
  4. Implement proper error handling and validation
  5. Use progress reporting for long operations
  6. Keep tool operations focused and atomic
  7. Document expected return value structures
  8. Implement proper timeouts
  9. Consider rate limiting for resource-intensive operations
  10. Log tool usage for debugging and monitoring


## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#security-considerations)
Security considerations
When exposing tools:
### 
[​](https://modelcontextprotocol.io/docs/concepts/tools#input-validation)
Input validation
  * Validate all parameters against the schema
  * Sanitize file paths and system commands
  * Validate URLs and external identifiers
  * Check parameter sizes and ranges
  * Prevent command injection


### 
[​](https://modelcontextprotocol.io/docs/concepts/tools#access-control)
Access control
  * Implement authentication where needed
  * Use appropriate authorization checks
  * Audit tool usage
  * Rate limit requests
  * Monitor for abuse


### 
[​](https://modelcontextprotocol.io/docs/concepts/tools#error-handling)
Error handling
  * Don’t expose internal errors to clients
  * Log security-relevant errors
  * Handle timeouts appropriately
  * Clean up resources after errors
  * Validate return values


## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#tool-discovery-and-updates)
Tool discovery and updates
MCP supports dynamic tool discovery:
  1. Clients can list available tools at any time
  2. Servers can notify clients when tools change using `notifications/tools/list_changed`
  3. Tools can be added or removed during runtime
  4. Tool definitions can be updated (though this should be done carefully)


## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#error-handling-2)
Error handling
Tool errors should be reported within the result object, not as MCP protocol-level errors. This allows the LLM to see and potentially handle the error. When a tool encounters an error:
  1. Set `isError` to `true` in the result
  2. Include error details in the `content` array


Here’s an example of proper error handling for tools:
  * TypeScript
  * Python


Copy
```
try {
 // Tool operation
 const result = performOperation();
 return {
  content: [
   {
    type: "text",
    text: `Operation successful: ${result}`
   }
  ]
 };
} catch (error) {
 return {
  isError: true,
  content: [
   {
    type: "text",
    text: `Error: ${error.message}`
   }
  ]
 };
}

```

This approach allows the LLM to see that an error occurred and potentially take corrective action or request human intervention.
## 
[​](https://modelcontextprotocol.io/docs/concepts/tools#testing-tools)
Testing tools
A comprehensive testing strategy for MCP tools should cover:
  * **Functional testing** : Verify tools execute correctly with valid inputs and handle invalid inputs appropriately
  * **Integration testing** : Test tool interaction with external systems using both real and mocked dependencies
  * **Security testing** : Validate authentication, authorization, input sanitization, and rate limiting
  * **Performance testing** : Check behavior under load, timeout handling, and resource cleanup
  * **Error handling** : Ensure tools properly report errors through the MCP protocol and clean up resources


Was this page helpful?
YesNo
[Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)[Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Overview](https://modelcontextprotocol.io/docs/concepts/tools#overview)
  * [Tool definition structure](https://modelcontextprotocol.io/docs/concepts/tools#tool-definition-structure)
  * [Implementing tools](https://modelcontextprotocol.io/docs/concepts/tools#implementing-tools)
  * [Example tool patterns](https://modelcontextprotocol.io/docs/concepts/tools#example-tool-patterns)
  * [System operations](https://modelcontextprotocol.io/docs/concepts/tools#system-operations)
  * [API integrations](https://modelcontextprotocol.io/docs/concepts/tools#api-integrations)
  * [Data processing](https://modelcontextprotocol.io/docs/concepts/tools#data-processing)
  * [Best practices](https://modelcontextprotocol.io/docs/concepts/tools#best-practices)
  * [Security considerations](https://modelcontextprotocol.io/docs/concepts/tools#security-considerations)
  * [Input validation](https://modelcontextprotocol.io/docs/concepts/tools#input-validation)
  * [Access control](https://modelcontextprotocol.io/docs/concepts/tools#access-control)
  * [Error handling](https://modelcontextprotocol.io/docs/concepts/tools#error-handling)
  * [Tool discovery and updates](https://modelcontextprotocol.io/docs/concepts/tools#tool-discovery-and-updates)
  * [Error handling](https://modelcontextprotocol.io/docs/concepts/tools#error-handling-2)
  * [Testing tools](https://modelcontextprotocol.io/docs/concepts/tools#testing-tools)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Concepts
Transports
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Concepts
# Transports
Learn about MCP’s communication mechanisms
Transports in the Model Context Protocol (MCP) provide the foundation for communication between clients and servers. A transport handles the underlying mechanics of how messages are sent and received.
## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#message-format)
Message Format
MCP uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 as its wire format. The transport layer is responsible for converting MCP protocol messages into JSON-RPC format for transmission and converting received JSON-RPC messages back into MCP protocol messages.
There are three types of JSON-RPC messages used:
### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#requests)
Requests
Copy
```
{
 jsonrpc: "2.0",
 id: number | string,
 method: string,
 params?: object
}

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#responses)
Responses
Copy
```
{
 jsonrpc: "2.0",
 id: number | string,
 result?: object,
 error?: {
  code: number,
  message: string,
  data?: unknown
 }
}

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#notifications)
Notifications
Copy
```
{
 jsonrpc: "2.0",
 method: string,
 params?: object
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#built-in-transport-types)
Built-in Transport Types
MCP includes two standard transport implementations:
### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio)
Standard Input/Output (stdio)
The stdio transport enables communication through standard input and output streams. This is particularly useful for local integrations and command-line tools.
Use stdio when:
  * Building command-line tools
  * Implementing local integrations
  * Needing simple process communication
  * Working with shell scripts


  * TypeScript (Server)
  * TypeScript (Client)
  * Python (Server)
  * Python (Client)


Copy
```
const server = new Server({
 name: "example-server",
 version: "1.0.0"
}, {
 capabilities: {}
});
const transport = new StdioServerTransport();
await server.connect(transport);

```

### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse)
Server-Sent Events (SSE)
SSE transport enables server-to-client streaming with HTTP POST requests for client-to-server communication.
Use SSE when:
  * Only server-to-client streaming is needed
  * Working with restricted networks
  * Implementing simple updates


  * TypeScript (Server)
  * TypeScript (Client)
  * Python (Server)
  * Python (Client)


Copy
```
import express from "express";
const app = express();
const server = new Server({
 name: "example-server",
 version: "1.0.0"
}, {
 capabilities: {}
});
let transport: SSEServerTransport | null = null;
app.get("/sse", (req, res) => {
 transport = new SSEServerTransport("/messages", res);
 server.connect(transport);
});
app.post("/messages", (req, res) => {
 if (transport) {
  transport.handlePostMessage(req, res);
 }
});
app.listen(3000);

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#custom-transports)
Custom Transports
MCP makes it easy to implement custom transports for specific needs. Any transport implementation just needs to conform to the Transport interface:
You can implement custom transports for:
  * Custom network protocols
  * Specialized communication channels
  * Integration with existing systems
  * Performance optimization


  * TypeScript
  * Python


Copy
```
interface Transport {
 // Start processing messages
 start(): Promise<void>;
 // Send a JSON-RPC message
 send(message: JSONRPCMessage): Promise<void>;
 // Close the connection
 close(): Promise<void>;
 // Callbacks
 onclose?: () => void;
 onerror?: (error: Error) => void;
 onmessage?: (message: JSONRPCMessage) => void;
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#error-handling)
Error Handling
Transport implementations should handle various error scenarios:
  1. Connection errors
  2. Message parsing errors
  3. Protocol errors
  4. Network timeouts
  5. Resource cleanup


Example error handling:
  * TypeScript
  * Python


Copy
```
class ExampleTransport implements Transport {
 async start() {
  try {
   // Connection logic
  } catch (error) {
   this.onerror?.(new Error(`Failed to connect: ${error}`));
   throw error;
  }
 }
 async send(message: JSONRPCMessage) {
  try {
   // Sending logic
  } catch (error) {
   this.onerror?.(new Error(`Failed to send message: ${error}`));
   throw error;
  }
 }
}

```

## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#best-practices)
Best Practices
When implementing or using MCP transport:
  1. Handle connection lifecycle properly
  2. Implement proper error handling
  3. Clean up resources on connection close
  4. Use appropriate timeouts
  5. Validate messages before sending
  6. Log transport events for debugging
  7. Implement reconnection logic when appropriate
  8. Handle backpressure in message queues
  9. Monitor connection health
  10. Implement proper security measures


## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations)
Security Considerations
When implementing transport:
### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#authentication-and-authorization)
Authentication and Authorization
  * Implement proper authentication mechanisms
  * Validate client credentials
  * Use secure token handling
  * Implement authorization checks


### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#data-security)
Data Security
  * Use TLS for network transport
  * Encrypt sensitive data
  * Validate message integrity
  * Implement message size limits
  * Sanitize input data


### 
[​](https://modelcontextprotocol.io/docs/concepts/transports#network-security)
Network Security
  * Implement rate limiting
  * Use appropriate timeouts
  * Handle denial of service scenarios
  * Monitor for unusual patterns
  * Implement proper firewall rules


## 
[​](https://modelcontextprotocol.io/docs/concepts/transports#debugging-transport)
Debugging Transport
Tips for debugging transport issues:
  1. Enable debug logging
  2. Monitor message flow
  3. Check connection states
  4. Validate message formats
  5. Test error scenarios
  6. Use network analysis tools
  7. Implement health checks
  8. Monitor resource usage
  9. Test edge cases
  10. Use proper error tracking


Was this page helpful?
YesNo
[Roots](https://modelcontextprotocol.io/docs/concepts/roots)[What's New](https://modelcontextprotocol.io/development/updates)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Message Format](https://modelcontextprotocol.io/docs/concepts/transports#message-format)
  * [Requests](https://modelcontextprotocol.io/docs/concepts/transports#requests)
  * [Responses](https://modelcontextprotocol.io/docs/concepts/transports#responses)
  * [Notifications](https://modelcontextprotocol.io/docs/concepts/transports#notifications)
  * [Built-in Transport Types](https://modelcontextprotocol.io/docs/concepts/transports#built-in-transport-types)
  * [Standard Input/Output (stdio)](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio)
  * [Server-Sent Events (SSE)](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse)
  * [Custom Transports](https://modelcontextprotocol.io/docs/concepts/transports#custom-transports)
  * [Error Handling](https://modelcontextprotocol.io/docs/concepts/transports#error-handling)
  * [Best Practices](https://modelcontextprotocol.io/docs/concepts/transports#best-practices)
  * [Security Considerations](https://modelcontextprotocol.io/docs/concepts/transports#security-considerations)
  * [Authentication and Authorization](https://modelcontextprotocol.io/docs/concepts/transports#authentication-and-authorization)
  * [Data Security](https://modelcontextprotocol.io/docs/concepts/transports#data-security)
  * [Network Security](https://modelcontextprotocol.io/docs/concepts/transports#network-security)
  * [Debugging Transport](https://modelcontextprotocol.io/docs/concepts/transports#debugging-transport)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Tutorials
Debugging
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Tutorials
# Debugging
A comprehensive guide to debugging Model Context Protocol (MCP) integrations
Effective debugging is essential when developing MCP servers or integrating them with applications. This guide covers the debugging tools and approaches available in the MCP ecosystem.
This guide is for macOS. Guides for other platforms are coming soon.
## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#debugging-tools-overview)
Debugging tools overview
MCP provides several tools for debugging at different levels:
  1. **MCP Inspector**
     * Interactive debugging interface
     * Direct server testing
     * See the [Inspector guide](https://modelcontextprotocol.io/docs/tools/inspector) for details
  2. **Claude Desktop Developer Tools**
     * Integration testing
     * Log collection
     * Chrome DevTools integration
  3. **Server Logging**
     * Custom logging implementations
     * Error tracking
     * Performance monitoring


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#debugging-in-claude-desktop)
Debugging in Claude Desktop
### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#checking-server-status)
Checking server status
The Claude.app interface provides basic server status information:
  1. Click the ![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-plug-icon.svg) icon to view:
     * Connected servers
     * Available prompts and resources
  2. Click the ![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg) icon to view:
     * Tools made available to the model


### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#viewing-logs)
Viewing logs
Review detailed MCP logs from Claude Desktop:
Copy
```
# Follow logs in real-time
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log

```

The logs capture:
  * Server connection events
  * Configuration issues
  * Runtime errors
  * Message exchanges


### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#using-chrome-devtools)
Using Chrome DevTools
Access Chrome’s developer tools inside Claude Desktop to investigate client-side errors:
  1. Create a `developer_settings.json` file with `allowDevTools` set to true:


Copy
```
echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json

```

  1. Open DevTools: `Command-Option-Shift-i`


Note: You’ll see two DevTools windows:
  * Main content window
  * App title bar window


Use the Console panel to inspect client-side errors.
Use the Network panel to inspect:
  * Message payloads
  * Connection timing


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#common-issues)
Common issues
### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#working-directory)
Working directory
When using MCP servers with Claude Desktop:
  * The working directory for servers launched via `claude_desktop_config.json` may be undefined (like `/` on macOS) since Claude Desktop could be started from anywhere
  * Always use absolute paths in your configuration and `.env` files to ensure reliable operation
  * For testing servers directly via command line, the working directory will be where you run the command


For example in `claude_desktop_config.json`, use:
Copy
```
{
 "command": "npx",
 "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/data"]
}

```

Instead of relative paths like `./data`
### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#environment-variables)
Environment variables
MCP servers inherit only a subset of environment variables automatically, like `USER`, `HOME`, and `PATH`.
To override the default variables or provide your own, you can specify an `env` key in `claude_desktop_config.json`:
Copy
```
{
 "myserver": {
  "command": "mcp-server-myapp",
  "env": {
   "MYAPP_API_KEY": "some_key",
  }
 }
}

```

### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#server-initialization)
Server initialization
Common initialization problems:
  1. **Path Issues**
     * Incorrect server executable path
     * Missing required files
     * Permission problems
     * Try using an absolute path for `command`
  2. **Configuration Errors**
     * Invalid JSON syntax
     * Missing required fields
     * Type mismatches
  3. **Environment Problems**
     * Missing environment variables
     * Incorrect variable values
     * Permission restrictions


### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#connection-problems)
Connection problems
When servers fail to connect:
  1. Check Claude Desktop logs
  2. Verify server process is running
  3. Test standalone with [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
  4. Verify protocol compatibility


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#implementing-logging)
Implementing logging
### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#server-side-logging)
Server-side logging
When building a server that uses the local stdio [transport](https://modelcontextprotocol.io/docs/concepts/transports), all messages logged to stderr (standard error) will be captured by the host application (e.g., Claude Desktop) automatically.
Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation.
For all [transports](https://modelcontextprotocol.io/docs/concepts/transports), you can also provide logging to the client by sending a log message notification:
  * Python
  * TypeScript


Copy
```
server.request_context.session.send_log_message(
 level="info",
 data="Server started successfully",
)

```

Important events to log:
  * Initialization steps
  * Resource access
  * Tool execution
  * Error conditions
  * Performance metrics


### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#client-side-logging)
Client-side logging
In client applications:
  1. Enable debug logging
  2. Monitor network traffic
  3. Track message exchanges
  4. Record error states


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#debugging-workflow)
Debugging workflow
### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#development-cycle)
Development cycle
  1. Initial Development
     * Use [Inspector](https://modelcontextprotocol.io/docs/tools/inspector) for basic testing
     * Implement core functionality
     * Add logging points
  2. Integration Testing
     * Test in Claude Desktop
     * Monitor logs
     * Check error handling


### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#testing-changes)
Testing changes
To test changes efficiently:
  * **Configuration changes** : Restart Claude Desktop
  * **Server code changes** : Use Command-R to reload
  * **Quick iteration** : Use [Inspector](https://modelcontextprotocol.io/docs/tools/inspector) during development


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#best-practices)
Best practices
### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#logging-strategy)
Logging strategy
  1. **Structured Logging**
     * Use consistent formats
     * Include context
     * Add timestamps
     * Track request IDs
  2. **Error Handling**
     * Log stack traces
     * Include error context
     * Track error patterns
     * Monitor recovery
  3. **Performance Tracking**
     * Log operation timing
     * Monitor resource usage
     * Track message sizes
     * Measure latency


### 
[​](https://modelcontextprotocol.io/docs/tools/debugging#security-considerations)
Security considerations
When debugging:
  1. **Sensitive Data**
     * Sanitize logs
     * Protect credentials
     * Mask personal information
  2. **Access Control**
     * Verify permissions
     * Check authentication
     * Monitor access patterns


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#getting-help)
Getting help
When encountering issues:
  1. **First Steps**
     * Check server logs
     * Test with [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
     * Review configuration
     * Verify environment
  2. **Support Channels**
     * GitHub issues
     * GitHub discussions
  3. **Providing Information**
     * Log excerpts
     * Configuration files
     * Steps to reproduce
     * Environment details


## 
[​](https://modelcontextprotocol.io/docs/tools/debugging#next-steps)
Next steps
## [MCP InspectorLearn to use the MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
Was this page helpful?
YesNo
[Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)[Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Debugging tools overview](https://modelcontextprotocol.io/docs/tools/debugging#debugging-tools-overview)
  * [Debugging in Claude Desktop](https://modelcontextprotocol.io/docs/tools/debugging#debugging-in-claude-desktop)
  * [Checking server status](https://modelcontextprotocol.io/docs/tools/debugging#checking-server-status)
  * [Viewing logs](https://modelcontextprotocol.io/docs/tools/debugging#viewing-logs)
  * [Using Chrome DevTools](https://modelcontextprotocol.io/docs/tools/debugging#using-chrome-devtools)
  * [Common issues](https://modelcontextprotocol.io/docs/tools/debugging#common-issues)
  * [Working directory](https://modelcontextprotocol.io/docs/tools/debugging#working-directory)
  * [Environment variables](https://modelcontextprotocol.io/docs/tools/debugging#environment-variables)
  * [Server initialization](https://modelcontextprotocol.io/docs/tools/debugging#server-initialization)
  * [Connection problems](https://modelcontextprotocol.io/docs/tools/debugging#connection-problems)
  * [Implementing logging](https://modelcontextprotocol.io/docs/tools/debugging#implementing-logging)
  * [Server-side logging](https://modelcontextprotocol.io/docs/tools/debugging#server-side-logging)
  * [Client-side logging](https://modelcontextprotocol.io/docs/tools/debugging#client-side-logging)
  * [Debugging workflow](https://modelcontextprotocol.io/docs/tools/debugging#debugging-workflow)
  * [Development cycle](https://modelcontextprotocol.io/docs/tools/debugging#development-cycle)
  * [Testing changes](https://modelcontextprotocol.io/docs/tools/debugging#testing-changes)
  * [Best practices](https://modelcontextprotocol.io/docs/tools/debugging#best-practices)
  * [Logging strategy](https://modelcontextprotocol.io/docs/tools/debugging#logging-strategy)
  * [Security considerations](https://modelcontextprotocol.io/docs/tools/debugging#security-considerations)
  * [Getting help](https://modelcontextprotocol.io/docs/tools/debugging#getting-help)
  * [Next steps](https://modelcontextprotocol.io/docs/tools/debugging#next-steps)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Tutorials
Inspector
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Tutorials
# Inspector
In-depth guide to using the MCP Inspector for testing and debugging Model Context Protocol servers
The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](https://modelcontextprotocol.io/docs/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector’s features and capabilities.
## 
[​](https://modelcontextprotocol.io/docs/tools/inspector#getting-started)
Getting started
### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#installation-and-basic-usage)
Installation and basic usage
The Inspector runs directly through `npx` without requiring installation:
Copy
```
npx @modelcontextprotocol/inspector <command>

```

Copy
```
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>

```

#### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#inspecting-servers-from-npm-or-pypi)
Inspecting servers from NPM or PyPi
A common way to start server packages from [NPM](https://npmjs.com) or [PyPi](https://pypi.com).
  * NPM package
  * PyPi package


Copy
```
npx -y @modelcontextprotocol/inspector npx <package-name> <args>
# For example
npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb

```

#### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#inspecting-locally-developed-servers)
Inspecting locally developed servers
To inspect servers locally developed or downloaded as a repository, the most common way is:
  * TypeScript
  * Python


Copy
```
npx @modelcontextprotocol/inspector node path/to/server/index.js args...

```

Please carefully read any attached README for the most accurate instructions.
## 
[​](https://modelcontextprotocol.io/docs/tools/inspector#feature-overview)
Feature overview
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/mcp-inspector.png)
The MCP Inspector interface
The Inspector provides several features for interacting with your MCP server:
### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#server-connection-pane)
Server connection pane
  * Allows selecting the [transport](https://modelcontextprotocol.io/docs/concepts/transports) for connecting to the server
  * For local servers, supports customizing the command-line arguments and environment


### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#resources-tab)
Resources tab
  * Lists all available resources
  * Shows resource metadata (MIME types, descriptions)
  * Allows resource content inspection
  * Supports subscription testing


### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#prompts-tab)
Prompts tab
  * Displays available prompt templates
  * Shows prompt arguments and descriptions
  * Enables prompt testing with custom arguments
  * Previews generated messages


### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#tools-tab)
Tools tab
  * Lists available tools
  * Shows tool schemas and descriptions
  * Enables tool testing with custom inputs
  * Displays tool execution results


### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#notifications-pane)
Notifications pane
  * Presents all logs recorded from the server
  * Shows notifications received from the server


## 
[​](https://modelcontextprotocol.io/docs/tools/inspector#best-practices)
Best practices
### 
[​](https://modelcontextprotocol.io/docs/tools/inspector#development-workflow)
Development workflow
  1. Start Development
     * Launch Inspector with your server
     * Verify basic connectivity
     * Check capability negotiation
  2. Iterative testing
     * Make server changes
     * Rebuild the server
     * Reconnect the Inspector
     * Test affected features
     * Monitor messages
  3. Test edge cases
     * Invalid inputs
     * Missing prompt arguments
     * Concurrent operations
     * Verify error handling and error responses


## 
[​](https://modelcontextprotocol.io/docs/tools/inspector#next-steps)
Next steps
## [Inspector RepositoryCheck out the MCP Inspector source code](https://github.com/modelcontextprotocol/inspector)## [Debugging GuideLearn about broader debugging strategies](https://modelcontextprotocol.io/docs/tools/debugging)
Was this page helpful?
YesNo
[Debugging](https://modelcontextprotocol.io/docs/tools/debugging)[Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Getting started](https://modelcontextprotocol.io/docs/tools/inspector#getting-started)
  * [Installation and basic usage](https://modelcontextprotocol.io/docs/tools/inspector#installation-and-basic-usage)
  * [Inspecting servers from NPM or PyPi](https://modelcontextprotocol.io/docs/tools/inspector#inspecting-servers-from-npm-or-pypi)
  * [Inspecting locally developed servers](https://modelcontextprotocol.io/docs/tools/inspector#inspecting-locally-developed-servers)
  * [Feature overview](https://modelcontextprotocol.io/docs/tools/inspector#feature-overview)
  * [Server connection pane](https://modelcontextprotocol.io/docs/tools/inspector#server-connection-pane)
  * [Resources tab](https://modelcontextprotocol.io/docs/tools/inspector#resources-tab)
  * [Prompts tab](https://modelcontextprotocol.io/docs/tools/inspector#prompts-tab)
  * [Tools tab](https://modelcontextprotocol.io/docs/tools/inspector#tools-tab)
  * [Notifications pane](https://modelcontextprotocol.io/docs/tools/inspector#notifications-pane)
  * [Best practices](https://modelcontextprotocol.io/docs/tools/inspector#best-practices)
  * [Development workflow](https://modelcontextprotocol.io/docs/tools/inspector#development-workflow)
  * [Next steps](https://modelcontextprotocol.io/docs/tools/inspector#next-steps)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Get Started
Example Servers
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Get Started
# Example Servers
A list of example servers and implementations
This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol’s capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.
## 
[​](https://modelcontextprotocol.io/examples#reference-implementations)
Reference implementations
These official reference servers demonstrate core MCP features and SDK usage:
### 
[​](https://modelcontextprotocol.io/examples#data-and-file-systems)
Data and file systems
  * **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - Secure file operations with configurable access controls
  * **[PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** - Read-only database access with schema inspection capabilities
  * **[SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)** - Database interaction and business intelligence features
  * **[Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive)** - File access and search capabilities for Google Drive


### 
[​](https://modelcontextprotocol.io/examples#development-tools)
Development tools
  * **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - Tools to read, search, and manipulate Git repositories
  * **[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github)** - Repository management, file operations, and GitHub API integration
  * **[GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)** - GitLab API integration enabling project management
  * **[Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry)** - Retrieving and analyzing issues from Sentry.io


### 
[​](https://modelcontextprotocol.io/examples#web-and-browser-automation)
Web and browser automation
  * **[Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** - Web and local search using Brave’s Search API
  * **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - Web content fetching and conversion optimized for LLM usage
  * **[Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** - Browser automation and web scraping capabilities


### 
[​](https://modelcontextprotocol.io/examples#productivity-and-communication)
Productivity and communication
  * **[Slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)** - Channel management and messaging capabilities
  * **[Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps)** - Location services, directions, and place details
  * **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - Knowledge graph-based persistent memory system


### 
[​](https://modelcontextprotocol.io/examples#ai-and-specialized-tools)
AI and specialized tools
  * **[EverArt](https://github.com/modelcontextprotocol/servers/tree/main/src/everart)** - AI image generation using various models
  * **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - Dynamic problem-solving through thought sequences
  * **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers/tree/main/src/aws-kb-retrieval-server)** - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime


## 
[​](https://modelcontextprotocol.io/examples#official-integrations)
Official integrations
These MCP servers are maintained by companies for their platforms:
  * **[Axiom](https://github.com/axiomhq/mcp-server-axiom)** - Query and analyze logs, traces, and event data using natural language
  * **[Browserbase](https://github.com/browserbase/mcp-server-browserbase)** - Automate browser interactions in the cloud
  * **[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** - Deploy and manage resources on the Cloudflare developer platform
  * **[E2B](https://github.com/e2b-dev/mcp-server)** - Execute code in secure cloud sandboxes
  * **[Neon](https://github.com/neondatabase/mcp-server-neon)** - Interact with the Neon serverless Postgres platform
  * **[Obsidian Markdown Notes](https://github.com/calclavia/mcp-obsidian)** - Read and search through Markdown notes in Obsidian vaults
  * **[Qdrant](https://github.com/qdrant/mcp-server-qdrant/)** - Implement semantic memory using the Qdrant vector search engine
  * **[Raygun](https://github.com/MindscapeHQ/mcp-server-raygun)** - Access crash reporting and monitoring data
  * **[Search1API](https://github.com/fatwang2/search1api-mcp)** - Unified API for search, crawling, and sitemaps
  * **[Stripe](https://github.com/stripe/agent-toolkit)** - Interact with the Stripe API
  * **[Tinybird](https://github.com/tinybirdco/mcp-tinybird)** - Interface with the Tinybird serverless ClickHouse platform
  * **[Weaviate](https://github.com/weaviate/mcp-server-weaviate)** - Enable Agentic RAG through your Weaviate collection(s)


## 
[​](https://modelcontextprotocol.io/examples#community-highlights)
Community highlights
A growing ecosystem of community-developed servers extends MCP’s capabilities:
  * **[Docker](https://github.com/ckreiling/mcp-server-docker)** - Manage containers, images, volumes, and networks
  * **[Kubernetes](https://github.com/Flux159/mcp-server-kubernetes)** - Manage pods, deployments, and services
  * **[Linear](https://github.com/jerhadf/linear-mcp-server)** - Project management and issue tracking
  * **[Snowflake](https://github.com/datawiz168/mcp-snowflake-service)** - Interact with Snowflake databases
  * **[Spotify](https://github.com/varunneal/spotify-mcp)** - Control Spotify playback and manage playlists
  * **[Todoist](https://github.com/abhiz123/todoist-mcp-server)** - Task management integration


> **Note:** Community servers are untested and should be used at your own risk. They are not affiliated with or endorsed by Anthropic.
For a complete list of community servers, visit the [MCP Servers Repository](https://github.com/modelcontextprotocol/servers).
## 
[​](https://modelcontextprotocol.io/examples#getting-started)
Getting started
### 
[​](https://modelcontextprotocol.io/examples#using-reference-servers)
Using reference servers
TypeScript-based servers can be used directly with `npx`:
Copy
```
npx -y @modelcontextprotocol/server-memory

```

Python-based servers can be used with `uvx` (recommended) or `pip`:
Copy
```
# Using uvx
uvx mcp-server-git
# Using pip
pip install mcp-server-git
python -m mcp_server_git

```

### 
[​](https://modelcontextprotocol.io/examples#configuring-with-claude)
Configuring with Claude
To use an MCP server with Claude, add it to your configuration:
Copy
```
{
 "mcpServers": {
  "memory": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-memory"]
  },
  "filesystem": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
  },
  "github": {
   "command": "npx",
   "args": ["-y", "@modelcontextprotocol/server-github"],
   "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
   }
  }
 }
}

```

## 
[​](https://modelcontextprotocol.io/examples#additional-resources)
Additional resources
  * [MCP Servers Repository](https://github.com/modelcontextprotocol/servers) - Complete collection of reference implementations and community servers
  * [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) - Curated list of MCP servers
  * [MCP CLI](https://github.com/wong2/mcp-cli) - Command-line inspector for testing MCP servers
  * [MCP Get](https://mcp-get.com) - Tool for installing and managing MCP servers
  * [Supergateway](https://github.com/supercorp-ai/supergateway) - Run MCP stdio servers over SSE


Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to engage with the MCP community.
Was this page helpful?
YesNo
[For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)[Example Clients](https://modelcontextprotocol.io/clients)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Reference implementations](https://modelcontextprotocol.io/examples#reference-implementations)
  * [Data and file systems](https://modelcontextprotocol.io/examples#data-and-file-systems)
  * [Development tools](https://modelcontextprotocol.io/examples#development-tools)
  * [Web and browser automation](https://modelcontextprotocol.io/examples#web-and-browser-automation)
  * [Productivity and communication](https://modelcontextprotocol.io/examples#productivity-and-communication)
  * [AI and specialized tools](https://modelcontextprotocol.io/examples#ai-and-specialized-tools)
  * [Official integrations](https://modelcontextprotocol.io/examples#official-integrations)
  * [Community highlights](https://modelcontextprotocol.io/examples#community-highlights)
  * [Getting started](https://modelcontextprotocol.io/examples#getting-started)
  * [Using reference servers](https://modelcontextprotocol.io/examples#using-reference-servers)
  * [Configuring with Claude](https://modelcontextprotocol.io/examples#configuring-with-claude)
  * [Additional resources](https://modelcontextprotocol.io/examples#additional-resources)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Get Started
Introduction
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Get Started
# Introduction
Get started with the Model Context Protocol (MCP)
C# SDK released! Check out [what else is new.](https://modelcontextprotocol.io/development/updates)
MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
## 
[​](https://modelcontextprotocol.io/introduction#why-mcp%3F)
Why MCP?
MCP helps you build agents and complex workflows on top of LLMs. LLMs frequently need to integrate with data and tools, and MCP provides:
  * A growing list of pre-built integrations that your LLM can directly plug into
  * The flexibility to switch between LLM providers and vendors
  * Best practices for securing your data within your infrastructure


### 
[​](https://modelcontextprotocol.io/introduction#general-architecture)
General architecture
At its core, MCP follows a client-server architecture where a host application can connect to multiple servers:
Internet
Your Computer
MCP Protocol
MCP Protocol
MCP Protocol
Web APIs
Host with MCP Client(Claude, IDEs, Tools)
MCP Server A
MCP Server B
MCP Server C
LocalData Source A
LocalData Source B
RemoteService C
  * **MCP Hosts** : Programs like Claude Desktop, IDEs, or AI tools that want to access data through MCP
  * **MCP Clients** : Protocol clients that maintain 1:1 connections with servers
  * **MCP Servers** : Lightweight programs that each expose specific capabilities through the standardized Model Context Protocol
  * **Local Data Sources** : Your computer’s files, databases, and services that MCP servers can securely access
  * **Remote Services** : External systems available over the internet (e.g., through APIs) that MCP servers can connect to


## 
[​](https://modelcontextprotocol.io/introduction#get-started)
Get started
Choose the path that best fits your needs:
#### 
[​](https://modelcontextprotocol.io/introduction#quick-starts)
Quick Starts
## [For Server DevelopersGet started building your own server to use in Claude for Desktop and other clients](https://modelcontextprotocol.io/quickstart/server)## [For Client DevelopersGet started building your own client that can integrate with all MCP servers](https://modelcontextprotocol.io/quickstart/client)## [For Claude Desktop UsersGet started using pre-built servers in Claude for Desktop](https://modelcontextprotocol.io/quickstart/user)
#### 
[​](https://modelcontextprotocol.io/introduction#examples)
Examples
## [Example ServersCheck out our gallery of official MCP servers and implementations](https://modelcontextprotocol.io/examples)## [Example ClientsView the list of clients that support MCP integrations](https://modelcontextprotocol.io/clients)
## 
[​](https://modelcontextprotocol.io/introduction#tutorials)
Tutorials
## [Building MCP with LLMsLearn how to use LLMs like Claude to speed up your MCP development](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)## [Debugging GuideLearn how to effectively debug MCP servers and integrations](https://modelcontextprotocol.io/docs/tools/debugging)## [MCP InspectorTest and inspect your MCP servers with our interactive debugging tool](https://modelcontextprotocol.io/docs/tools/inspector)## [MCP Workshop (Video, 2hr)](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)
## 
[​](https://modelcontextprotocol.io/introduction#explore-mcp)
Explore MCP
Dive deeper into MCP’s core concepts and capabilities:
## [Core architectureUnderstand how MCP connects clients, servers, and LLMs](https://modelcontextprotocol.io/docs/concepts/architecture)## [ResourcesExpose data and content from your servers to LLMs](https://modelcontextprotocol.io/docs/concepts/resources)## [PromptsCreate reusable prompt templates and workflows](https://modelcontextprotocol.io/docs/concepts/prompts)## [ToolsEnable LLMs to perform actions through your server](https://modelcontextprotocol.io/docs/concepts/tools)## [SamplingLet your servers request completions from LLMs](https://modelcontextprotocol.io/docs/concepts/sampling)## [TransportsLearn about MCP’s communication mechanism](https://modelcontextprotocol.io/docs/concepts/transports)
## 
[​](https://modelcontextprotocol.io/introduction#contributing)
Contributing
Want to contribute? Check out our [Contributing Guide](https://modelcontextprotocol.io/development/contributing) to learn how you can help improve MCP.
## 
[​](https://modelcontextprotocol.io/introduction#support-and-feedback)
Support and Feedback
Here’s how to get help or provide feedback:
  * For bug reports and feature requests related to the MCP specification, SDKs, or documentation (open source), please [create a GitHub issue](https://github.com/modelcontextprotocol)
  * For discussions or Q&A about the MCP specification, use the [specification discussions](https://github.com/modelcontextprotocol/specification/discussions)
  * For discussions or Q&A about other MCP open source components, use the [organization discussions](https://github.com/orgs/modelcontextprotocol/discussions)
  * For bug reports, feature requests, and questions related to Claude.app and claude.ai’s MCP integration, please email mcp-support@anthropic.com


Was this page helpful?
YesNo
[For Server Developers](https://modelcontextprotocol.io/quickstart/server)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Why MCP?](https://modelcontextprotocol.io/introduction#why-mcp%3F)
  * [General architecture](https://modelcontextprotocol.io/introduction#general-architecture)
  * [Get started](https://modelcontextprotocol.io/introduction#get-started)
  * [Quick Starts](https://modelcontextprotocol.io/introduction#quick-starts)
  * [Examples](https://modelcontextprotocol.io/introduction#examples)
  * [Tutorials](https://modelcontextprotocol.io/introduction#tutorials)
  * [Explore MCP](https://modelcontextprotocol.io/introduction#explore-mcp)
  * [Contributing](https://modelcontextprotocol.io/introduction#contributing)
  * [Support and Feedback](https://modelcontextprotocol.io/introduction#support-and-feedback)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
    * [For Server Developers](https://modelcontextprotocol.io/quickstart/server)
    * [For Client Developers](https://modelcontextprotocol.io/quickstart/client)
    * [For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Quickstart
For Client Developers
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Quickstart
# For Client Developers
Get started building your own client that can integrate with all MCP servers.
In this tutorial, you’ll learn how to build a LLM-powered chatbot client that connects to MCP servers. It helps to have gone through the [Server quickstart](https://modelcontextprotocol.io/quickstart/server) that guides you through the basic of building your first server.
  * Python
  * Node
  * Java
  * Kotlin
  * C#


[You can find the complete code for this tutorial here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/mcp-client-python)
## System Requirements
Before starting, ensure your system meets these requirements:
  * Mac or Windows computer
  * Latest Python version installed
  * Latest version of `uv` installed


## Setting Up Your Environment
First, create a new Python project with `uv`:
Copy
```
# Create project directory
uv init mcp-client
cd mcp-client
# Create virtual environment
uv venv
# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
# Install required packages
uv add mcp anthropic python-dotenv
# Remove boilerplate files
rm main.py
# Create our main file
touch client.py

```

## Setting Up Your API Key
You’ll need an Anthropic API key from the [Anthropic Console](https://console.anthropic.com/settings/keys).
Create a `.env` file to store it:
Copy
```
# Create .env file
touch .env

```

Add your key to the `.env` file:
Copy
```
ANTHROPIC_API_KEY=<your key here>

```

Add `.env` to your `.gitignore`:
Copy
```
echo ".env" >> .gitignore

```

Make sure you keep your `ANTHROPIC_API_KEY` secure!
## Creating the Client
### Basic Client Structure
First, let’s set up our imports and create the basic client class:
Copy
```
import asyncio
from typing import Optional
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv() # load environment variables from .env
class MCPClient:
  def __init__(self):
    # Initialize session and client objects
    self.session: Optional[ClientSession] = None
    self.exit_stack = AsyncExitStack()
    self.anthropic = Anthropic()
  # methods will go here

```

### Server Connection Management
Next, we’ll implement the method to connect to an MCP server:
Copy
```
async def connect_to_server(self, server_script_path: str):
  """Connect to an MCP server
  Args:
    server_script_path: Path to the server script (.py or .js)
  """
  is_python = server_script_path.endswith('.py')
  is_js = server_script_path.endswith('.js')
  if not (is_python or is_js):
    raise ValueError("Server script must be a .py or .js file")
  command = "python" if is_python else "node"
  server_params = StdioServerParameters(
    command=command,
    args=[server_script_path],
    env=None
  )
  stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
  self.stdio, self.write = stdio_transport
  self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))
  await self.session.initialize()
  # List available tools
  response = await self.session.list_tools()
  tools = response.tools
  print("\nConnected to server with tools:", [tool.name for tool in tools])

```

### Query Processing Logic
Now let’s add the core functionality for processing queries and handling tool calls:
Copy
```
async def process_query(self, query: str) -> str:
  """Process a query using Claude and available tools"""
  messages = [
    {
      "role": "user",
      "content": query
    }
  ]
  response = await self.session.list_tools()
  available_tools = [{
    "name": tool.name,
    "description": tool.description,
    "input_schema": tool.inputSchema
  } for tool in response.tools]
  # Initial Claude API call
  response = self.anthropic.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    messages=messages,
    tools=available_tools
  )
  # Process response and handle tool calls
  final_text = []
  assistant_message_content = []
  for content in response.content:
    if content.type == 'text':
      final_text.append(content.text)
      assistant_message_content.append(content)
    elif content.type == 'tool_use':
      tool_name = content.name
      tool_args = content.input
      # Execute tool call
      result = await self.session.call_tool(tool_name, tool_args)
      final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")
      assistant_message_content.append(content)
      messages.append({
        "role": "assistant",
        "content": assistant_message_content
      })
      messages.append({
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": content.id,
            "content": result.content
          }
        ]
      })
      # Get next response from Claude
      response = self.anthropic.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        messages=messages,
        tools=available_tools
      )
      final_text.append(response.content[0].text)
  return "\n".join(final_text)

```

### Interactive Chat Interface
Now we’ll add the chat loop and cleanup functionality:
Copy
```
async def chat_loop(self):
  """Run an interactive chat loop"""
  print("\nMCP Client Started!")
  print("Type your queries or 'quit' to exit.")
  while True:
    try:
      query = input("\nQuery: ").strip()
      if query.lower() == 'quit':
        break
      response = await self.process_query(query)
      print("\n" + response)
    except Exception as e:
      print(f"\nError: {str(e)}")
async def cleanup(self):
  """Clean up resources"""
  await self.exit_stack.aclose()

```

### Main Entry Point
Finally, we’ll add the main execution logic:
Copy
```
async def main():
  if len(sys.argv) < 2:
    print("Usage: python client.py <path_to_server_script>")
    sys.exit(1)
  client = MCPClient()
  try:
    await client.connect_to_server(sys.argv[1])
    await client.chat_loop()
  finally:
    await client.cleanup()
if __name__ == "__main__":
  import sys
  asyncio.run(main())

```

You can find the complete `client.py` file [here.](https://gist.github.com/zckly/f3f28ea731e096e53b39b47bf0a2d4b1)
## Key Components Explained
### 1. Client Initialization
  * The `MCPClient` class initializes with session management and API clients
  * Uses `AsyncExitStack` for proper resource management
  * Configures the Anthropic client for Claude interactions


### 2. Server Connection
  * Supports both Python and Node.js servers
  * Validates server script type
  * Sets up proper communication channels
  * Initializes the session and lists available tools


### 3. Query Processing
  * Maintains conversation context
  * Handles Claude’s responses and tool calls
  * Manages the message flow between Claude and tools
  * Combines results into a coherent response


### 4. Interactive Interface
  * Provides a simple command-line interface
  * Handles user input and displays responses
  * Includes basic error handling
  * Allows graceful exit


### 5. Resource Management
  * Proper cleanup of resources
  * Error handling for connection issues
  * Graceful shutdown procedures


## Common Customization Points
  1. **Tool Handling**
     * Modify `process_query()` to handle specific tool types
     * Add custom error handling for tool calls
     * Implement tool-specific response formatting
  2. **Response Processing**
     * Customize how tool results are formatted
     * Add response filtering or transformation
     * Implement custom logging
  3. **User Interface**
     * Add a GUI or web interface
     * Implement rich console output
     * Add command history or auto-completion


## Running the Client
To run your client with any MCP server:
Copy
```
uv run client.py path/to/server.py # python server
uv run client.py path/to/build/index.js # node server

```

If you’re continuing the weather tutorial from the server quickstart, your command might look something like this: `python client.py .../quickstart-resources/weather-server-python/weather.py`
The client will:
  1. Connect to the specified server
  2. List available tools
  3. Start an interactive chat session where you can: 
     * Enter queries
     * See tool executions
     * Get responses from Claude


Here’s an example of what it should look like if connected to the weather server from the server quickstart:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/client-claude-cli-python.png)
## How It Works
When you submit a query:
  1. The client gets the list of available tools from the server
  2. Your query is sent to Claude along with tool descriptions
  3. Claude decides which tools (if any) to use
  4. The client executes any requested tool calls through the server
  5. Results are sent back to Claude
  6. Claude provides a natural language response
  7. The response is displayed to you


## Best practices
  1. **Error Handling**
     * Always wrap tool calls in try-catch blocks
     * Provide meaningful error messages
     * Gracefully handle connection issues
  2. **Resource Management**
     * Use `AsyncExitStack` for proper cleanup
     * Close connections when done
     * Handle server disconnections
  3. **Security**
     * Store API keys securely in `.env`
     * Validate server responses
     * Be cautious with tool permissions


## Troubleshooting
### Server Path Issues
  * Double-check the path to your server script is correct
  * Use the absolute path if the relative path isn’t working
  * For Windows users, make sure to use forward slashes (/) or escaped backslashes (\\) in the path
  * Verify the server file has the correct extension (.py for Python or .js for Node.js)


Example of correct path usage:
Copy
```
# Relative path
uv run client.py ./server/weather.py
# Absolute path
uv run client.py /Users/username/projects/mcp-server/weather.py
# Windows path (either format works)
uv run client.py C:/projects/mcp-server/weather.py
uv run client.py C:\\projects\\mcp-server\\weather.py

```

### Response Timing
  * The first response might take up to 30 seconds to return
  * This is normal and happens while: 
    * The server initializes
    * Claude processes the query
    * Tools are being executed
  * Subsequent responses are typically faster
  * Don’t interrupt the process during this initial waiting period


### Common Error Messages
If you see:
  * `FileNotFoundError`: Check your server path
  * `Connection refused`: Ensure the server is running and the path is correct
  * `Tool execution failed`: Verify the tool’s required environment variables are set
  * `Timeout error`: Consider increasing the timeout in your client configuration


## 
[​](https://modelcontextprotocol.io/quickstart/client#next-steps)
Next steps
## [Example serversCheck out our gallery of official MCP servers and implementations](https://modelcontextprotocol.io/examples)## [ClientsView the list of clients that support MCP integrations](https://modelcontextprotocol.io/clients)## [Building MCP with LLMsLearn how to use LLMs like Claude to speed up your MCP development](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)## [Core architectureUnderstand how MCP connects clients, servers, and LLMs](https://modelcontextprotocol.io/docs/concepts/architecture)
Was this page helpful?
YesNo
[For Server Developers](https://modelcontextprotocol.io/quickstart/server)[For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Next steps](https://modelcontextprotocol.io/quickstart/client#next-steps)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
    * [For Server Developers](https://modelcontextprotocol.io/quickstart/server)
    * [For Client Developers](https://modelcontextprotocol.io/quickstart/client)
    * [For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Quickstart
For Server Developers
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Quickstart
# For Server Developers
Get started building your own server to use in Claude for Desktop and other clients.
In this tutorial, we’ll build a simple MCP weather server and connect it to a host, Claude for Desktop. We’ll start with a basic setup, and then progress to more complex use cases.
### 
[​](https://modelcontextprotocol.io/quickstart/server#what-we%E2%80%99ll-be-building)
What we’ll be building
Many LLMs do not currently have the ability to fetch the forecast and severe weather alerts. Let’s use MCP to solve that!
We’ll build a server that exposes two tools: `get-alerts` and `get-forecast`. Then we’ll connect the server to an MCP host (in this case, Claude for Desktop):
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/weather-alerts.png)
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/current-weather.png)
Servers can connect to any client. We’ve chosen Claude for Desktop here for simplicity, but we also have guides on [building your own client](https://modelcontextprotocol.io/quickstart/client) as well as a [list of other clients here](https://modelcontextprotocol.io/clients).
Why Claude for Desktop and not Claude.ai?
Because servers are locally run, MCP currently only supports desktop hosts. Remote hosts are in active development.
### 
[​](https://modelcontextprotocol.io/quickstart/server#core-mcp-concepts)
Core MCP Concepts
MCP servers can provide three main types of capabilities:
  1. **Resources** : File-like data that can be read by clients (like API responses or file contents)
  2. **Tools** : Functions that can be called by the LLM (with user approval)
  3. **Prompts** : Pre-written templates that help users accomplish specific tasks


This tutorial will primarily focus on tools.
  * Python
  * Node
  * Java
  * Kotlin
  * C#


Let’s get started with building our weather server! [You can find the complete code for what we’ll be building here.](https://github.com/modelcontextprotocol/quickstart-resources/tree/main/weather-server-python)
### Prerequisite knowledge
This quickstart assumes you have familiarity with:
  * Python
  * LLMs like Claude


### System requirements
  * Python 3.10 or higher installed.
  * You must use the Python MCP SDK 1.2.0 or higher.


### Set up your environment
First, let’s install `uv` and set up our Python project and environment:
MacOS/Linux
Windows
Copy
```
curl -LsSf https://astral.sh/uv/install.sh | sh

```

Make sure to restart your terminal afterwards to ensure that the `uv` command gets picked up.
Now, let’s create and set up our project:
MacOS/Linux
Windows
Copy
```
# Create a new directory for our project
uv init weather
cd weather
# Create virtual environment and activate it
uv venv
source .venv/bin/activate
# Install dependencies
uv add "mcp[cli]" httpx
# Create our server file
touch weather.py

```

Now let’s dive into building your server.
## Building your server
### Importing packages and setting up the instance
Add these to the top of your `weather.py`:
Copy
```
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
# Initialize FastMCP server
mcp = FastMCP("weather")
# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

```

The FastMCP class uses Python type hints and docstrings to automatically generate tool definitions, making it easy to create and maintain MCP tools.
### Helper functions
Next, let’s add our helper functions for querying and formatting the data from the National Weather Service API:
Copy
```
async def make_nws_request(url: str) -> dict[str, Any] | None:
  """Make a request to the NWS API with proper error handling."""
  headers = {
    "User-Agent": USER_AGENT,
    "Accept": "application/geo+json"
  }
  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(url, headers=headers, timeout=30.0)
      response.raise_for_status()
      return response.json()
    except Exception:
      return None
def format_alert(feature: dict) -> str:
  """Format an alert feature into a readable string."""
  props = feature["properties"]
  return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

```

### Implementing tool execution
The tool execution handler is responsible for actually executing the logic of each tool. Let’s add it:
Copy
```
@mcp.tool()
async def get_alerts(state: str) -> str:
  """Get weather alerts for a US state.
  Args:
    state: Two-letter US state code (e.g. CA, NY)
  """
  url = f"{NWS_API_BASE}/alerts/active/area/{state}"
  data = await make_nws_request(url)
  if not data or "features" not in data:
    return "Unable to fetch alerts or no alerts found."
  if not data["features"]:
    return "No active alerts for this state."
  alerts = [format_alert(feature) for feature in data["features"]]
  return "\n---\n".join(alerts)
@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
  """Get weather forecast for a location.
  Args:
    latitude: Latitude of the location
    longitude: Longitude of the location
  """
  # First get the forecast grid endpoint
  points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
  points_data = await make_nws_request(points_url)
  if not points_data:
    return "Unable to fetch forecast data for this location."
  # Get the forecast URL from the points response
  forecast_url = points_data["properties"]["forecast"]
  forecast_data = await make_nws_request(forecast_url)
  if not forecast_data:
    return "Unable to fetch detailed forecast."
  # Format the periods into a readable forecast
  periods = forecast_data["properties"]["periods"]
  forecasts = []
  for period in periods[:5]: # Only show next 5 periods
    forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
    forecasts.append(forecast)
  return "\n---\n".join(forecasts)

```

### Running the server
Finally, let’s initialize and run the server:
Copy
```
if __name__ == "__main__":
  # Initialize and run the server
  mcp.run(transport='stdio')

```

Your server is complete! Run `uv run weather.py` to confirm that everything’s working.
Let’s now test your server from an existing MCP host, Claude for Desktop.
## Testing your server with Claude for Desktop
Claude for Desktop is not yet available on Linux. Linux users can proceed to the [Building a client](https://modelcontextprotocol.io/quickstart/client) tutorial to build an MCP client that connects to the server we just built.
First, make sure you have Claude for Desktop installed. [You can install the latest version here.](https://claude.ai/download) If you already have Claude for Desktop, **make sure it’s updated to the latest version.**
We’ll need to configure Claude for Desktop for whichever MCP servers you want to use. To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor. Make sure to create the file if it doesn’t exist.
For example, if you have [VS Code](https://code.visualstudio.com/) installed:
  * MacOS/Linux
  * Windows


Copy
```
code ~/Library/Application\ Support/Claude/claude_desktop_config.json

```

You’ll then add your servers in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.
In this case, we’ll add our single weather server like so:
  * MacOS/Linux
  * Windows


Python
Copy
```
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
        "run",
        "weather.py"
      ]
    }
  }
}

```

You may need to put the full path to the `uv` executable in the `command` field. You can get this by running `which uv` on MacOS/Linux or `where uv` on Windows.
Make sure you pass in the absolute path to your server.
This tells Claude for Desktop:
  1. There’s an MCP server named “weather”
  2. To launch it by running `uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/weather run weather.py`


Save the file, and restart **Claude for Desktop**.
### 
[​](https://modelcontextprotocol.io/quickstart/server#test-with-commands)
Test with commands
Let’s make sure Claude for Desktop is picking up the two tools we’ve exposed in our `weather` server. You can do this by looking for the hammer ![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg) icon:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/visual-indicator-mcp-tools.png)
After clicking on the hammer icon, you should see two tools listed:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/available-mcp-tools.png)
If your server isn’t being picked up by Claude for Desktop, proceed to the [Troubleshooting](https://modelcontextprotocol.io/quickstart/server#troubleshooting) section for debugging tips.
If the hammer icon has shown up, you can now test your server by running the following commands in Claude for Desktop:
  * What’s the weather in Sacramento?
  * What are the active weather alerts in Texas?


![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/current-weather.png)
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/weather-alerts.png)
Since this is the US National Weather service, the queries will only work for US locations.
## 
[​](https://modelcontextprotocol.io/quickstart/server#what%E2%80%99s-happening-under-the-hood)
What’s happening under the hood
When you ask a question:
  1. The client sends your question to Claude
  2. Claude analyzes the available tools and decides which one(s) to use
  3. The client executes the chosen tool(s) through the MCP server
  4. The results are sent back to Claude
  5. Claude formulates a natural language response
  6. The response is displayed to you!


## 
[​](https://modelcontextprotocol.io/quickstart/server#troubleshooting)
Troubleshooting
Claude for Desktop Integration Issues
**Getting logs from Claude for Desktop**
Claude.app logging related to MCP is written to log files in `~/Library/Logs/Claude`:
  * `mcp.log` will contain general logging about MCP connections and connection failures.
  * Files named `mcp-server-SERVERNAME.log` will contain error (stderr) logging from the named server.


You can run the following command to list recent logs and follow along with any new ones:
Copy
```
# Check Claude's logs for errors
tail -n 20 -f ~/Library/Logs/Claude/mcp*.log

```

**Server not showing up in Claude**
  1. Check your `claude_desktop_config.json` file syntax
  2. Make sure the path to your project is absolute and not relative
  3. Restart Claude for Desktop completely


**Tool calls failing silently**
If Claude attempts to use the tools but they fail:
  1. Check Claude’s logs for errors
  2. Verify your server builds and runs without errors
  3. Try restarting Claude for Desktop


**None of this is working. What do I do?**
Please refer to our [debugging guide](https://modelcontextprotocol.io/docs/tools/debugging) for better debugging tools and more detailed guidance.
Weather API Issues
**Error: Failed to retrieve grid point data**
This usually means either:
  1. The coordinates are outside the US
  2. The NWS API is having issues
  3. You’re being rate limited


Fix:
  * Verify you’re using US coordinates
  * Add a small delay between requests
  * Check the NWS API status page


**Error: No active alerts for [STATE]**
This isn’t an error - it just means there are no current weather alerts for that state. Try a different state or check during severe weather.
For more advanced troubleshooting, check out our guide on [Debugging MCP](https://modelcontextprotocol.io/docs/tools/debugging)
## 
[​](https://modelcontextprotocol.io/quickstart/server#next-steps)
Next steps
## [Building a clientLearn how to build your own MCP client that can connect to your server](https://modelcontextprotocol.io/quickstart/client)## [Example serversCheck out our gallery of official MCP servers and implementations](https://modelcontextprotocol.io/examples)## [Debugging GuideLearn how to effectively debug MCP servers and integrations](https://modelcontextprotocol.io/docs/tools/debugging)## [Building MCP with LLMsLearn how to use LLMs like Claude to speed up your MCP development](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
Was this page helpful?
YesNo
[Introduction](https://modelcontextprotocol.io/introduction)[For Client Developers](https://modelcontextprotocol.io/quickstart/client)
[github](https://github.com/modelcontextprotocol)
On this page
  * [What we’ll be building](https://modelcontextprotocol.io/quickstart/server#what-we%E2%80%99ll-be-building)
  * [Core MCP Concepts](https://modelcontextprotocol.io/quickstart/server#core-mcp-concepts)
  * [Test with commands](https://modelcontextprotocol.io/quickstart/server#test-with-commands)
  * [What’s happening under the hood](https://modelcontextprotocol.io/quickstart/server#what%E2%80%99s-happening-under-the-hood)
  * [Troubleshooting](https://modelcontextprotocol.io/quickstart/server#troubleshooting)
  * [Next steps](https://modelcontextprotocol.io/quickstart/server#next-steps)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
    * [For Server Developers](https://modelcontextprotocol.io/quickstart/server)
    * [For Client Developers](https://modelcontextprotocol.io/quickstart/client)
    * [For Claude Desktop Users](https://modelcontextprotocol.io/quickstart/user)
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Quickstart
For Claude Desktop Users
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Quickstart
# For Claude Desktop Users
Get started using pre-built servers in Claude for Desktop.
In this tutorial, you will extend [Claude for Desktop](https://claude.ai/download) so that it can read from your computer’s file system, write new files, move files, and even search files.
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-filesystem.png)
Don’t worry — it will ask you for your permission before executing these actions!
## 
[​](https://modelcontextprotocol.io/quickstart/user#1-download-claude-for-desktop)
1. Download Claude for Desktop
Start by downloading [Claude for Desktop](https://claude.ai/download), choosing either macOS or Windows. (Linux is not yet supported for Claude for Desktop.)
Follow the installation instructions.
If you already have Claude for Desktop, make sure it’s on the latest version by clicking on the Claude menu on your computer and selecting “Check for Updates…”
Why Claude for Desktop and not Claude.ai?
Because servers are locally run, MCP currently only supports desktop hosts. Remote hosts are in active development.
## 
[​](https://modelcontextprotocol.io/quickstart/user#2-add-the-filesystem-mcp-server)
2. Add the Filesystem MCP Server
To add this filesystem functionality, we will be installing a pre-built [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) to Claude for Desktop. This is one of dozens of [servers](https://github.com/modelcontextprotocol/servers/tree/main) created by Anthropic and the community.
Get started by opening up the Claude menu on your computer and select “Settings…” Please note that these are not the Claude Account Settings found in the app window itself.
This is what it should look like on a Mac:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-menu.png)
Click on “Developer” in the left-hand bar of the Settings pane, and then click on “Edit Config”:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-developer.png)
This will create a configuration file at:
  * macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  * Windows: `%APPDATA%\Claude\claude_desktop_config.json`


if you don’t already have one, and will display the file in your file system.
Open up the configuration file in any text editor. Replace the file contents with this:
  * MacOS/Linux
  * Windows


Copy
```
{
 "mcpServers": {
  "filesystem": {
   "command": "npx",
   "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/username/Desktop",
    "/Users/username/Downloads"
   ]
  }
 }
}

```

Make sure to replace `username` with your computer’s username. The paths should point to valid directories that you want Claude to be able to access and modify. It’s set up to work for Desktop and Downloads, but you can add more paths as well.
You will also need [Node.js](https://nodejs.org) on your computer for this to run properly. To verify you have Node installed, open the command line on your computer.
  * On macOS, open the Terminal from your Applications folder
  * On Windows, press Windows + R, type “cmd”, and press Enter


Once in the command line, verify you have Node installed by entering in the following command:
Copy
```
node --version

```

If you get an error saying “command not found” or “node is not recognized”, download Node from [nodejs.org](https://nodejs.org/).
**How does the configuration file work?**
This configuration file tells Claude for Desktop which MCP servers to start up every time you start the application. In this case, we have added one server called “filesystem” that will use the Node `npx` command to install and run `@modelcontextprotocol/server-filesystem`. This server, described [here](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem), will let you access your file system in Claude for Desktop.
**Command Privileges**
Claude for Desktop will run the commands in the configuration file with the permissions of your user account, and access to your local files. Only add commands if you understand and trust the source.
## 
[​](https://modelcontextprotocol.io/quickstart/user#3-restart-claude)
3. Restart Claude
After updating your configuration file, you need to restart Claude for Desktop.
Upon restarting, you should see a hammer ![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/claude-desktop-mcp-hammer-icon.svg) icon in the bottom right corner of the input box:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-hammer.png)
After clicking on the hammer icon, you should see the tools that come with the Filesystem MCP Server:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-tools.png)
If your server isn’t being picked up by Claude for Desktop, proceed to the [Troubleshooting](https://modelcontextprotocol.io/quickstart/user#troubleshooting) section for debugging tips.
## 
[​](https://modelcontextprotocol.io/quickstart/user#4-try-it-out)
4. Try it out!
You can now talk to Claude and ask it about your filesystem. It should know when to call the relevant tools.
Things you might try asking Claude:
  * Can you write a poem and save it to my desktop?
  * What are some work-related files in my downloads folder?
  * Can you take all the images on my desktop and move them to a new folder called “Images”?


As needed, Claude will call the relevant tools and seek your approval before taking an action:
![](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/quickstart-approve.png)
## 
[​](https://modelcontextprotocol.io/quickstart/user#troubleshooting)
Troubleshooting
Server not showing up in Claude / hammer icon missing
  1. Restart Claude for Desktop completely
  2. Check your `claude_desktop_config.json` file syntax
  3. Make sure the file paths included in `claude_desktop_config.json` are valid and that they are absolute and not relative
  4. Look at [logs](https://modelcontextprotocol.io/quickstart/user#getting-logs-from-claude-for-desktop) to see why the server is not connecting
  5. In your command line, try manually running the server (replacing `username` as you did in `claude_desktop_config.json`) to see if you get any errors:


  * MacOS/Linux
  * Windows


Copy
```
npx -y @modelcontextprotocol/server-filesystem /Users/username/Desktop /Users/username/Downloads

```

Getting logs from Claude for Desktop
Claude.app logging related to MCP is written to log files in:
  * macOS: `~/Library/Logs/Claude`
  * Windows: `%APPDATA%\Claude\logs`
  * `mcp.log` will contain general logging about MCP connections and connection failures.
  * Files named `mcp-server-SERVERNAME.log` will contain error (stderr) logging from the named server.


You can run the following command to list recent logs and follow along with any new ones (on Windows, it will only show recent logs):
  * MacOS/Linux
  * Windows


Copy
```
# Check Claude's logs for errors
tail -n 20 -f ~/Library/Logs/Claude/mcp*.log

```

Tool calls failing silently
If Claude attempts to use the tools but they fail:
  1. Check Claude’s logs for errors
  2. Verify your server builds and runs without errors
  3. Try restarting Claude for Desktop


None of this is working. What do I do?
Please refer to our [debugging guide](https://modelcontextprotocol.io/docs/tools/debugging) for better debugging tools and more detailed guidance.
ENOENT error and `${APPDATA}` in paths on Windows
If your configured server fails to load, and you see within its logs an error referring to `${APPDATA}` within a path, you may need to add the expanded value of `%APPDATA%` to your `env` key in `claude_desktop_config.json`:
Copy
```
{
 "brave-search": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-brave-search"],
  "env": {
   "APPDATA": "C:\\Users\\user\\AppData\\Roaming\\",
   "BRAVE_API_KEY": "..."
  }
 }
}

```

With this change in place, launch Claude Desktop once again.
**NPM should be installed globally**
The `npx` command may continue to fail if you have not installed NPM globally. If NPM is already installed globally, you will find `%APPDATA%\npm` exists on your system. If not, you can install NPM globally by running the following command:
Copy
```
npm install -g npm

```

## 
[​](https://modelcontextprotocol.io/quickstart/user#next-steps)
Next steps
## [Explore other serversCheck out our gallery of official MCP servers and implementations](https://modelcontextprotocol.io/examples)## [Build your own serverNow build your own custom server to use in Claude for Desktop and other clients](https://modelcontextprotocol.io/quickstart/server)
Was this page helpful?
YesNo
[For Client Developers](https://modelcontextprotocol.io/quickstart/client)[Example Servers](https://modelcontextprotocol.io/examples)
[github](https://github.com/modelcontextprotocol)
On this page
  * [1. Download Claude for Desktop](https://modelcontextprotocol.io/quickstart/user#1-download-claude-for-desktop)
  * [2. Add the Filesystem MCP Server](https://modelcontextprotocol.io/quickstart/user#2-add-the-filesystem-mcp-server)
  * [3. Restart Claude](https://modelcontextprotocol.io/quickstart/user#3-restart-claude)
  * [4. Try it out!](https://modelcontextprotocol.io/quickstart/user#4-try-it-out)
  * [Troubleshooting](https://modelcontextprotocol.io/quickstart/user#troubleshooting)
  * [Next steps](https://modelcontextprotocol.io/quickstart/user#next-steps)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Java
  * [Overview](https://modelcontextprotocol.io/sdk/java/mcp-overview)
  * [MCP Client](https://modelcontextprotocol.io/sdk/java/mcp-client)
  * [MCP Server](https://modelcontextprotocol.io/sdk/java/mcp-server)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Java
MCP Client
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Java
# MCP Client
Learn how to use the Model Context Protocol (MCP) client to interact with MCP servers
# 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#model-context-protocol-client)
Model Context Protocol Client
The MCP Client is a key component in the Model Context Protocol (MCP) architecture, responsible for establishing and managing connections with MCP servers. It implements the client-side of the protocol, handling:
  * Protocol version negotiation to ensure compatibility with servers
  * Capability negotiation to determine available features
  * Message transport and JSON-RPC communication
  * Tool discovery and execution
  * Resource access and management
  * Prompt system interactions
  * Optional features like roots management and sampling support


The [Spring-AI MCP Client](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html) integration extends the MCP Java SDK to provide auto-configuration for MCP client functionality in Spring Boot applications and integrating with Spring AI’s [tool execution framework](https://docs.spring.io/spring-ai/reference/api/tools.html).
The client provides both synchronous and asynchronous APIs for flexibility in different application contexts.
  * Sync API
  * Async API


Copy
```
// Create a sync client with custom configuration
McpSyncClient client = McpClient.sync(transport)
  .requestTimeout(Duration.ofSeconds(10))
  .capabilities(ClientCapabilities.builder()
    .roots(true)   // Enable roots capability
    .sampling()    // Enable sampling capability
    .build())
  .sampling(request -> new CreateMessageResult(response))
  .build();
// Initialize connection
client.initialize();
// List available tools
ListToolsResult tools = client.listTools();
// Call a tool
CallToolResult result = client.callTool(
  new CallToolRequest("calculator", 
    Map.of("operation", "add", "a", 2, "b", 3))
);
// List and read resources
ListResourcesResult resources = client.listResources();
ReadResourceResult resource = client.readResource(
  new ReadResourceRequest("resource://uri")
);
// List and use prompts
ListPromptsResult prompts = client.listPrompts();
GetPromptResult prompt = client.getPrompt(
  new GetPromptRequest("greeting", Map.of("name", "Spring"))
);
// Add/remove roots
client.addRoot(new Root("file:///path", "description"));
client.removeRoot("file:///path");
// Close client
client.closeGracefully();

```

## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#client-transport)
Client Transport
The transport layer handles the communication between MCP clients and servers, providing different implementations for various use cases. The client transport manages message serialization, connection establishment, and protocol-specific communication patterns.
  * STDIO
  * SSE (HttpClient)
  * SSE (WebFlux)


Creates transport for in-process based communication
Copy
```
ServerParameters params = ServerParameters.builder("npx")
  .args("-y", "@modelcontextprotocol/server-everything", "dir")
  .build();
McpTransport transport = new StdioClientTransport(params);

```

## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#client-capabilities)
Client Capabilities
The client can be configured with various capabilities:
Copy
```
var capabilities = ClientCapabilities.builder()
  .roots(true)   // Enable filesystem roots support with list changes notifications
  .sampling()    // Enable LLM sampling support
  .build();

```

### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#roots-support)
Roots Support
Roots define the boundaries of where servers can operate within the filesystem:
Copy
```
// Add a root dynamically
client.addRoot(new Root("file:///path", "description"));
// Remove a root
client.removeRoot("file:///path");
// Notify server of roots changes
client.rootsListChangedNotification();

```

The roots capability allows servers to:
  * Request the list of accessible filesystem roots
  * Receive notifications when the roots list changes
  * Understand which directories and files they have access to


### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#sampling-support)
Sampling Support
Sampling enables servers to request LLM interactions (“completions” or “generations”) through the client:
Copy
```
// Configure sampling handler
Function<CreateMessageRequest, CreateMessageResult> samplingHandler = request -> {
  // Sampling implementation that interfaces with LLM
  return new CreateMessageResult(response);
};
// Create client with sampling support
var client = McpClient.sync(transport)
  .capabilities(ClientCapabilities.builder()
    .sampling()
    .build())
  .sampling(samplingHandler)
  .build();

```

This capability allows:
  * Servers to leverage AI capabilities without requiring API keys
  * Clients to maintain control over model access and permissions
  * Support for both text and image-based interactions
  * Optional inclusion of MCP server context in prompts


## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#using-mcp-clients)
Using MCP Clients
### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#tool-execution)
Tool Execution
Tools are server-side functions that clients can discover and execute. The MCP client provides methods to list available tools and execute them with specific parameters. Each tool has a unique name and accepts a map of parameters.
  * Sync API
  * Async API


Copy
```
// List available tools and their names
var tools = client.listTools();
tools.forEach(tool -> System.out.println(tool.getName()));
// Execute a tool with parameters
var result = client.callTool("calculator", Map.of(
  "operation", "add",
  "a", 1,
  "b", 2
));

```

### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#resource-access)
Resource Access
Resources represent server-side data sources that clients can access using URI templates. The MCP client provides methods to discover available resources and retrieve their contents through a standardized interface.
  * Sync API
  * Async API


Copy
```
// List available resources and their names
var resources = client.listResources();
resources.forEach(resource -> System.out.println(resource.getName()));
// Retrieve resource content using a URI template
var content = client.getResource("file", Map.of(
  "path", "/path/to/file.txt"
));

```

### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-client#prompt-system)
Prompt System
The prompt system enables interaction with server-side prompt templates. These templates can be discovered and executed with custom parameters, allowing for dynamic text generation based on predefined patterns.
  * Sync API
  * Async API


Copy
```
// List available prompt templates
var prompts = client.listPrompts();
prompts.forEach(prompt -> System.out.println(prompt.getName()));
// Execute a prompt template with parameters
var response = client.executePrompt("echo", Map.of(
  "text", "Hello, World!"
));

```

Was this page helpful?
YesNo
[Overview](https://modelcontextprotocol.io/sdk/java/mcp-overview)[MCP Server](https://modelcontextprotocol.io/sdk/java/mcp-server)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Model Context Protocol Client](https://modelcontextprotocol.io/sdk/java/mcp-client#model-context-protocol-client)
  * [Client Transport](https://modelcontextprotocol.io/sdk/java/mcp-client#client-transport)
  * [Client Capabilities](https://modelcontextprotocol.io/sdk/java/mcp-client#client-capabilities)
  * [Roots Support](https://modelcontextprotocol.io/sdk/java/mcp-client#roots-support)
  * [Sampling Support](https://modelcontextprotocol.io/sdk/java/mcp-client#sampling-support)
  * [Using MCP Clients](https://modelcontextprotocol.io/sdk/java/mcp-client#using-mcp-clients)
  * [Tool Execution](https://modelcontextprotocol.io/sdk/java/mcp-client#tool-execution)
  * [Resource Access](https://modelcontextprotocol.io/sdk/java/mcp-client#resource-access)
  * [Prompt System](https://modelcontextprotocol.io/sdk/java/mcp-client#prompt-system)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Java
  * [Overview](https://modelcontextprotocol.io/sdk/java/mcp-overview)
  * [MCP Client](https://modelcontextprotocol.io/sdk/java/mcp-client)
  * [MCP Server](https://modelcontextprotocol.io/sdk/java/mcp-server)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Java
Overview
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Java
# Overview
Introduction to the Model Context Protocol (MCP) Java SDK
Java SDK for the [Model Context Protocol](https://modelcontextprotocol.org/docs/concepts/architecture) enables standardized integration between AI models and tools.
### Breaking Changes in 0.8.x ⚠️
**Note:** Version 0.8.x introduces several breaking changes including a new session-based architecture. If you’re upgrading from 0.7.0, please refer to the [Migration Guide](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md) for detailed instructions.
## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-overview#features)
Features
  * MCP Client and MCP Server implementations supporting: 
    * Protocol [version compatibility negotiation](https://spec.modelcontextprotocol.io/specification/2024-11-05/basic/lifecycle/#initialization)
    * [Tool](https://spec.modelcontextprotocol.io/specification/2024-11-05/server/tools/) discovery, execution, list change notifications
    * [Resource](https://spec.modelcontextprotocol.io/specification/2024-11-05/server/resources/) management with URI templates
    * [Roots](https://spec.modelcontextprotocol.io/specification/2024-11-05/client/roots/) list management and notifications
    * [Prompt](https://spec.modelcontextprotocol.io/specification/2024-11-05/server/prompts/) handling and management
    * [Sampling](https://spec.modelcontextprotocol.io/specification/2024-11-05/client/sampling/) support for AI model interactions
  * Multiple transport implementations: 
    * Default transports: 
      * Stdio-based transport for process-based communication
      * Java HttpClient-based SSE client transport for HTTP SSE Client-side streaming
      * Servlet-based SSE server transport for HTTP SSE Server streaming
    * Spring-based transports: 
      * WebFlux SSE client and server transports for reactive HTTP streaming
      * WebMVC SSE transport for servlet-based HTTP streaming
  * Supports Synchronous and Asynchronous programming paradigms


[Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html) extends the MCP Java SDK with Spring Boot integration, providing both [Client](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-client-boot-starter-docs.html) and [Server](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) Boot Starters. You can bootstrap your AI Spring applications using the [Spring Initializer](https://start.spring.io/).
## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-overview#architecture)
Architecture
The SDK follows a layered architecture with clear separation of concerns:
![MCP Stack Architecture](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/mcp-stack.svg)
  * **Client/Server Layer (McpClient/McpServer)** : Both use McpSession for sync/async operations, with McpClient handling client-side protocol operations and McpServer managing server-side protocol operations.
  * **Session Layer (McpSession)** : Manages communication patterns and state using DefaultMcpSession implementation.
  * **Transport Layer (McpTransport)** : Handles JSON-RPC message serialization/deserialization via: 
    * StdioTransport (stdin/stdout) in the core module
    * HTTP SSE transports in dedicated transport modules (Java HttpClient, Spring WebFlux, Spring WebMVC)


The MCP Client is a key component in the Model Context Protocol (MCP) architecture, responsible for establishing and managing connections with MCP servers. It implements the client-side of the protocol.
![Java MCP Client Architecture](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-client-architecture.jpg)
The MCP Server is a foundational component in the Model Context Protocol (MCP) architecture that provides tools, resources, and capabilities to clients. It implements the server-side of the protocol.
![Java MCP Server Architecture](https://mintlify.s3.us-west-1.amazonaws.com/mcp/images/java/java-mcp-server-architecture.jpg)
Key Interactions:
  * **Client/Server Initialization** : Transport setup, protocol compatibility check, capability negotiation, and implementation details exchange.
  * **Message Flow** : JSON-RPC message handling with validation, type-safe response processing, and error handling.
  * **Resource Management** : Resource discovery, URI template-based access, subscription system, and content retrieval.


## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-overview#dependencies)
Dependencies
Add the following Maven dependency to your project:
  * Maven
  * Gradle


The core MCP functionality:
Copy
```
<dependency>
  <groupId>io.modelcontextprotocol.sdk</groupId>
  <artifactId>mcp</artifactId>
</dependency>

```

For HTTP SSE transport implementations, add one of the following dependencies:
Copy
```
<!-- Spring WebFlux-based SSE client and server transport -->
<dependency>
  <groupId>io.modelcontextprotocol.sdk</groupId>
  <artifactId>mcp-spring-webflux</artifactId>
</dependency>
<!-- Spring WebMVC-based SSE server transport -->
<dependency>
  <groupId>io.modelcontextprotocol.sdk</groupId>
  <artifactId>mcp-spring-webmvc</artifactId>
</dependency>

```

### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-overview#bill-of-materials-bom)
Bill of Materials (BOM)
The Bill of Materials (BOM) declares the recommended versions of all the dependencies used by a given release. Using the BOM from your application’s build script avoids the need for you to specify and maintain the dependency versions yourself. Instead, the version of the BOM you’re using determines the utilized dependency versions. It also ensures that you’re using supported and tested versions of the dependencies by default, unless you choose to override them.
Add the BOM to your project:
  * Maven
  * Gradle


Copy
```
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>io.modelcontextprotocol.sdk</groupId>
      <artifactId>mcp-bom</artifactId>
      <version>0.8.1</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

```

Replace the version number with the version of the BOM you want to use.
### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-overview#available-dependencies)
Available Dependencies
The following dependencies are available and managed by the BOM:
  * Core Dependencies 
    * `io.modelcontextprotocol.sdk:mcp` - Core MCP library providing the base functionality and APIs for Model Context Protocol implementation.
  * Transport Dependencies 
    * `io.modelcontextprotocol.sdk:mcp-spring-webflux` - WebFlux-based Server-Sent Events (SSE) transport implementation for reactive applications.
    * `io.modelcontextprotocol.sdk:mcp-spring-webmvc` - WebMVC-based Server-Sent Events (SSE) transport implementation for servlet-based applications.
  * Testing Dependencies 
    * `io.modelcontextprotocol.sdk:mcp-test` - Testing utilities and support for MCP-based applications.


Was this page helpful?
YesNo
[MCP Client](https://modelcontextprotocol.io/sdk/java/mcp-client)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Features](https://modelcontextprotocol.io/sdk/java/mcp-overview#features)
  * [Architecture](https://modelcontextprotocol.io/sdk/java/mcp-overview#architecture)
  * [Dependencies](https://modelcontextprotocol.io/sdk/java/mcp-overview#dependencies)
  * [Bill of Materials (BOM)](https://modelcontextprotocol.io/sdk/java/mcp-overview#bill-of-materials-bom)
  * [Available Dependencies](https://modelcontextprotocol.io/sdk/java/mcp-overview#available-dependencies)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Java
  * [Overview](https://modelcontextprotocol.io/sdk/java/mcp-overview)
  * [MCP Client](https://modelcontextprotocol.io/sdk/java/mcp-client)
  * [MCP Server](https://modelcontextprotocol.io/sdk/java/mcp-server)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Java
MCP Server
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Java
# MCP Server
Learn how to implement and configure a Model Context Protocol (MCP) server
### Breaking Changes in 0.8.x ⚠️
**Note:** Version 0.8.x introduces several breaking changes including a new session-based architecture. If you’re upgrading from 0.7.0, please refer to the [Migration Guide](https://github.com/modelcontextprotocol/java-sdk/blob/main/migration-0.8.0.md) for detailed instructions.
## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#overview)
Overview
The MCP Server is a foundational component in the Model Context Protocol (MCP) architecture that provides tools, resources, and capabilities to clients. It implements the server-side of the protocol, responsible for:
  * Exposing tools that clients can discover and execute
  * Managing resources with URI-based access patterns
  * Providing prompt templates and handling prompt requests
  * Supporting capability negotiation with clients
  * Implementing server-side protocol operations
  * Managing concurrent client connections
  * Providing structured logging and notifications


The [Spring-AI MCP Server](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) integration extends the MCP Java SDK to provide auto-configuration for MCP server functionality in Spring Boot applications.
The server supports both synchronous and asynchronous APIs, allowing for flexible integration in different application contexts.
  * Sync API
  * Async API


Copy
```
// Create a server with custom configuration
McpSyncServer syncServer = McpServer.sync(transportProvider)
  .serverInfo("my-server", "1.0.0")
  .capabilities(ServerCapabilities.builder()
    .resources(true)   // Enable resource support
    .tools(true)     // Enable tool support
    .prompts(true)    // Enable prompt support
    .logging()      // Enable logging support
    .build())
  .build();
// Register tools, resources, and prompts
syncServer.addTool(syncToolSpecification);
syncServer.addResource(syncResourceSpecification);
syncServer.addPrompt(syncPromptSpecification);
// Send logging notifications
syncServer.loggingNotification(LoggingMessageNotification.builder()
  .level(LoggingLevel.INFO)
  .logger("custom-logger")
  .data("Server initialized")
  .build());
// Close the server when done
syncServer.close();

```

## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#server-transport-providers)
Server Transport Providers
The transport layer in the MCP SDK is responsible for handling the communication between clients and servers. It provides different implementations to support various communication protocols and patterns. The SDK includes several built-in transport provider implementations:
  * STDIO
  * SSE (WebFlux)
  * SSE (WebMvc)
  * SSE (Servlet)


Create in-process based transport:
Copy
```
StdioServerTransportProvider transportProvider = new StdioServerTransportProvider(new ObjectMapper());

```

Provides bidirectional JSON-RPC message handling over standard input/output streams with non-blocking message processing, serialization/deserialization, and graceful shutdown support.
Key features:
  * Bidirectional communication through stdin/stdout
  * Process-based integration support
  * Simple setup and configuration
  * Lightweight implementation


## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#server-capabilities)
Server Capabilities
The server can be configured with various capabilities:
Copy
```
var capabilities = ServerCapabilities.builder()
  .resources(false, true) // Resource support with list changes notifications
  .tools(true)      // Tool support with list changes notifications
  .prompts(true)     // Prompt support with list changes notifications
  .logging()       // Enable logging support (enabled by default with logging level INFO)
  .build();

```

### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#logging-support)
Logging Support
The server provides structured logging capabilities that allow sending log messages to clients with different severity levels:
Copy
```
// Send a log message to clients
server.loggingNotification(LoggingMessageNotification.builder()
  .level(LoggingLevel.INFO)
  .logger("custom-logger")
  .data("Custom log message")
  .build());

```

Clients can control the minimum logging level they receive through the `mcpClient.setLoggingLevel(level)` request. Messages below the set level will be filtered out. Supported logging levels (in order of increasing severity): DEBUG (0), INFO (1), NOTICE (2), WARNING (3), ERROR (4), CRITICAL (5), ALERT (6), EMERGENCY (7)
### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#tool-specification)
Tool Specification
The Model Context Protocol allows servers to [expose tools](https://spec.modelcontextprotocol.io/specification/2024-11-05/server/tools/) that can be invoked by language models. The Java SDK allows implementing a Tool Specifications with their handler functions. Tools enable AI models to perform calculations, access external APIs, query databases, and manipulate files:
  * Sync
  * Async


Copy
```
// Sync tool specification
var schema = """
      {
       "type" : "object",
       "id" : "urn:jsonschema:Operation",
       "properties" : {
        "operation" : {
         "type" : "string"
        },
        "a" : {
         "type" : "number"
        },
        "b" : {
         "type" : "number"
        }
       }
      }
      """;
var syncToolSpecification = new McpServerFeatures.SyncToolSpecification(
  new Tool("calculator", "Basic calculator", schema),
  (exchange, arguments) -> {
    // Tool implementation
    return new CallToolResult(result, false);
  }
);

```

The Tool specification includes a Tool definition with `name`, `description`, and `parameter schema` followed by a call handler that implements the tool’s logic. The function’s first argument is `McpAsyncServerExchange` for client interaction, and the second is a map of tool arguments.
### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#resource-specification)
Resource Specification
Specification of a resource with its handler function. Resources provide context to AI models by exposing data such as: File contents, Database records, API responses, System information, Application state. Example resource specification:
  * Sync
  * Async


Copy
```
// Sync resource specification
var syncResourceSpecification = new McpServerFeatures.syncResourceSpecification(
  new Resource("custom://resource", "name", "description", "mime-type", null),
  (exchange, request) -> {
    // Resource read implementation
    return new ReadResourceResult(contents);
  }
);

```

The resource specification comprised of resource definitions and resource read handler. The resource definition including `name`, `description`, and `MIME type`. The first argument of the function that handles resource read requests is an `McpAsyncServerExchange` upon which the server can interact with the connected client. The second arguments is a `McpSchema.ReadResourceRequest`.
### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#prompt-specification)
Prompt Specification
As part of the [Prompting capabilities](https://spec.modelcontextprotocol.io/specification/2024-11-05/server/prompts/), MCP provides a standardized way for servers to expose prompt templates to clients. The Prompt Specification is a structured template for AI model interactions that enables consistent message formatting, parameter substitution, context injection, response formatting, and instruction templating.
  * Sync
  * Async


Copy
```
// Sync prompt specification
var syncPromptSpecification = new McpServerFeatures.syncPromptSpecification(
  new Prompt("greeting", "description", List.of(
    new PromptArgument("name", "description", true)
  )),
  (exchange, request) -> {
    // Prompt implementation
    return new GetPromptResult(description, messages);
  }
);

```

The prompt definition includes name (identifier for the prompt), description (purpose of the prompt), and list of arguments (parameters for templating). The handler function processes requests and returns formatted templates. The first argument is `McpAsyncServerExchange` for client interaction, and the second argument is a `GetPromptRequest` instance.
### 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#using-sampling-from-a-server)
Using Sampling from a Server
To use [Sampling capabilities](https://spec.modelcontextprotocol.io/specification/2024-11-05/client/sampling/), connect to a client that supports sampling. No special server configuration is needed, but verify client sampling support before making requests. Learn about [client sampling support](https://modelcontextprotocol.io/sdk/java/mcp-client#sampling-support).
Once connected to a compatible client, the server can request language model generations:
  * Sync API
  * Async API


Copy
```
// Create a server
McpSyncServer server = McpServer.sync(transportProvider)
  .serverInfo("my-server", "1.0.0")
  .build();
// Define a tool that uses sampling
var calculatorTool = new McpServerFeatures.SyncToolSpecification(
  new Tool("ai-calculator", "Performs calculations using AI", schema),
  (exchange, arguments) -> {
    // Check if client supports sampling
    if (exchange.getClientCapabilities().sampling() == null) {
      return new CallToolResult("Client does not support AI capabilities", false);
    }
    
    // Create a sampling request
    McpSchema.CreateMessageRequest request = McpSchema.CreateMessageRequest.builder()
      .content(new McpSchema.TextContent("Calculate: " + arguments.get("expression")))
      .modelPreferences(McpSchema.ModelPreferences.builder()
        .hints(List.of(
          McpSchema.ModelHint.of("claude-3-sonnet"),
          McpSchema.ModelHint.of("claude")
        ))
        .intelligencePriority(0.8) // Prioritize intelligence
        .speedPriority(0.5)     // Moderate speed importance
        .build())
      .systemPrompt("You are a helpful calculator assistant. Provide only the numerical answer.")
      .maxTokens(100)
      .build();
    
    // Request sampling from the client
    McpSchema.CreateMessageResult result = exchange.createMessage(request);
    
    // Process the result
    String answer = result.content().text();
    return new CallToolResult(answer, false);
  }
);
// Add the tool to the server
server.addTool(calculatorTool);

```

The `CreateMessageRequest` object allows you to specify: `Content` - the input text or image for the model, `Model Preferences` - hints and priorities for model selection, `System Prompt` - instructions for the model’s behavior and `Max Tokens` - maximum length of the generated response.
## 
[​](https://modelcontextprotocol.io/sdk/java/mcp-server#error-handling)
Error Handling
The SDK provides comprehensive error handling through the McpError class, covering protocol compatibility, transport communication, JSON-RPC messaging, tool execution, resource management, prompt handling, timeouts, and connection issues. This unified error handling approach ensures consistent and reliable error management across both synchronous and asynchronous operations.
Was this page helpful?
YesNo
[MCP Client](https://modelcontextprotocol.io/sdk/java/mcp-client)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Overview](https://modelcontextprotocol.io/sdk/java/mcp-server#overview)
  * [Server Transport Providers](https://modelcontextprotocol.io/sdk/java/mcp-server#server-transport-providers)
  * [Server Capabilities](https://modelcontextprotocol.io/sdk/java/mcp-server#server-capabilities)
  * [Logging Support](https://modelcontextprotocol.io/sdk/java/mcp-server#logging-support)
  * [Tool Specification](https://modelcontextprotocol.io/sdk/java/mcp-server#tool-specification)
  * [Resource Specification](https://modelcontextprotocol.io/sdk/java/mcp-server#resource-specification)
  * [Prompt Specification](https://modelcontextprotocol.io/sdk/java/mcp-server#prompt-specification)
  * [Using Sampling from a Server](https://modelcontextprotocol.io/sdk/java/mcp-server#using-sampling-from-a-server)
  * [Error Handling](https://modelcontextprotocol.io/sdk/java/mcp-server#error-handling)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
* [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
* [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
* [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
* [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
* [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
* [Specification](https://spec.modelcontextprotocol.io)
##### Get Started
  * [Introduction](https://modelcontextprotocol.io/introduction)
  * Quickstart
  * [Example Servers](https://modelcontextprotocol.io/examples)
  * [Example Clients](https://modelcontextprotocol.io/clients)


##### Tutorials
  * [Building MCP with LLMs](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms)
  * [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
  * [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)


##### Concepts
  * [Core architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
  * [Resources](https://modelcontextprotocol.io/docs/concepts/resources)
  * [Prompts](https://modelcontextprotocol.io/docs/concepts/prompts)
  * [Tools](https://modelcontextprotocol.io/docs/concepts/tools)
  * [Sampling](https://modelcontextprotocol.io/docs/concepts/sampling)
  * [Roots](https://modelcontextprotocol.io/docs/concepts/roots)
  * [Transports](https://modelcontextprotocol.io/docs/concepts/transports)


##### Development
  * [What's New](https://modelcontextprotocol.io/development/updates)
  * [Roadmap](https://modelcontextprotocol.io/development/roadmap)
  * [Contributing](https://modelcontextprotocol.io/development/contributing)


[Model Context Protocol home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg)](https://modelcontextprotocol.io/)
Search...
Ctrl K
  * [GitHub](https://github.com/modelcontextprotocol)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Tutorials
Building MCP with LLMs
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
[Documentation](https://modelcontextprotocol.io/introduction)[SDKs](https://modelcontextprotocol.io/sdk/java/mcp-overview)
* [GitHub](https://github.com/modelcontextprotocol)
Tutorials
# Building MCP with LLMs
Speed up your MCP development using LLMs such as Claude!
This guide will help you use LLMs to help you build custom Model Context Protocol (MCP) servers and clients. We’ll be focusing on Claude for this tutorial, but you can do this with any frontier LLM.
## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#preparing-the-documentation)
Preparing the documentation
Before starting, gather the necessary documentation to help Claude understand MCP:
  1. Visit <https://modelcontextprotocol.io/llms-full.txt> and copy the full documentation text
  2. Navigate to either the [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) or [Python SDK repository](https://github.com/modelcontextprotocol/python-sdk)
  3. Copy the README files and other relevant documentation
  4. Paste these documents into your conversation with Claude


## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#describing-your-server)
Describing your server
Once you’ve provided the documentation, clearly describe to Claude what kind of server you want to build. Be specific about:
  * What resources your server will expose
  * What tools it will provide
  * Any prompts it should offer
  * What external systems it needs to interact with


For example:
Copy
```
Build an MCP server that:
- Connects to my company's PostgreSQL database
- Exposes table schemas as resources
- Provides tools for running read-only SQL queries
- Includes prompts for common data analysis tasks

```

## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#working-with-claude)
Working with Claude
When working with Claude on MCP servers:
  1. Start with the core functionality first, then iterate to add more features
  2. Ask Claude to explain any parts of the code you don’t understand
  3. Request modifications or improvements as needed
  4. Have Claude help you test the server and handle edge cases


Claude can help implement all the key MCP features:
  * Resource management and exposure
  * Tool definitions and implementations
  * Prompt templates and handlers
  * Error handling and logging
  * Connection and transport setup


## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#best-practices)
Best practices
When building MCP servers with Claude:
  * Break down complex servers into smaller pieces
  * Test each component thoroughly before moving on
  * Keep security in mind - validate inputs and limit access appropriately
  * Document your code well for future maintenance
  * Follow MCP protocol specifications carefully


## 
[​](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#next-steps)
Next steps
After Claude helps you build your server:
  1. Review the generated code carefully
  2. Test the server with the MCP Inspector tool
  3. Connect it to Claude.app or other MCP clients
  4. Iterate based on real usage and feedback


Remember that Claude can help you modify and improve your server as requirements change over time.
Need more guidance? Just ask Claude specific questions about implementing MCP features or troubleshooting issues that arise.
Was this page helpful?
YesNo
[Example Clients](https://modelcontextprotocol.io/clients)[Debugging](https://modelcontextprotocol.io/docs/tools/debugging)
[github](https://github.com/modelcontextprotocol)
On this page
  * [Preparing the documentation](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#preparing-the-documentation)
  * [Describing your server](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#describing-your-server)
  * [Working with Claude](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#working-with-claude)
  * [Best practices](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#best-practices)
  * [Next steps](https://modelcontextprotocol.io/tutorials/building-mcp-with-llms#next-steps)


