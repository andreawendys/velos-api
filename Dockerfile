# ---------- Etage 1 : construction ----------
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Etage 2 : tests (construit uniquement avec --target test) ----------
FROM python:3.12-slim AS test
WORKDIR /app
COPY --from=builder /install /usr/local
RUN pip install --no-cache-dir pytest
COPY app.py .
COPY tests/ tests/
RUN python -m pytest -q

# ---------- Etage 3 : image finale ----------
FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 1001 appli
COPY --from=builder /install /usr/local
COPY app.py .
COPY db/ db/
ENV PORT=8000
EXPOSE 8000
USER appli
CMD ["python", "app.py"]
