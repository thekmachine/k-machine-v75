import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="K-Machine v75", page_icon="⚡", layout="wide")

# ====================== CUSTOM CSS ======================
st.markdown("""
<style>
    .main {background: linear-gradient(to bottom, #0a0a0a, #1a1a2e);}
    h1, h2, h3 {color: #00ff9d !important; text-shadow: 0 0 15px #00ff9d;}
    .card {
        background: rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 255, 157, 0.15);
        border: 1px solid rgba(0, 255, 157, 0.3);
        transition: all 0.3s ease;
    }
    .card:hover {transform: scale(1.03); box-shadow: 0 15px 40px 0 rgba(0, 255, 157, 0.3);}
    .stButton>button {background: #00ff9d; color: #0a0a0a; font-weight: bold; border-radius: 12px;}
    .stButton>button:hover {background: #ffffff; color: #0a0a0a;}
</style>
""", unsafe_allow_html=True)

# ====================== HERO ======================
st.markdown("""
<div style="text-align:center; padding: 60px 20px; background: linear-gradient(90deg, #0a0a0a, #1a1a2e); border-radius: 20px; margin-bottom: 30px;">
    <h1 style="font-size: 3.8rem; margin:0;">⚡ K-MACHINE v75</h1>
    <p style="font-size: 1.8rem; color:#ffffff; margin:15px 0 40px;">AI That Beats the Line • Precision Predictions • Real Edge</p>
    <a href="#" style="background:#00ff9d; color:#0a0a0a; padding:18px 50px; border-radius:50px; text-decoration:none; font-weight:bold; font-size:1.4rem;">GET TODAY'S EDGE →</a>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🔥 Today's Hot Picks • Live Model Running")

# ====================== PERFORMANCE METRICS ======================
col1, col2, col3, col4 = st.columns(4)
col1.metric("Overall Win Rate", "68.4%", "↑ 3.2%")
col2.metric("Avg Edge vs Books", "+4.8%", "↑ 0.9%")
col3.metric("Games Analyzed", "1,247", "This season")
col4.metric("ROI This Month", "21.7%", "🔥")

# ====================== SIDEBAR ======================
st.sidebar.title("⚡ K-Machine Controls")
sport_filter = st.sidebar.selectbox("Focus Sport", ["All Sports", "NFL", "NBA", "MLB", "NHL", "Premier League"])
min_conf = st.sidebar.slider("Minimum Confidence %", 55, 95, 65)
st.sidebar.button("🔄 Refresh All Predictions")

# ====================== SAMPLE DATA (replace this with your real model later) ======================
sports_data = {
    "NFL": [
        {"home": "Chiefs", "away": "Ravens", "pick": "Chiefs -3.5", "conf": 82, "edge": 5.2, "reason": "Mahomes hot streak + defensive mismatch"},
        {"home": "Eagles", "away": "Packers", "pick": "Over 48", "conf": 76, "edge": 4.1, "reason": "High-scoring projected game script"},
        {"home": "49ers", "away": "Cowboys", "pick": "49ers ML", "conf": 71, "edge": 3.8, "reason": "Injury advantage + home field"},
    ],
    "NBA": [
        {"home": "Celtics", "away": "Lakers", "pick": "Celtics -6.5", "conf": 85, "edge": 6.3, "reason": "Boston dominance + LeBron rest"},
        {"home": "Warriors", "away": "Suns", "pick": "Over 228", "conf": 79, "edge": 4.9, "reason": "Pace + 3PT explosion expected"},
    ],
    "MLB": [
        {"home": "Yankees", "away": "Red Sox", "pick": "Yankees -1.5", "conf": 74, "edge": 3.7, "reason": "Cole pitching + bullpen edge"},
    ],
    "NHL": [
        {"home": "Maple Leafs", "away": "Bruins", "pick": "Leafs ML", "conf": 68, "edge": 2.9, "reason": "Toronto firepower vs Boston injuries"},
    ],
    "Premier League": [
        {"home": "Arsenal", "away": "Man City", "pick": "Arsenal +0.5", "conf": 77, "edge": 4.4, "reason": "Home advantage + City rotation"},
    ]
}

def create_prediction_card(game, sport):
    with st.container():
        st.markdown(f"""
        <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:1.4rem;">{game['home']} <span style="color:#00ff9d;">vs</span> {game['away']}</div>
                <div style="background:#00ff9d; color:#0a0a0a; padding:4px 12px; border-radius:20px; font-weight:bold;">{sport}</div>
            </div>
            <h3 style="margin:10px 0; color:#ffffff;">{game['pick']}</h3>
            <div style="display:flex; gap:15px; align-items:center;">
                <div style="flex:1;">
                    <div style="color:#00ff9d; font-size:0.9rem;">Confidence</div>
                    <div style="height:12px; background:#333; border-radius:10px; overflow:hidden;">
                        <div style="width:{game['conf']}%; height:100%; background:linear-gradient(90deg, #00ff9d, #00cc7a);"></div>
                    </div>
                </div>
                <div style="text-align:center; font-size:2rem; font-weight:bold; color:#00ff9d;">{game['conf']}%</div>
                <div>
                    <div style="color:#00ff9d; font-size:0.9rem;">Edge</div>
                    <div style="font-size:1.5rem; color:#ffd700;">+{game['edge']}%</div>
                </div>
            </div>
            <details style="margin-top:15px; color:#ccc;">
                <summary>Why this pick?</summary>
                {game['reason']}
            </details>
        </div>
        """, unsafe_allow_html=True)

# ====================== SPORTS TABS ======================
tab_labels = ["All Sports", "NFL", "NBA", "MLB", "NHL", "Premier League"]
tabs = st.tabs(tab_labels)

for i, tab in enumerate(tabs):
    with tab:
        current_sport = tab_labels[i]
        display_sports = list(sports_data.keys()) if current_sport == "All Sports" else [current_sport.replace("Premier League", "Premier League")]
        
        st.subheader(f"🔥 {current_sport} Predictions")
        games_to_show = []
        for sport_name in display_sports:
            if sport_name in sports_data:
                for game in sports_data[sport_name]:
                    if game['conf'] >= min_conf:
                        games_to_show.append((sport_name, game))
        
        if not games_to_show:
            st.info("No games meet your confidence filter right now.")
        else:
            cols = st.columns(3)
            for idx, (sport_name, game) in enumerate(games_to_show):
                with cols[idx % 3]:
                    create_prediction_card(game, sport_name)

# ====================== PERFORMANCE DASHBOARD ======================
st.markdown("---")
st.subheader("📊 Model Performance This Season")
perf_col1, perf_col2 = st.columns(2)
with perf_col1:
    fig = go.Figure(go.Indicator(mode="gauge+number", value=68.4, title={'text': "Overall Win Rate"}, gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#00ff9d"}}))
    st.plotly_chart(fig, use_container_width=True)
with perf_col2:
    st.write("**ROI by Sport**")
    roi_data = pd.DataFrame({"Sport": ["NFL", "NBA", "MLB", "NHL", "Premier League"], "ROI": [18.3, 24.7, 12.9, 15.4, 21.1]})
    st.bar_chart(roi_data.set_index("Sport"))

st.caption("K-Machine v75 • AI predictions for entertainment only • Always bet responsibly")
st.success("✅ Fully polished K-Machine is ready!")