import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
from pathlib import Path
import html

# ============================================================
# GLOBAL MARKET EXPLORER | boAt x GERMANY
# ============================================================

st.set_page_config(
    page_title="Global Market Explorer | boAt",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DESIGN SYSTEM
# ============================================================

CYAN = "#16D9FF"
BLUE = "#168BFF"
NAVY = "#061326"
PANEL = "#07182B"
TEXT = "#DCEBFA"
MUTED = "#7892AA"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Rajdhani:wght@400;500;600;700&display=swap');

:root {
    --cyan: #16d9ff;
    --blue: #168bff;
    --navy: #061326;
    --panel: #07182b;
    --text: #dcebfa;
    --muted: #7892aa;
}

.stApp {
    background:
        radial-gradient(ellipse at 50% 25%,
        #0a2544 0%, #061326 48%, #020812 100%);
    color: var(--text);
    font-family: 'Rajdhani', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1800px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, p, label, span {
    font-family: 'Rajdhani', sans-serif;
}

[data-testid="stSidebar"] {
    background: #04101f;
    border-right: 1px solid #12446a;
}

footer, #MainMenu {
    visibility: hidden;
}

.topline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #16466c;
    padding: 8px 2px 14px;
    margin-bottom: 18px;
}

.brandmark {
    font-family: 'Orbitron', sans-serif;
    color: var(--cyan);
    font-size: 12px;
    letter-spacing: 3px;
    text-shadow: 0 0 12px #16d9ff66;
}

.topmeta {
    font-family: 'Orbitron', sans-serif;
    color: #7fa6c8;
    font-size: 9px;
    letter-spacing: 2px;
    text-align: right;
    line-height: 1.8;
}

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(24px, 3vw, 42px);
    font-weight: 700;
    letter-spacing: 3px;
    color: #eaf8ff;
    text-shadow: 0 0 18px #16d9ff55;
    margin: 8px 0 2px;
}

.hero-sub {
    font-family: 'Orbitron', sans-serif;
    font-size: 9px;
    letter-spacing: 3px;
    color: #7fa6c8;
    margin-bottom: 16px;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 11px;
    letter-spacing: 2px;
    color: #bceeff;
    border-bottom: 1px solid #16466c;
    padding-bottom: 8px;
    margin: 10px 0 12px;
}

.hud-card {
    position: relative;
    min-height: 105px;
    padding: 13px 15px;
    background: linear-gradient(
        135deg, rgba(9,36,65,.94), rgba(3,15,29,.94)
    );
    border: 1px solid #15517a;
    box-shadow: inset 0 0 20px #0b5a8a18;
}

.hud-card:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 42px;
    height: 2px;
    background: var(--cyan);
    box-shadow: 0 0 9px var(--cyan);
}

.hud-label {
    font-family: 'Orbitron', sans-serif;
    font-size: 8px;
    letter-spacing: 2px;
    color: #83a9c8;
}

.hud-value {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(18px, 2vw, 27px);
    font-weight: 700;
    color: var(--cyan);
    margin-top: 8px;
    text-shadow: 0 0 12px #16d9ff55;
}

.hud-note {
    font-size: 11px;
    color: #7892aa;
    margin-top: 4px;
}

