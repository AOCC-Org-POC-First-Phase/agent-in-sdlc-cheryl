"""
Category model for the Tailspin Toys Crowd Funding platform.
This module defines the Category entity with relationships to Games,
including validation and data conversion methods.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key, name):
        """
        Validates the category name field.
        
        Args:
            key (str): The field name being validated
            name (str): The name value to validate
            
        Returns:
            str: The validated name
            
        Raises:
            ValueError: If name is invalid
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key, description):
        """
        Validates the category description field.
        
        Args:
            key (str): The field name being validated
            description (str or None): The description value to validate
            
        Returns:
            str or None: The validated description
            
        Raises:
            ValueError: If description is invalid
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self):
        """
        Returns a string representation of the Category object.
        
        Returns:
            str: A formatted string showing the category name
        """
        return f'<Category {self.name}>'
        
    def to_dict(self):
        """
        Converts the Category object to a dictionary representation.
        
        Returns:
            dict: A dictionary containing category data including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }