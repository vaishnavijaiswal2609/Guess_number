import streamlit as st
import random

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Reset & Root ── */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: #0a0a0f;
    min-height: 100vh;
}

/* ── Main card ── */
.game-card {
    background: linear-gradient(145deg, #111118 0%, #16161f 100%);
    border: 1px solid #2a2a3d;
    border-radius: 20px;
    padding: 40px 44px;
    margin-top: 20px;
    box-shadow: 0 0 60px rgba(99, 102, 241, 0.07), 0 20px 40px rgba(0,0,0,0.4);
}

/* ── Badge / eyebrow ── */
.badge {
    display: inline-block;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #818cf8;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 20px;
    margin-bottom: 18px;
}

/* ── Title ── */
.game-title {
    font-size: 36px;
    font-weight: 700;
    color: #f0f0ff;
    line-height: 1.15;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
}

.game-subtitle {
    color: #6b7280;
    font-size: 15px;
    margin-bottom: 32px;
}

/* ── Range indicator bar ── */
.range-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    background: #1a1a26;
    border: 1px solid #2a2a3d;
    border-radius: 10px;
    padding: 12px 18px;
    margin-bottom: 28px;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
}

.range-label { color: #4b5563; }
.range-val   { color: #818cf8; font-weight: 700; }
.range-dash  { color: #374151; }

/* ── Attempts counter ── */
.attempts-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 28px;
}

.attempts-pill {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.25);
    color: #34d399;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    padding: 5px 14px;
    border-radius: 20px;
}

.attempts-label {
    color: #4b5563;
    font-size: 13px;
}

/* ── History strip ── */
.history-label {
    color: #4b5563;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-family: 'Space Mono', monospace;
    margin-bottom: 10px;
}

.history-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 28px;
    min-height: 32px;
}

.hist-chip {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid;
}