.intel-card {
    background: linear-gradient(120deg, #081c32, #061326);
    border: 1px solid #123e62;
    border-left: 2px solid #168bff;
    padding: 10px 12px;
    margin-bottom: 8px;
}

.intel-head {
    font-family: 'Orbitron', sans-serif;
    color: var(--cyan);
    font-size: 9px;
    letter-spacing: 1.5px;
    margin-bottom: 5px;
}

.intel-body {
    color: #c5d9eb;
    font-size: 13px;
}

div[data-testid="stMetric"] {
    background: #07182b;
    border: 1px solid #15517a;
    padding: 10px;
}

div[data-testid="stMetricValue"] {
    color: var(--cyan);
    font-family: 'Orbitron', sans-serif;
}

div[data-baseweb="select"] > div {
    background: #07182b;
    border-color: #15517a;
    color: #eaf8ff;
}

.stButton > button {
    background: #08223b;
    color: #dff8ff;
    border: 1px solid #168bff;
    border-radius: 2px;
    font-family: 'Orbitron', sans-serif;
    font-size: 9px;
    letter-spacing: 1px;
}

.stButton > button:hover {
    background: #0b426b;
    border-color: var(--cyan);
    color: white;
    box-shadow: 0 0 12px #16d9ff55;
}

.stTextInput input, .stTextArea textarea {
    background: #07182b;
    color: #eaf8ff;
    border: 1px solid #15517a;
}

div[data-testid="stExpander"] {
    background: #07182b;
    border: 1px solid #16466c;
}

[data-testid="stDataFrame"] {
    border: 1px solid #16466c;
}

hr {
    border-color: #16466c;
}

div[role="radiogroup"] {
    gap: 7px;
    flex-wrap: wrap;
}

div[role="radiogroup"] label {
    background: #06182b;
    border: 1px solid #17486d;
    padding: 5px 11px;
    border-radius: 2px;
    color: #cce8fa !important;
}

div[role="radiogroup"] label[data-checked="true"] {
    background: #0b3554;
    border-color: #16d9ff;
    box-shadow: 0 0 10px #16d9ff33;
}

div[role="radiogroup"] label p {
    font-family: 'Orbitron', sans-serif;
    font-size: 8px;
    letter-spacing: 1px;
}

.stCaption {
    color: #7892aa !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT DATA
# ============================================================

segments = pd.DataFrame({
    "Segment": [
        "Young Professionals",
        "Students",
        "Fitness Enthusiasts",
        "Technology Enthusiasts",
        "Budget-conscious"
    ],
    "Score": [3.85, 3.60, 3.25, 3.50, 3.55]
})

brands = pd.DataFrame([
    ["Apple", "Premium ecosystem",
     "Device integration and premium brand perception",
     "Accessible pricing and cross-platform use"],

    ["JBL", "Mainstream audio specialist",
     "Broad audio portfolio and brand recognition",
     "Selective value and design differentiation"],

    ["Sony", "Premium audio and technology",
     "Audio expertise and noise cancellation",
     "Everyday audio at accessible prices"],

    ["Samsung", "Consumer technology ecosystem",
     "Galaxy device integration",
     "Customers less tied to one ecosystem"],

    ["Soundcore", "Feature-rich value audio",
     "Value and feature proposition",
     "Local service and distinctive identity"],

    ["boAt", "Affordable, style-led audio",
     "Value-focused and youth-oriented brand",
     "Build German awareness and local support"]
], columns=[
    "Brand", "Positioning", "Strength", "Potential opening for boAt"
])

scores = pd.DataFrame({
    "Brand": ["Apple", "JBL", "Sony", "Samsung", "Soundcore", "boAt"],
    "Sound quality": [5, 4, 5, 4, 4, 3],
    "Technology": [5, 4, 5, 5, 4, 3],
    "Value": [2, 4, 2, 3, 5, 5],
    "Brand familiarity in Germany": [5, 5, 5, 5, 3, 1]
})

pestle = {
    "POLITICAL": (
        "Germany is part of the EU single market. Entry requires suitable import, distribution and responsible-operator arrangements.",
        "Identify the EU importer and confirm customs and distribution responsibilities."
    ),
    "ECONOMIC": (
        "Purchasing power, inflation, exchange rates and household spending can influence demand and margins.",
        "Model landed cost, VAT, retailer margin, fulfilment and returns."
    ),
    "SOCIAL": (
        "Students, commuters, professionals and fitness consumers are potential use-case groups; local preferences need validation.",
        "Conduct German-language customer interviews or a product test."
    ),
    "TECHNOLOGICAL": (
        "Customers may compare ANC, microphone quality, battery life, comfort, connectivity and compatibility.",
        "Benchmark exact boAt models against products sold in Germany."
    ),
    "LEGAL": (
        "Radio equipment, electrical safety, batteries, chemicals, packaging and consumer-rights rules may apply.",
        "Obtain specialist advice and verify applicable EU conformity and registration steps."
    ),
    "ENVIRONMENTAL": (
        "Battery life, repairability, packaging and end-of-life handling can affect compliance and consumer perception.",
        "Plan applicable battery, WEEE and packaging obligations."
    )
}

segment_detail = pd.DataFrame([
    ["Young professionals", "22–35 (proposed profile)",
     "Commuting, calls, music and podcasts",
     "Comfort, call quality, battery",
     "Primary target hypothesis"],

    ["University students", "18–25 (proposed profile)",
     "Study, travel and entertainment",
     "Price, battery and style",
     "Secondary target hypothesis"],

    ["Fitness enthusiasts", "Cross-age lifestyle segment",
     "Workout and outdoor activity",
     "Secure fit and durability",
     "Niche opportunity"],

    ["Technology enthusiasts", "Cross-age interest segment",
     "New audio technology",
     "ANC and connectivity",
     "Feature-led niche"],

    ["Budget-conscious consumers", "Cross-age value segment",
     "Everyday audio",
     "Price and essential features",
     "Cross-cutting segment"]
], columns=[
    "Segment", "Profile", "Use case",
    "Purchase priorities", "Initial assessment"
])


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def header(title, subtitle):
    st.markdown(
        f'<div class="hero-title">{title}</div>'
        f'<div class="hero-sub">{subtitle}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        "<hr style='border:0;border-top:1px solid #16466c;margin:10px 0 16px;'>",
        unsafe_allow_html=True
    )


def section(title):
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )


def card(col, label, value, note=""):
    with col:
        st.markdown(
            f'<div class="hud-card">'
            f'<div class="hud-label">{html.escape(str(label))}</div>'
            f'<div class="hud-value">{html.escape(str(value))}</div>'
            f'<div class="hud-note">{html.escape(str(note))}</div>'
            f'</div>',
            unsafe_allow_html=True
        )


def intel(title, body):
    st.markdown(
        f'<div class="intel-card">'
        f'<div class="intel-head">{html.escape(str(title))}</div>'
        f'<div class="intel-body">{html.escape(str(body))}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def chart_style(fig, height=300):
    fig.update_layout(
        height=height,
        paper_bgcolor="#061326",
        plot_bgcolor="#061326",
        font=dict(color="#dcebfa", family="Rajdhani", size=11),
        margin=dict(l=12, r=12, t=28, b=25),
        legend=dict(font=dict(color="#c5d9eb", size=9))
    )
    fig.update_xaxes(gridcolor="#15344f", zerolinecolor="#15344f")
    fig.update_yaxes(gridcolor="#15344f", zerolinecolor="#15344f")
    return fig


# ============================================================
# INTERACTIVE 3D EARTH
# ============================================================

def render_earth_globe():

    texture_path = Path(__file__).parent / "assets" / "earth.jpg"

    if texture_path.exists():
        with open(texture_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
        earth_texture = f"data:image/jpeg;base64,{image_data}"
    else:
        earth_texture = (
            "https://raw.githubusercontent.com/mrdoob/three.js/"
            "dev/examples/textures/planets/earth_atmos_2048.jpg"
        )

    html_code = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* { box-sizing: border-box; }

html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    overflow: hidden;
    background: #03101f;
}

#globe-container {
    width: 100%;
    height: 100%;
    min-height: 620px;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(
            circle at center,
            #0a2542 0%,
            #041326 58%,
            #020914 100%
        );
}

canvas {
    display: block;
    width: 100%;
    height: 100%;
    touch-action: none;
}

#globe-status {
    position: absolute;
    top: 17px;
    left: 16px;
    z-index: 5;
    color: #16dfff;
    font: 11px Arial, sans-serif;
    letter-spacing: 1.5px;
    background: rgba(2,15,29,.7);
    padding: 8px 11px;
    border-left: 2px solid #16dfff;
}

