
# PayLink - AI Prompt Log

This document records how AI tools were used during Phase 1
of the PayLink project.

## Entry 1 - FastAPI Application Setup

**Initial Prompt:**

Create a simple FastAPI application for the PayLink project
with a home endpoint and a health check endpoint.

**Result:**

The AI generated a basic FastAPI application using Python.

**Evaluation:**

The response was correct and suitable for the initial project setup.

---

## Entry 2 - Docker Configuration

**Initial Prompt:**

Create a Dockerfile and Docker Compose configuration
for a Python FastAPI application with a PostgreSQL database.

**Result:**

The AI generated a Dockerfile and a Compose configuration
containing two services: API and PostgreSQL.

**Evaluation:**

The configuration was tested by running Docker Compose.
The application started successfully.

---

## Entry 3 - GitHub Actions CI Workflow

**Initial Prompt:**

Create a GitHub Actions workflow to build, lint,
and test a FastAPI application.

**Initial AI Response Issue:**

The first response did not clearly specify the required
project structure and dependency installation steps.

**Improved Prompt:**

Create a complete GitHub Actions CI workflow for a Python 3.12
FastAPI project. The workflow must check out the repository,
install dependencies from requirements.txt, run Ruff,
execute Pytest, and build the Docker image.

**Final Result:**

The improved workflow successfully ran on both push
and pull_request events.

**Evaluation:**

The workflow passed successfully on GitHub Actions.

---

## Entry 4 - Python Code Linting

**Initial Prompt:**

Check the Python test file for code quality issues.

**Initial AI Response Issue:**

The initial response did not explain the exact Ruff
import sorting error or how to fix it automatically.

**Improved Prompt:**

Explain the Ruff I001 import sorting error in test_main.py
and provide the exact command to automatically fix it.
Then provide a command to verify that the issue is resolved.

**Final Result:**

The command `ruff check app test_main.py --fix`
successfully fixed the import formatting issue.

**Evaluation:**

Ruff reported that all checks passed after the correction.

---

## Entry 5 - Automated Testing

**Initial Prompt:**

Write tests for the PayLink FastAPI application.

**Result:**

The AI generated tests for the home endpoint
and the health check endpoint using FastAPI TestClient.

**Evaluation:**

Both tests passed successfully using Pytest.

---

## Conclusion

AI tools were used to support application setup,
Docker configuration, CI automation, linting,
and automated testing.

All generated configurations and code were reviewed
and tested before being included in the project.
