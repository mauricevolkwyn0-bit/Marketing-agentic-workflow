"""Initialize database tables"""

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DATABASE_URL = os.getenv("DATABASE_URL")

def create_tables():
    """Create all necessary tables"""
    
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    
    # Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            source VARCHAR(50),
            acquisition_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            cac DECIMAL(10,2),
            activated BOOLEAN DEFAULT FALSE,
            metadata JSONB
        )
    """)
    
    # Content table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS content (
            id SERIAL PRIMARY KEY,
            content_type VARCHAR(50),
            platform VARCHAR(50),
            title TEXT,
            body TEXT,
            status VARCHAR(20) DEFAULT 'draft',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            published_at TIMESTAMP,
            performance_score DECIMAL(5,2),
            metadata JSONB
        )
    """)
    
    # Metrics table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id SERIAL PRIMARY KEY,
            content_id INTEGER REFERENCES content(id),
            metric_date DATE DEFAULT CURRENT_DATE,
            views INTEGER DEFAULT 0,
            engagement_rate DECIMAL(5,4),
            clicks INTEGER DEFAULT 0,
            conversions INTEGER DEFAULT 0
        )
    """)
    
    print("✅ Database tables created successfully!")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()