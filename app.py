from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self, rank):
        return {
            'rank': rank,
            'username': self.username,
            'score': self.score,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scores', methods=['GET'])
def get_scores():
    # Ranking Logic: 
    # 1. Primary: Score descending
    # 2. Secondary: Timestamp ascending (first to achieve the score wins ties)
    scores_query = Score.query.order_by(Score.score.desc(), Score.timestamp.asc()).limit(10).all()
    leaderboard = [s.to_dict(i + 1) for i, s in enumerate(scores_query)]
    return jsonify(leaderboard)

@app.route('/api/scores', methods=['POST'])
def submit_score():
    data = request.get_json()
    if not data or 'username' not in data or 'score' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_score = Score(username=data['username'], score=int(data['score']))
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'message': 'Score submitted successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
