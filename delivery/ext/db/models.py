from delivery.ext.db import db

# To understand what is happening here:
# We have 7 tables (Category, Store, Items, Order, Order_Items, Checkout and Address),
# with each one containing it's attributes (columns).

### User table is alocate in the auth directory for best management.

# primary_key=True to set this column as the table's primary key. 

# unique=True do not allow duplicate values in this column.

# ForeignKey represents a relationship between two tables (one-to-many relationship),
# db.relationship() represents the object-oriented view of that realtionship
# Example: the primary key in Category will work as the "one" side, we will have an id for each category
# and in Store the db.relationship() will work as the "many" side,
# so if you look in the category_id there will be many stores for each id
# but in a Store there will be only one category_id that represents the store.




class Category(db.Model):
    __tablename__ = "category"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)
    on_menu = db.Column("on_menu", db.Boolean)


class Store(db.Model):
    __tablename__ = "store"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id")
    )
    activity = db.Column("activity", db.Boolean)

    user = db.relationship("User", foreign_keys=user_id)
    category = db.relationship("Category", foreign_keys=category_id)


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    image = db.Column("image", db.Unicode)
    price = db.Column("price", db.Numeric)
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))
    available = db.Column("available", db.Boolean)

    store = db.relationship("Store", foreign_keys=store_id)


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))
    address_id = db.Column(
        "address_id", db.Integer, db.ForeignKey("address.id")
    )

    user = db.relationship("User", foreign_keys=user_id)
    store = db.relationship("Store", foreign_keys=store_id)
    address = db.relationship("Address", foreign_keys=address_id)


class OrderItems(db.Model):
    __tablename__ = "order_items"
    id = db.Column("id", db.Integer, primary_key=True)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    items_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))
    quant = db.Column("quant", db.Integer)

    order = db.relationship("Order", foreign_keys=order_id)
    items = db.relationship("Items", foreign_keys=items_id)


class Checkout(db.Model):
    __tablename__ = "check_out"
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    order = db.relationship("Order", foreign_keys=order_id)


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zip", db.Unicode)
    country = db.Column("country", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", foreign_keys=user_id)

