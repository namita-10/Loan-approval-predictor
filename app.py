import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="LoanWise | Loan Predictor",
    page_icon="🏦",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: #F4F7FB;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* HERO */
.hero {
    background: linear-gradient(120deg, #102A43, #164E63);
    padding: 28px 38px;
    border-radius: 18px;
    color: white;
    margin-bottom: 20px;
}

.hero-label {
    color: #D9EAF2;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 1px;
}

.hero h1 {
    color: white !important;
    font-size: 38px;
    font-weight: 800;
    line-height: 1.2;
    margin: 12px 0;
}

.hero p {
    color: #D9EAF2;
    font-size: 15px;
    margin-bottom: 0;
}

/* PANELS */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #DFE8F3;
    border-radius: 14px;
    padding: 16px;
}

/* HEADINGS */
.section-title {
    color: #102A43;
    font-size: 23px;
    font-weight: 700;
}

.section-subtitle {
    color: #627D98;
    font-size: 13px;
    margin-bottom: 12px;
}

h3, h4 {
    color: #102A43 !important;
}

/* COMPACT FORM */
div[data-testid="stForm"] {
    border: none;
    padding: 0;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.65rem;
}

label {
    color: #243B53 !important;
    font-weight: 600 !important;
}

/* BUTTON */
div[data-testid="stFormSubmitButton"] > button {
    background-color: #0F766E !important;
    color: #FFFFFF !important;
    border: 2px solid #0F766E !important;
    border-radius: 9px !important;
    min-height: 48px;
    font-size: 15px;
    font-weight: 700;
    transition: 0.2s;
}

div[data-testid="stFormSubmitButton"] > button:hover {
    background-color: #115E59 !important;
    color: #FFFFFF !important;
    border-color: #115E59 !important;
}

div[data-testid="stFormSubmitButton"] > button:focus,
div[data-testid="stFormSubmitButton"] > button:active {
    background-color: #0F766E !important;
    color: #FFFFFF !important;
}

/* RESULT CARDS */
.approved-card {
    background: #ECFDF5;
    border: 1px solid #A7F3D0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin: 10px 0;
}

.approved-card h2 {
    color: #047857;
    margin: 8px 0;
    font-size: 27px;
}

.approved-card p {
    color: #065F46;
    font-size: 14px;
    margin-bottom: 0;
}

.rejected-card {
    background: #FFF1F2;
    border: 1px solid #FECDD3;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin: 10px 0;
}

.rejected-card h2 {
    color: #BE123C;
    margin: 8px 0;
    font-size: 27px;
}

.rejected-card p {
    color: #9F1239;
    font-size: 14px;
    margin-bottom: 0;
}

/* WHY CARD */
.why-card {
    background: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 10px;
    padding: 16px;
    margin-top: 12px;
}

.why-card h4 {
    color: #1D4ED8 !important;
    margin-top: 0;
}

/* NOTE */
.note-card {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 14px;
    margin-top: 12px;
    color: #486581;
    font-size: 13px;
}

/* HOW IT WORKS */
.step-card {
    background: #F4F8FC;
    border-radius: 10px;
    padding: 14px 8px;
    text-align: center;
    min-height: 115px;
}

.step-number {
    background: #DCEEFE;
    color: #0F766E;
    font-size: 17px;
    font-weight: 700;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    margin: auto auto 8px auto;
    padding-top: 5px;
}

.step-card h4 {
    font-size: 13px;
    margin: 5px 0;
}

.step-card p {
    color: #627D98;
    font-size: 11px;
    margin-bottom: 0;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #829AB1;
    font-size: 11px;
    padding: 12px;
    margin-top: 12px;
}

/* REMOVE EXTRA STREAMLIT SPACING */
div[data-testid="stMarkdownContainer"] p {
    margin-bottom: 0.4rem;
}

