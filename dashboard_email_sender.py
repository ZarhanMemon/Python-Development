# ===========================
# 📌 IMPORTING LIBRARIES
# ===========================

import streamlit as st
import smtplib
from email.message import EmailMessage
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64  # Used to encode images directly into the HTML email body

# ===========================
# 📌 PAGE CONFIGURATION
# ===========================

st.set_page_config(page_title="Email Dashboard", layout="wide")
st.title("📧 Smart Email Dashboard (With Analytics)")


# ===========================
# 📌 SIDEBAR CONFIGURATION
# ===========================

with st.sidebar:
    st.header("SMTP Configuration")
    sender_email = st.text_input("Sender Email", value="technologyxyz18@gmail.com")
    app_password = st.text_input("App Password", type="password", value="wushslrqfkaoaxcq")


# ===========================
# 📌 SAMPLE DATA CREATION (PANDAS)
# ===========================

data = {
    "Name": ["Amit", "Sara", "Rahul", "Neha", "Raj", "Kiran"],
    "Email": [
        "amit@gmail.com",
        "sara@gmail.com",
        "rahul@gmail.com",
        "neha@gmail.com",
        "raj@gmail.com",
        "kiran@gmail.com"
    ],
    "Age": [21, 22, 20, 23, 24, 22],
    "City": ["Pune", "Mumbai", "Delhi", "Bangalore", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)


# ===========================
# 📌 KPI METRICS (DASHBOARD STATS)
# ===========================

total_users = len(df)
unique_cities = df["City"].nunique()
avg_age = round(df["Age"].mean(), 1)

col1, col2, col3 = st.columns(3)
col1.metric("Total Users", total_users)
col2.metric("Unique Cities", unique_cities)
col3.metric("Avg Age", avg_age)

st.divider()


# ===========================
# 📌 DATA TABLE VIEW
# ===========================

st.subheader("📊 Customer Data")
st.dataframe(df, use_container_width=True)


# ===========================
# 📌 DATA VISUALIZATION SECTION
# ===========================

st.subheader("📈 Analytics Dashboard")
colA, colB = st.columns(2)

# Helper function to convert Matplotlib figures to Base64 strings for HTML injection
def fig_to_base64(figure):
    img_buf = io.BytesIO()
    figure.savefig(img_buf, format="png", bbox_inches="tight")
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.read()).decode("utf-8")
    return img_base64

# 📊 BAR CHART - CITY DISTRIBUTION
with colA:
    st.write("### City Distribution")
    city_counts = df["City"].value_counts()
    fig1, ax1 = plt.subplots()
    city_counts.plot(kind="bar", ax=ax1, color="#4F8BF9")
    ax1.set_xlabel("City")
    ax1.set_ylabel("Users")
    st.pyplot(fig1)
    chart1_base64 = fig_to_base64(fig1)

