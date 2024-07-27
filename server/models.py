from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Integer, String, DateTime
from sqlalchemy.orm import validates
import pytz
from datetime import datetime
import re

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Url(db.Model):
    __tablename__ = "Url"

    id = db.Column(Integer, primary_key=True)
    original_url = db.Column(String(500))
    short_url = db.Column(String(10), unique=True)
    created_at = db.Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.timezone('Africa/Nairobi')))

    @validates('original_url')
    def validate_original_url(self, key, value):
        if not value:
            raise ValueError("Original URL cannot be empty.")
        
        # Validate URL format (basic validation)
        url_regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
            r'localhost|' # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if not re.match(url_regex, value):
            raise ValueError("Original URL is not valid.")
        
        return value

    @validates('short_url')
    def validate_short_url(self, key, value):
        if not value:
            raise ValueError("Short URL cannot be empty.")
        
        if len(value) >= 10:
            raise ValueError("Short URL must be less than 10 characters long.")

        # Check for uniqueness in the database
        if Url.query.filter_by(short_url=value).first() is not None:
            raise ValueError(f"Short URL '{value}' is already taken.")
        
        return value
