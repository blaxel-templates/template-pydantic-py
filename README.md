# Blaxel Pydantic AI Agent

<p align="center">
  <img src="https://blaxel.ai/logo.png" alt="Blaxel" width="200"/>
</p>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic AI](https://img.shields.io/badge/Pydantic_AI-powered-brightgreen.svg)](https://ai.pydantic.dev/)
[![UV](https://img.shields.io/badge/UV-package_manager-blue.svg)](https://github.com/astral-sh/uv)

</div>

A template implementation of a conversational agent using Pydantic AI and GPT-4. This agent demonstrates the power of Pydantic AI for building interactive AI agents with type-safe tool integration capabilities and structured data validation.

## 📑 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running Locally](#running-the-server-locally)
  - [Testing](#testing-your-agent)
  - [Deployment](#deploying-to-blaxel)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## ✨ Features

- Interactive conversational interface with Pydantic type validation
- Tool integration support with type-safe function calling
- Streaming responses for real-time interaction
- Built on Pydantic AI for structured data handling and validation
- Type-safe agent development with Python type hints
- Easy deployment and integration with Blaxel platform
- Comprehensive error handling and validation

## 🚀 Quick Start

For those who want to get up and running quickly:

```bash
# Clone the repository
git clone https://github.com/blaxel-ai/template-pydantic-py.git

# Navigate to the project directory
cd template-pydantic-py

# Install dependencies
uv sync

# Start the server
bl serve --hotreload

# In another terminal, test the agent
bl chat --local blaxel-agent
```

## 📋 Prerequisites

- **Python:** 3.10 or later
- **[UV](https://github.com/astral-sh/uv):** An extremely fast Python package and project manager, written in Rust
- **Blaxel Platform Setup:** Complete Blaxel setup by following the [quickstart guide](https://docs.blaxel.ai/Get-started#quickstart)
  - **[Blaxel CLI](https://docs.blaxel.ai/Get-started):** Ensure you have the Blaxel CLI installed. If not, install it globally:
    ```bash
    curl -fsSL https://raw.githubusercontent.com/blaxel-ai/toolkit/main/install.sh | BINDIR=/usr/local/bin sudo -E sh
    ```
  - **Blaxel login:** Login to Blaxel platform
    ```bash
    bl login YOUR-WORKSPACE
    ```

## 💻 Installation

**Clone the repository and install dependencies:**

```bash
git clone https://github.com/blaxel-ai/template-pydantic-py.git
cd template-pydantic-py
uv sync
```

## 🔧 Usage

### Running the Server Locally

Start the development server with hot reloading:

```bash
bl serve --hotreload
```

_Note:_ This command starts the server and enables hot reload so that changes to the source code are automatically reflected.

### Testing your agent

You can test your agent using the chat interface:

```bash
bl chat --local blaxel-agent
```

Or run it directly with specific input:

```bash
bl run agent blaxel-agent --local --data '{"input": "What is the weather in Paris?"}'
```

### Deploying to Blaxel

When you are ready to deploy your application:

```bash
bl deploy
```

This command uses your code and the configuration files under the `.blaxel` directory to deploy your application.

## 📁 Project Structure

- **src/main.py** - Application entry point
- **src/agent.py** - Core agent implementation with Pydantic AI integration
- **src/server/** - Server implementation and routing
  - **router.py** - API route definitions
  - **middleware.py** - Request/response middleware
- **pyproject.toml** - UV package manager configuration
- **blaxel.toml** - Blaxel deployment configuration

## ❓ Troubleshooting

### Common Issues

1. **Blaxel Platform Issues**:
   - Ensure you're logged in to your workspace: `bl login MY-WORKSPACE`
   - Verify models are available: `bl get models`
   - Check that functions exist: `bl get functions`

2. **Pydantic Validation Errors**:
   - Check data schema definitions and validation rules
   - Verify type annotations match expected data formats
   - Review Pydantic model configurations

3. **Tool Integration Problems**:
   - Ensure tool functions have proper type annotations
   - Check tool parameter validation in Blaxel platform
   - Verify tool execution permissions

4. **Type Checking Issues**:
   - Run `mypy src/` to check for type errors
   - Ensure all function signatures are properly typed
   - Check Pydantic model definitions

5. **Agent Response Formatting**:
   - Verify agent response schemas are properly defined
   - Check streaming response configuration
   - Review error handling in agent responses

For more help, please [submit an issue](https://github.com/blaxel-templates/template-pydantic-py/issues) on GitHub.

## 👥 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Submit** a Pull Request

Please make sure to update tests as appropriate and follow the code style of the project.

## 🆘 Support

If you need help with this template:

- [Submit an issue](https://github.com/blaxel-templates/template-pydantic-py/issues) for bug reports or feature requests
- Visit the [Blaxel Documentation](https://docs.blaxel.ai) for platform guidance
- Check the [Pydantic AI Documentation](https://ai.pydantic.dev/) for framework-specific help
- Join our [Discord Community](https://discord.gg/G3NqzUPcHP) for real-time assistance

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
