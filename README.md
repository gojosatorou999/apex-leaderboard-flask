# Apex Leaderboard System

A high-performance Flask based leaderboard system for storing and ranking player scores with a premium, glassmorphic UI.

## 🚀 Features

- **Store & Rank Scores**: Persistent SQLite database to track player performance.
- **Real-time Updates**: Fetches and displays the top 10 players dynamically.
- **Premium Design**: Modern dark-mode interface with smooth animations and tie-breaking logic.

## 📊 Ranking Logic

The ranking system is designed to be fair and competitive using the following rules:

1. **Primary Metric (Score Descending)**: Players are primarily ranked by their total score. Higher scores always rank higher.
2. **Tie-Breaking (Timestamp Ascending)**: In the event of a tie (two players having the exact same score), the **first player to achieve that score** holds the higher rank. This rewards early achievement and consistency.
3. **Capacity**: The UI displays the Top 10 global leaders, while the database maintains the full history.

## 🛠️ Setup

1. **Install Dependencies**:
   ```bash
   pip install flask flask-sqlalchemy
   ```

2. **Run the Server**:
   ```bash
   python app.py
   ```

3. **Access**:
   Open `http://127.0.0.1:5000` in your browser.

## 📡 API Endpoints

- `GET /api/scores`: Returns the top 10 ranked players.
- `POST /api/scores`: Submit a new score (JSON body: `{"username": "name", "score": 100}`).

---
*Built with Flask & SQLite*