#globe-controls {
    position: absolute;
    top: 12px;
    right: 12px;
    z-index: 5;
    display: flex;
    gap: 7px;
}

#globe-controls button {
    background: rgba(2,18,35,.92);
    color: #16dfff;
    border: 1px solid #0879ad;
    padding: 9px 13px;
    cursor: pointer;
    font-size: 11px;
}

#globe-controls button:hover {
    background: #0879ad;
    color: white;
}

#globe-footer {
    position: absolute;
    bottom: 12px;
    left: 14px;
    color: #73cce8;
    font: 10px Arial, sans-serif;
    letter-spacing: 1.2px;
    z-index: 5;
}

#target-label {
    position: absolute;
    right: 15px;
    bottom: 12px;
    color: #16dfff;
    font: 10px Arial, sans-serif;
    z-index: 5;
}
</style>
</head>

<body>
<div id="globe-container">

    <div id="globe-status">INITIALIZING 3D EARTH...</div>

    <div id="globe-controls">
        <button id="pauseBtn">PAUSE</button>
        <button id="resetBtn">RESET</button>
        <button id="germanyBtn">GERMANY</button>
    </div>

    <div id="globe-footer">
        REAL 3D SATELLITE EARTH · AUTO ROTATION · DRAG TO ROTATE · SCROLL TO ZOOM
    </div>

    <div id="target-label">TARGET: DE</div>
</div>

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
  }
}
</script>

<script type="module">
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const container = document.getElementById("globe-container");
const status = document.getElementById("globe-status");

const EARTH_TEXTURE = "__EARTH_TEXTURE__";

let scene, camera, renderer, earth, controls;
let rotating = true;
let animationStarted = false;

