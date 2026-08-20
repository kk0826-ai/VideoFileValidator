import streamlit as st
import streamlit.components.v1 as components

# 1. Hide Streamlit's default padding
st.set_page_config(page_title="Video Validator", layout="wide")
st.markdown("""
    <style>
        .block-container { padding: 0rem !important; }
        header { visibility: hidden; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# 2. Commercial-Grade HTML/JS Code with Isolated Workspaces
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200;300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- MP4Box.js for deep client-side metadata parsing -->
    <script src="https://cdn.jsdelivr.net/npm/mp4box@0.5.2/dist/mp4box.all.min.js"></script>
    
    <style>
        /* Global & Reset */
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Manrope', sans-serif; font-weight: 400; }
        body { background-color: #FAFAFA; color: #0F172A; padding-bottom: 250px; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }

        /* Premium Header */
        header {
            background-image: url('https://i.ibb.co/nMTJF4B9/vj-HZbu8-Imgur.jpg');
            background-size: cover;
            background-position: center;
            height: 80px; 
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 2rem;
            box-shadow: inset 0 0 0 2000px rgba(15, 23, 42, 0.75); 
            border-bottom: 4px solid #111827;
        }
        
        header h1 { 
            color: #FFFFFF; 
            font-size: 40px; 
            font-family: 'Century Gothic', Arial, sans-serif; 
            font-weight: 400; 
            letter-spacing: 2px; 
        }

        /* Spec Navigation Tabs */
        .spec-tabs-container {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 2rem;
        }
        .spec-tab {
            background-color: #FFFFFF;
            color: #64748B;
            border: 1px solid #CBD5E1;
            padding: 12px 28px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.2s ease;
            border-radius: 0px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .spec-tab:hover {
            border-color: #0F172A;
            color: #0F172A;
        }
        .spec-tab.active {
            background-color: #2C0A38;
            color: #FFFFFF;
            border-color: #2C0A38;
            box-shadow: 0 4px 6px -1px rgba(44, 10, 56, 0.25);
        }

        /* Sharp Upload Dropzone */
        .upload-section {
            background-color: #FFFFFF;
            border: 1.5px dashed #CBD5E1;
            padding: 45px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-bottom: 2rem;
            border-radius: 0px; 
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .upload-section:hover, .upload-section.dragover {
            border-color: #0F172A;
            background-color: #F8FAFC;
        }
        .upload-icon { width: 42px; height: 42px; color: #64748B; margin-bottom: 12px; transition: color 0.2s ease; }
        .upload-section:hover .upload-icon { color: #0F172A; }
        .upload-text { color: #0F172A; font-size: 15px; font-weight: 400; letter-spacing: 0.3px; }
        .upload-subtext { color: #64748B; font-size: 13px; margin-top: 6px; font-weight: 400; }
        #file-input { display: none; }

        /* Summary Dashboard */
        .summary-dashboard {
            display: none; 
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 2rem;
        }
        .summary-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            border-radius: 0px; 
        }
        .summary-value { font-size: 28px; font-weight: 400; color: #0F172A; line-height: 1; }
        .summary-label { 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            gap: 6px; 
            font-size: 11px; 
            color: #64748B; 
            text-transform: uppercase; 
            font-weight: 400; 
            letter-spacing: 0.5px; 
            margin-top: 10px; 
        }

        /* Action Bar */
        .action-bar-container {
            display: none;
            justify-content: center;
            margin-top: 2rem;
            margin-bottom: 2rem;
        }
        .clear-btn {
            background-color: #111827;
            color: #FFFFFF;
            border: none;
            padding: 12px 24px;
            font-size: 13px;
            font-weight: 400;
            border-radius: 0px; 
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: background-color 0.2s, transform 0.1s;
        }
        .clear-btn:hover { background-color: #334155; }
        .clear-btn:active { transform: scale(0.98); }

        /* Data Tables */
        .table-wrapper {
            background: transparent;
            margin-bottom: 3rem;
            display: none; 
        }
        
        .table-header-title {
            padding: 0 0 12px 0;
            font-size: 18px;
            font-weight: 400;
            color: #334155;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .table-container {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 0px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
            overflow: visible; 
        }

        table { width: 100%; border-collapse: collapse; table-layout: fixed; }
        
        th { 
            background-color: #2C0A38; 
            color: #FFFFFF; 
            padding: 10px 16px; 
            font-size: 11px; 
            font-weight: 400; 
            text-transform: uppercase; 
            letter-spacing: 0.05em; 
            text-align: center; 
            border-bottom: none; 
            white-space: nowrap; 
        }

        .th-content { display: flex; align-items: center; gap: 8px; }
        
        th:nth-child(1) { text-align: left; }
        th:not(:nth-child(1)) .th-content { justify-content: center; }
        .th-content svg { width: 14px; height: 14px; fill: #FFFFFF; }
        
        td { 
            padding: 14px 16px; 
            font-size: 13px; 
            color: #0F172A; 
            text-align: center; 
            border-bottom: 1px solid #E2E8F0; 
            vertical-align: middle; 
            word-break: break-word; 
            overflow-wrap: anywhere;
            font-weight: 400; 
        }

        td:nth-child(1) { text-align: left; }

        tr:last-child td { border-bottom: none; }
        tr.data-row:hover td { background-color: #F8FAFC !important; cursor: default; }

        .status-container { display: flex; flex-direction: column; gap: 4px; }
        .status-main { display: flex; align-items: center; justify-content: center; gap: 8px; font-weight: 400; font-size: 13px; }
        
        .status-text-pass { color: #22C55E; }
        .status-text-fail { color: #DC2626; }    

        .text-error-detail { color: #DC2626; font-weight: 400; }
        
        /* App Footer Styling */
        .app-footer {
            margin-top: 5rem;
            padding-top: 24px;
            border-top: 1px solid #E2E8F0;
            text-align: center;
            font-size: 12px;
            color: #64748B;
            line-height: 1.6;
            letter-spacing: 0.5px;
        }
        .app-footer strong {
            color: #0F172A;
            font-weight: 600;
        }
        .app-footer-team {
            font-size: 11px;
            text-transform: uppercase;
            color: #94A3B8;
            font-weight: 500;
            margin-top: 2px;
            letter-spacing: 1px;
        }
    </style>
</head>
<body>
    <header id="main-header"><h1>Video Validator</h1></header>
    
    <div class="container">
        
        <!-- SECTION SELECTOR TABS -->
        <div class="spec-tabs-container">
            <button class="spec-tab active" id="tab-olv" onclick="switchSpecMode('OLV')">
                <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                OLV Specs
            </button>
            <button class="spec-tab" id="tab-ctv" onclick="switchSpecMode('CTV')">
                <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/></svg>
                CTV / BVOD / OTT Specs
            </button>
        </div>

        <div class="summary-dashboard" id="summary-dashboard">
            <div class="summary-card">
                <div class="summary-value" style="color: #22C55E;" id="count-pass">0</div>
                <div class="summary-label">
                    <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" class="val-pass"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Compliant
                </div>
            </div>
            <div class="summary-card">
                <div class="summary-value" style="color: #EF4444;" id="count-fail">0</div>
                <div class="summary-label">
                    <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" class="val-fail"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    Non-Compliant
                </div>
            </div>
        </div>

        <div class="upload-section" id="dropzone" onclick="document.getElementById('file-input').click();">
            <svg class="upload-icon" id="upload-icon-svg" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"></path>
            </svg>
            <span class="upload-text" id="upload-main-text">Drag & drop your video files here</span>
            <span class="upload-subtext" id="upload-sub-text">or click to browse files (MP4 only, max 250MB)</span>
            <input type="file" id="file-input" multiple accept="video/mp4">
        </div>

        <div class="table-wrapper" id="wrapper-fail">
            <div style="padding: 0 0 12px 0;">
                <div class="table-header-title" style="padding-bottom: 4px;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                        <line x1="12" y1="9" x2="12" y2="13"></line>
                        <line x1="12" y1="17" x2="12.01" y2="17"></line>
                    </svg> 
                    Non-Compliant
                </div>
            </div>
            <div class="table-container">
                <table>
                    <thead id="thead-fail"></thead>
                    <tbody id="tbody-fail"></tbody>
                </table>
            </div>
        </div>

        <div class="table-wrapper" id="wrapper-pass">
            <div class="table-header-title">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#22C55E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
                Compliant
            </div>
            <div class="table-container">
                <table>
                    <thead id="thead-pass"></thead>
                    <tbody id="tbody-pass"></tbody>
                </table>
            </div>
        </div>

        <div class="action-bar-container" id="action-bar">
            <button class="clear-btn" onclick="clearResults()">
                <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                Clear Current Results
            </button>
        </div>

        <footer class="app-footer">
            <div>Made by <strong>KIRANKUMAR</strong></div>
            <div class="app-footer-team">MiQ Ad Ops Team</div>
        </footer>

    </div>

    <script>
        // Separate state management for the two tabs
        const state = {
            OLV: {
                processedFiles: new Set(),
                compliantCount: 0,
                nonCompliantCount: 0,
                passRows: [],
                failRows: []
            },
            CTV: {
                processedFiles: new Set(),
                compliantCount: 0,
                nonCompliantCount: 0,
                passRows: [],
                failRows: []
            }
        };

        let currentSpecMode = 'OLV'; // 'OLV' or 'CTV'

        const iconPass = `<svg width="18" height="18" viewBox="0 0 24 24" fill="#22C55E" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="11"/><path d="M8 12.5L10.5 15L16 9" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
        const iconFail = `<svg width="18" height="18" viewBox="0 0 24 24" fill="#DC2626" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="11"/><path d="M15 9L9 15M9 9L15 15" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;

        function getHeaderHTML() {
            if (currentSpecMode === 'OLV') {
                return `
                    <tr>
                        <th style="width: 32%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg> FILE NAME</div></th>
                        <th style="width: 15%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zM6 20V4h7v5h5v11H6z"/></svg> FILE TYPE</div></th>
                        <th style="width: 15%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h18v14zM5 15h14v3H5z"/></svg> SIZE</div></th>
                        <th style="width: 18%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg> AUDIO CODEC</div></th>
                        <th style="width: 20%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> STATUS</div></th>
                    </tr>
                `;
            } else {
                return `
                    <tr>
                        <th style="width: 25%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg> FILE NAME</div></th>
                        <th style="width: 13%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zM6 20V4h7v5h5v11H6z"/></svg> FILE TYPE</div></th>
                        <th style="width: 12%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h18v14zM5 15h14v3H5z"/></svg> SIZE</div></th>
                        <th style="width: 15%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg> AUDIO CODEC</div></th>
                        <th style="width: 22%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> AMAZON CTV SPECS</div></th>
                        <th style="width: 13%;"><div class="th-content"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> STATUS</div></th>
                    </tr>
                `;
            }
        }

        function updateHeaders() {
            document.getElementById('thead-fail').innerHTML = getHeaderHTML();
            document.getElementById('thead-pass').innerHTML = getHeaderHTML();
        }

        updateHeaders();

        const dropzone = document.getElementById('dropzone');
        const fileInput = document.getElementById('file-input');
        
        function switchSpecMode(mode) {
            if (currentSpecMode === mode) return;
            currentSpecMode = mode;
            
            // Toggle tab active class
            document.getElementById('tab-olv').classList.toggle('active', mode === 'OLV');
            document.getElementById('tab-ctv').classList.toggle('active', mode === 'CTV');
            
            // Update Dropzone hints
            if (mode === 'OLV') {
                document.getElementById('upload-sub-text').innerText = "or click to browse files (MP4 only, max 250MB)";
                fileInput.accept = "video/mp4";
            } else {
                document.getElementById('upload-sub-text').innerText = "or click to browse files (MP4 or MOV, max 500MB)";
                fileInput.accept = "video/mp4,video/quicktime,.mov";
            }
            
            // Re-render headers and table with the target tab's existing state
            updateHeaders();
            renderCurrentState();
        }

        function renderCurrentState() {
            let activeState = state[currentSpecMode];
            
            document.getElementById('count-pass').innerText = activeState.compliantCount;
            document.getElementById('count-fail').innerText = activeState.nonCompliantCount;
            
            document.getElementById('tbody-pass').innerHTML = activeState.passRows.join('');
            document.getElementById('tbody-fail').innerHTML = activeState.failRows.join('');
            
            let total = activeState.compliantCount + activeState.nonCompliantCount;
            
            if (total > 0) {
                document.getElementById('summary-dashboard').style.display = "grid";
                document.getElementById('action-bar').style.display = "flex";
                document.getElementById('wrapper-fail').style.display = activeState.nonCompliantCount > 0 ? "block" : "none";
                document.getElementById('wrapper-pass').style.display = activeState.compliantCount > 0 ? "block" : "none";
            } else {
                document.getElementById('summary-dashboard').style.display = "none";
                document.getElementById('action-bar').style.display = "none";
                document.getElementById('wrapper-fail').style.display = "none";
                document.getElementById('wrapper-pass').style.display = "none";
            }
        }

        function clearResults() {
            // ONLY clear the currently active tab's state
            state[currentSpecMode] = {
                processedFiles: new Set(),
                compliantCount: 0,
                nonCompliantCount: 0,
                passRows: [],
                failRows: []
            };
            
            fileInput.value = ""; 
            renderCurrentState();
            
            try { document.getElementById('main-header').scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch(e) {}
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        dropzone.addEventListener('dragover', (e) => { e.preventDefault(); dropzone.classList.add('dragover'); });
        dropzone.addEventListener('dragleave', () => { dropzone.classList.remove('dragover'); });
        dropzone.addEventListener('drop', (e) => { e.preventDefault(); dropzone.classList.remove('dragover'); handleFiles(e.dataTransfer.files); });
        fileInput.addEventListener('change', (e) => handleFiles(e.target.files));

        function checkVideoMetadata(file) {
            return new Promise((resolve) => {
                let resolved = false;
                const mp4boxfile = MP4Box.createFile();
                
                let metadataResult = {
                    hasAudio: false,
                    isAAC: false,
                    codecName: "None",
                    sampleRate: 0,
                    audioBitrate: 0,
                    audioChannels: 0,
                    audioStreamCount: 0,
                    videoStreamCount: 0,
                    videoCodec: "None",
                    videoBitrate: 0,
                    fps: 0,
                    width: 0,
                    height: 0
                };

                const timeout = setTimeout(() => {
                    if (!resolved) {
                        resolved = true;
                        resolve(metadataResult); // Returns default/failed if timeout
                    }
                }, 3000);

                mp4boxfile.onReady = function(info) {
                    if (resolved) return;
                    clearTimeout(timeout);
                    resolved = true;
                    
                    let fileDurationSecs = info.duration / info.timescale;

                    for (let i = 0; i < info.tracks.length; i++) {
                        let track = info.tracks[i];
                        if (track.audio) {
                            metadataResult.audioStreamCount++;
                            metadataResult.hasAudio = true;
                            metadataResult.codecName = track.codec || "AAC";
                            if (metadataResult.codecName.toLowerCase().startsWith('mp4a') || metadataResult.codecName.toLowerCase().includes('aac')) {
                                metadataResult.isAAC = true;
                                metadataResult.codecName = "AAC";
                            }
                            metadataResult.sampleRate = track.audio.sample_rate || 0;
                            metadataResult.audioChannels = track.audio.channel_count || 0;
                            metadataResult.audioBitrate = track.bitrate || 0;
                        }
                        if (track.video) {
                            metadataResult.videoStreamCount++;
                            metadataResult.videoCodec = track.codec || "None";
                            metadataResult.width = track.video.width || 0;
                            metadataResult.height = track.video.height || 0;
                            metadataResult.videoBitrate = track.bitrate || 0;
                            
                            if (fileDurationSecs > 0) {
                                metadataResult.fps = track.nb_samples / fileDurationSecs;
                            }
                        }
                    }
                    resolve(metadataResult);
                };

                mp4boxfile.onError = function(e) {
                    if (resolved) return;
                    clearTimeout(timeout);
                    resolved = true;
                    resolve(metadataResult);
                };

                const reader = new FileReader();
                reader.onload = function(e) {
                    try {
                        const buffer = e.target.result;
                        buffer.fileStart = 0;
                        mp4boxfile.appendBuffer(buffer);
                        mp4boxfile.flush();
                    } catch(err) {
                        if (!resolved) {
                            resolved = true;
                            clearTimeout(timeout);
                            resolve(metadataResult);
                        }
                    }
                };
                
                const slice = file.slice(0, 1024 * 1024 * 15); 
                reader.readAsArrayBuffer(slice);
            });
        }

        async function handleFiles(files) {
            document.getElementById('upload-main-text').innerText = "Processing videos (This may take a second)...";
            document.getElementById('upload-icon-svg').style.color = "#3B82F6";
            await new Promise(resolve => setTimeout(resolve, 50)); 

            let activeState = state[currentSpecMode];
            const maxMBAllowed = currentSpecMode === 'OLV' ? 250 : 500;
            const allowedFormats = currentSpecMode === 'OLV' ? ['MP4'] : ['MP4', 'MOV'];

            for (let file of files) {
                let fileId = file.name + "_" + file.size;
                
                // Prevent duplicate processing in the CURRENT tab
                if (activeState.processedFiles.has(fileId)) continue;
                activeState.processedFiles.add(fileId);

                let status = "Pass", errors = [];
                let sizeMB = file.size / (1024 * 1024);
                let sizeStr = sizeMB.toFixed(2) + " MB";
                
                let rawExt = file.name.split('.').pop();
                let logicExt = rawExt.toUpperCase();
                let displayExt = "." + rawExt.toLowerCase();
                let audioCodecHtml = "-";
                let amazonSpecHtml = "-";
                
                if (!allowedFormats.includes(logicExt)) {
                    status = "Fail"; 
                    let expectedMsg = allowedFormats.join(' or ');
                    errors.push(`Invalid format: ${displayExt}. Expected ${expectedMsg}`);
                    let redDisplayExt = `<span class='text-error-detail'>${displayExt}</span>`;
                    appendRowToState(file.name, redDisplayExt, sizeStr, "-", "-", status, errors, sizeMB, maxMBAllowed, activeState);
                    continue;
                }
                
                if (sizeMB > maxMBAllowed) { 
                    status = "Fail";
                    errors.push(`File size exceeds ${maxMBAllowed} MB limit`);
                }

                let vMeta = await checkVideoMetadata(file);
                
                if (!vMeta.hasAudio) {
                    status = "Fail";
                    audioCodecHtml = `<span class='text-error-detail'>No Audio</span>`;
                    errors.push("Missing audio track");
                } else if (!vMeta.isAAC) {
                    status = "Fail";
                    audioCodecHtml = `<span class='text-error-detail'>${vMeta.codecName}</span>`;
                    errors.push(`Invalid audio codec: ${vMeta.codecName}. Expected AAC`);
                } else {
                    audioCodecHtml = vMeta.codecName;
                }

                // Amazon CTV Specific Forensic Checks
                if (currentSpecMode === 'CTV') {
                    let amazonErrors = [];
                    
                    if (vMeta.videoStreamCount !== 1) amazonErrors.push(`Found ${vMeta.videoStreamCount} video streams (Expected 1)`);
                    if (vMeta.audioStreamCount !== 1) amazonErrors.push(`Found ${vMeta.audioStreamCount} audio streams (Expected 1)`);
                    
                    if (vMeta.audioChannels !== 2 && vMeta.audioChannels > 0) amazonErrors.push(`Audio channels: ${vMeta.audioChannels} (Expected 2/Stereo)`);
                    
                    // Allow 44.1 kHz OR 48 kHz
                    if (vMeta.sampleRate > 0) {
                        let is44k = Math.abs(vMeta.sampleRate - 44100) < 100;
                        let is48k = Math.abs(vMeta.sampleRate - 48000) < 100;
                        if (!is44k && !is48k) {
                            amazonErrors.push(`Sample rate: ${(vMeta.sampleRate/1000).toFixed(2)} kHz (Expected 44.1 or 48 kHz)`);
                        }
                    }

                    let bitrateKbps = vMeta.audioBitrate / 1000;
                    if (bitrateKbps > 0 && bitrateKbps < 192) amazonErrors.push(`Audio bitrate: ${bitrateKbps.toFixed(0)} Kbps (Expected min 192 Kbps)`);

                    let vCodec = vMeta.videoCodec.toLowerCase();
                    if (!vCodec.includes('avc1') && !vCodec.includes('h264') && vCodec !== "none") {
                        amazonErrors.push(`Video codec: ${vMeta.videoCodec} (Expected H.264/avc1)`);
                    }
                    
                    let videoBitrateMbps = vMeta.videoBitrate / 1000000;
                    if (videoBitrateMbps > 0 && videoBitrateMbps < 15) amazonErrors.push(`Video bitrate: ${videoBitrateMbps.toFixed(1)} Mbps (Expected min 15 Mbps)`);

                    // Check for 1920x1080 OR 1080x1920
                    if (vMeta.width > 0 && vMeta.height > 0) {
                        let aspectRatio = vMeta.width / vMeta.height;
                        let is16x9 = Math.abs(aspectRatio - (16/9)) <= 0.05;
                        let is9x16 = Math.abs(aspectRatio - (9/16)) <= 0.05;
                        
                        if (!is16x9 && !is9x16) {
                            amazonErrors.push(`Aspect ratio is ${(aspectRatio).toFixed(2)} (Expected 16:9 or 9:16)`);
                        }

                        if ((is16x9 && (vMeta.width < 1920 || vMeta.height < 1080)) || 
                            (is9x16 && (vMeta.width < 1080 || vMeta.height < 1920))) {
                            amazonErrors.push(`Resolution: ${vMeta.width}x${vMeta.height} (Expected 1920x1080 or 1080x1920)`);
                        }
                    }

                    if (vMeta.fps > 0) {
                        let validFps = [23.976, 24, 25, 29.97, 30];
                        let isFpsValid = validFps.some(f => Math.abs(vMeta.fps - f) < 0.5);
                        if (!isFpsValid) {
                            amazonErrors.push(`Frame rate: ${vMeta.fps.toFixed(2)} fps is not supported`);
                        }
                    }

                    if (amazonErrors.length > 0) {
                        status = "Fail";
                        amazonSpecHtml = `<span class='text-error-detail'>Failed Amazon Criteria</span>`;
                        amazonErrors.forEach(ae => errors.push(`[Amazon] ${ae}`));
                    } else {
                        amazonSpecHtml = `<span style="color: #22C55E;">Meets Amazon Specs</span>`;
                    }
                }

                appendRowToState(file.name, displayExt, sizeStr, audioCodecHtml, amazonSpecHtml, status, errors, sizeMB, maxMBAllowed, activeState);
            }

            document.getElementById('upload-main-text').innerText = "Drag & drop your video files here";
            document.getElementById('upload-icon-svg').style.color = "#64748B";
            
            // Re-render the UI with the updated state
            renderCurrentState();
        }

        function appendRowToState(name, displayExt, sizeStr, audioCodecHtml, amazonSpecHtml, status, errors, sizeMB, maxMBAllowed, activeState) {
            let formattedSize = sizeMB > maxMBAllowed ? `<span class='text-error-detail'>${sizeStr}</span>` : sizeStr;

            let finalMessages = [];
            errors.forEach(e => finalMessages.push(`<div class='text-error-detail' style='font-size:12px; line-height:1.25;'>• ${e}</div>`));
            let msgHtml = finalMessages.join("");

            let statusBlock = "";

            if (status === "Pass") {
                activeState.compliantCount++;
                statusBlock = `<div class='status-container'><div class='status-main status-text-pass'>${iconPass} Pass</div></div>`;
            } else {
                activeState.nonCompliantCount++;
                statusBlock = `<div class='status-container'><div class='status-main status-text-fail'>${iconFail} Fail</div>${msgHtml}</div>`;
            }

            let rowHTML = "";
            if (currentSpecMode === 'OLV') {
                rowHTML = `<tr class='data-row'>
                    <td>${name}</td>
                    <td>${displayExt}</td>
                    <td>${formattedSize}</td>
                    <td>${audioCodecHtml}</td>
                    <td>${statusBlock}</td>
                </tr>`;
            } else {
                rowHTML = `<tr class='data-row'>
                    <td>${name}</td>
                    <td>${displayExt}</td>
                    <td>${formattedSize}</td>
                    <td>${audioCodecHtml}</td>
                    <td>${amazonSpecHtml}</td>
                    <td>${statusBlock}</td>
                </tr>`;
            }

            if (status === "Pass") {
                activeState.passRows.push(rowHTML);
            } else {
                activeState.failRows.push(rowHTML);
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=1200, scrolling=True)
