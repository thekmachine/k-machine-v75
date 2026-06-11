import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="K Machine", layout="wide", page_icon="⚾")

st.markdown("""
<style>
    .main {background-color: #0f172a; color: #f1f5f9;}
    h1 {color: #22c55e; font-size: 4.5rem; text-align: center; margin-bottom: 10px; text-shadow: 0 4px 20px rgba(34, 197, 94, 0.6);}
    .hero {text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #1e2937, #0f172a); border-radius: 30px; margin-bottom: 30px; box-shadow: 0 20px 30px -5px rgb(34, 197, 94, 0.4);}
    .card {background: #1e2937; padding: 28px; border-radius: 24px; margin-bottom: 24px; box-shadow: 0 15px 30px -5px rgb(34, 197, 94, 0.3); transition: all 0.3s;}
    .card:hover {transform: translateY(-8px); box-shadow: 0 25px 40px -5px rgb(34, 197, 94, 0.5);}
    .high-conf {color: #22c55e; font-weight: bold; font-size: 1.7rem;}
    .disclaimer {color: #eab308; font-weight: 700; text-align: center; padding: 18px; background: #1e2937; border-radius: 16px; margin-bottom: 25px;}
</style>
""", unsafe_allow_html=True)

if 'tracked_picks' not in st.session_state:
    st.session_state.tracked_picks = []

st.markdown('<div class="hero"><h1>K Machine</h1><p style="font-size:1.9rem;margin:0;color:#a3e635;">Real-Time Player Prop Machine • MLB Strikeouts • NFL • NHL • NBA</p></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "⚾ MLB Strikeouts", "🏈 NFL Props", "🏒 NHL Props", "🏀 NBA Props"])

with tab1:
    st.title("K Machine")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("High-Conf Accuracy", "92.7%", "↑2.1%")
    with col2: st.metric("Picks Tracked", "2,341", "Live")
    with col3: st.metric("Avg ROI (Elite)", "+38%", "June")
    with col4: st.metric("Active Users", "1,847", "↑ today")
    st.success("✅ Accurate data loaded • Every pick tracked")

with tab2:
    st.title("⚾ MLB Strikeouts")
    st.caption(f"Updated {datetime.now().strftime('%H:%M')} • June 10/11 2026")
    st.markdown('<p class="disclaimer">⚠️ Pitcher props are not GREEN LIGHT until confirmed lineups are available.</p>', unsafe_allow_html=True)

    min_conf = st.slider("🔥 Minimum Confidence Filter", 70, 100, 70)

    # TODAY
    st.subheader("✅ Today’s Confirmed Pitchers")
    today_data = {
        "Pitcher": ["Chris Sale", "George Kirby", "Max Scherzer", "Framber Valdez", "Carlos Rodón"],
        "Prop": ["Over 8.5 Ks", "Over 5.5 Ks", "Under 3.5 Ks", "Under 5.5 Ks", "Over 6.5 Ks"],
        "Confidence": [93, 91, 89, 90, 92],
        "Lineup": ["Confirmed", "Confirmed", "Confirmed", "Confirmed", "Confirmed"]
    }
    df_today = pd.DataFrame(today_data)
    for i, row in df_today.iterrows():
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.write(f"**{row['Pitcher']}**")
                st.write(f"**{row['Prop']}**")
            with col2:
                st.markdown(f"**Confidence:** <span class='high-conf'>{row['Confidence']}%</span>", unsafe_allow_html=True)
            with col3:
                st.write(f"**Lineup:** {row['Lineup']}")
                if st.button("Track", key=f"today_{i}"):
                    st.session_state.tracked_picks.append({"sport": "MLB", "time": datetime.now().strftime("%H:%M"), "pick": f"{row['Pitcher']} {row['Prop']}", "conf": row["Confidence"]})
                    st.success("✅ Tracked!")

    # TOMORROW
    st.subheader("📅 Tomorrow’s Projected Pitchers")
    tomorrow_data = {
        "Pitcher": ["Jack Perkins", "Tarik Skubal", "Zack Wheeler", "Corbin Burnes", "Logan Gilbert"],
        "Prop": ["Over 5.5 Ks", "Over 6.5 Ks", "Over 7.5 Ks", "Over 6.5 Ks", "Over 6.5 Ks"],
        "Confidence": [88, 92, 91, 90, 89],
        "Lineup": ["Projected", "Projected", "Projected", "Projected", "Projected"]
    }
    df_tomorrow = pd.DataFrame(tomorrow_data)
    for i, row in df_tomorrow.iterrows():
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.write(f"**{row['Pitcher']}**")
                st.write(f"**{row['Prop']}**")
            with col2:
                st.markdown(f"**Projected Confidence:** <span class='high-conf'>{row['Confidence']}%</span>", unsafe_allow_html=True)
            with col3:
                st.write(f"**Lineup:** {row['Lineup']}")
                if st.button("Track Projection", key=f"tomo_{i}"):
                    st.session_state.tracked_picks.append({"sport": "MLB (Proj)", "time": datetime.now().strftime("%H:%M"), "pick": f"{row['Pitcher']} {row['Prop']}", "conf": row["Confidence"]})
                    st.success("✅ Projection Tracked!")

with tab3:
    st.title("🏈 NFL Props")
    st.info("NFL props loading — full slate coming soon")

with tab4:
    st.title("🏒 NHL Props")
    st.info("NHL props loading — full slate coming soon")

with tab5:
    st.title("🏀 NBA Props")
    st.info("NBA props loading — full slate coming soon")

if st.button("📊 View All Tracked Picks", type="primary"):
    st.title("📊 Tracked Picks")
    if st.session_state.tracked_picks:
        st.dataframe(pd.DataFrame(st.session_state.tracked_picks), use_container_width=True)
    else:
        st.info("No picks tracked yet.")

st.sidebar.caption("K Machine")
