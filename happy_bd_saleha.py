import streamlit as st
import random
import time
from datetime import datetime, date
import base64
from PIL import Image
import io
import pytz
import requests
from io import BytesIO
import numpy as np
import math
import os
import hashlib

# Page configuration
st.set_page_config(
    page_title="✨ Saleha's Special Day ✨",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium animations and styling
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Dancing+Script:wght@700&display=swap');
    
    body {
        overflow-x: hidden;
    }
    
    .main {
        background: linear-gradient(135deg, #f0f8f0 0%, #d4e6d4 100%);
    }

    .stApp {
        background: radial-gradient(ellipse at center, #f0f8f0 0%, #d4e6d4 100%);
    }
    
    .floating-element {
        animation: float 6s ease-in-out infinite;
        transform-origin: center;
    }
    
    @keyframes float {
        0% { transform: translateY(0) rotate(0deg); }
        25% { transform: translateY(-10px) rotate(2deg); }
        50% { transform: translateY(0) rotate(0deg); }
        75% { transform: translateY(10px) rotate(-2deg); }
        100% { transform: translateY(0) rotate(0deg); }
    }
    
    .premium-container {
        border: 1px solid rgba(152, 251, 152, 0.3);
        background-color: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05), 0 1px 8px rgba(0,0,0,0.05), 0 0 1px rgba(0,0,0,0.05);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        transition: all 0.5s ease;
    }
    
    .premium-container:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1), 0 5px 15px rgba(0,0,0,0.05);
    }

    .reflection {
        position: relative;
        overflow: hidden;
    }
    
    .reflection::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 50%;
        height: 100%;
        background: linear-gradient(
            to right,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.3) 100%
        );
        transform: skewX(-25deg);
        animation: reflection 6s infinite;
    }
    
    @keyframes reflection {
        0% { left: -100%; }
        20%, 100% { left: 100%; }
    }
    
    .shimmer-text {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        font-size: 4rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .elegant-wish {
        font-family: 'Dancing Script', cursive;
        font-size: 2.5rem;
        color: #98fb98;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        margin: 30px 0;
    }
    
    .countdown {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        margin: 30px 0;
        color: #333;
    }
    
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    
    .countdown-box {
        background: linear-gradient(145deg, #f5f5f5, #ffffff);
        box-shadow: 8px 8px 16px #d9d9d9, -8px -8px 16px #ffffff;
        color: #333;
        padding: 20px;
        border-radius: 15px;
        min-width: 100px;
        text-align: center;
    }
    
    .countdown-value {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 5px;
        background: linear-gradient(to right, #98fb98, #90ee90);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .countdown-label {
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #666;
    }
    
    .premium-button {
        background: linear-gradient(to right, #98fb98, #90ee90);
        color: #fff;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: none;
        border-radius: 50px;
        padding: 12px 30px;
        box-shadow: 0 10px 20px rgba(152, 251, 152, 0.3);
        transition: all 0.3s ease;
    }
    
    .premium-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(152, 251, 152, 0.4);
    }
    
    .gold-border {
        border: 2px solid #98fb98;
        border-radius: 20px;
        padding: 30px;
        position: relative;
    }
    
    .gold-border::before {
        content: "";
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        border-radius: 20px;
        background: linear-gradient(45deg, #98fb98, #90ee90, #98fb98, #90ee90);
        background-size: 400% 400%;
        z-index: -1;
        animation: border-shift 5s linear infinite;
    }
    
    @keyframes border-shift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    
    .message-card {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        font-family: 'Montserrat', sans-serif;
        position: relative;
        overflow: hidden;
    }
    
    .message-card::before {
        content: "";
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(152, 251, 152, 0.3) 0%, rgba(255, 255, 255, 0) 70%);
        top: -100px;
        left: -100px;
    }
    
    .message-card::after {
        content: "";
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(152, 251, 152, 0.2) 0%, rgba(255, 255, 255, 0) 70%);
        bottom: -100px;
        right: -100px;
    }
    
    .rose-gold-text {
        background: linear-gradient(to right, #98fb98, #90ee90);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
    }
    
    .photo-frame {
        border: 10px solid white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transform: rotate(2deg);
        transition: all 0.5s ease;
    }
    
    .photo-frame:hover {
        transform: rotate(0deg) scale(1.05);
    }
    
    .photo-placeholder {
        width: 100%;
        max-width: 560px;
        aspect-ratio: 1 / 1;
        background: linear-gradient(145deg, #f0f8f0, #d4e6d4);
        border: 2px solid #98fb98;
        border-radius: 16px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.06);
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto;
        position: relative;
    }

    .photo-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .shake-animation {
        animation: shake 5s ease-in-out infinite;
        transform-origin: center;
    }
    
    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        5%, 15% { transform: rotate(-5deg); }
        10%, 20% { transform: rotate(5deg); }
        25% { transform: rotate(0deg); }
    }
    
    .memory-polaroid {
        background: white;
        padding: 15px 15px 60px 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: rotate(random() * 10 - 5 + deg);
        transition: all 0.3s ease;
        position: relative;
        margin: 20px;
    }
    
    .memory-polaroid:hover {
        transform: scale(1.05) rotate(0deg);
        z-index: 10;
    }
    
    .memory-polaroid::after {
        content: "Memories";
        position: absolute;
        bottom: 20px;
        left: 0;
        right: 0;
        text-align: center;
        font-family: 'Dancing Script', cursive;
        font-size: 1.5rem;
        color: #333;
    }
    
    .sparkle {
        position: absolute;
        width: 20px;
        height: 20px;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E%3Cpath d='M10 0L12 7H19L13 12L15 20L10 15L5 20L7 12L1 7H8L10 0Z' fill='%23FFD700'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-size: contain;
        opacity: 0;
    }
    
    @keyframes sparkle-fade {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1); opacity: 1; }
        100% { transform: scale(0); opacity: 0; }
    }
    
    .cake-animation {
        animation: cake-float 3s ease-in-out infinite, cake-glow 2s ease-in-out infinite;
    }
    
    @keyframes cake-float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes cake-glow {
        0%, 100% { filter: drop-shadow(0 0 8px rgba(152, 251, 152, 0.7)); }
        50% { filter: drop-shadow(0 0 15px rgba(152, 251, 152, 1)); }
    }
    
    </style>
    """, unsafe_allow_html=True)

# Security: password verification
HASHED_PASSWORD = "53a2113962eb45c7f56822145457f8f12a6336557c62d59368095ec929a68a25"

def verify_password(plain_text: str) -> bool:
    try:
        return hashlib.sha256(plain_text.encode("utf-8")).hexdigest() == HASHED_PASSWORD
    except Exception:
        return False

# Function to auto-play audio from URL
def autoplay_audio_url(url):
    try:
        response = requests.get(url)
        audio_bytes = response.content
        b64 = base64.b64encode(audio_bytes).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)
    except Exception:
        st.error("Could not load background music. Please ensure you have an internet connection.")

# Function to generate premium confetti
def generate_confetti():
    confetti_html = ""
    colors = ["#98fb98", "#90ee90", "#98fb98", "#90ee90", "#C9A9A6"]
    
    for i in range(50):
        size = random.randint(5, 15)
        delay = random.uniform(0, 5)
        duration = random.uniform(3, 8)
        color = random.choice(colors)
        left_pos = random.randint(0, 100)
        opacity = random.uniform(0.6, 1)
        
        confetti_html += f"""
        <div style="
            position: fixed; 
            left: {left_pos}%; 
            top: -5%; 
            width: {size}px; 
            height: {size * 1.5}px; 
            background-color: {color}; 
            opacity: {opacity};
            animation: confetti-fall {duration}s {delay}s ease-in-out infinite;
            z-index: -1;
            transform: rotate({random.randint(0, 360)}deg);
        "></div>
        """
    
    st.markdown(confetti_html, unsafe_allow_html=True)

# Function to generate sparkles
def generate_sparkles():
    sparkle_html = ""
    
    for i in range(30):
        size = random.randint(10, 20)
        delay = random.uniform(0, 15)
        duration = random.uniform(2, 4)
        left_pos = random.randint(0, 100)
        top_pos = random.randint(0, 100)
        
        sparkle_html += f"""
        <div style="
            position: fixed; 
            left: {left_pos}%; 
            top: {top_pos}%; 
            width: {size}px; 
            height: {size}px;
            background-image: url('data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22%3E%3Cpath fill=%22%23FFD700%22 d=%22M12,1L9,9L1,12L9,15L12,23L15,15L23,12L15,9Z%22/%3E%3C/svg%3E');
            background-size: cover;
            animation: sparkle-fade {duration}s {delay}s ease-in-out infinite;
            z-index: 1;
        "></div>
        """
    
    st.markdown(sparkle_html, unsafe_allow_html=True)

# Premium birthday wish templates
def get_premium_birthday_wishes():
    return [
        "Happy Birthday, Saleha! May this year bring you all the success, joy, and adventure you deserve.",
        "To my amazing friend Saleha - may your birthday be filled with laughter, love, and everything that makes you smile.",
        "Another year older, another year wiser! Happy Birthday to the best friend anyone could ask for.",
        "On your special day, I want you to know how much you mean to me. Happy Birthday, Saleha!",
        "May your birthday be as awesome as you are, friend! Here's to another year of amazing memories together.",
        "Happy Birthday to my partner in crime, my best friend - Saleha!",
        "Today we celebrate you, friend! May your birthday bring you all the happiness and success you deserve.",
        "Another year of being the incredible person you are. Happy Birthday, Saleha!"
    ]

# Function to create fancy text with sparkle animation
def fancy_header(text, element_class="shimmer-text", tag="h1"):
    return f'<{tag} class="{element_class}">{text}</{tag}>'

# Personal memories and quotes for Waris
def get_personal_memories():
    return [
        "Remember when we used to hang out together? Those were the best times!",
        "Your determination and hard work always inspire me, Saleha.",
        "Thanks for always being there when I needed you most.",
        "Your sense of humor can brighten up any room, Saleha.",
        "You're not just my friend, you're my best friend.",
        "Watching you grow into the amazing person you are has been a privilege.",
        "Your kindness and generosity towards everyone around you is truly admirable.",
        "That time we stayed up all night talking about our dreams and future plans."
    ]

# Check if today is Saleha's birthday (you can modify the date as needed)
def is_birthday():
    # Use Pakistan timezone
    timezone = pytz.timezone('Asia/Karachi')
    today = datetime.now(timezone).date()
    # You can change this to Waris's actual birthday date
    # For example, if Waris's birthday is August 10th, change it to: return today.month == 8 and today.day == 10
    return today.month == 9 and today.day == 19  # Saleha's birthday is December 27th

# Calculate time until Saleha's birthday
def time_until_birthday():
    timezone = pytz.timezone('Asia/Karachi')
    now = datetime.now(timezone)
    current_year = now.year
    
    # Create birthday datetime object for this year (change the date to Waris's actual birthday)
    birthday = timezone.localize(datetime(current_year, 12, 27, 0, 0, 0))  # Saleha's birthday is December 27th
    
    # If birthday has already passed this year, look for next year
    if now > birthday:
        birthday = timezone.localize(datetime(current_year + 1, 12, 27, 0, 0, 0))  # Saleha's birthday is December 27th
    
    # Calculate time remaining
    delta = birthday - now
    
    # Extract days, hours, minutes and seconds
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Display premium countdown
def show_premium_countdown():
    days, hours, minutes, seconds = time_until_birthday()
    
    if days > 0 or hours > 0 or minutes > 0 or seconds > 0:
        st.markdown("""
        <div class="premium-container reflection">
            <h2 style="text-align: center; font-family: 'Playfair Display', serif; margin-bottom: 30px; color: black;">
                Saleha's Birthday Celebration
            </h2>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="countdown">
            <div class="countdown-container">
                <div class="countdown-box">
                    <div class="countdown-value">{days}</div>
                    <div class="countdown-label">Days</div>
                </div>
                <div class="countdown-box">
                    <div class="countdown-value">{hours}</div>
                    <div class="countdown-label">Hours</div>
                </div>
                <div class="countdown-box">
                    <div class="countdown-value">{minutes}</div>
                    <div class="countdown-label">Minutes</div>
                </div>
                <div class="countdown-box">
                    <div class="countdown-value">{seconds}</div>
                    <div class="countdown-label">Seconds</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style="text-align: center; font-family: 'Montserrat', sans-serif; font-size: 1.2rem; margin: 30px 0;">
            A special celebration is being prepared just for you.
        </p>
        
        <div style="text-align: center; margin: 40px 0;">
            <img src="https://media.giphy.com/media/l0MYyDa8S9ghzNebm/giphy.gif" width="300" style="border-radius: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.1);">
        </div>
        
        <p style="text-align: center; font-family: 'Dancing Script', cursive; font-size: 2rem; color: #98fb98; margin-top: 20px;">
            Coming Soon...
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        return False
    else:
        return True

