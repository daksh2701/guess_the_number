# 🎯 Guess the Number Game

A modern, interactive number guessing game built with Streamlit featuring beautiful animations, difficulty levels, smart hints, and comprehensive statistics tracking. Challenge your intuition and logical thinking in this classic guessing game with a professional twist!

![Guess the Number](https://img.shields.io/badge/Game-Number%20Guessing-blue)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.7%2B-green)
![Interactive](https://img.shields.io/badge/Interface-Interactive-orange)

## 🌟 Features

### 🎮 Core Gameplay
- **🎯 Mystery Number**: Computer generates a random number between 1-100
- **🟢 Easy Mode**: 10 attempts to guess the correct number
- **🔴 Hard Mode**: 5 attempts for the ultimate challenge
- **💡 Smart Hints**: "Too High" or "Too Low" feedback with visual indicators
- **🏆 Win/Loss Tracking**: Complete game outcome management

### 🎨 Visual Experience
- **🎭 ASCII Art Logo**: Eye-catching retro-style game logo
- **🌈 Gradient Design**: Modern purple-blue color scheme
- **✨ Smooth Animations**: Bounce, pulse, shake, and celebration effects
- **📱 Responsive Layout**: Perfect on desktop, tablet, and mobile
- **🎪 Victory Celebrations**: Balloons and animations for successful guesses

### 🧠 Smart Features
- **📊 Intelligent Range Display**: Shows optimal guessing range based on previous attempts
- **📜 Guess History**: Complete log of all attempts with timestamps
- **📈 Performance Statistics**: Win rate, best scores, and game analytics
- **🎯 Strategic Hints**: Visual feedback guides your next move
- **⏱️ Real-time Updates**: Instant feedback and status changes

### 🏅 Statistics & Analytics
- **🎮 Games Played Counter**: Track total gameplay sessions
- **🏆 Win Rate Calculation**: Performance percentage tracking
- **⚡ Best Score Recording**: Minimum attempts to solve
- **📊 Sidebar Dashboard**: Quick access to all statistics

## 🎲 Game Rules

### Objective
Guess the mystery number between 1 and 100 in the fewest attempts possible!

### How to Play
1. **Choose Difficulty**: Select Easy (10 attempts) or Hard (5 attempts) mode
2. **Make Your Guess**: Enter a number between 1-100
3. **Use the Hints**: 
   - 📈 **Too Low**: Your guess is smaller than the target
   - 📉 **Too High**: Your guess is larger than the target
   - 🎯 **Correct**: You found the mystery number!
4. **Track Progress**: Monitor remaining attempts and guess history
5. **Win or Learn**: Celebrate victory or try again with new strategy!

### Difficulty Levels
- **🟢 Easy Mode**: 10 attempts - Perfect for beginners and casual play
- **🔴 Hard Mode**: 5 attempts - Challenge for experienced players

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/guess-the-number-game.git
   cd guess-the-number-game
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit
   ```

   Or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running the Game

To start the Number Guessing Game on your localhost:

```bash
streamlit run app.py
```

**Note**: This is a Streamlit web application that runs on localhost. After running the command, Streamlit will automatically open your browser to `http://localhost:8501` where you can play the game.

The terminal will display:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

## 📁 Project Structure

```
guess-the-number-game/
│
├── app.py                # Main Streamlit application
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── assets/              # Screenshots and demo files (optional)
    ├── demo.gif
    ├── easy_mode.png
    ├── hard_mode.png
    └── victory_screen.png
```

## 🎮 Gameplay Features

### 🎯 Smart Guessing System
The game includes an intelligent range calculator that helps players make strategic decisions:

```python
# Example: After guessing 75 (Too High) and 25 (Too Low)
# Smart Range Display: 26 - 74
# This helps focus your next guess!
```

### 📊 Statistics Dashboard
Track your performance with comprehensive analytics:
- **Total Games Played**
- **Games Won**
- **Win Rate Percentage**
- **Best Score (Minimum Attempts)**

### 📜 Guess History
Every guess is recorded with:
- **Guess Number**: Sequential attempt counter
- **Your Guess**: The number you entered
- **Result**: Too High, Too Low, or Correct
- **Timestamp**: When the guess was made
- **Attempts Left**: Remaining chances

## 🎨 Design Philosophy

### Visual Design
- **Modern Aesthetics**: Clean, professional interface with subtle animations
- **Color Psychology**: Blue/purple gradients for focus and calm
- **Accessibility**: High contrast ratios and clear typography
- **Responsive**: Mobile-first design that scales beautifully

### User Experience
- **Intuitive Navigation**: Clear buttons and logical flow
- **Immediate Feedback**: Real-time hints and status updates
- **Progressive Disclosure**: Information revealed as needed
- **Error Prevention**: Input validation and helpful constraints

## 🧮 Algorithm & Logic

### Random Number Generation
```python
import random
mystery_number = random.randint(1, 100)  # Cryptographically sufficient for games
```

### Guess Evaluation Logic
```python
def evaluate_guess(user_guess, target_number):
    if user_guess > target_number:
        return "Too High"
    elif user_guess < target_number:
        return "Too Low"
    else:
        return "Correct"
```

### Smart Range Calculation
The app calculates optimal guessing ranges based on previous attempts to help players make strategic decisions.

## 🎓 Educational Value

Perfect for:
- **Programming Education**: Demonstrates loops, conditionals, and user input
- **Logic Development**: Enhances problem-solving and strategic thinking
- **Mathematics**: Binary search concepts and optimization strategies
- **Game Design**: User experience and interface design principles

## 🏆 Strategy Tips

### For Beginners
1. **Start with 50**: Middle of the range gives maximum information
2. **Use Binary Search**: Always guess the middle of remaining range
3. **Track Your Guesses**: Review history to avoid repeated mistakes

### For Advanced Players
1. **Optimal Strategy**: Binary search guarantees success in ≤7 attempts
2. **Risk Management**: In hard mode, be more conservative with guesses
3. **Pattern Recognition**: Learn from statistics to improve over time

## 🛠️ Technical Details

### Built With
- **Python 3.7+**: Core programming language
- **Streamlit**: Web application framework
- **HTML/CSS**: Custom styling and animations
- **Random Module**: Number generation
- **Datetime**: Timestamp tracking

### Key Components
- **Session State Management**: Persistent game data
- **Real-time Updates**: Dynamic content updates
- **Responsive Design**: Mobile-optimized layout
- **Animation System**: CSS3 animations and transitions

## 🚀 Deployment Options

### Streamlit Cloud (Recommended)
1. Push code to GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub and deploy
4. Get instant public URL!

### Alternative Platforms
- **Heroku**: Traditional web hosting
- **Railway**: Modern deployment platform
- **Render**: Simple cloud hosting
- **Replit**: Online IDE with instant sharing

## 🤝 Contributing

We welcome contributions! Here are ways to help:

### Ideas for Enhancement
- **🎵 Sound Effects**: Add audio feedback for guesses
- **🏅 Achievement System**: Unlock badges for milestones
- **👥 Multiplayer Mode*
