import streamlit as st
import datetime

# --- Page Config ---
st.set_page_config(page_title="Assignment Alarm", page_icon="⏰", layout="centered")

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .title {
            text-align: center;
            color: #333;
            font-size: 48px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 20px;
            margin-bottom: 20px;
        }
        .assignment-box {
            background-color: #ffffff;
            border-left: 6px solid #4CAF50;
            padding: 10px 20px;
            margin-bottom: 15px;
            border-radius: 5px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="title">📚 Assignment Alarm</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Track your deadlines and stay ahead!</div>', unsafe_allow_html=True)

# --- Session State Setup ---
if 'assignments' not in st.session_state:
    st.session_state.assignments = []

# --- Add Assignment ---
with st.expander("➕ Add New Assignment", expanded=True):
    with st.form("add_assignment"):
        name = st.text_input("Assignment Name")
        due_date = st.date_input("Due Date", min_value=datetime.date.today())
        submitted = st.form_submit_button("Add Assignment")

        if submitted and name:
            st.session_state.assignments.append({
                "name": name,
                "due_date": due_date
            })
            st.success(f"✅ '{name}' added for {due_date}!")

# --- Show Assignments ---
if st.session_state.assignments:
    st.markdown("### 🗂️ Upcoming Assignments")

    today = datetime.date.today()
    for a in st.session_state.assignments:
        days_left = (a["due_date"] - today).days
        if days_left < 0:
            status = f"❌ Overdue by {-days_left} day(s)"
            color = "#e74c3c"
        elif days_left == 0:
            status = "🚨 Due TODAY!"
            color = "#f39c12"
        elif days_left <= 2:
            status = f"⚠️ Due in {days_left} day(s)"
            color = "#f1c40f"
        else:
            status = f"📅 Due in {days_left} day(s)"
            color = "#2ecc71"

        st.markdown(f"""
            <div class="assignment-box" style="border-left-color: {color}">
                <strong>{a['name']}</strong> — {a['due_date']}<br>
                <span style="color:{color}">{status}</span>
            </div>
        """, unsafe_allow_html=True)
else:
    st.info("No assignments added yet.")

# --- Clear Button ---
st.markdown("---")
if st.button("🗑️ Clear All Assignments"):
    st.session_state.assignments.clear()
    st.success("✅ All assignments cleared.")