# Create floating images with parallax effect
def create_floating_image(image_url, size=200, rotation=5, delay=0):
    return f"""
    <img src="{image_url}" width="{size}" style="
        border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transform: rotate({rotation}deg);
        animation: float 6s {delay}s ease-in-out infinite;
    ">
    """

# Main function
def main():
    # Password gate
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("""
            <div class="premium-container" style="max-width: 500px; margin: 60px auto; text-align: center;">
                <h2 style="font-family: 'Playfair Display', serif; margin-bottom: 10px; color: #333;">🔒 Access Required</h2>
                <p style="font-family: 'Montserrat', sans-serif; color: #666;">Enter the password to continue</p>
            </div>
        """, unsafe_allow_html=True)

        with st.form("password_form", clear_on_submit=False):
            password_input = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Unlock")
            if submitted:
                if verify_password(password_input):
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Incorrect password")

        if not st.session_state.authenticated:
            st.stop()

    # Add timezone information to the app
    st.sidebar.markdown("### Celebration Details")
    st.sidebar.markdown("**Timezone:** Asia/Karachi (Pakistan Time)")
    st.sidebar.markdown("**Current Date in Selected Timezone:**")
    timezone = pytz.timezone('Asia/Karachi')
    current_time = datetime.now(timezone)
    st.sidebar.markdown(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    local_css()
    generate_confetti()
    generate_sparkles()
    
    # Play background music (a peaceful happy birthday instrumental)
    try:
        # Using a publicly available audio URL - replace with your preferred music
        audio_url = "https://github.com/AkashGutha/birthday-greetings/raw/master/song.mp3"
        autoplay_audio_url(audio_url)
    except:
        pass  # Silently fail if audio can't be loaded
    
    # Check if today is Waris's birthday
    show_full_content = is_birthday()
    
    # If it's not Waris's birthday, show countdown instead
    if not show_full_content:
        access_granted = show_premium_countdown()
        
        # Add a backdoor for testing (remove in production)
        if st.sidebar.checkbox("Preview Birthday Content", value=False):
            access_granted = True
            st.sidebar.warning("Preview mode enabled")
        
        if not access_granted:
            # Add footer
            st.markdown("""
            <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
                <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666;">
                    Crafted with ❤️ for Saleha's Special Day | 2025
                </p>
            </div>
            """, unsafe_allow_html=True)
            return
    
    # Fixed recipient information
    recipient_name = "Saleha"
    
    # Full birthday content
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Header
        st.markdown(f"""
        <div class="premium-container reflection" style="text-align: center;">
            {fancy_header(f"Happy Birthday {recipient_name}", "shimmer-text")}
            <p class="elegant-wish">Celebrating Your Special Day</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Premium birthday layout
    st.markdown("""
    <div class="premium-container gold-border">
        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <div class="shake-animation" style="margin-bottom: 30px;">
                <span style="font-size: 80px;">✨👑✨</span>
            </div>
    """, unsafe_allow_html=True)
    
    # Display premium personalized message
    birthday_message = random.choice(get_premium_birthday_wishes())
    
    st.markdown(f"""
        <div class="message-card">
            <h2 style="font-family: 'Montserrat', sans-serif; font-weight: 600; margin-bottom: 20px; color: #333;">
                Dearest Saleha,
            </h2>
            <p style="font-family: 'Playfair Display', serif; font-size: 1.3rem; line-height: 1.8; color: #444; margin-bottom: 20px;">
                {birthday_message}
            </p>
            <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666; margin-top: 30px;">
                On this remarkable day, I wanted to create something special to celebrate your birthday, friend. Your kindness, strength, and wonderful spirit deserve nothing but the best celebration. You're not just my friend, you're my best friend and I'm so grateful to have you in my life.
            </p>
            <p class="rose-gold-text" style="text-align: right; font-size: 1.5rem; margin-top: 30px;">
                With love and appreciation,
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Birthday memories and quotes
    st.markdown("""
        <h3 style="font-family: 'Playfair Display', serif; text-align: center; margin: 40px 0 20px; color: #333;">
            ✨ Celebrating What Makes You Special ✨
        </h3>
    """, unsafe_allow_html=True)
    
    # Special memories and quotes in 4 columns
    memories = get_personal_memories()
    
    # Create 4 columns for memories
    col1, col2, col3, col4 = st.columns(4)
    memory_cols = [col1, col2, col3, col4]
    
    # Distribute memories across columns
    for i, memory in enumerate(memories):
        col_index = i % 4  # Determine which column to place the memory
        with memory_cols[col_index]:
            st.markdown(f"""
                <div style="
                    background: linear-gradient(145deg, #ffffff, #f5f5f5);
                    border-radius: 20px;
                    padding: 20px;
                    box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
                    transform: rotate({random.uniform(-2, 2)}deg);
                    margin: 10px 5px;
                    min-height: 150px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                ">
                    <p style="font-family: 'Montserrat', sans-serif; font-size: 1rem; color: #555; text-align: center;">
                        "{memory}"
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)
    
    # Local default images (from same folder)
    st.markdown("""
        <h3 style=\"font-family: 'Playfair Display', serif; text-align: center; margin: 20px 0; color: #333;\">
            Featured Photos
        </h3>
    """, unsafe_allow_html=True)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_image_names = ["sari.jpg", "n_img.jpg", "red.jpg"]
    default_image_paths = []
    for image_name in default_image_names:
        image_path = os.path.join(script_dir, image_name)
        if os.path.exists(image_path):
            default_image_paths.append(image_path)

    if default_image_paths:
        cols = st.columns(3)
        for idx, path in enumerate(default_image_paths):
            with cols[idx % 3]:
                try:
                    # Read and embed image as base64 to ensure fixed-size placeholder rendering
                    with open(path, "rb") as f:
                        img_bytes = f.read()
                    ext = os.path.splitext(path)[1].lower()
                    mime = "image/jpeg" if ext in [".jpg", ".jpeg"] else "image/png"
                    b64 = base64.b64encode(img_bytes).decode()
                    st.markdown(f"""
                        <div class=\"photo-placeholder\">
                            <img class=\"photo-img\" src=\"data:{mime};base64,{b64}\" />
                        </div>
                    """, unsafe_allow_html=True)
                except Exception:
                    pass

    # (Image uploader removed by request)

    # Interactive "gift" - digital birthday cake
    st.markdown("""
        <h3 style="font-family: 'Playfair Display', serif; text-align: center; margin: 40px 0 20px; color: #333;">
            Your Birthday Cake
        </h3>
        
        <div style="text-align: center; margin: 40px 0;">
            <div class="cake-animation" style="font-size: 120px; margin: 20px 0 40px 0; display: inline-block;">
                🎂
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Make a wish section
    st.markdown("""
        <div class="premium-container" style="text-align: center; max-width: 600px; margin: 30px auto;">
            <h3 style="font-family: 'Dancing Script', cursive; font-size: 2.5rem; color: #98fb98; margin-bottom: 20px;">
                Make a Wish
            </h3>
            <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666; margin-bottom: 30px;">
                Close your eyes, make a wish, and click the button below to make it come true!
            </p>
    """, unsafe_allow_html=True)
    
    # Wish button with animation - centered using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Make Birthday Wish ✨", key="wish_button", use_container_width=True):
            st.balloons()
            st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <h3 style="font-family: 'Dancing Script', cursive; font-size: 2rem; color: #98fb98;">
                    Your wish has been sent to the universe!
                </h3>
                <p style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; color: #666;">
                    May all your dreams and wishes come true this year and always.
                </p>
                <div style="font-size: 50px; margin: 20px 0;">
                    ✨🌈💫
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)
    
    # Birthday quotes carousel
    st.markdown("""
        <div style="text-align: center; margin: 40px 0;">
            <h3 style="font-family: 'Playfair Display', serif; color: #333; margin-bottom: 20px;">
                Birthday Blessings
            </h3>
            <div class="premium-container" style="background: linear-gradient(to right, rgba(152, 251, 152, 0.1), rgba(144, 238, 144, 0.1)); text-align: center; padding: 30px;">
                <p style="font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: #333;">
                    "May your birthday be the start of a year filled with good luck, good health, and much happiness."
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Final birthday wish
    st.markdown("""
   <style>
                 <div class="premium-container" style="text-align: center; margin: 50px 0;">
        <img src="https://media.giphy.com/media/KdC9XVrVYOVu5sKhI9/giphy.gif" width="300" 
             style="border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin-bottom: 30px;">
        
        <h2 style="font-family: 'Dancing Script', cursive; font-size: 3rem; color: #98fb98; margin: 20px 0;">
            Happy Birthday Saleha!
        </h2>
        
        <p style="font-family: 'Montserrat', sans-serif; font-size: 1.2rem; color: #666; margin-bottom: 40px;">
            May your special day bring you all that your heart desires, friend!
        </p>
    </div>
                </style>
""", unsafe_allow_html=True)
    
    # End the container
    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid #eee;">
        <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; color: #666;">
            Crafted with ❤️ especially for Saleha | 2025
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()