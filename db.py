from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.exc import IntegrityError

# Create engine
engine = create_engine('sqlite:///data.sqlite')
Base = declarative_base()

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    qty = Column(String(50), default='1 serving')
    category = Column(String(50), default='Main Course')
    cuisine = Column(String(50), default='Indian')

    def __str__(self):
        return f"{self.name} {self.price:}"
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)