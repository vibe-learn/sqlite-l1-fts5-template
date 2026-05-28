"""Homework scaffold — sqlite lesson `l1_fts5` (Vibe Learn).

Задача: мини-поисковик по статьям на FTS5: index_article + search (MATCH + ORDER BY rank bm25), сравнение с LIKE.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

SQLite встроена в Python через stdlib `sqlite3` — никакого драйвера ставить
не нужно, сервера нет. БД это файл (DATABASE_PATH) или ":memory:" в тестах.
"""

import os
import sqlite3


def database_path() -> str:
    """Путь к файлу БД из env. Дефолт ":memory:" — БД живёт в процессе."""
    return os.environ.get("DATABASE_PATH", ":memory:")


def connect(path: str | None = None) -> sqlite3.Connection:
    """Открыть соединение sqlite3 (по умолчанию из database_path())."""
    return sqlite3.connect(path if path is not None else database_path())


# ----- TODO #1: ensure_fts -----
def ensure_fts(conn) -> None:
    """создать FTS5 virtual table articles_fts (проверь доступность FTS5 через pragma compile_options / try-except)"""
    raise NotImplementedError("ensure_fts: реализуй меня")


# ----- TODO #2: index_article -----
def index_article(conn, title: str, body: str) -> int:
    """проиндексировать статью, вернуть rowid"""
    raise NotImplementedError("index_article: реализуй меня")


# ----- TODO #3: search -----
def search(conn, query: str, limit: int = 10) -> list[tuple[str, float]]:
    """FTS5 MATCH + ORDER BY rank (bm25); вернуть [(title, score)] по релевантности"""
    raise NotImplementedError("search: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — sqlite lesson scaffold up")
    print(f"DATABASE_PATH: {database_path()} (stdlib sqlite3, no server)")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
