# OmniMind OS - Contributing Guidelines

We welcome contributions to OmniMind OS! This document outlines the process for contributing to the project.

## 🤝 How to Contribute

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/my-new-agent`
3. **Make your changes:** Ensure you follow the architecture principles in the [Developer Guide](docs/03_DEVELOPER_GUIDE.md).
4. **Test your changes:** Run the CLI demo (`python -m src.main`) to verify execution.
5. **Submit a Pull Request:** Describe your changes, why they are needed, and how you tested them.

## 📝 Coding Standards

- **Type Hints:** All function signatures must include Python type hints.
- **Docstrings:** All modules, classes, and public functions must have docstrings.
- **Formatting:** Code should be readable and consistent with existing patterns.
- **Modularity:** Ensure changes inside `src/core/` or `src/discovery/` do not tightly couple to specific agents.

## 🐛 Bug Reports & Feature Requests

Please use the issue tracker to report bugs or suggest new features. Include:
- A clear, descriptive title.
- Steps to reproduce the bug (if applicable).
- Expected vs actual behavior.

Thank you for contributing to OmniMind OS!
