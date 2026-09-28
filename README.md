# Skill Wallet: Legal-Ease Platform

An AI-augmented digital portfolio ecosystem built to verify, manage, and audit professional credentials for legal service providers (advocates, arbitrators, notaries, and corporate consultants). 

This portal maps specific legal skillsets directly to complex client document requirements using generative AI.

## 🚀 Key Features

- **Decentralized Skill Wallet:** Store and display verified, tamper-proof professional credentials (e.g., Bar Council registrations, specialized legal certifications).
- **AI Document Assessor:** Integrates with **Google Gemini 2.5** to evaluate incoming legal agreements, flag structural risks, and dynamically specify the "Skill Wallet" competencies required to draft or audit the document.
- **Verification Pipeline:** Simulates institutional workflows where advocates submit document proofs to get new skills verified and added to their profile.
- **Cryptographic Audit Log:** Provides a clear audit trail of credential history for regulatory compliance.

## 🛠️ Tech Stack

- **Frontend/Dashboard:** Streamlit (Python UI)
- **AI Analytics:** Google GenAI SDK (`gemini-2.5-flash`)
- **Environment Management:** Python-Dotenv

## 📦 Local Installation

1. **Clone or Download the Project:**
   Ensure you have `app.py`, `requirements.txt`, and `README.md` in one directory.

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add your Google Gemini API Key:
   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```
   *(Alternatively, you can input the API Key directly into the application's sidebar interface when running).*

4. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the Portal:**
   Open your browser and navigate to the local address displayed in your terminal (typically `http://localhost:8501`).
