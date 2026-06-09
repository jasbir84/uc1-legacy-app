# Legacy Invoice App

A deliberately buggy Python project for testing automated code refactoring with Managed Agents.

## Structure

```
uc1-legacy-app/
├── src/
│   ├── __init__.py
│   ├── utils.py        ← Utility functions (has bugs)
│   └── models.py       ← Data models (has bugs)
├── tests/
│   ├── __init__.py
│   ├── test_utils.py   ← 6 tests (some will fail)
│   └── test_models.py  ← 4 tests (some will fail)
└── requirements.txt
```

## Known Bugs (for the agent to find and fix)

There are **3 root-cause bugs** across the codebase (causing 6 test failures):

1. **`utils.py`** — `calculate_total()` does arithmetic on a string `tax_rate` without converting to float
2. **`utils.py`** — `normalize_name()` crashes on `None` input (no null check)
3. **`models.py`** — `Invoice.summary()` references `self.total` (method object) instead of `self.total()` (method call)

## Running Tests

```bash
pip install -r requirements.txt
pytest -v
```

Expected: **10 tests, 6 failures** before fixes, **10 tests, 0 failures** after.
