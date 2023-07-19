import streamlit as st
from db import sessionmaker, MenuItem, create_engine
import pandas as pd

engine = create_engine('sqlite:///data.sqlite')

def open_db():
    Session = sessionmaker(bind=engine)
    return Session()

def add_item(name, price, qty, category, cuisine):
    db = open_db()
    item = MenuItem(name=name, price=price, qty=qty, category=category, cuisine=cuisine)
    db.add(item)
    db.commit()
    db.close()

st.title("Database app")
t1, t2 = st.tabs(['Add Item', 'View Items'])

t1.subheader("Add Item")
f1 = t1.form("add_item")
name = f1.text_input("Name")
price = f1.number_input("Price", min_value=0.0, step=0.5)
qty = f1.text_input("Quantity")
category = f1.text_input("Category")
cuisine = f1.text_input("Cuisine")
submit = f1.form_submit_button("Add Item")

if submit:
    add_item(name, price, qty, category, cuisine)
    t1.success("Item added successfully")
    

t2.subheader("View Items")
df = pd.read_sql("select * from menu_items", engine)
t2.dataframe(df, use_container_width=True)

query = st.text_input("Enter query")
if query:
    db = open_db()
    result = db.query(MenuItem).filter(MenuItem.name.like(f'%{query}%')).all()
    if result:
        for item in result:
            st.write(f'{item.name} {item.price} {item.qty} {item.category} {item.cuisine}')
    else:
        st.error("No results found")



# streamlit run crudapp.py

    
