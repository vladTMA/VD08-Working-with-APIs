## **📘 Project: Working with APIs

Quotes • Weather • Accounts • Leaflet Map • Docker Deploy

A multifunctional Flask web application combining API integrations, modern UI, user accounts, and Docker‑based deployment preparation.
The project serves as a practical learning platform for mastering Flask architecture, API usage, UI/UX, and server‑side infrastructure.

---

### **Quotes**
- 📜 Random quotes (ZenQuotes API)  
- 🌐 Automatic translation (MyMemory API)
- 🔤 Smart author transliteration
- 📚 Dictionary of 200+ authors with correct Russian transliterations 
- 📝 Logging of unknown authors   
- 🗂 Quote history (localStorage + server archive)
    - localStorage (user history)
    - `quotes_archive.txt` (server archive)
-  Buttons:
   - Copy  
   - Speak EN  
   - Speak RU  
   - Show another quote   
- 🎨 Responsive UI with animations

---

### **Weather**
- Weather search by city  
- Automatic translation of weather descriptions into Russian  
- Sunrise/sunset in:
  - UTC  
  - Moscow  
  - local city time 
- 🌅 Day length calculation
- 🗺 Map display (Leaflet)
- Weather icons  

---

### **User System**
- Registration  
- Login  
- Profile editing  
- Avatar upload  
- Password hashing (bcrypt)  

---

## 🛠 **Tech Stack**

- Python 3  
- Flask  
- Flask‑Login  
- SQLAlchemy  
- Bootstrap 5  
- Leaflet  
- MyMemory API  
- ZenQuotes API  
- OpenWeather API  

---

## 🐳 Docker & Deployment Preparation

The project includes a full set of configuration files for running the application in Docker containers:

- Dockerfile — application image build
- docker-compose.yml — base configuration
- docker-compose.dev.yml — development environment
- docker-compose.prod.yml — production environment
- gunicorn.conf.py — Gunicorn configuration
- deploy/nginx/nginx.conf — Nginx configuration
- deploy/certs/ — SSL certificate structure

These files are used for educational purposes to demonstrate how to prepare a Flask application for deployment on a VPS or cloud server.

---

## 📦 **Installation (Local Run)**

```bash
git clone <repo_url>
cd <project_folder>

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

---

## 📁 **Project Structure**

```
VD08-Working-with-APIs/
│
├── app/
│   ├── data/
│   │   └── quotes_archive.txt
│   ├── static/
│   │   ├── avatars/
│   │   │   └── default.png
│   │   ├── icons/
│   │   │   ├── sunrise.jfif
│   │   │   └── sunset.jfif
│   │   ├── snow.js
│   │   └── style.css
│   ├── templates/
│   │   ├── account.html
│   │   ├── base.html
│   │   ├── edit_profile.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── quotes.html
│   │   ├── quotes_history.html
│   │   ├── register.html
│   │   └── weather.html
│   ├── authors.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── translit.py
│   ├── utils.py
│   └── __init__.py
│
├── deploy/
│   ├── certs/
│   ├── certs-data/
│   └── nginx/
│       ├── logs/
│       └── nginx.conf
│
├── instance/
│   └── site.db
│
├── screenshots/
│   ├── account.png
│   ├── edit_profile.png
│   ├── history.png
│   ├── home.png
│   ├── quotes.png
│   └── weather.png
│
├── .env
├── .gitattributes
├── .gitignore
├── config.py
├── create_db.py
├── docker-compose.yml
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── Dockerfile
├── gunicorn.conf.py
├── LICENSE
├── main.py
├── missing_authors.log
├── README.md
├── READMEru.md
├── READMEen.md
└── requirements.txt

```

---

## 🔧 **Implementation Details**

- Smart transliteration of author names  
- Exceptions for service words: *de, van, von, da, di…*  
- Logging unknown authors  
- Server‑side quote archive  
- Browser quote history  
- Flip‑card animations  
- Snowflake background  
- Responsive design  

---

## 📸 Screenshots

<table>
  <tr>
    <td align="center">
      <img src="screenshots/home.png" alt="Home Page" style="width: 100%; max-width: 450px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
      <div style="margin-top: 8px; font-weight: bold;">Home Page</div>
    </td>
    <td align="center">
      <img src="screenshots/quotes.png" alt="Quotes" style="width: 100%; max-width: 450px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
      <div style="margin-top: 8px; font-weight: bold;">Quotes Page</div>
    </td>
  </tr>

  <tr>
    <td align="center">
      <img src="screenshots/history.png" alt="History" style="width: 100%; max-width: 450px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
      <div style="margin-top: 8px; font-weight: bold;">Quote History</div>
    </td>
    <td align="center">
      <img src="screenshots/weather.png" alt="Weather" style="width: 100%; max-width: 450px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
      <div style="margin-top: 8px; font-weight: bold;">Weather</div>
    </td>
  </tr>

  <tr>
    <td align="center">
      <img src="screenshots/account.png" alt="Account" style="width: 100%; max-width: 450px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
      <div style="margin-top: 8px; font-weight: bold;">User Profile</div>
    </td>
    <td align="center">
      <img src="screenshots/edit_profile.png" alt="Edit Profile" style="width: 100%; max-width: 450px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
      <div style="margin-top: 8px; font-weight: bold;">Edit Profile</div>
    </td>
  </tr>
</table>

---

## 📌 **Roadmap**

- Export quotes to CSV
- View server‑side archive
- Dark theme
- Enhanced card animations
- Automatic author dictionary expansion
- Full deployment (Docker + Gunicorn + Nginx) 

---

## 📄 License
MIT License (or any other license of your choice)

---

## 👤 Author
Developed as part of a learning project focused on API integration, Flask architecture, and modern UI.

---

**Vladimir**  
📧 vladtma@tutamail.com

```
