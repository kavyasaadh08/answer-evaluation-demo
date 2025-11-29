1. OVERVIEW: 
This project is a rule-based AI Interview Evaluation Agent designed for HR pre-screening of fresher candidates.
The agent enables companies to define a job role and required skills, conduct a structured interview, and objectively evaluate candidate responses using transparent, explainable logic.
Unlike generic AI chatbots that arbitrarily score answers, this agent ensures role-specific, bias-aware, and reproducible evaluation, making it suitable for real-world hiring scenarios where accountability is important.
WHAT THE AGENT DOES?
i) Allows a company/jury to configure:
Job role (via dropdown)
Required skills (via dropdown)
Conducts a structured interview with 5 standard HR + technical questions
ii) Evaluates answers using:
Skill alignment checks
Concept-level keyword matching
Detection of random / low-effort responses
iii) Produces:
Per-question score (out of 10)
Total score (out of 50)
Clear Qualified / Not Qualified decision
Provides a reset option to test multiple candidates easily

2. KEY FEATURES AND LIMITATIONS:
i) KEY FEATURES:
Job role & skill-based configuration
Structured interview with 5 standard questions
Detection of random/irrelevant answers
Transparent, rule-based scoring
Clear qualification decision

ii) LIMITATIONS:
Text-based evaluation only
Keyword-based matching (no deep semantic NLP)
Does not prevent intentional misuse (e.g., external help)
Designed for pre-screening, not final candidate selection

3. TECH STACK AND TOOLS USED:
Python – core logic
Streamlit – UI and interaction
Rule-based evaluation logic – explainable AI
GitHub – version control

4. SETUP AND INSTRUCTIONS:
This project is implemented as a local Streamlit web application.
Python 3.x installed on the system in PyCharm Community.
Steps to Run the Application
1. Clone the repository
2. Install required dependency: pip install streamlit
3. Run the application using: streamlit run app.py
4. Open the browser and access the application at:
   http://localhost:8501
The interface allows the jury/company to configure job roles and skills, conduct interview evaluation, and view qualification results interactively.
[OR] 
Page can be directly reached with this link:
https://answer-evaluation-demo-zo4r9azmcu3imuxe4b4kun.streamlit.app/

5. POTENTIAL IMPROVEMENTS:
Semantic similarity scoring using transformer-based models
Voice input to analyze confidence and communication skills
Resume-to-skill auto-mapping
Admin dashboard to view multiple evaluations
Anti-cheating mechanisms (time limits, plagiarism checks)
Deployment on Streamlit Cloud
