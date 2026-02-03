"""Simple Copywriting Agent"""

import os
import openai

class CopywritingAgent:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate_tiktok_script(self, topic: str) -> dict:
        """Generate TikTok video script"""
        
        prompt = f"""
        Create a 30-second TikTok script about: {topic}
        
        Format:
        HOOK (3 seconds): [Attention-grabbing opening]
        VALUE (20 seconds): [Main content]
        CTA (7 seconds): [Call to action]
        
        Make it engaging, casual, and conversion-focused.
        Target audience: People looking for flexible work.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral TikTok scriptwriter."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.8
        )
        
        script = response.choices[0].message.content
        
        return {
            "topic": topic,
            "script": script,
            "platform": "tiktok",
            "estimated_length": "30 seconds"
        }

# Test function
if __name__ == "__main__":
    agent = CopywritingAgent()
    result = agent.generate_tiktok_script("How to find your first freelance client")
    print(result)