from app import app, db
from models import Url

def seed_urls():
    # List of initial URLs to seed into the database
    urls = [
        {
            "original_url": "https://www.example.com",
            "short_url": "exmpl1"
        },
        {
            "original_url": "https://www.google.com",
            "short_url": "goog1"
        },
        {
            "original_url": "https://www.github.com",
            "short_url": "gith2"
        },
        {
            "original_url": "https://www.openai.com",
            "short_url": "git2"
        }
    ]
    
    # Create instances of Url and add them to the session
    for url_data in urls:
        url = Url(
            original_url=url_data['original_url'],
            short_url=url_data['short_url']
        )
        db.session.add(url)

    # Commit the session to save the URLs to the database
    db.session.commit()
    print("Database seeded!")

if __name__ == "__main__":
    with app.app_context():
        # Create the tables if they don't exist
        db.create_all()
        
        # Seed the database
        seed_urls()
