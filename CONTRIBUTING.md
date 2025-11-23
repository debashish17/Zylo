# Contributing to Zylo

## Development Setup

See [README.md](README.md) for initial setup instructions.

## Project Structure

This is a monorepo managed by Turborepo and pnpm. All packages share dependencies and can import from each other.

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Follow the coding standards:
- TypeScript: Use strict mode, avoid `any`
- React: Use functional components with hooks
- Python: Follow PEP 8, use type hints
- Formatting: Prettier for TS/JS, Black for Python

### 3. Test Your Changes

```bash
# Frontend
cd apps/web
pnpm typecheck
pnpm lint

# Python services
cd services/compliance
python -m pytest  # (when tests are added)
```

### 4. Commit

Use conventional commits:

```bash
git commit -m "feat: add background removal feature"
git commit -m "fix: resolve canvas rendering bug"
git commit -m "docs: update API documentation"
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

## Code Review Process

1. All PRs require at least one approval
2. All checks must pass (lint, typecheck, build)
3. Keep PRs focused and small when possible

## Questions?

Open an issue or reach out to the maintainers.
