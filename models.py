from typing import TYPE_CHECKING, Optional

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    BOOLEAN,
    CheckConstraint,
    DECIMAL,
    ForeignKey,
    create_engine,
    delete,
    select,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    id = Column(INT, autoincrement=True, primary_key=True)

    # def model_dump(self):
    #     data = self.__dict__
    #     data.pop("_sa_instance_state", None)
    #     return data


class Category(Base):
    __tablename__ = "categories"

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
    is_published = Column(BOOLEAN, default=False, nullable=False)

    category = relationship(argument=Category, back_populates="products")


engine = create_engine("sqlite:///db.sqlite3")
session = sessionmaker(bind=engine)

# with session() as s:
#     category = Category(name="Coffee")
#     s.add(category)
#     s.commit()

# with session() as s:
    # objs = (
    #     s.query(Category, Product)
    #     .join(Product)
    #     .filter(Product.is_published == True)
    #     .order_by(Product.price.desc())
    # ).all()
    # print(objs)
    # objs = s.execute(
    #     select(Category, Product)
    #     .join(Product)
    #     .filter(Product.is_published == True)
    #     .order_by(Product.price.desc())
    #     # .slice(1, 3)
    # ).all()
    # for category, product in objs:
    #     print(category.name, product.name, product.price)
    # prod1 = Product(name="Latte", price=4.5, is_published=True, category_id=1)
    # prod2 = Product(name="Cappuccino", price=4.5, is_published=False, category_id=1)
    # s.add_all((prod1, prod2))
    # s.commit()
    # prod3 = Product(name="Hot Coffee", price=4, is_published=True, category_id=1)
    # s.add(prod3)
    # s.commit()
    # print(prod3.id)
    # s.refresh(prod3)
    # print(prod3.id)
    # obj = s.get(Category, ident=1, options=[selectinload(Category.products)])
    # print(obj)
    # objs = s.scalars(select(Category).options(selectinload(Category.products))).one()
    # objs = s.execute(select(Category, Product).join(Product, isouter=True)).all()
    # print(objs)
    # print(objs.products)
    # objs = (
    #     s.query(Category)
    #     .filter(or_(Category.id > 2, Category.id < 5))
    #     .order_by(Category.name.desc())
    #     .all()
    # )
    # print(objs)
    # c = s.scalar(
    #     select(count(Product.id)).where(
    #         and_(Product.category_id == 1, Product.is_published == True)
    #     )
    # )
    # select count (products.id) where category_id = 1 and is_published = 1;
    # print(c)
    # p = s.get(Product, 4)
    # p.name = "Ice Latte"
    # s.commit()
    # update product set is_published = 0 where id = 4;
    # s.execute(
    #     update(Product).values(is_published=False).filter(Product.name.like("%Latte%"))
    # )
    # s.commit()
    # objs = s.scalars(select(Product).filter(Product.name.contains("tte"))).all()
    # print(objs)
    # p = s.get(Product, 4)
    # s.delete(p)
    # s.commit()
    # s.execute(
    #     delete(Product)
    #     .filter_by(id=4)
    # )
    # s.commit()


from pydantic import BaseModel, Field, PositiveInt, field_validator
from decimal import Decimal


class ProductDetail(BaseModel):
    id: PositiveInt
    is_published: bool
    name: str = Field(max_length=128)
    price: Decimal = Field(max_digits=8, decimal_places=2)
    category_id: PositiveInt


class CategoryRegisterForm(BaseModel):
    name: str = Field(default=..., max_length=32)

    # @field_validator("name", mode="after")
    # def name_unique_validator(cls, name: str) -> str:
    #     with session() as s:
    #         obj = s.scalar(select(Category).filter_by(name=name))
    #         if obj is None:
    #             return name
    #         raise ValueError("name is not unique")


class CategoryDetail(CategoryRegisterForm):
    id: PositiveInt
    is_published: bool
    products: Optional[list[ProductDetail]] = Field(default=None)


# with session() as s:
#     cat = s.get(Category, 2)
#     schema = CategoryDetail.model_validate(cat, from_attributes=True)
#     print(schema.model_dump_json(indent=2))


# data = {
#     "name": "TV"
# }
# schema = CategoryRegisterForm(**data)
# ...
# with session() as s:
#     new_category = Category(**schema.model_dump())
#     s.add(new_category)
#     try:
#         s.commit()
#     except IntegrityError:
#         response = {"error": "name is not unique"}
#     else:
#         response = CategoryDetail.model_validate(new_category, from_attributes=True)
#     finally:
#         print(response)
