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
            animation: blink 1s infinite;
        }}
        .term-text {{
            font-family: ui-monospace, 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
            font-size: 13px;
            letter-spacing: 0.5px;
        }}
        .green {{ fill: #00ff66; }}
        .red {{ fill: #ff0033; }}
        .dim {{ fill: #666666; }}
        .white {{ fill: #e6e6e6; }}
        .cyan {{ fill: #00e5ff; }}
        .yellow {{ fill: #ffcc00; }}
    </style>

    <!-- Terminal Window Frame -->
    <rect width="650" height="320" rx="10" fill="#050505" stroke="#ff0033" stroke-width="1.5" />

    <!-- Title Bar -->
    <path d="M 0 10 C 0 4.477 4.477 0 10 0 L 640 0 C 645.523 0 650 4.477 650 10 L 650 34 L 0 34 Z" fill="#0d0d0d" />
    <line x1="0" y1="34" x2="650" y2="34" stroke="#222" stroke-width="1" />

    <!-- Window Controls -->
    <circle cx="20" cy="17" r="6" fill="#ff5f56" />
    <circle cx="40" cy="17" r="6" fill="#ffbd2e" />
    <circle cx="60" cy="17" r="6" fill="#27c93f" />

    <!-- Terminal Title -->
    <text x="325" y="22" text-anchor="middle" class="term-text dim" font-size="11" font-weight="bold">fsociety://root@vymsk:~ (zsh)</text>

    <!-- Scanline effect -->
    <line x1="0" y1="35" x2="650" y2="35" stroke="rgba(255, 0, 51, 0.08)" stroke-width="2">
        <animate attributeName="y1" from="35" to="320" dur="4s" repeatCount="indefinite" />
        <animate attributeName="y2" from="35" to="320" dur="4s" repeatCount="indefinite" />
    </line>

    <!-- Content / Commands -->
    <g transform="translate(24, 60)" class="term-text">
        <!-- Line 1 -->
        <text y="0">
            <tspan class="red" font-weight="bold">root@vymsk</tspan><tspan class="dim">:</tspan><tspan class="cyan">~</tspan><tspan class="dim"># </tspan><tspan class="white">whoami --details</tspan>
        </text>

        <!-- Line 2 & 3 Output -->
        <text y="24" class="dim">UID=0(root) GID=0(fsociety) SEC_LEVEL=ELEVATED</text>
        <text y="44" class="green">✔ STATUS: INFILTRATING SYSTEMS / BUILDING REPOS</text>

        <!-- Line 4 -->
        <text y="76">
            <tspan class="red" font-weight="bold">root@vymsk</tspan><tspan class="dim">:</tspan><tspan class="cyan">~</tspan><tspan class="dim"># </tspan><tspan class="white">nmap -sS -O target.sys</tspan>
        </text>

        <!-- Line 5 & 6 Output -->
        <text y="100" class="dim">PORT 22/tcp  OPEN  ssh (Apple OpenSSH 9.8)</text>
        <text y="120" class="dim">PORT 443/tcp OPEN  https (TLSv1.3 Encrypted)</text>
        <text y="140" class="yellow">OS: macOS / Darwin Kernel (ARM64/x86_64)</text>

        <!-- Line 7 -->
        <text y="174">
            <tspan class="red" font-weight="bold">root@vymsk</tspan><tspan class="dim">:</tspan><tspan class="cyan">~</tspan><tspan class="dim"># </tspan><tspan class="white">cat /var/log/presence.now</tspan>
        </text>

        <!-- Line 8 Output -->
        <text y="198" class="green">ACTIVE_SYNC: {timestamp}</text>
        <text y="218">
            <tspan class="dim">&gt; “Our democracy has been hacked.” </tspan>
            <tspan class="red cursor" font-weight="bold">█</tspan>
        </text>
    </g>
</svg>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(svg, encoding="utf-8")
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    generate_terminal_svg(base_dir / "assets" / "terminal.svg")