hr {
    margin: 10px 0 !important;
    border-color: #E2E8F0 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="hero-label">LOANWISE &nbsp; | &nbsp; SMART FINANCE</div>
    <h1>Your Loan Eligibility,<br>Simplified.</h1>
    <p>
        Explore your loan approval prediction using a
        Machine Learning-powered assessment.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- MAIN LAYOUT ----------------
left, right = st.columns([1.15, 1], gap="medium")


# ==================================================
# LEFT PANEL - APPLICANT FORM
# ==================================================
with left:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">Applicant Information</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Complete your details to generate a loan prediction.'
            '</div>',
            unsafe_allow_html=True
        )

        with st.form("loan_form"):

            # PERSONAL DETAILS
            st.markdown("#### Personal Details")

            c1, c2 = st.columns(2)

            with c1:
                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=100,
                    value=25
                )

                marital_status = st.selectbox(
                    "Marital Status",
                    ["Single", "Married", "Other"]
                )

                dependents = st.selectbox(
                    "Number of Dependents",
                    ["0", "1", "2", "3+"]
                )

            with c2:
                education = st.selectbox(
                    "Education",
                    ["Graduate", "Not Graduate"]
                )

                employment_type = st.selectbox(
                    "Employment Type",
                    ["Salaried", "Self-Employed", "Business", "Other"]
                )

                property_area = st.selectbox(
                    "Property Area",
                    ["Urban", "Semi-Urban", "Rural"]
                )

            st.divider()

            # FINANCIAL DETAILS
            st.markdown("#### Financial Details")

            c3, c4 = st.columns(2)

            with c3:
                income = st.number_input(
                    "Annual Income (₹)",
                    min_value=0,
                    max_value=100000000,
                    value=500000,
                    step=25000
                )

                credit_score = st.slider(
                    "Credit Score",
                    min_value=300,
                    max_value=900,
                    value=750,
                    step=5
                )

            with c4:
                existing_emi = st.number_input(
                    "Monthly Existing EMI (₹)",
                    min_value=0,
                    max_value=10000000,
                    value=0,
                    step=1000
                )

                other_income = st.number_input(
                    "Other Annual Income (₹)",
                    min_value=0,
                    max_value=100000000,
                    value=0,
                    step=10000
                )

            st.divider()

            # LOAN DETAILS
            st.markdown("#### Loan Details")

            c5, c6 = st.columns(2)

            with c5:
                loan_amount = st.number_input(
                    "Requested Loan Amount (₹)",
                    min_value=0,
                    max_value=100000000,
                    value=200000,
                    step=10000
                )

                loan_term = st.selectbox(
                    "Loan Tenure",
                    [
                        "12 Months",
                        "24 Months",
                        "36 Months",
                        "60 Months",
                        "120 Months",
                        "240 Months"
                    ]
                )

            with c6:
                loan_purpose = st.selectbox(
                    "Loan Purpose",
                    [
                        "Home Purchase",
                        "Education",
                        "Vehicle",
                        "Personal",
                        "Business",
                        "Other"
                    ]
                )

                employment_years = st.slider(
                    "Employment Experience (Years)",
                    min_value=0,
                    max_value=50,
                    value=5
                )

            st.write("")

            consent = st.checkbox(
                "I confirm that the information provided is accurate."
            )

            submitted = st.form_submit_button(
                "Proceed to Loan Prediction  →",
                use_container_width=True
            )