.hist-low  { background: rgba(239,68,68,0.08);  border-color: rgba(239,68,68,0.25);  color: #f87171; }
.hist-high { background: rgba(251,191,36,0.08); border-color: rgba(251,191,36,0.25); color: #fbbf24; }

/* ── Feedback box ── */
.feedback-box {
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 24px;
    font-size: 15px;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 12px;
    border: 1px solid;
}

.fb-low  { background: rgba(239,68,68,0.08);  border-color: rgba(239,68,68,0.2);  color: #fca5a5; }
.fb-high { background: rgba(251,191,36,0.08); border-color: rgba(251,191,36,0.2); color: #fde68a; }
.fb-win  { background: rgba(16,185,129,0.10); border-color: rgba(16,185,129,0.25); color: #6ee7b7; }

/* ── Win banner ── */
.win-banner {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, rgba(99,102,241,0.15) 0%, rgba(16,185,129,0.10) 100%);
    border: 1px solid rgba(99,102,241,0.3);
    border-radius: 16px;
    margin-bottom: 24px;
}

.win-emoji { font-size: 48px; margin-bottom: 10px; }
.win-title {
    font-size: 24px;
    font-weight: 700;
    color: #f0f0ff;
    margin-bottom: 6px;
}
.win-sub {
    color: #818cf8;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
}

/* ── Streamlit widget overrides ── */
div[data-testid="stNumberInput"] input {
    background: #1a1a26 !important;
    border: 1.5px solid #2a2a3d !important;
    border-radius: 10px !important;
    color: #f0f0ff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}

div[data-testid="stNumberInput"] label {
    color: #9ca3af !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
}

/* Primary button */
div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
    border: none !important;
    border-radius: 10px !important;
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 12px 32px !important;
    width: 100% !important;
    transition: opacity 0.15s, transform 0.1s;
    letter-spacing: 0.2px;
}

div[data-testid="stButton"] > button[kind="primary"]:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px);
}

/* Secondary button */
div[data-testid="stButton"] > button:not([kind="primary"]) {
    background: transparent !important;
    border: 1px solid #2a2a3d !important;
    border-radius: 10px !important;
    color: #6b7280 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    padding: 10px 24px !important;
    width: 100% !important;
}

div[data-testid="stButton"] > button:not([kind="primary"]):hover {
    border-color: #6366f1 !important;
    color: #818cf8 !important;
}

/* Divider */
hr { border-color: #1e1e2e !important; margin: 28px 0 !important; }

/* Footer */
.footer-note {
    text-align: center;
    color: #374151;
    font-size: 12px;
    font-family: 'Space Mono', monospace;
    margin-top: 24px;
    letter-spacing: 0.5px;
}

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── State init ────────────────────────────────────────────────────────────────
if "secret"   not in st.session_state:
    st.session_state.secret   = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "history"  not in st.session_state:
    st.session_state.history  = []   # list of (value, "low"|"high"|"win")
if "won"      not in st.session_state:
    st.session_state.won      = False
if "feedback" not in st.session_state:
    st.session_state.feedback = None  # ("low"|"high"|"win", number)

def new_game():
    st.session_state.secret   = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history  = []
    st.session_state.won      = False
    st.session_state.feedback = None

def make_guess():
    guess = st.session_state.guess_input
    if guess is None:
        return
    secret = st.session_state.secret
    st.session_state.attempts += 1

    if guess < secret:
        st.session_state.feedback = ("low", guess)
        st.session_state.history.append((guess, "low"))
    elif guess > secret:
        st.session_state.feedback = ("high", guess)
        st.session_state.history.append((guess, "high"))
    else:
        st.session_state.feedback = ("win", guess)
        st.session_state.history.append((guess, "win"))
        st.session_state.won = True

# ── Layout ────────────────────────────────────────────────────────────────────
col_l, col_c, col_r = st.columns([1, 3, 1])

with col_c:
    st.markdown('<div class="badge">🎯 MINI GAME</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-title">Guess the Number</div>', unsafe_allow_html=True)
    st.markdown('<div class="game-subtitle">I picked a number between 1 and 100. Can you crack it?</div>', unsafe_allow_html=True)

    # Range bar
    st.markdown("""
    <div class="range-bar">
        <span class="range-label">RANGE</span>
        <span class="range-val">1</span>
        <span class="range-dash">────────────</span>
        <span class="range-val">100</span>
    </div>
    """, unsafe_allow_html=True)

    # Attempts counter
    attempts = st.session_state.attempts
    st.markdown(f"""
    <div class="attempts-row">
        <span class="attempts-pill">× {attempts}</span>
        <span class="attempts-label">{"attempt" if attempts == 1 else "attempts"} so far</span>
    </div>
    """, unsafe_allow_html=True)

    # History strip
    if st.session_state.history:
        chips = ""
        for val, kind in st.session_state.history:
            css = "hist-low" if kind == "low" else ("hist-high" if kind == "high" else "hist-win")
            arrow = "↑" if kind == "low" else ("↓" if kind == "high" else "✓")
            chips += f'<span class="hist-chip {css}">{val} {arrow}</span>'
        st.markdown(f'<div class="history-label">Previous guesses</div><div class="history-strip">{chips}</div>', unsafe_allow_html=True)

    # Feedback
    fb = st.session_state.feedback
    if fb:
        kind, val = fb
        if kind == "low":
            st.markdown(f'<div class="feedback-box fb-low">🔴 <span>{val} is too low — aim higher.</span></div>', unsafe_allow_html=True)
        elif kind == "high":
            st.markdown(f'<div class="feedback-box fb-high">🟡 <span>{val} is too high — come down a bit.</span></div>', unsafe_allow_html=True)
        elif kind == "win":
            st.markdown(f"""
            <div class="win-banner">
                <div class="win-emoji">🎉</div>
                <div class="win-title">You got it!</div>
                <div class="win-sub">The number was {val} · solved in {attempts} {"try" if attempts == 1 else "tries"}</div>
            </div>
            """, unsafe_allow_html=True)

    # Input + buttons
    if not st.session_state.won:
        st.number_input(
            "Your guess",
            min_value=1,
            max_value=100,
            step=1,
            key="guess_input",
            placeholder="Enter 1 – 100",
            label_visibility="visible",
        )
        st.button("Submit Guess →", type="primary", on_click=make_guess)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.button("↺  New Game", on_click=new_game)

    st.markdown('<div class="footer-note">built with Python · Streamlit · 🎯</div>', unsafe_allow_html=True)