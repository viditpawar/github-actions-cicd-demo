# GitHub Actions CI/CD Demo

A demonstration project showcasing a complete CI/CD pipeline implementation using GitHub Actions for automated linting, testing, build, and deployment workflows.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Scripts](#scripts)
- [Testing](#testing)
- [Linting](#linting)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project demonstrates a professional CI/CD setup using GitHub Actions. It includes a simple math utility library with comprehensive test coverage, linting, and automated workflows that run on every push and pull request.

The pipeline is designed to:
- Automatically test code across multiple Node.js versions
- Enforce code quality standards with ESLint
- Build and validate the application
- Report results back to GitHub

## Features

✅ **Multi-version Testing** - Tests run on Node.js 18.x, 20.x, and 22.x  
✅ **Automated Linting** - ESLint configuration for code quality  
✅ **Comprehensive Testing** - Jest test suite with multiple test cases  
✅ **Build Pipeline** - Automated build process  
✅ **GitHub Actions Integration** - Automated CI/CD on push and pull requests  
✅ **Code Quality Checks** - Dedicated code quality job in the pipeline  

## Prerequisites

- **Node.js** - Version 18.x or higher
- **npm** - Version 8 or higher
- **Git** - For cloning and version control

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/viditpawar/github-actions-cicd-demo.git
   cd github-actions-cicd-demo
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

## Usage

### Running the Application

Execute the main application:

```bash
node src/index.js
```

**Expected Output:**
```
CI/CD Demo Application
Addition result: 15
Subtraction result: 5
Multiplication result: 50
Division result: 2
```

### Using the Math Library

Import and use the math utilities in your own code:

```javascript
const { add, subtract, multiply, divide } = require("./src/math");

console.log(add(10, 5));        // 15
console.log(subtract(10, 5));   // 5
console.log(multiply(10, 5));   // 50
console.log(divide(10, 5));     // 2
```

## Project Structure

```
github-actions-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD workflow
├── src/
│   ├── index.js                # Main entry point demonstrating the library
│   └── math.js                 # Math utility functions (add, subtract, multiply, divide)
├── tests/
│   └── math.test.js            # Jest test suite for math functions
├── .eslintrc.json              # ESLint configuration
├── jest.config.js              # Jest testing framework configuration
├── package.json                # Project metadata and dependencies
├── LICENSE                      # ISC license
└── README.md                    # This file
```

## Scripts

The following npm scripts are available:

| Script | Description |
|--------|-------------|
| `npm test` | Run Jest test suite |
| `npm run lint` | Run ESLint to check code quality |
| `npm run build` | Build the project |

## Testing

The project uses **Jest** for unit testing. The test suite is located in `tests/math.test.js` and covers:

- ➕ Addition functionality
- ➖ Subtraction functionality  
- ✖️ Multiplication functionality
- ➗ Division functionality
- Error handling (dividing by zero)

### Run Tests

```bash
npm test
```

**Example Output:**
```
PASS  tests/math.test.js
  ✓ adds two numbers correctly (2 ms)
  ✓ subtracts two numbers correctly (1 ms)
  ✓ multiplies two numbers correctly (1 ms)
  ✓ divides two numbers correctly (1 ms)
  ✓ throws error when dividing by zero (1 ms)

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
```

## Linting

The project uses **ESLint** to maintain consistent code quality and style.

### Run Linting

```bash
npm run lint
```

ESLint configuration is defined in `.eslintrc.json` and applied to:
- Source files in `src/`
- Test files in `tests/`

## CI/CD Pipeline

The GitHub Actions pipeline is configured in `.github/workflows/ci.yml` and provides automated quality assurance.

### Workflow Overview

The pipeline executes on:
- **Triggers**: Push to `main` or `develop` branches, and on pull requests
- **Matrix Testing**: Runs across Node.js versions 18.x, 20.x, and 22.x

### Pipeline Jobs

#### 1. **Test Job** (ubuntu-latest)
Runs across multiple Node.js versions:
- ✓ Checkout code
- ✓ Setup Node.js (18.x, 20.x, 22.x)
- ✓ Install dependencies
- ✓ Run ESLint
- ✓ Run Jest tests
- ✓ Build project

#### 2. **Code Quality Job** (ubuntu-latest)
Additional code quality verification:
- ✓ Checkout code
- ✓ Setup Node.js (18.x)
- ✓ Install dependencies
- ✓ Run ESLint checks

#### 3. **Success Notification Job**
Confirms all previous jobs completed successfully:
- ✓ Displays success message if all checks pass

### View Pipeline Results

Pipeline results are available in the **Actions** tab of the GitHub repository. Each commit shows the status of all jobs and detailed logs.

## Contributing

Contributions are welcome! When submitting changes:

1. Create a feature branch from `develop`
2. Ensure all tests pass (`npm test`)
3. Ensure linting passes (`npm run lint`)
4. Submit a pull request with a clear description
5. The CI/CD pipeline will automatically validate your changes

## License

This project is licensed under the **ISC License**. See the [LICENSE](LICENSE) file for details.