function initializeGlobe() {

    try {

        scene = new THREE.Scene();

        camera = new THREE.PerspectiveCamera(
            38,
            container.clientWidth / container.clientHeight,
            0.1,
            100
        );

        camera.position.set(0, 0, 3.25);

        renderer = new THREE.WebGLRenderer({
            antialias: true,
            alpha: true
        });

        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.outputColorSpace = THREE.SRGBColorSpace;

        container.appendChild(renderer.domElement);

        controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.045;
        controls.enableZoom = true;
        controls.enablePan = false;
        controls.minDistance = 2.1;
        controls.maxDistance = 5.5;
        controls.autoRotate = false;

        scene.add(new THREE.AmbientLight(0xffffff, 1.15));

        const sunlight = new THREE.DirectionalLight(0xffffff, 2.1);
        sunlight.position.set(-4, 2, 5);
        scene.add(sunlight);

        const geometry = new THREE.SphereGeometry(1, 128, 128);
        const loader = new THREE.TextureLoader();
        loader.setCrossOrigin("anonymous");

        loader.load(
            EARTH_TEXTURE,

            function(texture) {

                texture.colorSpace = THREE.SRGBColorSpace;

                const material = new THREE.MeshPhongMaterial({
                    map: texture,
                    shininess: 12,
                    specular: new THREE.Color(0x223344)
                });

                earth = new THREE.Mesh(geometry, material);
                scene.add(earth);

                // Atmospheric blue halo
                const atmosphereGeometry =
                    new THREE.SphereGeometry(1.045, 96, 96);

                const atmosphereMaterial = new THREE.ShaderMaterial({

                    vertexShader: `
                        varying vec3 vNormal;
                        varying vec3 vViewPosition;

                        void main() {
                            vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
                            vNormal = normalize(normalMatrix * normal);
                            vViewPosition = -mvPosition.xyz;
                            gl_Position = projectionMatrix * mvPosition;
                        }
                    `,

                    fragmentShader: `
                        varying vec3 vNormal;
                        varying vec3 vViewPosition;

                        void main() {
                            float intensity = pow(
                                0.72 - dot(
                                    normalize(vNormal),
                                    normalize(vViewPosition)
                                ),
                                3.0
                            );

                            gl_FragColor = vec4(
                                0.02,
                                0.42,
                                1.0,
                                clamp(intensity * 1.5, 0.0, 0.75)
                            );
                        }
                    `,

                    blending: THREE.AdditiveBlending,
                    side: THREE.BackSide,
                    transparent: true,
                    depthWrite: false
                });

                const atmosphere = new THREE.Mesh(
                    atmosphereGeometry,
                    atmosphereMaterial
                );

                scene.add(atmosphere);

                // Star field
                const starGeometry = new THREE.BufferGeometry();
                const starPositions = [];

                for (let i = 0; i < 1600; i++) {
                    starPositions.push(
                        (Math.random() - 0.5) * 18,
                        (Math.random() - 0.5) * 18,
                        (Math.random() - 0.5) * 18
                    );
                }

                starGeometry.setAttribute(
                    "position",
                    new THREE.Float32BufferAttribute(starPositions, 3)
                );

                const starMaterial = new THREE.PointsMaterial({
                    color: 0x8ccfff,
                    size: 0.012,
                    transparent: true,
                    opacity: 0.75
                });

                scene.add(new THREE.Points(starGeometry, starMaterial));

                status.textContent = "3D SATELLITE EARTH ONLINE · AUTO ROTATION ACTIVE";

                if (!animationStarted) {
                    animationStarted = true;
                    animate();
                }
            },

            undefined,

            function(error) {
                console.error("Earth texture failed:", error);
                status.textContent =
                    "EARTH TEXTURE FAILED · CHECK INTERNET OR assets/earth.jpg";
            }
        );

    } catch (error) {
        console.error("Globe initialization failed:", error);
        status.textContent = "3D RENDERER ERROR · CHECK BROWSER WEBGL";
    }
}

function animate() {

    requestAnimationFrame(animate);

    if (earth && rotating) {
        earth.rotation.y += 0.0015;
    }

    if (controls) controls.update();

    if (renderer && scene && camera) {
        renderer.render(scene, camera);
    }
}

document.getElementById("pauseBtn").addEventListener("click", function() {
    rotating = !rotating;
    this.textContent = rotating ? "PAUSE" : "RESUME";
    status.textContent = rotating
        ? "3D SATELLITE EARTH ONLINE · AUTO ROTATION ACTIVE"
        : "3D SATELLITE EARTH · ROTATION PAUSED";
});

document.getElementById("resetBtn").addEventListener("click", function() {

    if (earth) earth.rotation.set(0, 0, 0);

    if (camera && controls) {
        camera.position.set(0, 0, 3.25);
        controls.target.set(0, 0, 0);
        controls.update();
    }

    rotating = true;
    document.getElementById("pauseBtn").textContent = "PAUSE";
    status.textContent = "3D SATELLITE EARTH ONLINE · AUTO ROTATION ACTIVE";
});

document.getElementById("germanyBtn").addEventListener("click", function() {

    if (!earth) return;

    // Approximate orientation towards Europe
    earth.rotation.y = -0.15;
    earth.rotation.x = -0.05;
    rotating = true;

    document.getElementById("pauseBtn").textContent = "PAUSE";
});

window.addEventListener("resize", function() {

    if (!camera || !renderer) return;

    const width = container.clientWidth;
    const height = container.clientHeight;

    camera.aspect = width / height;
    camera.updateProjectionMatrix();

    renderer.setSize(width, height);
});

initializeGlobe();
</script>
</body>
</html>
"""

    html_code = html_code.replace("__EARTH_TEXTURE__", earth_texture)

    components.html(
        html_code,
        height=650,
        scrolling=False
    )


# ============================================================
# TOP BAR AND NAVIGATION
# ============================================================

st.markdown("""
<div class="topline">
    <div class="brandmark">◉ GLOBAL INTELLIGENCE SYSTEM</div>
    <div class="topmeta">
        MARKET ANALYSIS DIVISION<br>
        boAt × GERMANY · 2026
    </div>
