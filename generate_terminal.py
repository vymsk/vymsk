import datetime
import os
from pathlib import Path

def generate_terminal_svg(output_path: Path):
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="650" height="320" viewBox="0 0 650 320" fill="none">
    <style>
        @keyframes blink {{
            0%, 49% {{ opacity: 1; }}
            50%, 100% {{ opacity: 0; }}
        }}
        .cursor {{
            animation: blink 0.9s infinite;
        }}
        .term-text {{
            font-family: ui-monospace, 'SF Mono', 'Menlo', 'Cascadia Code', monospace;
            font-size: 13px;
            letter-spacing: 0.4px;
        }}
        .white {{ fill: #f0f0f0; }}
        .bright {{ fill: #ffffff; font-weight: bold; }}
        .gray-light {{ fill: #b0b0b0; }}
        .gray-mid {{ fill: #707070; }}
        .gray-dark {{ fill: #404040; }}
    </style>

    <!-- Terminal Window Frame (Monochrome Noir) -->
    <rect width="650" height="320" rx="8" fill="#09090b" stroke="#27272a" stroke-width="1.2" />

    <!-- Title Bar -->
    <path d="M 0 8 C 0 3.58 3.58 0 8 0 L 642 0 C 646.42 0 650 3.58 650 8 L 650 32 L 0 32 Z" fill="#141416" />
    <line x1="0" y1="32" x2="650" y2="32" stroke="#222225" stroke-width="1" />

    <!-- Window Controls (Grayscale Dots) -->
    <circle cx="20" cy="16" r="5" fill="#404040" />
    <circle cx="36" cy="16" r="5" fill="#2d2d2d" />
    <circle cx="52" cy="16" r="5" fill="#222222" />

    <!-- Terminal Title -->
    <text x="325" y="21" text-anchor="middle" class="term-text gray-mid" font-size="11">fsociety://root@vymsk:~ [noir-mode]</text>

    <!-- Subtle Monochrome Scanline -->
    <line x1="0" y1="33" x2="650" y2="33" stroke="rgba(255, 255, 255, 0.04)" stroke-width="1.5">
        <animate attributeName="y1" from="33" to="320" dur="5s" repeatCount="indefinite" />
        <animate attributeName="y2" from="33" to="320" dur="5s" repeatCount="indefinite" />
    </line>

    <!-- Content / Commands -->
    <g transform="translate(24, 60)" class="term-text">
        <!-- Line 1 -->
        <text y="0">
            <tspan class="bright">root@vymsk</tspan><tspan class="gray-dark">:</tspan><tspan class="gray-light">~</tspan><tspan class="gray-dark"># </tspan><tspan class="white">whoami --details</tspan>
        </text>

        <!-- Line 2 & 3 Output -->
        <text y="24" class="gray-mid">UID=0(root) GID=0(fsociety) PRIVILEGE=ABSOLUTE</text>
        <text y="44" class="white">● STATUS: RUNNING IN THE SHADOWS / CREATING REPOS</text>

        <!-- Line 4 -->
        <text y="76">
            <tspan class="bright">root@vymsk</tspan><tspan class="gray-dark">:</tspan><tspan class="gray-light">~</tspan><tspan class="gray-dark"># </tspan><tspan class="white">sysctl -n machdep.cpu.brand_string</tspan>
        </text>

        <!-- Line 5 & 6 Output -->
        <text y="100" class="gray-mid">Darwin Kernel / Apple Silicon Architecture</text>
        <text y="120" class="gray-light">SEC_PROTO: SSH-ED25519 [AUTHENTICATED]</text>

        <!-- Line 7 -->
        <text y="154">
            <tspan class="bright">root@vymsk</tspan><tspan class="gray-dark">:</tspan><tspan class="gray-light">~</tspan><tspan class="gray-dark"># </tspan><tspan class="white">cat /var/log/presence.now</tspan>
        </text>

        <!-- Line 8 Output -->
        <text y="178" class="gray-light">TIMESTAMP: {timestamp}</text>
        <text y="202">
            <tspan class="gray-mid">&gt; “Control is an illusion. Hello, friend.” </tspan>
            <tspan class="bright cursor">█</tspan>
        </text>
    </g>
</svg>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg, encoding="utf-8")
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    generate_terminal_svg(base_dir / "assets" / "terminal-noir.svg")
