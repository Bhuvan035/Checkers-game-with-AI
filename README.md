# Checkers AI 🤖♟

This project is an **AI agent** designed to play Checkers. The AI is implemented in **Python** and follows the American/British ruleset for Checkers. It intelligently selects moves based on game state and opponent actions.  

## 📌 Features  
✅ Implements a Checkers AI that makes strategic moves.  
✅ Uses the `Board`, `Move`, and `Checker` classes to interact with the game.  
✅ Can compete against other AI agents.  
✅ Supports different board sizes.  

## 🚀 Setup  

### 1⃣ **Install Dependencies**  
Ensure you are using **Python 3.5.2**.  

```sh
module load python/3.5.2   
```

### 2⃣ **Run the AI in Manual Mode**  
To play the AI in manual mode, use:  

```sh
python3 main.py {col} {row} {p} m {start_player (0 or 1)}
```

### 3⃣ **Test AI vs. Another AI**  
To test the AI against another AI locally:  

```sh
python3 AI_Runner.py {col} {row} {p} l {AI_1_path} {AI_2_path}
```

## 🏆 AI Tournament  
This AI can be tested in a tournament setting, competing against other AI agents to determine the best strategy. The game is played with a fixed time limit per move (8 minutes max).  

## 👨‍💻 Author  
- **Bhuvan Chandra**  
- **Email:** bhuvanchandra3008@gmail.com  

---