# ==================================================
# RIGHT PANEL - PREDICTION SUMMARY
# ==================================================
with right:

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">Prediction Summary</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Your prediction will appear here after submission.'
            '</div>',
            unsafe_allow_html=True
        )

        # ---------------- RESULT ----------------
        if submitted:

            if not consent:
                st.warning(
                    "Please confirm your information before proceeding."
                )

            elif income <= 0 or loan_amount <= 0:
                st.warning(
                    "Annual income and loan amount must be greater than zero."
                )

            else:
                input_data = {
                    "income": income,
                    "credit_score": credit_score,
                    "loan_amount": loan_amount,
                    "employment_years": employment_years
                }

                try:
                    with st.spinner("Analyzing your details..."):

                        response = requests.post(
                            "http://127.0.0.1:8000/predict",
                            json=input_data,
                            timeout=15
                        )

                    if response.status_code == 200:

                        result = response.json()["result"]

                        # APPROVED
                        if result == "Loan Approved":

                            st.markdown("""
                            <div class="approved-card">
                                <div style="font-size:35px;">✓</div>
                                <h2>Loan Approved</h2>
                                <p>
                                    The model predicts an approved
                                    loan status for the details provided.
                                </p>
                            </div>
                            """, unsafe_allow_html=True)

                            st.markdown("""
                            <div class="why-card">
                                <h4>✓ Prediction Summary</h4>
                                <p style="color:#1E40AF;font-size:14px;">
                                    The submitted financial details match
                                    the approval patterns learned by
                                    the model.
                                </p>
                            </div>
                            """, unsafe_allow_html=True)

                        # NOT APPROVED
                        else:

                            st.markdown("""
                            <div class="rejected-card">
                                <div style="font-size:35px;">✕</div>
                                <h2>Loan Not Approved</h2>
                                <p>
                                    The model predicts a not-approved
                                    loan status for the details provided.
                                </p>
                            </div>
                            """, unsafe_allow_html=True)

                            # Potential factors to review.
                            # These are indicative checks, NOT
                            # the model's exact explanation.
                            possible_factors = []

                            if credit_score < 650:
                                possible_factors.append(
                                    "Credit score is relatively low. "
                                    "Review your credit history."
                                )

                            if income > 0 and loan_amount / income > 5:
                                possible_factors.append(
                                    "Requested loan amount is high "
                                    "compared with annual income."
                                )

                            if employment_years < 1:
                                possible_factors.append(
                                    "Limited employment experience "
                                    "may require further review."
                                )

                            st.markdown("""
                            <div class="why-card">
                                <h4>Why was the loan not approved?</h4>
                            </div>
                            """, unsafe_allow_html=True)

                            if possible_factors:

                                for factor in possible_factors:
                                    st.markdown(
                                        f"- {factor}"
                                    )

                            else:
                                st.markdown(
                                    "The model returned a not-approved "
                                    "prediction, but the current model "
                                    "does not provide an exact reason code."
                                )

                            st.caption(
                                "These are possible factors to review, "
                                "not confirmed reasons from the model."
                            )

                        # IMPORTANT NOTE
                        st.markdown("""
                        <div class="note-card">
                            <b>Important Note</b><br>
                            This prediction is for educational
                            demonstration only. It is not an actual
                            bank decision.
                        </div>
                        """, unsafe_allow_html=True)

                    else:
                        st.error(
                            f"Prediction failed. Status: "
                            f"{response.status_code}"
                        )

                except requests.exceptions.ConnectionError:
                    st.error(
                        "Backend is not running. Start FastAPI first."
                    )

                except requests.exceptions.Timeout:
                    st.error(
                        "Request timed out. Please try again."
                    )

                except Exception as e:
                    st.error(f"Unexpected error: {e}")

        # ---------------- INITIAL STATE ----------------
        else:

            st.markdown("""
            <div style="
                background:#F4F8FC;
                border:1px dashed #CBD5E1;
                border-radius:12px;
                padding:22px;
                text-align:center;
                margin:10px 0;
            ">
                <div style="font-size:35px;">🏦</div>
                <h4 style="color:#102A43;">Ready for Assessment</h4>
                <p style="color:#627D98;font-size:13px;">
                    Enter your applicant details and proceed
                    to view your loan prediction.
                </p>
            </div>
            """, unsafe_allow_html=True)

        # ---------------- HOW IT WORKS ----------------
        st.divider()

        st.markdown("### How It Works")

        step1, step2, step3 = st.columns(3)

        with step1:
            st.markdown("""
            <div class="step-card">
                <div class="step-number">1</div>
                <h4>Enter Details</h4>
                <p>Fill in your applicant information.</p>
            </div>
            """, unsafe_allow_html=True)

        with step2:
            st.markdown("""
            <div class="step-card">
                <div class="step-number">2</div>
                <h4>Analyze</h4>
                <p>Submit details for assessment.</p>
            </div>
            """, unsafe_allow_html=True)

        with step3:
            st.markdown("""
            <div class="step-card">
                <div class="step-number">3</div>
                <h4>Get Result</h4>
                <p>View your prediction instantly.</p>
            </div>
            """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    LOANWISE &nbsp; | &nbsp; Machine Learning Project<br>
    Built with Python · FastAPI · Streamlit · Random Forest
</div>
""", unsafe_allow_html=True)