# 🥧 PIE CHART - CITY SHARE
with colB:
    st.write("### City Share")
    fig2, ax2 = plt.subplots()
    df["City"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    ax2.set_ylabel("")
    st.pyplot(fig2)
    chart2_base64 = fig_to_base64(fig2)

# 📊 HISTOGRAM - AGE DISTRIBUTION
st.subheader("📊 Age Distribution")
fig3, ax3 = plt.subplots()
ax3.hist(df["Age"], bins=5, color="skyblue", edgecolor="black") 
ax3.set_xlabel("Age")
ax3.set_ylabel("Count")
st.pyplot(fig3)
chart3_base64 = fig_to_base64(fig3)

# Clean up all matplotlib plots from memory after rendering
plt.close('all')


# ===========================
# 📌 EMAIL SENDING SECTION
# ===========================

st.divider()
receiver_email = "zarhanmemon2006@gmail.com"
st.info(f"Receiver Email: {receiver_email}")
subject = "📊 Live Analytics Dashboard Report"

# 🚀 Action Button prevents the email from automatically sending on every page refresh!
if True:  
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        # Clean HTML conversion of DataFrame (without the invalid direct 'style' argument)
        df_html = df.to_html(index=False, classes='dataframe', border=0)

        # 📄 DESIGNING THE HTML EMAIL BODY
        # Note: 'display: flex' has poor support in email clients (like older Outlook versions), 
        # so we use traditional HTML styling/tables or standard divs with inline blocks for bulletproof rendering.
        html_body = f"""
        <html>
            <head>
                <style>
                    .dataframe {{
                        border-collapse: collapse; 
                        width: 100%; 
                        border: 1px solid #DDD; 
                        text-align: left;
                        font-family: Arial, sans-serif;
                    }}
                    .dataframe th {{ 
                        background-color: #F2F2F2; 
                        padding: 8px; 
                        font-weight: bold; 
                        border-bottom: 2px solid #DDD; 
                    }}
                    .dataframe td {{ 
                        padding: 8px; 
                        border-bottom: 1px solid #DDD; 
                    }}
                </style>
            </head>
            <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px;">
                <h2 style="color: #1E3A8A; border-bottom: 2px solid #1E3A8A; padding-bottom: 10px;">
                    📧 Smart Email Dashboard Report
                </h2>
                
                <div style="margin: 20px 0; overflow: hidden;">
                    <div style="background: #F3F4F6; padding: 15px; border-radius: 8px; text-align: center; width: 28%; float: left; border: 1px solid #E5E7EB; margin-right: 2%;">
                        <b style="color: #4B5563;">Total Users</b><br>
                        <span style="font-size: 24px; font-weight: bold; color: #2563EB;">{total_users}</span>
                    </div>
                    <div style="background: #F3F4F6; padding: 15px; border-radius: 8px; text-align: center; width: 28%; float: left; border: 1px solid #E5E7EB; margin-right: 2%;">
                        <b style="color: #4B5563;">Unique Cities</b><br>
                        <span style="font-size: 24px; font-weight: bold; color: #2563EB;">{unique_cities}</span>
                    </div>
                    <div style="background: #F3F4F6; padding: 15px; border-radius: 8px; text-align: center; width: 28%; float: left; border: 1px solid #E5E7EB;">
                        <b style="color: #4B5563;">Avg Age</b><br>
                        <span style="font-size: 24px; font-weight: bold; color: #2563EB;">{avg_age}</span>
                    </div>
                </div>
                
                <div style="clear: both;"></div>

                <h3>📊 Customer Data</h3>
                <div style="overflow-x: auto; margin-bottom: 25px;">
                    {df_html}
                </div>

                <h3>📈 Analytics Dashboard Charts</h3>
                <div style="margin: 20px 0; text-align: center;">
                    <h4 style="text-align: left; color: #4B5563;">City Distribution & Share</h4>
                    <img src="data:image/png;base64,{chart1_base64}" width="47%" style="margin-right: 2%; display: inline-block; vertical-align: top;" />
                    <img src="data:image/png;base64,{chart2_base64}" width="47%" style="display: inline-block; vertical-align: top;" />
                </div>
                
                <div style="margin: 30px 0; text-align: center;">
                    <h4 style="text-align: left; color: #4B5563;">Age Distribution Histogram</h4>
                    <img src="data:image/png;base64,{chart3_base64}" width="95%" />
                </div>

                <hr style="border: 0; border-top: 1px solid #E5E7EB; margin-top: 40px;">
                <p style="font-size: 12px; color: #9CA3AF; text-align: center;">Generated and Sent via Streamlit Automated SMTP Engine.</p>
            </body>
        </html>
        """
        
        # Set content fallback and HTML alternate
        msg.set_content("Please enable HTML viewing to see this dashboard report.") 
        msg.add_alternative(html_body, subtype="html")

        # Connect and dispatch
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password.replace(" ", ""))
            smtp.send_message(msg)

        st.success(f"Entire dashboard cleanly compiled and sent to {receiver_email} ✅")

    except Exception as e:
        st.error(f"Failed to dispatch: {str(e)}")