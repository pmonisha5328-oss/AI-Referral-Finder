import streamlit as st
from src.parser import extract_text

st.set_page_config(
    page_title="AI Referral Finder",
    page_icon="🚀",
    layout="wide"
)

# =====================
# CUSTOM CSS
# =====================

st.markdown("""
<style>

html {
    scroll-behavior: smooth;
}

.stApp {
    background: linear-gradient(
        135deg,
        #021024,
        #052659,
        #021024
    );
}

/* Hide Streamlit menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* HERO SECTION */

.hero {
    height: 100vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
}

.main-title {
    font-size: 6rem;
    font-weight: 900;
    color: white;
    animation: fadeInUp 2s ease;
}

.subtitle {
    font-size: 1.5rem;
    color: #dbeafe;
    margin-top: 20px;
    animation: fadeInUp 3s ease;
}

/* Fade Animation */
@keyframes fadeInUp {
    from {
        opacity:0;
        transform: translateY(80px);
    }

    to {
        opacity:1;
        transform: translateY(0);
    }
}

/* Bouncing Arrow */
.arrow {
    font-size: 2rem;
    color: white;
    margin-top: 50px;
    animation: bounce 1.5s infinite;
}

@keyframes bounce {
    0%,20%,50%,80%,100% {
        transform: translateY(0);
    }

    40% {
        transform: translateY(-12px);
    }

    60% {
        transform: translateY(-6px);
    }
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* Upload section spacing */
.upload-section {
    padding-top: 80px;
}

</style>
""", unsafe_allow_html=True)

# =====================
# HERO SECTION
# =====================

st.markdown("""
<div id="hero" class="hero">

<div class="main-title">
🚀 AI Referral Finder
<br>
& Outreach Assistant
</div>

<div class="subtitle">
Find referrals. Build connections.
<br>
Generate personalized outreach.
</div>

<div class="arrow">
⬇
</div>

</div>

<script>

window.addEventListener('load', function() {

    setTimeout(function() {

        document.addEventListener("click", function() {

            const uploadSection =
            window.parent.document.getElementById("upload-section");

            if(uploadSection){
                uploadSection.scrollIntoView({
                    behavior: "smooth"
                });
            }

        });

    }, 500);

});

</script>

""", unsafe_allow_html=True)

# =====================
# FEATURES
# =====================

st.markdown("## ✨ What This AI Does")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info("🎯 Resume Analysis")

with c2:
    st.info("🤝 Referral Discovery")

with c3:
    st.info("✉️ Outreach Messages")

with c4:
    st.info("📈 Networking Insights")

st.markdown("---")

# =====================
# UPLOAD SECTION
# =====================

st.markdown(
    '<div id="upload-section" class="upload-section"></div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)

with left:

    st.markdown("### 📄 Upload Resume")

    resume = st.file_uploader(
        "Choose PDF Resume",
        type=["pdf"]
    )

with right:

    st.markdown("### 💼 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

st.markdown("")

analyze = st.button(
    "🚀 Analyze Profile",
    use_container_width=True
)

# =====================
# ANALYSIS
# =====================

if analyze:

    if resume is None:
        st.warning("Please upload a resume.")

    else:

        resume_text = extract_text(resume)

        st.success("Resume uploaded successfully!")

        st.markdown("## 📋 Extracted Resume Text")

        st.text_area(
            "",
            resume_text,
            height=350
        )

        st.markdown("---")

        st.markdown("## 🤖 AI Analysis (Coming Soon)")

        m1, m2, m3 = st.columns(3)

        with m1:
            st.metric("Match Score", "--")

        with m2:
            st.metric("Referral Opportunities", "--")

        with m3:
            st.metric("Outreach Messages", "--")