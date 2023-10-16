# from sqlite3 import connect
#
# conn = connect("db.sqlite3")
# cur = conn.cursor()
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS categories(
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        name VARCHAR (32) NOT NULL UNIQUE,
#        is_published BOOLEAN DEFAULT (false)
#     );
# """
# )
# conn.commit()
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS products(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         category_id INTEGER NOT NULL,
#         name VARCHAR(128) NOT NULL,
#         descr TEXT,
#         price DECIMAL (8, 2) NOT NULL CHECK ( price > 0 ),
#         FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT
#     );
# """
# )
# conn.commit()
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS orders(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         date_created DATETIME NOT NULL,
#         is_payed BOOLEAN DEFAULT (false)
#     );
# """
# )
# conn.commit()
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS order_items(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         product_id INTEGER NOT NULL,
#         order_id INTEGER NOT NULL,
#         FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE NO ACTION,
#         FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
#     );
# """
# )
# conn.commit()
# # cur.execute(
# #     """
# #     CREATE INDEX category_id_index ON products(category_id);
# # """
# # )
# # conn.commit()
#
# # data = {"name": "PC", "is_published": True}
# # cur.execute(
# #     """
# #     INSERT INTO categories (name, is_published) VALUES (:name, :is_published);
# # """,
# #     data,
# # )
# # conn.commit()
#
# # cur.executemany(
# #     """
# #     INSERT INTO products (category_id, name, descr, price)
# #     VALUES (:category_id, :name, :descr, :price);
# # """,
# #     [
# #         {"name": "Redmi", "descr": "Xiaomi", "category_id": 2, "price": 1100},
# #         {"name": "JBL", "descr": "JBL Headphones", "category_id": 4, "price": 500},
# #     ],
# # )
# # conn.commit()
#
#
# # cur.execute(
# #     """
# #     UPDATE categories SET is_published = ?
# #     WHERE name LIKE '%Mobile%';
# # """,
# #     (False, "USB"),
# # )
# # conn.commit()
# # cur.execute(
# #     """
# #     DELETE FROM categories WHERE name = ?;
# # """,
# #     ("USB",),
# # )
# # conn.commit()
#
#
# # cur.execute(
# #     """
# #         SELECT name, price FROM products WHERE category_id = ? ORDER BY price;
# #     """,
# #     (4,),
# # )
# # print(cur.fetchall())
#
# # cur.execute(
# #     """
# #     SELECT categories.name, products.name, products.price FROM categories
# #     JOIN products ON categories.id = products.category_id
# #     ORDER BY categories.name;
# # """
# # )
# # print(cur.fetchall())
# # cur.execute(
# #     """
# #     SELECT MAX (products.price)
# #     FROM products
# #     JOIN categories
# #     ON products.category_id = categories.id
# #     WHERE categories.is_published = ?;
# # """,
# #     (True,),
# # )
# # print(cur.fetchall())
#
#
# # cur.execute(
# #     """
# #     SELECT products.name, CONCAT (products.name, ': ', products.price)
# #     FROM products;
# # """
# # )
# # print(cur.fetchall())
#
# # with open("categories.csv", "r", encoding="utf-8") as file:
# #     r = DictReader(file)
# #     cur.executemany(
# #         """
# #         INSERT INTO categories (name)
# #         VALUES (:name);
# #         """,
# #         [*r],
# #     )
# #     conn.commit()
#
#
# # cur.execute("select id, name, is_published from categories;")
# # with open("categories_dump.csv", "w", encoding="utf-8") as file:
# #     w = writer(file)
# #     w.writerow(["id", "name", "is_published"])
# #     w.writerows(cur.fetchall())
#
#
from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    CheckConstraint,
    DECIMAL,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


# SQLAlchemy < 2
# Base = declarative_base()


class Base(DeclarativeBase):
    id = Column(INT, autoincrement=True, primary_key=True)

    # @declared_attr.directive
    # def __tablename__(cls):
    #     return (
    #         "".join(f"_{i.lower()}" if i.isupper() else i for i in cls.__name__).strip(
    #             "_"
    #         )
    #     )


class Category(Base):
    __tablename__ = "categories"
    # __table_args__ = (CheckConstraint("char_length(name) >= 4"),)

    if TYPE_CHECKING:
        id: int
        name: str
        is_published: bool
        products: list["Product"]
    else:
        name = Column(VARCHAR(32), nullable=False, unique=True)
        is_published = Column(BOOLEAN, default=False, nullable=False)

        products = relationship(argument="Product", back_populates="category")

    def __str__(self) -> str:
        return self.name


class Product(Base):
    __tablename__ = "products"
    __table_args = (CheckConstraint("price > 0"),)

    name = Column(VARCHAR(128), nullable=False)
    price = Column(DECIMAL(precision=8, scale=2), nullable=False)
    category_id = Column(
        INT,
        ForeignKey(column="categories.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    category = relationship(argument=Category, back_populates="products")


engine = create_engine("sqlite:///db2.sqlite3")
session = sessionmaker(bind=engine)
# Base.metadata.create_all(bind=engine)
# with session() as s:
# cat1 = Category(name="Coffee")
# cat2 = Category(name="Tea")
# s.add_all([cat1, cat2])
# s.commit()
# prod1 = Product(name="Latte", price=5, category_id=1)
# prod2 = Product(name="Cappuccino", price=4.5, category_id=1)
# s.add_all([prod1, prod2])
# s.commit()
# cat = s.get(Product, 1)
# print(cat.category)
