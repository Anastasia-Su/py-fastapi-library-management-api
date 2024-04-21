from datetime import date, datetime

from sqlalchemy.orm import Session, joinedload

from db.database import SessionLocal
from db.models import DbAuthor, DbBook
from schemas import Author, AuthorCreate, Book, BookCreate


def get_author_list(db: Session):
    return db.query(DbAuthor).all()


def get_author_detail(db: Session, author_id: int):
    return db.query(DbAuthor).get(author_id)


def get_author_by_name(db: Session, name: str):
    return (
        db.query(DbAuthor).filter(DbAuthor.name == name).first()
    )


def create_author(db: Session, author: AuthorCreate):
    db_author = DbAuthor(
        name=author.name,
        bio=author.bio,
        books=author.books,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_book_list(
    db: Session,
    author: str | None = None,
):
    queryset = db.query(DbBook)

    if author is not None:
        queryset = queryset.filter(DbBook.author.has(name=author))

    return queryset.all()


def get_book_detail(db: Session, book_id: int):
    return db.query(DbBook).get(book_id)


def create_book(db: Session, book: BookCreate):
    db_book = DbBook(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

