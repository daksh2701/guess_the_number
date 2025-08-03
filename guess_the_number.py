import streamlit as st
import random
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Guess the Number Game",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for amazing styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .ascii-logo {
        font-family: 'Courier New', monospace;
        font-size: 0.4rem;
        color: #667eea;
        text-align: center;
        line-height: 1.2;
        margin: 1rem 0;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 15px;
        border: 2px solid #667eea;
        overflow-x: auto;
        white-space: pre;
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Orbitron', monospace;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        text-align: center;
        color: #6C757D;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    .game-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        color: white;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
    }
    
    .difficulty-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 5px solid #28a745;
    }
    
    .attempts-display {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
        animation: pulse 2s infinite;
    }
    
    .success-container {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(40, 167, 69, 0.3);
        animation: celebrateWin 1s ease-out;
    }
    
    .failure-container {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(220, 53, 69, 0.3);
        animation: shake 0.5s ease-in-out;
    }
    
    .hint-container {
        background: linear-gradient(135deg, #ffc107 0%, #ffca28 100%);
        color: #212529;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.3rem;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(255, 193, 7, 0.3);
        animation: bounceIn 0.6s ease-out;
    }
    
    .stats-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin: 2rem 0;
        border: 1px solid #e0e0e0;
    }
    
    .stat-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 1rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    
    .stat-label {
        font-weight: 600;
        color: #495057;
    }
    
    .stat-value {
        font-weight: 700;
        font-size: 1.2rem;
        color: #667eea;
    }
    
    .number-input {
        font-size: 2rem !important;
        text-align: center !important;
        font-weight: 700 !important;
        border: 3px solid #667eea !important;
        border-radius: 15px !important;
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%) !important;
        transition: all 0.3s ease !important;
    }
    
    .number-input:focus {
        border-color: #764ba2 !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3) !important;
        transform: scale(1.02) !important;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 15px;
        font-weight: 700;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #5a6fd8 0%, #6b5b95 100%);
    }
    
    .stButton > button:active {
        transform: translateY(-1px);
    }
    
    .difficulty-button {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%) !important;
    }
    
    .difficulty-button:hover {
        background: linear-gradient(135deg, #218838 0%, #1e7e34 100%) !important;
    }
    
    .game-info {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #2196f3;
        margin: 1rem 0;
    }
    
    .progress-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .history-item {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #6c757d;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .range-display {
        background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 1rem 0;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes bounceIn {
        0% {
            opacity: 0;
            transform: scale(0.3) translateY(-50px);
        }
        50% {
            opacity: 1;
            transform: scale(1.05);
        }
        70% {
            transform: scale(0.9);
        }
        100% {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    @keyframes celebrateWin {
        0% {
            transform: scale(1) rotate(0deg);
        }
        25% {
            transform: scale(1.1) rotate(-5deg);
        }
        50% {
            transform: scale(1.2) rotate(5deg);
        }
        75% {
            transform: scale(1.1) rotate(-2deg);
        }
        100% {
            transform: scale(1) rotate(0deg);
        }
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
    
    .sidebar-content {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .emoji-large {
        font-size: 2rem;
    }
    
    @media (max-width: 768px) {
        .ascii-logo {
            font-size: 0.25rem;
        }
        
        .main-header {
            font-size: 2rem;
        }
        
        .number-input {
            font-size: 1.5rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ASCII Logo
ascii_logo = """
 ██████  ██    ██ ███████ ███████ ███████     ████████ ██   ██ ███████     ███    ██ ██    ██ ███    ███ ██████  ███████ ██████       ██████   █████  ███    ███ ███████     
██       ██    ██ ██      ██      ██             ██    ██   ██ ██          ████   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██     ██       ██   ██ ████  ████ ██          
██   ███ ██    ██ █████   ███████ ███████        ██    ███████ █████       ██ ██  ██ ██    ██ ██ ████ ██ ██████  █████   ██████      ██   ███ ███████ ██ ████ ██ █████       
██    ██ ██    ██ ██           ██      ██        ██    ██   ██ ██          ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██     ██    ██ ██   ██ ██  ██  ██ ██          
 ██████   ██████  ███████ ███████ ███████        ██    ██   ██ ███████     ██   ████  ██████  ██      ██ ██████  ███████ ██   ██      ██████  ██   ██ ██      ██ ███████     
"""

# Initialize session state
def init_session_state():
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'difficulty' not in st.session_state:
        st.session_state.difficulty = None
    if 'answer' not in st.session_state:
        st.session_state.answer = None
    if 'attempts_left' not in st.session_state:
        st.session_state.attempts_left = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'won' not in st.session_state:
        st.session_state.won = False
    if 'guess_history' not in st.session_state:
        st.session_state.guess_history = []
    if 'total_games' not in st.session_state:
        st.session_state.total_games = 0
    if 'total_wins' not in st.session_state:
        st.session_state.total_wins = 0
    if 'last_hint' not in st.session_state:
        st.session_state.last_hint = ""
    if 'best_score' not in st.session_state:
        st.session_state.best_score = float('inf')

def start_new_game(difficulty):
    st.session_state.game_started = True
    st.session_state.difficulty = difficulty
    st.session_state.answer = random.randint(1, 100)
    st.session_state.attempts_left = 10 if difficulty == "Easy" else 5
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.guess_history = []
    st.session_state.last_hint = ""
    st.session_state.total_games += 1

def make_guess(guess):
    if st.session_state.attempts_left <= 0 or st.session_state.game_over:
        return
    
    st.session_state.attempts_left -= 1
    guess_time = datetime.now().strftime("%H:%M:%S")
    
    if guess == st.session_state.answer:
        st.session_state.won = True
        st.session_state.game_over = True
        st.session_state.total_wins += 1
        attempts_used = (10 if st.session_state.difficulty == "Easy" else 5) - st.session_state.attempts_left
        if attempts_used < st.session_state.best_score:
            st.session_state.best_score = attempts_used
        st.session_state.last_hint = f"🎉 CORRECT! The answer was {st.session_state.answer}!"
    elif guess > st.session_state.answer:
        st.session_state.last_hint = "📉 Too High! Try a smaller number."
    else:
        st.session_state.last_hint = "📈 Too Low! Try a bigger number."
    
    # Add to history
    result = "🎯 Correct!" if guess == st.session_state.answer else "📉 Too High" if guess > st.session_state.answer else "📈 Too Low"
    st.session_state.guess_history.append({
        'guess': guess,
        'result': result,
        'time': guess_time,
        'attempts_left': st.session_state.attempts_left
    })
    
    # Check if game over
    if st.session_state.attempts_left <= 0 and not st.session_state.won:
        st.session_state.game_over = True

def reset_game():
    st.session_state.game_started = False
    st.session_state.difficulty = None
    st.session_state.answer = None
    st.session_state.attempts_left = 0
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.guess_history = []
    st.session_state.last_hint = ""

# Initialize session state
init_session_state()

# Display ASCII Logo
st.markdown(f'<div class="ascii-logo">{ascii_logo}</div>', unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🎯 GUESS THE NUMBER</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Test your intuition and guess the mystery number!</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown("### 🎮 Game Settings")
    
    if not st.session_state.game_started:
        st.markdown("**Choose your challenge level:**")
        
        if st.button("🟢 EASY MODE", key="easy", help="10 attempts to guess"):
            start_new_game("Easy")
            st.rerun()
            
        if st.button("🔴 HARD MODE", key="hard", help="5 attempts to guess"):
            start_new_game("Hard")
            st.rerun()
    else:
        # Game controls
        if st.button("🔄 New Game"):
            reset_game()
            st.rerun()
            
        if st.button("🏠 Main Menu"):
            reset_game()
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistics
    if st.session_state.total_games > 0:
        st.markdown("### 📊 Your Statistics")
        win_rate = (st.session_state.total_wins / st.session_state.total_games) * 100
        
        st.markdown('<div class="stats-container">', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="stat-item">
            <span class="stat-label">🎮 Games Played:</span>
            <span class="stat-value">{st.session_state.total_games}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">🏆 Games Won:</span>
            <span class="stat-value">{st.session_state.total_wins}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">📈 Win Rate:</span>
            <span class="stat-value">{win_rate:.1f}%</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.best_score != float('inf'):
            st.markdown(f"""
            <div class="stat-item">
                <span class="stat-label">⚡ Best Score:</span>
                <span class="stat-value">{st.session_state.best_score} attempts</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Main game area
if not st.session_state.game_started:
    # Welcome screen
    st.markdown("""
    <div class="game-info">
        <h3>🎯 How to Play</h3>
        <p><strong>🎮 Objective:</strong> Guess the mystery number between 1 and 100!</p>
        <p><strong>🟢 Easy Mode:</strong> 10 attempts to find the number</p>
        <p><strong>🔴 Hard Mode:</strong> 5 attempts to find the number</p>
        <p><strong>💡 Strategy:</strong> Use the hints to narrow down your guesses!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="difficulty-container">
        <h3 style="text-align: center; color: #28a745;">🚀 Ready to Challenge Your Mind?</h3>
        <p style="text-align: center; font-size: 1.1rem;">Choose your difficulty level from the sidebar and let the guessing begin!</p>
    </div>
    """, unsafe_allow_html=True)
    
else:
    # Game in progress
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    
    # Game status
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"**🎮 Mode:** {st.session_state.difficulty}")
    with col2:
        st.markdown(f"**🎯 Range:** 1 - 100")
    with col3:
        st.markdown(f"**🔢 Mystery Number:** ???")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Attempts remaining
    if st.session_state.attempts_left > 0 and not st.session_state.game_over:
        st.markdown(f"""
        <div class="attempts-display">
            ⏱️ Attempts Remaining: {st.session_state.attempts_left}
        </div>
        """, unsafe_allow_html=True)
    
    # Range display
    if st.session_state.guess_history:
        # Calculate smart range based on previous guesses
        low_bound = 1
        high_bound = 100
        
        for guess_data in st.session_state.guess_history:
            if "Too High" in guess_data['result']:
                high_bound = min(high_bound, guess_data['guess'] - 1)
            elif "Too Low" in guess_data['result']:
                low_bound = max(low_bound, guess_data['guess'] + 1)
        
        if low_bound <= high_bound and not st.session_state.game_over:
            st.markdown(f"""
            <div class="range-display">
                🎯 Smart Range: {low_bound} - {high_bound}
            </div>
            """, unsafe_allow_html=True)
    
    # Hint display
    if st.session_state.last_hint and not st.session_state.game_over:
        st.markdown(f"""
        <div class="hint-container">
            {st.session_state.last_hint}
        </div>
        """, unsafe_allow_html=True)
    
    # Game over states
    if st.session_state.game_over:
        if st.session_state.won:
            attempts_used = (10 if st.session_state.difficulty == "Easy" else 5) - st.session_state.attempts_left
            st.markdown(f"""
            <div class="success-container">
                <h2>🎉 CONGRATULATIONS! 🎉</h2>
                <h3>You guessed it right!</h3>
                <p><strong>🎯 The number was: {st.session_state.answer}</strong></p>
                <p>🏆 You solved it in {attempts_used} attempts!</p>
                <p>💫 Difficulty: {st.session_state.difficulty} Mode</p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(f"""
            <div class="failure-container">
                <h2>😔 Game Over!</h2>
                <h3>Better luck next time!</h3>
                <p><strong>🎯 The number was: {st.session_state.answer}</strong></p>
                <p>💪 Don't give up - try again!</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Input section
    if not st.session_state.game_over and st.session_state.attempts_left > 0:
        st.markdown("### 🎯 Make Your Guess")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            guess = st.number_input(
                "Enter a number between 1 and 100:",
                min_value=1,
                max_value=100,
                value=50,
                step=1,
                key="guess_input"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Space for alignment
            if st.button("🚀 GUESS!", type="primary"):
                make_guess(guess)
                st.rerun()
    
    # Guess history
    if st.session_state.guess_history:
        with st.expander("📜 Guess History", expanded=True):
            st.markdown("### Your Previous Guesses")
            
            for i, guess_data in enumerate(reversed(st.session_state.guess_history)):
                guess_num = len(st.session_state.guess_history) - i
                st.markdown(f"""
                <div class="history-item">
                    <div>
                        <strong>Guess #{guess_num}:</strong> {guess_data['guess']} 
                        <span style="margin-left: 10px;">{guess_data['result']}</span>
                    </div>
                    <div style="font-size: 0.9rem; color: #6c757d;">
                        {guess_data['time']} | {guess_data['attempts_left']} left
                    </div>
                </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6C757D; font-size: 0.9rem;">
    <strong>🎯 Guess the Number Game</strong> | Built with Streamlit | 
    <em>Challenge your intuition and logical thinking!</em>
</div>
""", unsafe_allow_html=True)