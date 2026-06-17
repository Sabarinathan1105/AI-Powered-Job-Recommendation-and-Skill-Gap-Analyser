#FRONTEND 

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from resume_processor import (
    extract_text_from_file,
    extract_skills,
    compute_match_scores,
    get_skill_gap
)
from job_data import JOB_ROLES


# PAGE CONFIG

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

#CSS
st.markdown("""
<style>
    .metric-card {
        background: #1e1e2e;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #313244;
    }
    .skill-tag {
        display: inline-block;
        background: #a6e3a1;
        color: #1e1e2e;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 3px;
        font-size: 13px;
        font-weight: 600;
    }
    .missing-tag {
        display: inline-block;
        background: #f38ba8;
        color: #1e1e2e;
        padding: 3px 10px;
        border-radius: 20px;
        margin: 3px;
        font-size: 13px;
        font-weight: 600;
    }
    .stProgress > div > div { background-color: #89b4fa; }
</style>
""", unsafe_allow_html=True)

#SIDEBAR

with st.sidebar:
    st.title(" AI Resume Screener")
    st.caption("Powered by TF-IDF + Cosine Similarity")
    st.divider()

    st.subheader("Upload Resume")
    uploaded_file = st.file_uploader(
        "Drop your resume here",
        type=["pdf", "txt"],
        help="Supports PDF and plain text (.txt) formats"
    )

    st.divider()
    st.subheader("Settings")
    top_n = st.slider("Number of job matches to show", min_value=3, max_value=20, value=10)

    st.divider()
    st.subheader("Or paste resume text")
    pasted_text = st.text_area(
        "Paste your resume content here",
        height=200,
        placeholder="Paste resume text if you don't want to upload a file..."
    )

    analyse_btn = st.button("Analyse Resume", type="primary", use_container_width=True)



#BODY

st.title("AI-Powered Resume Screening & Job Recommender")
st.caption(f"Analysing against {len(JOB_ROLES)} job roles across 8 industries")

#Determine resume text source
resume_text = ""

if analyse_btn:
    if uploaded_file:
        with st.spinner("Extracting text from file..."):
            resume_text = extract_text_from_file(uploaded_file)
    elif pasted_text.strip():
        resume_text = pasted_text.strip()
    else:
        st.warning("Please upload a file or paste your resume text first.")
        st.stop()

    if resume_text.startswith("ERROR"):
        st.error(resume_text)
        st.stop()
#Save to session state so it persists across reruns
    st.session_state["resume_text"] = resume_text
    st.session_state["analysed"] = True

#Load from session state if already analysed
if st.session_state.get("analysed"):
    resume_text = st.session_state["resume_text"]
else:
    #Show landing screen
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📄 **Step 1**: Upload or paste your resume")
    with col2:
        st.info("🔍 **Step 2**: Click Analyse Resume")
    with col3:
        st.info("📊 **Step 3**: View matches, scores & skill gaps")
    st.stop()



#ANALYSIS
with st.spinner("Running NLP analysis..."):
    matched_skills   = extract_skills(resume_text)
    match_df         = compute_match_scores(resume_text, top_n=top_n)
    top_role         = match_df.iloc[0]["Job Role"]
    top_score        = match_df.iloc[0]["Match %"]
    skill_gap_data   = get_skill_gap(resume_text, top_role)

##SEVEN SECTIONS FOR STATISTICAL DATA

#SECTION 1: SUMMARY METRICS

st.subheader(" Summary")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Best Match", top_role, f"{top_score}%")
col2.metric("Skills Detected", len(matched_skills))
col3.metric("Roles Analysed", len(JOB_ROLES))
col4.metric("Skill Coverage", f"{skill_gap_data['match_percentage']}%",
            f"{skill_gap_data['total_matched']}/{skill_gap_data['total_required']} required")

#SECTION 2: TOP JOB MATCHES — BAR CHART

st.divider()
st.subheader("Top Job Role Matches")

