import streamlit as st
import re

st.set_page_config(page_title="AI Interview Evaluation Agent", layout="centered")

# -------------------------------
# Session initialization
# -------------------------------
if "locked" not in st.session_state:
    st.session_state.locked = False
    st.session_state.job_role = ""
    st.session_state.skills = []

# -------------------------------
# Title
# -------------------------------
st.title("AI Interview Evaluation Agent")
st.write(
    "This system performs responsible interview pre-screening using "
    "company-defined criteria and explainable evaluation logic."
)

st.divider()

# -------------------------------
# COMPANY SETUP
# -------------------------------
if not st.session_state.locked:
    st.subheader("🏢 Company Setup")

    role = st.selectbox(
        "Job Role *",
        ["Select Job Role", "IoT Engineer", "Embedded Engineer", "System Engineer"]
    )

    skills = st.multiselect(
        "Required Skills *",
        ["IoT", "Embedded Systems", "ESP32", "Sensors", "Actuators"]
    )

    if st.button("🔒 Lock Job Requirements"):
        if role == "Select Job Role" or not skills:
            st.error("Please select a job role and at least one skill.")
        else:
            st.session_state.job_role = role
            st.session_state.skills = [s.lower() for s in skills]
            st.session_state.locked = True
            st.success("Job requirements locked. Candidate section unlocked.")
            st.rerun()

# -------------------------------
# CANDIDATE INTERVIEW
# -------------------------------
else:
    st.subheader("👤 Candidate Interview")

    st.markdown(
        "<span style='color:gray;font-size:0.9em;'>"
        "The jury will manually evaluate the candidate responses entered below. "
        "External assistance during answering is discouraged."
        "</span>",
        unsafe_allow_html=True
    )

    st.write(f"**Job Role:** {st.session_state.job_role}")
    st.write(f"**Required Skills:** {', '.join(st.session_state.skills)}")

    questions = [
        "Tell me about yourself.",
        "Explain a core technical concept related to the role.",
        "Describe a project you have worked on.",
        "How would you approach solving a new technical problem?",
        "What are your strengths and weaknesses?"
    ]

    answers = []

    for i, q in enumerate(questions, start=1):
        st.markdown(f"### Q{i}. {q}")
        ans = st.text_area("Candidate Answer", height=140, key=f"ans_{i}")
        answers.append(ans)
        st.divider()

    # -------------------------------
    # Helper functions
    # -------------------------------
    def is_gibberish(text):
        text = text.strip().lower()
        if len(text) < 20:
            return True
        if " " not in text:
            return True
        if len(re.findall(r"[aeiou]", text)) < 3:
            return True
        return False

    def skill_match(text):
        return sum(1 for s in st.session_state.skills if s in text.lower())

    # -------------------------------
    # Evaluation
    # -------------------------------
    if st.button("✅ Evaluate Interview"):
        if any(a.strip() == "" for a in answers):
            st.error("All questions must be answered.")
        else:
            st.subheader("📊 Evaluation Result")

            total_score = 0
            disqualified = False

            for i, ans in enumerate(answers, start=1):
                st.markdown(f"**Question {i}**")

                if is_gibberish(ans):
                    st.write("❌ Low-effort or random response detected.")
                    st.write("Score: 0/10")
                    disqualified = True
                else:
                    matches = skill_match(ans)
                    if matches == 0:
                        st.write("⚠️ Poor alignment with required job skills.")
                        st.write("Score: 4/10")
                        total_score += 4
                    elif matches == 1:
                        st.write("✅ Partial alignment with job skills.")
                        st.write("Score: 6/10")
                        total_score += 6
                    else:
                        st.write("✅ Strong alignment with job skills.")
                        st.write("Score: 8/10")
                        total_score += 8

                st.divider()

            st.subheader("🏁 Final Decision")
            st.write(f"**Total Score:** {total_score}/50")

            if not disqualified and total_score >= 30:
                st.success("✅ QUALIFIED FOR NEXT ROUND")
            else:
                st.error("❌ NOT QUALIFIED")

            st.info(
                "Evaluation is fully rule-based and explainable. "
                "No external AI model influences the final decision."
            )

    if st.button("🔄 Reset for New Hiring Round"):
        st.session_state.clear()
        st.rerun()
