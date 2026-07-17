# OmniMind OS

OmniMind OS is a capability-based multi-agent orchestration framework for planning and executing complex tasks through specialized agents.

## Overview

The project combines:
- capability-based task planning
- dynamic agent discovery and selection
- execution tracing for explainability
- guardrails and tool integration for safer automation

## Installation

```bash
git clone https://github.com/rofen69/OmniMind-OS.git
cd OmniMind-OS
pip install -r requirements.txt
```

## Quick Start

Run the built-in demo:

```bash
python scripts/demo.py
```

Or start the main application:

```bash
python -m src.main
```

## Architecture

The runtime is organized around a planner, registry, orchestrator, and agent execution layer. For implementation details, see the developer documentation in [docs/02_SYSTEM_ARCHITECTURE.md](docs/02_SYSTEM_ARCHITECTURE.md) and [docs/03_DEVELOPER_GUIDE.md](docs/03_DEVELOPER_GUIDE.md).

## Project Structure

- [src](src) — core runtime, agents, and orchestration logic
- [scripts](scripts) — entry-point demos and utilities
- [docs](docs) — developer documentation
- [workspace](workspace) — local runtime workspace for generated artifacts

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the current development direction.

## Contributing

Contributions are welcome. Please review [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is licensed under the CC-BY 4.0 License. See [LICENSE](LICENSE) for details.