fig_bar = px.bar(
    match_df,
    x="Match %",
    y="Job Role",
    orientation='h',
    color="Match %",
    color_continuous_scale="Blues",
    text="Match %",
    hover_data=["Category"],
    height=max(350, top_n * 40)
)
fig_bar.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig_bar.update_layout(
    yaxis=dict(autorange="reversed"),
    xaxis_title="Match Score (%)",
    yaxis_title="",
    coloraxis_showscale=False,
    margin=dict(l=10, r=80, t=10, b=10),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)
st.plotly_chart(fig_bar, use_container_width=True)


# SECTION 3: MATCH TABLE
st.subheader("Detailed Match Table")

display_df = match_df.copy()
display_df.index = display_df.index + 1  # Start ranking at 1
display_df["Match %"] = display_df["Match %"].apply(lambda x: f"{x}%")
st.dataframe(display_df, use_container_width=True)



#SECTION 4: SKILL GAP ANALYSIS

st.divider()
st.subheader("Skill Gap Analysis")

# Let user pick which role to analyse
selected_role = st.selectbox(
    "Select a job role to analyse skill gaps:",
    options=list(JOB_ROLES.keys()),
    index=list(JOB_ROLES.keys()).index(top_role)
)

gap = get_skill_gap(resume_text, selected_role)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("#### Skills You Have")
    if gap["matched_skills"]:
        tags_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in gap["matched_skills"]])
        st.markdown(tags_html, unsafe_allow_html=True)
    else:
        st.warning("No matching skills found for this role.")

with col_right:
    st.markdown("#### Skills You're Missing")
    if gap["missing_skills"]:
        tags_html = " ".join([f'<span class="missing-tag">{s}</span>' for s in gap["missing_skills"]])
        st.markdown(tags_html, unsafe_allow_html=True)
    else:
        st.success("🎉 You have all the required skills for this role!")

# Progress bar showing skill coverage
st.markdown(f"**Skill Coverage for {selected_role}:** {gap['match_percentage']}%")
st.progress(gap["match_percentage"] / 100)


#SECTION 5: RADAR CHART — TOP 5 ROLES

st.divider()
st.subheader("🕸️ Skill Coverage Radar — Top 5 Roles")
st.caption("Shows what % of each role's required skills your resume covers")

top5_roles = match_df.head(5)["Job Role"].tolist()
coverage_scores = []
for role in top5_roles:
    g = get_skill_gap(resume_text, role)
    coverage_scores.append(g["match_percentage"])

fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=coverage_scores + [coverage_scores[0]],       # close the polygon
    theta=top5_roles + [top5_roles[0]],
    fill='toself',
    fillcolor='rgba(137, 180, 250, 0.25)',
    line=dict(color='#89b4fa', width=2),
    name="Skill Coverage"
))
fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100], ticksuffix="%"),
        bgcolor='rgba(0,0,0,0)'
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    showlegend=False,
    height=420
)
st.plotly_chart(fig_radar, use_container_width=True)



#SECTION 6: CATEGORY BREAKDOWN — PIE CHART

st.divider()
st.subheader("Match Distribution by Industry Category")

cat_df = match_df.groupby("Category")["Match %"].mean().reset_index()
cat_df.columns = ["Category", "Avg Match %"]
cat_df = cat_df.sort_values("Avg Match %", ascending=False)

fig_pie = px.pie(
    cat_df,
    names="Category",
    values="Avg Match %",
    hole=0.45,
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_pie.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    legend=dict(orientation='h', yanchor='bottom', y=-0.3)
)
st.plotly_chart(fig_pie, use_container_width=True)


#SECTION 7: DETECTED SKILLS

st.divider()
st.subheader("All Skills Detected in Your Resume")

if matched_skills:
    tags_html = " ".join([f'<span class="skill-tag">{s}</span>' for s in matched_skills])
    st.markdown(tags_html, unsafe_allow_html=True)
else:
    st.warning("No recognisable technical skills detected. Make sure your resume text contains skill keywords.")

#FOOTER SECTION

st.divider()
st.caption("ALL THE BEST!")
