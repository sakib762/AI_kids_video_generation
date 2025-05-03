# 🎬 AI Cartoon Video Generation Project

An AI-powered Django system that automatically **generates cartoon stories + images** and turns them into **animated videos for kids**.

Our goal:  
👉 Use **free APIs** only  
👉 Build a **fully automated system**  
👉 Handle everything from **story writing → image generation → video creation → YouTube upload**.

---

## 📌 **Progress so far**

✅ Django project and app set up  
✅ Integrated **OpenRouter API** (GPT-3.5) for story generation  
✅ Created `/generate-story/` API endpoint  
✅ Tested story generation via **PowerShell API call**  
✅ Configured `.env` to store API keys  
✅ Successfully tested the Django server locally  

---

## 📂 **Project Structure**
ai_kids_video_generation/ # Project root
├── cartoon_project/ # Django project
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── imagegen/ # Django app
│ ├── views.py
│ ├── urls.py
│ └── ...
├── .env # API key storage
├── manage.py
└── README.md

---

## 🛠️ **Technologies Used**

- Python 3.x
- Django
- OpenRouter API (text generation)
- PowerShell / cURL (for testing API calls)
- dotenv (.env file for environment variables)

---

## ⚙️ **How to Run**

### 1️⃣ **Clone the repository**

```bash
git clone <repo-url>
cd ai_kids_video_generation
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install django requests python-dotenv
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxx
python manage.py runserver

Invoke-RestMethod -Uri "http://127.0.0.1:8000/generate-story/" `
  -Method POST `
  -Headers @{"Content-Type" = "application/json"} `
  -Body '{"prompt": "Write a cartoon story about a puppy who dreams of flying."}'
🔗 Available API Endpoints
Method	Endpoint	Description
POST	/generate-story/	Generates a cartoon story based on a prompt

🧭 Our Future Plan
✅ Phase 1 (Completed):

Set up Django + OpenRouter API integration

Successfully generate text stories from prompts

🚧 Phase 2 (In Progress):

Use Replicate (or alternative free API) for cartoon image generation

Generate images for each scene in the story

🎯 Phase 3 (Planned):

Combine AI-generated stories + images into a video

Add background music + text-to-speech (TTS) narration

Export final video automatically

Auto-upload video to YouTube

Add multilingual support (English, Bengali, Hindi)

📝 Notes
Attempted image generation via Replicate API, but ran into free access and permission issues.

Successfully generating stories using OpenRouter GPT-3.5 API.

Exploring alternative free APIs for stable image generation (OpenAI, free Stable Diffusion endpoints, etc.).

🤝 Contributing
This is an experimental and educational project.
Feel free to fork, experiment, and contribute!

📢 Summary
👉 We are building a fully automated AI storytelling → cartoon video → YouTube upload pipeline using free or open APIs wherever possible.

So far, we’ve achieved automated story generation via an API endpoint.
Next step: integrate AI image generation → video rendering → publishing.

📬 Contact
Got a suggestion or want to collaborate? Feel free to reach out!
sakibburrahaman762@gmail.com


