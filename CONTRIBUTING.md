# Contributing Guidelines

Thank you for considering contributing to this project! By participating, you agree to abide by our code of conduct and follow these guidelines.

## How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker to report bugs.
- Include a clear title and a description of the problem.
- Provide steps to reproduce, expected behavior, and actual behavior.
- Include any relevant logs or screenshots.

### Suggesting Enhancements

- Open an issue with the "enhancement" label.
- Describe the proposed feature, its benefits, and any relevant design considerations.

### Submitting Pull Requests

1. **Fork the repository** and create a new branch for your changes.
2. **Write clear, concise commit messages**.
3. Ensure your code follows the project's style guidelines (see the `README` for linting commands).
4. **Include tests** for new functionality when applicable.
5. Update documentation if you add or modify features.
6. Submit the pull request against the `doc-update` branch.

### Code Style

- Follow PEP 8 for Python code.
- Use `black` and `flake8` for formatting and linting.
- Frontend code follows the default ESLint configuration provided by Next.js.

### Testing

- Run the test suite before submitting a PR:
  ```bash
  pytest
  ```
- Ensure all tests pass and coverage is not decreased.

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

---

For any questions, feel free to reach out to the maintainers via the issue tracker.
