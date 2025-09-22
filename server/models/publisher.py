"""
Publisher model for the Tailspin Toys Crowd Funding platform.
This module defines the Publisher entity with relationships to Games,
including validation and data conversion methods.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key, name):
        """
        Validates the publisher name field.
        
        Args:
            key (str): The field name being validated
            name (str): The name value to validate
            
        Returns:
            str: The validated name
            
        Raises:
            ValueError: If name is invalid
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """
        Validates the publisher description field.
        
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
        Returns a string representation of the Publisher object.
        
        Returns:
            str: A formatted string showing the publisher name
        """
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """
        Converts the Publisher object to a dictionary representation.
        
        Returns:
            dict: A dictionary containing publisher data including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }