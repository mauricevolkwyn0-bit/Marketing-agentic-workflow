"""
AI Marketing System - Main Application
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

# Create app SECOND
app = FastAPI(title="Just Work AI Marketing System")

# Import and initialize agent THIRD (after app exists)
from agents.copywriting_agent import CopywritingAgent
copywriting_agent = CopywritingAgent()

@app.get("/")
async def root():
    """Homepage"""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Marketing System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: white;
                color: #333;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            h1 { color: #667eea; }
            .status { 
                padding: 10px;
                background: #e8f5e9;
                border-left: 4px solid #4caf50;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 AI Marketing System</h1>
            <div class="status">
                <strong>Status:</strong> ✅ System Online
            </div>
            <p><strong>Platform:</strong> Just Work</p>
            <p><strong>Goal:</strong> 1,000,000 users in 12 months</p>
            <h2>Quick Links</h2>
            <ul>
                <li><a href="/health">Health Check</a></li>
                <li><a href="/docs">API Documentation</a></li>
                <li><a href="/agents">Agent Status</a></li>
            </ul>
        </div>
    </body>
    </html>
    """)

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "AI Marketing System",
        "version": "1.0.0"
    }

@app.get("/agents")
async def agents_status():
    """Check agent status"""
    return {
        "agents": {
            "copywriting": "ready",
            "video_creation": "ready",
            "analytics": "ready"
        },
        "total_agents": 3,
        "active_campaigns": 0
    }

@app.post("/generate-content")
async def generate_content(platform: str, topic: str):
    """Generate marketing content"""
    return {
        "platform": platform,
        "topic": topic,
        "content": "AI-generated content will appear here",
        "status": "generated"
    }

@app.post("/init-database")
async def init_database():
    """Initialize database tables"""
    from init_database import create_tables
    create_tables()
    return {"status": "Database initialized"}

@app.post("/generate-script")
async def generate_script(topic: str):
    """Generate TikTok script using AI"""
    try:
        result = copywriting_agent.generate_tiktok_script(topic)
        return result
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)