</div>
""", unsafe_allow_html=True)

pages = [
    "OVERVIEW",
    "MARKET ANALYSIS",
    "COMPETITOR ANALYSIS",
    "SWOT ANALYSIS",
    "CUSTOMER SEGMENTATION",
    "STP ANALYSIS",
    "MARKET ENTRY STRATEGY",
    "AI INSIGHTS"
]

page = st.radio(
    "NAVIGATION",
    pages,
    horizontal=True,
    label_visibility="collapsed",
    key="main_navigation"
)

st.markdown(
    "<hr style='border:0;border-top:1px solid #16466c;margin:10px 0 20px;'>",
    unsafe_allow_html=True
)


# ============================================================
# 1. OVERVIEW
# ============================================================

if page == "OVERVIEW":

    header(
        "GLOBAL MARKET EXPLORER",
        "WORLDWIDE MARKET INTELLIGENCE · GERMANY × boAt"
    )

    c1, c2, c3, c4 = st.columns(4)

    card(c1, "TARGET COUNTRY", "GERMANY", "EUROPE")
    card(c2, "BRANDS TRACKED", "06", "COMPETITOR SET")
    card(c3, "CUSTOMER SEGMENTS", "05", "IDENTIFIED GROUPS")
    card(c4, "TOP SEGMENT", "3.85 / 5", "YOUNG PROFESSIONALS")

    st.write("")

    left, mid, right = st.columns([1.05, 2.15, 1.05], gap="medium")

    with left:

        section("MARKET SEGMENTS")

        fig = px.bar(
            segments.sort_values("Score"),
            x="Score",
            y="Segment",
            orientation="h",
            text="Score",
            color="Score",
            color_continuous_scale=["#07517b", CYAN]
        )

        fig.update_traces(
            texttemplate="%{text:.2f}",
            textposition="inside"
        )

        fig.update_layout(
            xaxis=dict(range=[0, 5], title="SCORE / 5"),
            yaxis_title="",
            coloraxis_showscale=False,
            showlegend=False
        )

        st.plotly_chart(
            chart_style(fig, 275),
            use_container_width=True
        )

        st.caption("Illustrative evaluation scores; not market shares.")

        intel("PRIMARY TARGET", "Young professionals · proposed age profile 22–35")
        intel("SECONDARY TARGET", "University students · proposed age profile 18–25")

    with mid:

        section("GLOBAL GEOGRAPHIC MONITOR")

        render_earth_globe()

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:12px;
                color:#16d9ff;
                font-family:Orbitron;
                font-size:10px;
                letter-spacing:2px;
            ">
                TARGET MARKET · FEDERAL REPUBLIC OF GERMANY
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        section("COMPETITOR NETWORK")

        for i, brand in enumerate(brands.Brand.tolist(), 1):
            intel(f"COMPETITOR {i:02d}", brand)

        section("PROJECT STATUS")

        intel("ORIGIN", "INDIA")
        intel("TARGET", "GERMANY")
        intel("PRODUCT", "WIRELESS EARBUDS")


# ============================================================
# 2. MARKET ANALYSIS
# ============================================================

elif page == "MARKET ANALYSIS":

    header(
        "MARKET INTELLIGENCE",
        "GERMANY · ECONOMIC ENVIRONMENT · PESTLE"
    )

    cols = st.columns(4)

    card(cols[0], "TARGET COUNTRY", "GERMANY", "EUROPE")
    card(cols[1], "PRODUCT CATEGORY", "TWS AUDIO", "WIRELESS EARBUDS")
    card(cols[2], "ENTRY APPROACH", "PHASED", "ONLINE FIRST")
    card(cols[3], "RESEARCH STATUS", "VALIDATE", "SOURCE MARKET DATA")

    section("PESTLE ENVIRONMENTAL SCAN")

    left, right = st.columns(2)

    for i, (factor, (finding, action)) in enumerate(pestle.items()):

        with (left if i % 2 == 0 else right):

            with st.expander(factor, expanded=(i == 0)):

                st.write(finding)
                st.markdown(f"**IMPLICATION FOR boAt:** {action}")

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        section("POTENTIAL OPPORTUNITIES")

        intel("ONLINE ENTRY", "Test German online channels before wider retail expansion.")
        intel("VALUE POSITIONING", "Explore the accessible-price segment with a differentiated product offer.")
        intel("USE-CASE TARGETING", "Commuting, studying, work calls and fitness are potential use cases.")

    with right:

        section("KEY RISKS")

        intel("COMPETITION", "Established brands have stronger recognition and distribution.")
        intel("COMPLIANCE", "EU product and producer-responsibility requirements may increase costs.")
        intel("BRAND AWARENESS", "boAt needs local trust, support and product credibility.")

    section("RESEARCH VALIDATION CHECKLIST")

    st.checkbox("Find a reliable Germany headphone/TWS market-size source", key="pestle_1")
    st.checkbox("Compare current German retail prices for named earbud models", key="pestle_2")
    st.checkbox("Verify EU compliance and importer obligations", key="pestle_3")
    st.checkbox("Conduct or obtain German customer preference research", key="pestle_4")


# ============================================================
# 3. COMPETITOR ANALYSIS
# ============================================================

elif page == "COMPETITOR ANALYSIS":

    header(
        "COMPETITIVE INTELLIGENCE",
        "GERMANY · WIRELESS AUDIO BRAND LANDSCAPE"
    )

    cols = st.columns(3)

    card(cols[0], "BRANDS ANALYSED", "06", "FIVE COMPARISON BRANDS + boAt")
    card(cols[1], "MARKET FOCUS", "TWS", "WIRELESS EARBUDS")
    card(cols[2], "boAt POSITION", "VALUE", "STYLE-LED AUDIO")

    section("BRAND POSITIONING DATABASE")

    chosen = st.multiselect(
        "FILTER BRANDS",
        brands.Brand.tolist(),
        default=brands.Brand.tolist(),
        key="brandfilter"
    )

    st.dataframe(
        brands[brands.Brand.isin(chosen)],
        use_container_width=True,
        hide_index=True
    )

    section("QUALITATIVE COMPETITOR SCORECARD")

    st.caption(
        "Scale 1–5. Provisional analyst assessments, not independent product tests or verified market rankings."
    )

    metric = st.selectbox(
        "COMPARISON DIMENSION",
        [
            "Sound quality",
            "Technology",
            "Value",
            "Brand familiarity in Germany"
        ]
    )

    subset = scores[scores.Brand.isin(chosen)]

    fig = px.bar(
        subset.sort_values(metric),
        x=metric,
        y="Brand",
        orientation="h",
        color=metric,
        color_continuous_scale=["#07517b", CYAN],
        text=metric
    )

    fig.update_traces(
        texttemplate="%{text:.1f}/5",
        textposition="inside"
    )

    fig.update_layout(
        xaxis=dict(range=[0, 5], title="PROVISIONAL SCORE / 5"),
        yaxis_title="",
        coloraxis_showscale=False
    )

    st.plotly_chart(
        chart_style(fig, 350),
        use_container_width=True
    )

    section("MULTI-DIMENSIONAL BRAND COMPARISON")

    radar_brands = st.multiselect(
        "SELECT UP TO FIVE BRANDS",
        scores.Brand.tolist(),
        default=["Apple", "JBL", "Sony", "boAt"],
        max_selections=5,
        key="radarbrands"
    )

    dimensions = [
        "Sound quality",
        "Technology",
        "Value",
        "Brand familiarity in Germany"
    ]

    radar = go.Figure()

    for brand in radar_brands:

        row = scores[scores.Brand == brand].iloc[0]
        vals = [row[d] for d in dimensions]

        radar.add_trace(
            go.Scatterpolar(
                r=vals + [vals[0]],
                theta=dimensions + [dimensions[0]],
                fill="toself",
                name=brand,
                opacity=0.6
            )
        )

    radar.update_layout(
        polar=dict(
            bgcolor="#061326",
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                color=TEXT,
                gridcolor="#16466c"
            ),
            angularaxis=dict(
                color=TEXT,
                gridcolor="#16466c"
            )
        )
    )

    st.plotly_chart(
        chart_style(radar, 420),
        use_container_width=True
    )

    section("STRATEGIC IMPLICATIONS FOR boAt")

    intel("POTENTIAL ADVANTAGE", "Accessible pricing, distinctive design and everyday functionality.")
    intel("CAPABILITY GAP", "German brand awareness, local-language support and after-sales service.")
    intel("NEXT STEP", "Compare named products, prices and features before making final competitive claims.")


# ============================================================
# 4. SWOT ANALYSIS
# ============================================================

elif page == "SWOT ANALYSIS":

    header(
        "STRATEGIC SWOT ANALYSIS",
        "boAt · INTERNAL CAPABILITIES & EXTERNAL ENVIRONMENT"
    )

    left, right = st.columns(2)

    with left:

        section("STRENGTHS")

        intel("S1", "Established Indian audio brand.")
        intel("S2", "Value-focused product positioning.")
        intel("S3", "Youth-oriented brand identity.")
        intel("S4", "Experience in personal audio products.")

        section("WEAKNESSES")

        intel("W1", "Limited initial familiarity in Germany.")
        intel("W2", "Need to develop local customer support.")
        intel("W3", "Product-market fit and willingness to pay require validation.")

    with right:

        section("OPPORTUNITIES")

        intel("O1", "Online-first market testing.")
        intel("O2", "Potential use cases across commuting, study, work and fitness.")
        intel("O3", "Potential partnerships with local retailers.")
        intel("O4", "Differentiate through value, design and service.")

        section("THREATS")

        intel("T1", "Established brands such as Apple, JBL and Sony.")
        intel("T2", "Price competition and promotional pressure.")
        intel("T3", "EU compliance and producer-responsibility costs.")

    section("TOWS STRATEGIC RESPONSE")

    actions = pd.DataFrame([
        ["SO", "Use value positioning and brand identity to test online channels."],
        ["WO", "Build awareness through local creators and German-language support."],
        ["ST", "Differentiate through useful features and reliable service."],
        ["WT", "Start with a limited range and validate demand before scaling."]
    ], columns=["STRATEGY", "RECOMMENDED ACTION"])

    st.dataframe(actions, use_container_width=True, hide_index=True)


# ============================================================
# 5. CUSTOMER SEGMENTATION
# ============================================================

elif page == "CUSTOMER SEGMENTATION":

    header(
        "CUSTOMER INTELLIGENCE",
        "GERMANY · SEGMENT IDENTIFICATION & EVALUATION"
    )

    section("CUSTOMER SEGMENT DATABASE")

    st.dataframe(
        segment_detail,
        use_container_width=True,
        hide_index=True
    )

    section("SEGMENT ATTRACTIVENESS")

    fig = px.bar(
        segments.sort_values("Score"),
        x="Score",
        y="Segment",
        orientation="h",
        color="Score",
        color_continuous_scale=["#07517b", CYAN],
        text="Score"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="inside"
    )

    fig.update_layout(
        xaxis=dict(range=[0, 5], title="ANALYST-ASSIGNED SCORE / 5"),
        yaxis_title="",
        coloraxis_showscale=False
    )

    st.plotly_chart(
        chart_style(fig, 350),
        use_container_width=True
    )

    st.caption(
        "These scores reproduce the preliminary evaluation model. They are not survey results."
    )

    section("SEGMENT EXPLORER")

    selected = st.selectbox(
        "SELECT CUSTOMER GROUP",
        segment_detail.Segment.tolist()
    )

    row = segment_detail[segment_detail.Segment == selected].iloc[0]

    a, b = st.columns(2)

    card(a, "CUSTOMER PROFILE", row["Profile"], "PROPOSED SEGMENT")
    card(b, "INITIAL ASSESSMENT", row["Initial assessment"], "STRATEGIC EVALUATION")

    st.write("**USE CASE:**", row["Use case"])
    st.write("**PURCHASE PRIORITIES:**", row["Purchase priorities"])


# ============================================================
# 6. STP ANALYSIS
# ============================================================

elif page == "STP ANALYSIS":

    header(
        "STP INTELLIGENCE",
        "SEGMENTATION · TARGETING · POSITIONING"
    )

    section("01 · SEGMENTATION")

    st.write(
        "The proposed market is divided into young professionals, university students, fitness enthusiasts, technology enthusiasts and budget-conscious consumers. These groups may overlap."
    )

    section("02 · TARGETING")

    a, b = st.columns(2)

    card(a, "PRIMARY TARGET", "YOUNG PROFESSIONALS", "PRELIMINARY SCORE: 3.85 / 5")
    card(b, "SECONDARY TARGET", "UNIVERSITY STUDENTS", "PRELIMINARY SCORE: 3.60 / 5")

    a, b = st.columns(2)

    with a:
        st.write(
            "Adults approximately 22–35 who may use earbuds for commuting, work calls and entertainment."
        )

    with b:
        st.write(
            "Students who may value accessible pricing, comfort, battery life and everyday versatility."
        )

    section("03 · CUSTOMER PERSONA")

    a, b = st.columns([1, 2])

    with a:

        st.markdown("""
        <div class="hud-card" style="text-align:center;padding:24px;">
            <div style="font-size:42px;color:#16d9ff;">◉</div>
            <div style="font-family:Orbitron;color:#dff8ff;">
                LUKAS WEBER
            </div>
            <div class="hud-note">
                ILLUSTRATIVE PERSONA
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b:

        intel("AGE", "27 years")
        intel("LOCATION", "Berlin, Germany")
        intel("OCCUPATION", "Marketing executive")
        intel(
            "NEEDS",
            "Comfortable earbuds, clear calls, reliable battery and accessible pricing."
        )

    section("04 · POSITIONING")

    st.markdown("""
    <div style="
        border:1px solid #168bff;
        background:linear-gradient(90deg,#061326,#0a2b4a);
        padding:20px;
        text-align:center;
        font-family:Orbitron;
        color:#16d9ff;
        letter-spacing:2px;
        font-size:clamp(16px,2vw,24px);
    ">
        AFFORDABLE SOUND.<br>
        BOLD STYLE.<br>
        EVERYDAY PERFORMANCE.
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "For young professionals and students in Germany who want stylish and reliable wireless audio at an accessible price, boAt aims to offer modern earbuds combining useful everyday features, distinctive design and value."
    )

    st.caption("Proposed positioning. Validate with German customer research.")


# ============================================================
# 7. MARKET ENTRY STRATEGY
# ============================================================

elif page == "MARKET ENTRY STRATEGY":

    header(
        "MARKET ENTRY OPERATIONS",
        "GERMANY · INTERNATIONAL EXPANSION STRATEGY"
    )

    c1, c2, c3 = st.columns(3)

    card(c1, "ENTRY MODEL", "PHASED", "ONLINE-FIRST MARKET ENTRY")
    card(c2, "INITIAL SCOPE", "LIMITED", "SELECTED EARBUD MODELS")
    card(c3, "SCALE GATE", "VALIDATE", "DEMAND AND UNIT ECONOMICS")

    section("ENTRY ROADMAP")

    phases = pd.DataFrame([
        [
            "PHASE 01 · TEST",
            "Launch a limited product selection through a suitable online channel and measure customer response."
        ],
        [
            "PHASE 02 · PARTNER",
            "Evaluate local distributors and electronics retail partnerships after initial validation."
        ],
        [
            "PHASE 03 · SCALE",
            "Expand product range and retail presence only if demand, margins and service performance justify it."
        ]
    ], columns=["STAGE", "STRATEGIC ACTION"])

    st.dataframe(phases, use_container_width=True, hide_index=True)

    section("INTERNATIONAL MARKETING MIX · 4Ps")

    left, right = st.columns(2)

    with left:

        with st.expander("PRODUCT STRATEGY", expanded=True):
            st.write(
                "Select earbuds with comfortable fit, dependable microphone performance, useful battery life, USB-C charging and relevant water/sweat resistance. Confirm applicable EU conformity and German-language product information."
            )

        with st.expander("PRICE STRATEGY"):
            st.write(
                "Use competitive value-based pricing. Calculate German retail prices using landed cost, VAT, retailer margin, fulfilment, warranty and competitor comparisons."
            )

    with right:

        with st.expander("PLACE STRATEGY", expanded=True):
            st.write(
                "Assess a German-language online store, suitable marketplaces and later partnerships with established electronics retailers. Confirm seller, importer and fulfilment responsibilities."
            )

        with st.expander("PROMOTION STRATEGY"):
            st.write(
                "Use German-language product content, technology reviews, local creators, product demonstrations and measurable launch campaigns."
            )

    section("IMPLEMENTATION TRACKER")

    tasks = [
        "Select specific earbud models for Germany",
        "Calculate landed cost and target retail price",
        "Confirm EU compliance and importer obligations",
        "Arrange German-language support, warranty and returns",
        "Test online demand before wider rollout"
    ]

    for i, item in enumerate(tasks):
        st.checkbox(item, key=f"entry_check_{i}")


# ============================================================
# 8. AI INSIGHTS
# ============================================================

elif page == "AI INSIGHTS":

    header(
        "ARTIFICIAL INTELLIGENCE",
        "STRATEGIC MARKET ANALYSIS · AI INSIGHTS MODULE"
    )

    st.info(
        "This module prepares an analysis prompt. It is not connected to a live AI API yet."
    )

    section("INTELLIGENCE QUERY")

    question = st.text_area(
        "ENTER YOUR STRATEGIC QUESTION",
        placeholder="Example: What are the biggest risks boAt should address before entering Germany?",
        height=110
    )

    if st.button("GENERATE ANALYSIS PROMPT"):

        if question.strip():

            prompt = f"""
You are an international marketing analyst.

PROJECT:
boAt, an Indian audio brand, is considering a phased entry
into Germany's wireless earbuds market.

TARGET HYPOTHESES:
Young professionals and university students.

POTENTIAL COMPETITORS:
Apple, JBL, Sony, Samsung and Soundcore.

PROPOSED ENTRY:
Online-first testing followed by local distribution partnerships.

QUESTION:
{question}

INSTRUCTIONS:
Use supplied facts as facts.
Identify assumptions and missing evidence.
Do not invent market statistics, prices or market shares.
Provide a concise recommendation and measurable validation steps.
"""

            st.text_area(
                "YOUR AI ANALYSIS PROMPT",
                value=prompt,
                height=270
            )

        else:
            st.warning("Please enter a question first.")

    section("AI ANALYSIS FRAMEWORK")

    intel("MARKET ATTRACTIVENESS", "Assess market opportunity and evidence gaps.")
    intel("COMPETITIVE DIFFERENTIATION", "Evaluate brand positioning and competitor advantages.")
    intel("CUSTOMER FIT", "Assess target-segment needs and product suitability.")
    intel("RISK INTELLIGENCE", "Identify regulatory, operational and financial risks.")


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    "<hr style='border:0;border-top:1px solid #16466c;margin-top:25px;'>",
    unsafe_allow_html=True
)

st.markdown("""
<div style="
    text-align:center;
    padding:12px;
    font-family:Orbitron,Arial;
    font-size:8px;
    color:#6686a2;
    letter-spacing:2px;
">
    GLOBAL INTELLIGENCE SYSTEM · boAt × GERMANY · 2026
    <br>
    INTERNATIONAL MARKET EXPLORER
</div>
""", unsafe_allow_html=True)