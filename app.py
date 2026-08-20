import streamlit as st
import tempfile
import os
import subprocess
import json

# Set up the page
st.set_page_config(page_title="Video Specs Validator", page_icon="📹")
st.title("📹 Video Creative Validator")
st.write("Upload a video asset to verify if it meets the required specifications.")

# File Uploader
uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "mkv", "avi", "webm"])

if uploaded_file:
    st.markdown("### 📊 Validation Report")
    
    # Dictionary to keep track of passed/failed checks (easy to add more to this later!)
    validations = {}
    
    # -----------------------------------------
    # 1. FILE TYPE CHECK
    # -----------------------------------------
    file_ext = uploaded_file.name.split('.')[-1].lower()
    if file_ext == 'mp4':
        validations['File Type'] = (True, "MP4")
    else:
        validations['File Type'] = (False, f"Found '{file_ext.upper()}' — Expected MP4. Please ask for a replacement.")

    # -----------------------------------------
    # 2. FILE SIZE CHECK (Max 250 MB)
    # -----------------------------------------
    # Convert bytes to Megabytes
    size_mb = uploaded_file.size / (1024 * 1024)
    if size_mb <= 250.0:
        validations['File Size'] = (True, f"{size_mb:.2f} MB")
    else:
        validations['File Size'] = (False, f"Found {size_mb:.2f} MB — Expected max 250 MB. Please ask for a replacement.")

    # -----------------------------------------
    # 3. AUDIO CODEC CHECK (Expected: AAC)
    # -----------------------------------------
    # To read metadata, we must temporarily save the file to the server
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        # Run ffprobe (Standard video metadata extractor) to get JSON data
        cmd = [
            'ffprobe', '-v', 'quiet', 
            '-print_format', 'json', 
            '-show_streams', tmp_path
        ]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        metadata = json.loads(output)
        
        audio_codec = None
        # Loop through streams to find where codec_type is 'audio'
        for stream in metadata.get('streams', []):
            if stream.get('codec_type') == 'audio':
                audio_codec = stream.get('codec_name')
                break
        
        if audio_codec:
            if audio_codec.lower() == 'aac':
                validations['Audio Codec'] = (True, "AAC")
            else:
                validations['Audio Codec'] = (False, f"Found '{audio_codec.upper()}' — Expected AAC. Please ask for a replacement.")
        else:
            validations['Audio Codec'] = (False, "No audio stream found. Expected AAC. Please ask for a replacement.")
            
    except Exception as e:
        validations['Audio Codec'] = (False, "Error reading metadata. Make sure FFmpeg is installed on your system.")
    finally:
        # Clean up the temporary file so we don't fill up the server
        os.remove(tmp_path)

    # -----------------------------------------
    # DISPLAY RESULTS
    # -----------------------------------------
    all_passed = True
    for spec, (passed, message) in validations.items():
        if passed:
            st.success(f"**{spec}**: ✅ {message}")
        else:
            st.error(f"**{spec}**: ❌ {message}")
            all_passed = False
            
    st.markdown("---")
    if all_passed:
        st.balloons()
        st.success("🎉 **All specs met! The creative is approved.**")
    else:
        st.warning("⚠️ **Creative rejected. Please request a replacement based on the failed checks above.**")