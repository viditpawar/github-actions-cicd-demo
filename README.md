# GitHub Actions CI/CD Demo

A demonstration project showcasing a complete CI/CD pipeline implementation using GitHub Actions for automated testing, linting, code quality checks, and deployment workflows - built with **Python**.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Scripts & Commands](#scripts--commands)
- [Testing](#testing)
- [Code Quality](#code-quality)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates a professional CI/CD setup using GitHub Actions with **Python**. It includes a simple math utility library with comprehensive test coverage, automated code quality checks, and workflows that run on every push and pull request.

The pipeline is designed to:
- Automatically test code across multiple Python versions (3.9, 3.11, 3.12)
- Enforce code quality standards with Pylint, Flake8, and Black
- Validate code formatting and style
- Report results back to GitHub

## Features

✅ **Multi-version Testing** - Tests run on Python 3.9, 3.11, and 3.12  
✅ **Automated Linting** - Flake8 and Pylint for code quality  
✅ **Code Formatting** - Black for consistent code style  
✅ **Comprehensive Testing** - Pytest test suite with multiple test cases  
✅ **GitHub Actions Integration** - Automated CI/CD on push and pull requests  
✅ **Code Quality Checks** - Dedicated code quality job in the pipeline  

## Prerequisites

- **Python** - Version 3.9 or higher
- **pip** - Python package manager
- **Git** - For cloning and version control

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/viditpawar/github-actions-cicd-demo.git
   cd github-actions-cicd-demo
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

## Usage

### Running the Application

Execute the main application:

```bash
python src/main.py
```

**Expected Output:**
```
CI/CD Demo Application
Addition result: 15
Subtraction result: 5
Multiplication result: 50
Division result: 2.0
```

### Using the Math Library

Import and use the math utilities in your own code:

```python
from src.math import add, subtract, multiply, divide

print(add(10, 5))        # 15
print(subtract(10, 5))   # 5
print(multiply(10, 5))   # 50
print(divide(10, 5))     # 2.0
```

## Project Structure

```
github-actions-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI/CD workflow
├── src/
│   ├── __init__.py                 # Python package initialization
│   ├── main.py                     # Main entry point demonstrating the library
│   └── math.py                     # Math utility functions (add, subtract, multiply, divide)
├── tests/
│   ├── __init__.py                 # Python package initialization
│   └── test_math.py                # Pytest test suite for math functions
├── requirements.txt                # Runtime dependencies
├── requirements-dev.txt            # Development dependencies
├── LICENSE                         # ISC license
└── README.md                       # This file
```

## Scripts & Commands

### Testing

Run the test suite using pytest:

```bash
pytest tests/ -v
```

### Linting

Run Flake8 for basic linting:

```bash
flake8 src tests
```

Run Pylint for detailed code analysis:

```bash
pylint src/
```

### Code Formatting

Check code formatting with Black:

```bash
black --check src tests
```

Format code automatically:

```bash
black src tests
```

### Run All Checks

Run all checks in sequence:

```bash
flake8 src tests && pytest tests/ -v && pylint src/ && black --check src tests
```

## Testing

The project uses **Pytest** for unit testing. The test suite is located in `tests/test_math.py` and covers:

- ➕ Addition functionality
- ➖ Subtraction functionality  
- ✖️ Multiplication functionality
- ➗ Division functionality
- Error handling (dividing by zero)

### Run Tests

```bash
pytest tests/ -v
```

**Example Output:**
```
tests/test_math.py::test_add PASSED                                    [ 20%]
tests/test_math.py::test_subtract PASSED                              [ 40%]
tests/test_math.py::test_multiply PASSED                              [ 60%]
tests/test_math.py::test_divide PASSED                                [ 80%]
tests/test_math.py::test_divide_by_zero PASSED                        [100%]

============================== 5 passed in 0.05s ==============================
```

## Code Quality

The project uses three main tools for code quality:

### Flake8

Checks for PEP 8 compliance and common errors:

```bash
flake8 src tests
```

### Pylint

Provides detailed code analysis and ratings:

```bash
pylint src/
```

### Black

Ensures consistent code formatting:

```bash
black --check src tests  # Check formatting
black src tests          # Auto-format code
```

## CI/CD Pipeline

The GitHub Actions pipeline is configured in `.github/workflows/ci.yml` and provides automated quality assurance.

### Workflow Overview

The pipeline executes on:
- **Triggers**: Push to `main` or `develop` branches, and on pull requests
- **Matrix Testing**: Runs across Python versions 3.9, 3.11, and 3.12

### Pipeline Jobs

#### 1. **Test Job** (ubuntu-latest)
Runs across multiple Python versions:
- ✓ Checkout code
- ✓ Setup Python (3.9, 3.11, 3.12)
- ✓ Install dependencies
- ✓ Run Flake8 linting
- ✓ Run Black formatting check
- ✓ Run Pytest tests

#### 2. **Code Quality Job** (ubuntu-latest)
Additional code quality verification:
- ✓ Checkout code
- ✓ Setup Python (3.11)
- ✓ Install dependencies
- ✓ Run Pylint analysis

#### 3. **Success Notification Job**
Confirms all previous jobs completed successfully:
- ✓ Displays success message if all checks pass

### View Pipeline Results

Pipeline results are available in the **Actions** tab of the GitHub repository. Each commit shows the status of all jobs and detailed logs.

## Contributing

Contributions are welcome! When submitting changes:

1. Create a feature branch from `develop`
2. Ensure all tests pass (`pytest tests/ -v`)
3. Ensure code formatting passes (`black --check src tests`)
4. Ensure linting passes (`flake8 src tests`)
5. Submit a pull request with a clear description
6. The CI/CD pipeline will automatically validate your changes

## License

This project is licensed under the **ISC License**. See the [LICENSE](LICENSE) file for details.
