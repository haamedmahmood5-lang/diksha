import streamlit as st
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App Configuration
st.set_page_config(
    page_title="Skill Wallet - Legal-Ease Panel",
    page_icon="⚖️",
    layout="wide"
)

# Initialize Gemini Client if API key is present
API_KEY = os.getenv("GEMINI_API_KEY") or st.sidebar.text_input("Enter Gemini API Key:", type="password")
client = genai.Client(api_key=API_KEY) if API_KEY else None

# Mock Database / Session State for the "Skill Wallet"
if "verified_skills" not in st.session_state:
    st.session_state.verified_skills = [
        {"id": "SK-9081", "skill": "Contract Drafting & Review", "authority": "Bar Council Verified", "status": "Active ✅"},
        {"id": "SK-4412", "skill": "Corporate Compliance (MCA)", "authority": "ICSI Validation", "status": "Active ✅"},
        {"id": "SK-2391", "skill": "Arbitration & Dispute Resolution", "authority": "Indian Institute of Arbitration", "status": "Pending Review ⏳"}
    ]

# --- UI HEADER ---
st.title("⚖️ Skill Wallet: Legal-Ease Platform")
st.caption("Secure Professional Credentialing & AI-Assisted Legal Workflows")
st.markdown("---")

# --- SIDEBAR: Profile & Wallet Stats ---
st.sidebar.header("👤 Professional Profile")
st.sidebar.image("https://unsplash.com", width=100, caption="Adv. Rajesh Kumar")
st.sidebar.markdown("**BCI Registration:** MAH/4829/2022")
st.sidebar.markdown("**Wallet Status:** Verified 🔒")

# --- MAIN LAYOUT: TABS ---
tab1, tab2, tab3 = st.tabs(["💳 My Skill Wallet", "🔍 AI Document Assessor", "📜 Issuance Logs"])

# TAB 1: Skill Wallet Display
with tab1:
    st.subheader("Your Verified Legal Credentials")
    st.info("These credentials are tied to your decentralized Skill Wallet ID and cryptographically signed.")
    
    # Display credentials in card formats
    cols = st.columns(3)
    for idx, sk in enumerate(st.session_state.verified_skills):
        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"### {sk['skill']}")
                st.markdown(f"**ID:** `{sk['id']}`")
                st.markdown(f"**Issuer:** {sk['authority']}")
                st.markdown(f"**Status:** {sk['status']}")
                
    # Add a New Skill for verification
    st.markdown("### ➕ Claim New Certification")
    with st.form("add_skill_form"):
        new_skill = st.text_input("Skill / Certification Name")
        issuer = st.text_input("Issuing Authority (e.g., NALSAR, Bar Council)")
        doc_proof = st.file_uploader("Upload Certificate Proof (PDF)", type=["pdf"])
        submit = st.form_submit_button("Submit to Wallet for Verification")
        
        if submit and new_skill and issuer:
            st.session_state.verified_skills.append({
                "id": f"SK-{os.urandom(2).hex().upper()}",
                "skill": new_skill,
                "authority": issuer,
                "status": "Pending Review ⏳"
            })
            st.success(f"Successfully requested verification for '{new_skill}'!")
            st.rerun()

# TAB 2: AI Document Assessor
with tab2:
    st.subheader("AI-Powered Legal Clause Analysis")
    st.markdown("Upload legal drafts or paste text below to parse clauses and map required legal skill compliance.")
    
    doc_text = st.text_area("Paste Legal Agreement/Contract Text Here:", height=200, placeholder="E.g., NDA, Employment Contract, Rental Agreement...")
    
    if st.button("Analyze Document Requirements"):
        if not client:
            st.error("Please provide a valid Gemini API Key in the sidebar to run the analysis.")
        elif not doc_text.strip():
            st.warning("Please paste some legal text to analyze.")
        else:
            with st.spinner("Analyzing document structure and verifying compliance matches..."):
                try:
                    prompt = f"""
                    You are an expert AI Legal Consultant. Analyze the following contract text. 
                    1. Highlight the core legal risks or ambiguities.
                    2. List the specific legal 'Skills' or 'Certifications' an advocate must possess in their Skill Wallet to safely execute or litigate this contract (e.g., Corporate Law, Intellectual Property Law).
                    
                    Contract text:
                    {doc_text}
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    
                    st.markdown("### 📋 AI Assessment Result")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")

# TAB 3: Issuance Logs & Audit Trail
with tab3:
    st.subheader("Cryptographic Audit Trail")
    st.markdown("Every interaction, skill issuance, and digital signature is logged below for institutional compliance.")
    
    audit_data = [
        {"Timestamp": "2026-09-28 10:14:02", "Action": "Wallet Created", "Hash": "0x8f3c...a821"},
        {"Timestamp": "2026-09-28 11:30:15", "Action": "Skill SK-9081 Verified by BCI", "Hash": "0x4e2a...77b1"},
        {"Timestamp": "2026-09-28 14:22:09", "Action": "Skill SK-4412 Minted to Wallet", "Hash": "0x91da...cc34"},
    ]
    st.table(audit_data)
