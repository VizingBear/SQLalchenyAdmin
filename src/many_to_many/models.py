from sqlalchemy import ForeignKey, Column, Table, Integer, Date, String, Text
from sqlalchemy.orm import relationship

from src.database import Base

AssociationTable = Table(
    "association_table",
    Base.metadata,
    Column('itemId', Integer, ForeignKey('Employee.id')),
    Column('detailId', Integer, ForeignKey('Task.id')),
    Column('endDate', Date))


class Employee(Base):
    __tablename__ = 'Employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    task = relationship('Task', secondary=AssociationTable, backref='Employee')


class Task(Base):
    __tablename__ = 'Task'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    employee = relationship('Employee', secondary=AssociationTable, backref='Task')
