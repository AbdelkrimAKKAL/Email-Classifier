
Ensure these are set in your production environment (e.g., Render Dashboard):

- `HUGGINGFACE_API_KEY`: Required for smart reply generation.
- `GMAIL_CREDENTIALS_FILE`: Path to your `credentials.json`.
- `GMAIL_TOKEN_FILE`: Path to your `token.json`.
- `DATABASE_URL`: Set to a persistent disk or PostgreSQL URL if not using local SQLite.

## 🧪 The Complete CI/CD Pipeline

This project demonstrates a fully professional pipeline separating unit tests from integration tests.

### 1. Isolated Unit Tests (Fast & Free)
We mock the Hugging Face AI to test our FastAPI logic instantly without needing internet access or API tokens.
```bash
pytest tests/test_unit.py
```

### 2. Live Integration Tests (End-to-End)
We test the exact live workflow by sending requests to the Hugging Face Inference API. Requires `.env`.
```bash
pytest tests/test_integration.py
```

### 3. Containerized CI/CD Deployments
The `.github/workflows/ci-cd.yml` runs both of these test suites sequentially. If they pass, it builds your `Dockerfile` and pushes the container to Docker Hub, creating a seamless rollout system!

To run all tests dynamically via Docker locally:
```bash
docker-compose --profile test up --build
```


## License

MIT
