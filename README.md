# FarmTA - Farm Management App

🚀 **Ứng dụng quản lý trang trại hiện đại** với Backend API Python & Mobile React Native

## ✨ Tính Năng Chính

### 📱 Mobile App (iOS & Android)
- ✅ Quản lý vật nuôi (Animals Management)
- ✅ Theo dõi sức khỏe & tiêm chủng
- ✅ Quản lý lai tạo dòng gà (Chicken Genetics & Lineage)
- ✅ Ấp nở trứng gà thông minh (Smart Hatchery)
- ✅ Quản lý thuốc & vaccine
- ✅ Quản lý chi phí & doanh thu
- ✅ Dashboard analytics
- ✅ Offline Mode (SQLite)
- ✅ Real-time notifications

### 🔧 Backend API
- FastAPI (Python)
- MySQL Database
- Redis Cache
- JWT Authentication
- RESTful API
- WebSocket Support

### 🎨 Features Hiện Đại
- 🎯 AI-powered breeding recommendations
- 📊 Advanced analytics & reporting
- 🧬 Genetic analysis & pedigree tracking
- 💰 Financial management
- 🌤️ Weather integration
- 📡 IoT sensors support
- 👥 Team collaboration
- 🛒 E-commerce integration

## 🏗️ Cấu Trúc Dự Án

```
farmTA-app-mobile/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI entry point
│   │   ├── config.py          # Configuration
│   │   ├── models/            # Database models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── routes/            # API endpoints
│   │   ├── database.py        # Database connection
│   │   ├── auth.py            # Authentication logic
│   │   └── utils.py           # Utility functions
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── mobile/                     # React Native Mobile
│   ├── src/
│   │   ├── screens/
│   │   ├── components/
│   │   ├── services/
│   │   ├── redux/
│   │   └── navigation/
│   ├── app.json
│   └── package.json
│
├── docker-compose.yml
├── .gitignore
└── .env.example
```

## 🚀 Cách Cài Đặt

### Docker Setup (Recommended)
```bash
docker-compose up -d
```

### Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

**Mobile:**
```bash
cd mobile
npm install
expo start
```

## 📚 API Documentation

Base URL: `http://localhost:8000/api/v1`

### Main Endpoints
- `GET/POST /animals` - Animal management
- `GET/POST /hatchery` - Hatchery tracking
- `GET/POST /costs` - Cost management
- `GET/POST /medicines` - Medicine management
- `GET /lineage/{id}` - Pedigree & genetics

## 📝 License

MIT License

---

**Made with ❤️ for farmers worldwide** 🌾
