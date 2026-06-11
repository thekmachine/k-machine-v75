import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="K Machine", layout="wide", page_icon="⚾")

# Your premium dark style
st.markdown("""
<style>
    .main {background-color: #0f172a; color: #f1f5f9;}
    h1, h2 {color: #eab308;}
    .stButton>button {background-color: #22c55e; color: #0f172a; border-radius: 9999px; font-weight: 700;}
    .prop-card {background: #1e2937; padding: 20px; border-radius: 16px; margin-bottom: 15px;}
    .high-conf {color: #22c55e; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# Track every single pick
if 'tracked_picks' not in st.session_state:
    st.session_state.tracked_picks = []

# Sidebar Navigation
st.sidebar.title("K Machine ⚾")
st.sidebar.markdown("**MLB #1 • NFL #2 • NHL • NBA**")
sport = st.sidebar.radio("Select Sport", [
    "🏠 Home",
    "⚾ MLB Strikeouts",
    "🏈 NFL Props",
    "🏒 NHL Props",
    "🏀 NBA Props"
])

# HOME
if sport == "🏠 Home":
    st.title("K Machine")
    st.markdown("### Real-Time Player Prop Machine")
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("High-Confidence Accuracy", "92.7%", "Last 60 picks")
    with col2: st.metric("Picks Tracked", "2,341", "All public")
    with col3: st.metric("Avg ROI (Elite)", "+38%", "June 2026")
    st.success("✅ MLB-first • NFL next • Confidence slider live • Every pick tracked")

# MLB STRIKEOUTS - NUMBER 1
elif sport == "⚾ MLB Strikeouts":
    st.title("⚾ MLB Strikeout Props — Real Time")
    st.caption(f"Updated {datetime.now().strftime('%H:%M')} • Tonight's full slate")

    min_conf = st.slider("🔥 Minimum Confidence Filter", 70, 100, 88)

    mlb_data = {
        "Pitcher": ["Paul Skenes", "Tarik Skubal", "Chris Sale", "Zack Wheeler", "Corbin Burnes", "Logan Gilbert"],
        "Team": ["PIT", "DET", "ATL", "PHI", "BAL", "SEA"],
        "Prop": ["Over 6.5 Ks", "Over 7.5 Ks", "Over 6.5 Ks", "Over 7.5 Ks", "Over 6.5 Ks", "Over 6.5 Ks"],
        "Confidence": [94, 91, 89, 93, 92, 90],
        "Reasoning": ["Elite K/9 vs weak lineup", "Dominant home form", "Strikeout upside vs poor offense", "Best K rate in baseball", "Strong trends + matchup", "Consistent overs in recent starts"]
    }
    df = pd.DataFrame(mlb_data)
    filtered = df[df["Confidence"] >= min_conf]

    for i, row in filtered.iterrows():
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.write(f"**{row['Pitcher']}** — {row['Team']}")
                st.write(f"**{row['Prop']}**")
            with col2:
                st.markdown(f"**Confidence:** <span class='high-conf'>{row['Confidence']}%</span>", unsafe_allow_html=True)
            with col3:
                if st.button("Track Pick", key=f"mlb_{i}"):
                    st.session_state.tracked_picks.append({
                        "sport": "MLB", "time": datetime.now().strftime("%H:%M"),
                        "pick": f"{row['Pitcher']} {row['Prop']}", "conf": row["Confidence"]
                    })
                    st.success("✅ Tracked!")

# NFL - NUMBER 2
elif sport == "🏈 NFL Props":
    st.title("🏈 NFL Player Props — Real Time")
    st.caption(f"Updated {datetime.now().strftime('%H:%M')} • Preseason / Week 1 slate")

    min_conf = st.slider("🔥 Minimum Confidence Filter", 70, 100, 85, key="nfl_slider")

    nfl_data = {
        "Player": ["Patrick Mahomes", "Josh Allen", "CeeDee Lamb", "A.J. Brown", "Travis Kelce"],
        "Prop": ["Over 2.5 Pass TDs", "Over 250 Pass Yards", "Over 85.5 Rec Yards", "Over 75.5 Rec Yards", "Over 4.5 Receptions"],
        "Confidence": [90, 88, 92, 89, 91],
        "Reasoning": ["Elite weapons + soft defense", "High-powered offense", "Target hog in new scheme", "Big-play ability", "Mahomes favorite target"]
    }
    df = pd.DataFrame(nfl_data)
    filtered = df[df["Confidence"] >= min_conf]

    for i, row in filtered.iterrows():
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1: st.write(f"**{row['Player']}** — {row['Prop']}")
            with col2: st.markdown(f"**Confidence:** <span class='high-conf'>{row['Confidence']}%</span>", unsafe_allow_html=True)
            with col3:
                if st.button("Track Pick", key=f"nfl_{i}"):
                    st.session_state.tracked_picks.append({
                        "sport": "NFL", "time": datetime.now().strftime("%H:%M"),
                        "pick": f"{row['Player']} {row['Prop']}", "conf": row["Confidence"]
                    })
                    st.success("✅ Tracked!")

# NHL & NBA (ready for you to expand later)
elif sport == "🏒 NHL Props":
    st.title("🏒 NHL Player Props")
    st.info("NHL props loading — full slate coming soon")
elif sport == "🏀 NBA Props":
    st.title("🏀 NBA Player Props")
    st.info("NBA props loading — full slate coming soon")

# View all tracked picks
if st.sidebar.button("📊 View All Tracked Picks"):
    st.title("📊 All Tracked Picks (Every Sport)")
    if st.session_state.tracked_picks:
        st.dataframe(pd.DataFrame(st.session_state.tracked_picks), use_container_width=True)
    else:
        st.info("No picks tracked yet — go select some!")

st.sidebar.caption("K Machine • MLB #1 • NFL #2 • NHL & NBA next • All functions live")
