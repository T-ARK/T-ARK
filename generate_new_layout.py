import os

assets_dir = "/home/ark123/Documents/T-ARK/assets"
os.makedirs(assets_dir, exist_ok=True)

# =========================================================================
# 1. assets/01_top_section.svg
# Left: Terminal $ celefetch with ASCII Art + World Map with location ping
# Right: // WHO I AM code editor window
# =========================================================================
top_section_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="100%" height="100%">
  <defs>
    <linearGradient id="card-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d18" />
      <stop offset="100%" stop-color="#050811" />
    </linearGradient>

    <linearGradient id="editor-dark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#140b2a" />
      <stop offset="100%" stop-color="#0a0518" />
    </linearGradient>

    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'SF Mono', Consolas, 'Fira Code', 'Courier New', monospace; }
  </style>

  <!-- Left Column: Terminal & World Map -->
  <g transform="translate(0, 0)">
    <!-- 1. Terminal Celefetch Box -->
    <rect width="330" height="285" rx="8" fill="url(#card-dark)" stroke="#1e293b" stroke-width="1.2" />

    <!-- Terminal header & text -->
    <text x="14" y="24" class="font-mono" font-size="12" font-weight="700" fill="#38bdf8">$ celefetch</text>

    <!-- ASCII Art Character/Droplet -->
    <g class="font-mono" font-size="9" fill="#94a3b8" transform="translate(14, 40)" xml:space="preserve">
      <text y="0"><tspan fill="#64748b">       .':.</tspan></text>
      <text y="12"><tspan fill="#64748b">      .':clc.        ..:cc:'</tspan></text>
      <text y="24"><tspan fill="#64748b">     .':cllll:.    'lONWWKkl'</tspan></text>
      <text y="36"><tspan fill="#64748b">    .':cllllllc.  ;0NMMMMMWKo.</tspan></text>
      <text y="48"><tspan fill="#94a3b8">  .':clllllllll:.'kWMMMMMMMMMNk'</tspan></text>
      <text y="60"><tspan fill="#94a3b8">..':clc;...       ;0NMM0kOONMMMWx;</tspan></text>
      <text y="72"><tspan fill="#cbd5e1">':cll;'     .':cl:..c0WMMNk:..cKWMMWO:</tspan></text>
      <text y="84"><tspan fill="#cbd5e1">;cll:       ;0WMMNk'  ;OWMMNd.  ;OWMMNk'</tspan></text>
      <text y="96"><tspan fill="#cbd5e1">;cll:       'kMMMMX:   ;OWMMNd.  ;0WMMNk'</tspan></text>
      <text y="108"><tspan fill="#e2e8f0">;cllll:'   ;0WMMNk'     ;0WMMNk'  ;0WMMNk'</tspan></text>
      <text y="120"><tspan fill="#e2e8f0">;clllll:;cx0k;             .':doc::::;</tspan></text>
      <text y="132"><tspan fill="#94a3b8">;looooool:'                  .':clll:;</tspan></text>
      <text y="144"><tspan fill="#64748b">;loooool;.                    .':cll:;</tspan></text>
      <text y="156"><tspan fill="#94a3b8">;loool;cx0000kx:            ;x0WMMMNk'</tspan></text>
      <text y="168"><tspan fill="#cbd5e1">.':looooooodk00OkkOOOOOOOOkc. .ckNMMMN</tspan></text>
      <text y="180"><tspan fill="#64748b">   .':cloodddddddoolc;...       ;OWMM</tspan></text>
      <text y="192"><tspan fill="#475569">         .....                   :xX0</tspan></text>
    </g>

    <!-- 2. World Map Box -->
    <g transform="translate(0, 298)">
      <rect width="330" height="180" rx="8" fill="url(#card-dark)" stroke="#1e293b" stroke-width="1.2" />

      <!-- World Map Outline (Accurate Vector Silhouette) -->
      <g transform="translate(15, 18)" fill="#e2e8f0" opacity="0.9">
        <!-- North America -->
        <path d="M 28,15 L 36,12 L 48,10 L 68,14 L 80,24 L 84,36 L 76,46 L 70,58 L 62,64 L 54,60 L 50,48 L 40,46 L 30,34 L 20,26 Z" />
        <path d="M 44,58 L 52,66 L 56,76 L 62,84 L 56,92 L 50,88 L 46,74 Z" />
        <path d="M 62,8 L 82,6 L 88,14 L 78,18 Z" /> <!-- Greenland -->

        <!-- South America -->
        <path d="M 66,95 L 76,96 L 86,108 L 84,124 L 78,140 L 72,148 L 68,136 L 64,116 L 62,104 Z" />

        <!-- Europe -->
        <path d="M 128,24 L 140,22 L 148,28 L 146,38 L 138,44 L 130,46 L 126,38 L 122,34 Z" />
        <path d="M 120,20 L 124,14 L 128,18 L 124,24 Z" /> <!-- UK -->
        <path d="M 136,10 L 144,8 L 148,16 L 142,22 Z" /> <!-- Scandinavia -->

        <!-- Africa -->
        <path d="M 126,50 L 144,48 L 158,56 L 164,74 L 158,94 L 148,114 L 138,118 L 132,106 L 124,84 L 122,66 Z" />
        <path d="M 166,96 L 170,108 L 166,112 L 164,102 Z" /> <!-- Madagascar -->

        <!-- Asia -->
        <path d="M 152,20 L 180,18 L 210,22 L 240,28 L 255,42 L 246,58 L 228,62 L 214,54 L 202,46 L 188,48 L 174,44 L 158,34 Z" />
        <path d="M 218,60 L 230,68 L 242,76 L 232,84 L 222,78 L 216,68 Z" /> <!-- SE Asia -->
        <!-- India Subcontinent -->
        <path d="M 188,52 L 204,54 L 208,68 L 198,84 L 188,72 Z" fill="#ffffff" />
        <circle cx="196" cy="78" r="4" fill="#38bdf8" /> <!-- Kerala Pin -->

        <!-- Australia & Oceania -->
        <path d="M 240,102 L 260,98 L 272,108 L 268,124 L 254,128 L 242,122 L 236,110 Z" />
        <path d="M 276,128 L 282,138 L 278,142 Z" />
      </g>

      <!-- Kerala Radar Ping Effect -->
      <g transform="translate(211, 96)">
        <circle cx="0" cy="0" r="10" fill="none" stroke="#38bdf8" stroke-width="1.2" opacity="0.6">
          <animate attributeName="r" values="4;14" dur="2s" repeatCount="indefinite" />
          <animate attributeName="opacity" values="0.8;0" dur="2s" repeatCount="indefinite" />
        </circle>
        <circle cx="0" cy="0" r="3" fill="#38bdf8" filter="url(#soft-glow)" />
      </g>
    </g>
  </g>

  <!-- Right Column: // WHO I AM -->
  <g transform="translate(350, 0)">
    <!-- Header -->
    <text x="2" y="18" class="font-sans" font-size="15" font-weight="800" fill="#c084fc" letter-spacing="1.5">// WHO I AM</text>

    <!-- macOS Code Window -->
    <g transform="translate(0, 30)">
      <rect width="590" height="448" rx="10" fill="url(#editor-dark)" stroke="#381d63" stroke-width="1.2" />

      <!-- Top window bar -->
      <path d="M 0,10 C 0,4.5 4.5,0 10,0 L 580,0 C 585.5,0 590,4.5 590,10 L 590,32 L 0,32 Z" fill="#1b0e36" />
      <circle cx="18" cy="16" r="5" fill="#ef4444" />
      <circle cx="34" cy="16" r="5" fill="#f59e0b" />
      <circle cx="50" cy="16" r="5" fill="#10b981" />
      <text x="295" y="20" class="font-sans" font-size="12" fill="#a78bfa" text-anchor="middle" font-weight="600">developer.py</text>

      <!-- Code lines with exact formatting -->
      <g class="font-mono" font-size="11.5" transform="translate(20, 56)">
        <text y="0"><tspan fill="#c084fc" font-weight="700">class</tspan> <tspan fill="#fde047">Developer</tspan></text>
        <text y="18"><tspan fill="#c084fc" font-weight="700">def</tspan> <tspan fill="#60a5fa">__init__</tspan> <tspan fill="#c084fc">self</tspan></text>
        <text y="36"><tspan fill="#e9d5ff">self.name</tspan> <tspan fill="#86efac">"Arshid Chandran P K"</tspan></text>
        <text y="54"><tspan fill="#e9d5ff">self.location</tspan> <tspan fill="#86efac">"Kerala, India 🇮🇳"</tspan></text>
        <text y="72"><tspan fill="#e9d5ff">self.degree</tspan> <tspan fill="#86efac">"B.Tech - Computer Science</tspan></text>
        <text y="90"><tspan fill="#86efac">Engineering (Data Science)"</tspan></text>
        <text y="108"><tspan fill="#e9d5ff">self.role</tspan> <tspan fill="#86efac">"Aspiring Data Scientist &amp; Dev"</tspan></text>
        
        <text y="132"><tspan fill="#e9d5ff">self.stack</tspan></text>
        <text y="150"><tspan fill="#c084fc">"languages"</tspan> <tspan fill="#fde047">"Python"</tspan> <tspan fill="#fde047">"C"</tspan> <tspan fill="#fde047">"C++"</tspan> <tspan fill="#fde047">"JS"</tspan></text>
        <text y="168"><tspan fill="#c084fc">"web"</tspan> <tspan fill="#fde047">"HTML5"</tspan> <tspan fill="#fde047">"CSS3"</tspan> <tspan fill="#fde047">"Responsive"</tspan></text>
        <text y="186"><tspan fill="#c084fc">"data_science"</tspan> <tspan fill="#fde047">"NumPy"</tspan> <tspan fill="#fde047">"Pandas"</tspan> <tspan fill="#fde047">"Scikit"</tspan></text>

        <text y="214"><tspan fill="#e9d5ff">self.currently_learning</tspan></text>
        <text y="232"><tspan fill="#86efac">"Machine Learning"</tspan> <tspan fill="#86efac">"Cybersecurity"</tspan></text>
        <text y="250"><tspan fill="#86efac">"Advanced Data Visualization"</tspan></text>

        <text y="278"><tspan fill="#e9d5ff">self.interests</tspan> <tspan fill="#fde047">"Data Science"</tspan> <tspan fill="#fde047">"AI"</tspan></text>
        <text y="296"><tspan fill="#fde047">"Cybersecurity"</tspan> <tspan fill="#fde047">"Photography"</tspan> <tspan fill="#fde047">"Design"</tspan></text>

        <text y="318"><tspan fill="#e9d5ff">self.languages_spoken</tspan></text>
        <text y="336"><tspan fill="#86efac">"English"</tspan> <tspan fill="#86efac">"Malayalam"</tspan> <tspan fill="#86efac">"Hindi"</tspan> <tspan fill="#86efac">"Tamil"</tspan></text>

        <text y="358"><tspan fill="#e9d5ff">self.fun_fact</tspan> <tspan fill="#86efac">"I love debugging &amp; cameras 📷"</tspan></text>

        <text y="380"><tspan fill="#c084fc" font-weight="700">def</tspan> <tspan fill="#60a5fa">motto</tspan> <tspan fill="#c084fc">self</tspan></text>
        <text y="398"><tspan fill="#c084fc" font-weight="700">return</tspan> <tspan fill="#fde047">"Stay curious. Keep building."</tspan></text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "01_top_section.svg"), "w") as f:
    f.write(top_section_svg)

print("Created 01_top_section.svg")
# =========================================================================
# 2. assets/02_starred_topics.svg
# Header: 🔭 Starred topics + dense matrix of developer icons
# =========================================================================
starred_topics_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 195" width="100%" height="100%">
  <defs>
    <linearGradient id="topic-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c18" />
      <stop offset="100%" stop-color="#050811" />
    </linearGradient>

    <clipPath id="tile-clip">
      <rect width="36" height="36" rx="8" />
    </clipPath>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .icon-tile { rx: 8px; width: 36px; height: 36px; }
  </style>

  <!-- Container Box -->
  <rect width="940" height="195" rx="8" fill="url(#topic-bg)" stroke="#1e293b" stroke-width="1.2" />

  <!-- Header -->
  <g transform="translate(18, 22)">
    <text x="0" y="0" font-size="16">🔭</text>
    <text x="24" y="-1" class="font-sans" font-size="15" font-weight="700" fill="#38bdf8">Starred topics</text>
  </g>

  <!-- Icons Wall Matrix (4 Rows x 14 Columns) -->
  <g transform="translate(18, 38)">
    <!-- Row 1 -->
    <!-- 0: JS -->
    <g transform="translate(0, 0)">
      <rect width="36" height="36" rx="8" fill="#f7df1e" />
      <text x="12" y="26" font-family="sans-serif" font-size="16" font-weight="900" fill="#000000">JS</text>
    </g>
    <!-- 1: C++ -->
    <g transform="translate(48, 0)">
      <rect width="36" height="36" rx="8" fill="#00599c" />
      <circle cx="18" cy="18" r="12" fill="#004482" />
      <text x="10" y="23" font-family="sans-serif" font-size="13" font-weight="900" fill="#ffffff">C++</text>
    </g>
    <!-- 2: Linux -->
    <g transform="translate(96, 0)">
      <rect width="36" height="36" rx="8" fill="#18181b" />
      <!-- Tux penguin silhouette -->
      <ellipse cx="18" cy="20" rx="9" ry="11" fill="#ffffff" />
      <ellipse cx="18" cy="20" rx="6" ry="8" fill="#000000" />
      <polygon points="18,14 15,17 21,17" fill="#f59e0b" />
      <ellipse cx="14" cy="30" rx="4" ry="2" fill="#f59e0b" />
      <ellipse cx="22" cy="30" rx="4" ry="2" fill="#f59e0b" />
    </g>
    <!-- 3: HTML5 -->
    <g transform="translate(144, 0)">
      <rect width="36" height="36" rx="8" fill="#e34f26" />
      <text x="11" y="26" font-family="sans-serif" font-size="17" font-weight="900" fill="#ffffff">5</text>
    </g>
    <!-- 4: CSS3 -->
    <g transform="translate(192, 0)">
      <rect width="36" height="36" rx="8" fill="#1572b6" />
      <text x="11" y="26" font-family="sans-serif" font-size="17" font-weight="900" fill="#ffffff">3</text>
    </g>
    <!-- 5: AWS -->
    <g transform="translate(240, 0)">
      <rect width="36" height="36" rx="8" fill="#232f3e" />
      <text x="7" y="20" font-family="sans-serif" font-size="10" font-weight="900" fill="#ffffff">aws</text>
      <path d="M 8,24 Q 18,30 28,24" fill="none" stroke="#ff9900" stroke-width="2" stroke-linecap="round" />
    </g>
    <!-- 6: Git -->
    <g transform="translate(288, 0)">
      <rect width="36" height="36" rx="8" fill="#f05032" />
      <rect x="9" y="9" width="18" height="18" rx="2" transform="rotate(45 18 18)" fill="#ffffff" />
      <circle cx="15" cy="18" r="2.2" fill="#f05032" />
      <circle cx="21" cy="14" r="2.2" fill="#f05032" />
      <line x1="15" y1="18" x2="21" y2="14" stroke="#f05032" stroke-width="1.6" />
    </g>
    <!-- 7: Docker -->
    <g transform="translate(336, 0)">
      <rect width="36" height="36" rx="8" fill="#2496ed" />
      <rect x="11" y="14" width="4" height="4" fill="#ffffff" />
      <rect x="16" y="14" width="4" height="4" fill="#ffffff" />
      <rect x="21" y="14" width="4" height="4" fill="#ffffff" />
      <rect x="16" y="9" width="4" height="4" fill="#ffffff" />
      <path d="M 7,20 C 10,27 26,27 29,20 Z" fill="#ffffff" />
    </g>
    <!-- 8: Arduino -->
    <g transform="translate(384, 0)">
      <rect width="36" height="36" rx="8" fill="#00979d" />
      <circle cx="13" cy="18" r="6" fill="none" stroke="#ffffff" stroke-width="1.8" />
      <circle cx="23" cy="18" r="6" fill="none" stroke="#ffffff" stroke-width="1.8" />
      <text x="11" y="20" font-family="sans-serif" font-size="7" font-weight="900" fill="#ffffff">-</text>
      <text x="21" y="21" font-family="sans-serif" font-size="7" font-weight="900" fill="#ffffff">+</text>
    </g>
    <!-- 9: SQL / Database -->
    <g transform="translate(432, 0)">
      <rect width="36" height="36" rx="8" fill="#336791" />
      <ellipse cx="18" cy="11" rx="10" ry="3.5" fill="#ffffff" />
      <path d="M 8,11 L 8,18 C 8,20 12,22 18,22 C 24,22 28,20 28,18 L 28,11" fill="none" stroke="#ffffff" stroke-width="1.5" />
      <path d="M 8,18 L 8,25 C 8,27 12,29 18,29 C 24,29 28,27 28,25 L 28,18" fill="none" stroke="#ffffff" stroke-width="1.5" />
    </g>
    <!-- 10: Bitcoin -->
    <g transform="translate(480, 0)">
      <rect width="36" height="36" rx="8" fill="#f7931a" />
      <text x="12" y="25" font-family="sans-serif" font-size="18" font-weight="900" fill="#ffffff">₿</text>
    </g>
    <!-- 11: Chrome -->
    <g transform="translate(528, 0)">
      <rect width="36" height="36" rx="8" fill="#1e293b" />
      <circle cx="18" cy="18" r="12" fill="#ea4335" />
      <circle cx="18" cy="18" r="7" fill="#fbbc05" />
      <circle cx="18" cy="18" r="5" fill="#4285f4" />
    </g>
    <!-- 12: Google -->
    <g transform="translate(576, 0)">
      <rect width="36" height="36" rx="8" fill="#ffffff" />
      <text x="10" y="26" font-family="sans-serif" font-size="20" font-weight="900" fill="#4285f4">G</text>
    </g>
    <!-- 13: Azure -->
    <g transform="translate(624, 0)">
      <rect width="36" height="36" rx="8" fill="#0089d6" />
      <polygon points="12,26 21,8 27,21 19,26" fill="#ffffff" />
    </g>
    <!-- 14: DevOps -->
    <g transform="translate(672, 0)">
      <rect width="36" height="36" rx="8" fill="#0284c7" />
      <text x="8" y="24" font-family="sans-serif" font-size="18" fill="#ffffff">∞</text>
    </g>
    <!-- 15: Octocat -->
    <g transform="translate(720, 0)">
      <rect width="36" height="36" rx="8" fill="#24292e" />
      <circle cx="18" cy="18" r="10" fill="#ffffff" />
      <circle cx="18" cy="18" r="7" fill="#24292e" />
      <path d="M 14,18 C 14,22 22,22 22,18 Z" fill="#ffffff" />
    </g>
    <!-- 16: Terminal -->
    <g transform="translate(768, 0)">
      <rect width="36" height="36" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1" />
      <text x="8" y="23" font-family="monospace" font-size="13" font-weight="900" fill="#38bdf8">&gt;_</text>
    </g>
    <!-- 17: GitHub -->
    <g transform="translate(816, 0)">
      <rect width="36" height="36" rx="8" fill="#181717" />
      <circle cx="18" cy="18" r="11" fill="#ffffff" />
      <path d="M 12,22 C 12,25 24,25 24,22 Z" fill="#181717" />
    </g>
    <!-- 18: Vue -->
    <g transform="translate(864, 0)">
      <rect width="36" height="36" rx="8" fill="#1e293b" />
      <polygon points="8,10 18,26 28,10 23,10 18,18 13,10" fill="#42b883" />
      <polygon points="13,10 18,18 23,10 19,10 18,12 17,10" fill="#35495e" />
    </g>

    <!-- Row 2 (y=44) -->
    <!-- 19: Bash -->
    <g transform="translate(0, 44)">
      <rect width="36" height="36" rx="8" fill="#293138" />
      <text x="6" y="22" font-family="monospace" font-size="8" font-weight="900" fill="#4eaa25">_BASH</text>
    </g>
    <!-- 20: Tor/Net -->
    <g transform="translate(48, 44)">
      <rect width="36" height="36" rx="8" fill="#59316b" />
      <circle cx="18" cy="18" r="10" fill="none" stroke="#ffffff" stroke-width="2" />
      <circle cx="18" cy="18" r="5" fill="none" stroke="#ffffff" stroke-width="2" />
    </g>
    <!-- 21: Raspberry Pi -->
    <g transform="translate(96, 44)">
      <rect width="36" height="36" rx="8" fill="#c51a4a" />
      <circle cx="18" cy="20" r="7" fill="#ffffff" />
      <polygon points="14,11 18,15 22,11" fill="#6cc04a" />
    </g>
    <!-- 22: Terminal -->
    <g transform="translate(144, 44)">
      <rect width="36" height="36" rx="8" fill="#000000" />
      <text x="7" y="23" font-family="monospace" font-size="14" font-weight="900" fill="#22c55e">&gt;_</text>
    </g>
    <!-- 23: TypeScript -->
    <g transform="translate(192, 44)">
      <rect width="36" height="36" rx="8" fill="#3178c6" />
      <text x="9" y="25" font-family="sans-serif" font-size="14" font-weight="900" fill="#ffffff">TS</text>
    </g>
    <!-- 24: iOS -->
    <g transform="translate(240, 44)">
      <rect width="36" height="36" rx="8" fill="#000000" />
      <text x="8" y="23" font-family="sans-serif" font-size="12" font-weight="700" fill="#ffffff">iOS</text>
    </g>
    <!-- 25: Android -->
    <g transform="translate(288, 44)">
      <rect width="36" height="36" rx="8" fill="#3ddc84" />
      <path d="M 12,20 C 12,14 24,14 24,20 Z" fill="#ffffff" />
      <circle cx="15" cy="17" r="1" fill="#3ddc84" />
      <circle cx="21" cy="17" r="1" fill="#3ddc84" />
    </g>
    <!-- 26: Cloudflare -->
    <g transform="translate(336, 44)">
      <rect width="36" height="36" rx="8" fill="#f38020" />
      <ellipse cx="18" cy="20" rx="9" ry="6" fill="#ffffff" />
      <circle cx="15" cy="16" r="4" fill="#ffffff" />
    </g>
    <!-- 27: Node.js -->
    <g transform="translate(384, 44)">
      <rect width="36" height="36" rx="8" fill="#339933" />
      <polygon points="18,10 26,14 26,22 18,26 10,22 10,14" fill="#ffffff" />
    </g>
    <!-- 28: Windows -->
    <g transform="translate(432, 44)">
      <rect width="36" height="36" rx="8" fill="#0078d4" />
      <rect x="10" y="10" width="7" height="7" fill="#ffffff" />
      <rect x="19" y="10" width="7" height="7" fill="#ffffff" />
      <rect x="10" y="19" width="7" height="7" fill="#ffffff" />
      <rect x="19" y="19" width="7" height="7" fill="#ffffff" />
    </g>
    <!-- 29: Vite -->
    <g transform="translate(480, 44)">
      <rect width="36" height="36" rx="8" fill="#1e1e20" />
      <polygon points="18,8 26,16 20,16 23,28 10,18 16,18" fill="#bd34fe" />
    </g>
    <!-- 30: Firefox -->
    <g transform="translate(528, 44)">
      <rect width="36" height="36" rx="8" fill="#ff7139" />
      <circle cx="18" cy="18" r="9" fill="#00539f" />
      <path d="M 12,24 C 10,16 24,14 26,24 Z" fill="#ffe900" />
    </g>
    <!-- 31: Angular -->
    <g transform="translate(576, 44)">
      <rect width="36" height="36" rx="8" fill="#dd0031" />
      <polygon points="18,8 26,11 24,24 18,27 12,24 10,11" fill="#c3002f" />
      <text x="13" y="22" font-family="sans-serif" font-size="12" font-weight="900" fill="#ffffff">A</text>
    </g>
    <!-- 32: npm -->
    <g transform="translate(624, 44)">
      <rect width="36" height="36" rx="8" fill="#cb3837" />
      <text x="6" y="23" font-family="sans-serif" font-size="11" font-weight="900" fill="#ffffff">npm</text>
    </g>
    <!-- 33: GraphQL -->
    <g transform="translate(672, 44)">
      <rect width="36" height="36" rx="8" fill="#e10098" />
      <circle cx="18" cy="18" r="8" fill="none" stroke="#ffffff" stroke-width="1.8" />
      <polygon points="18,10 25,22 11,22" fill="none" stroke="#ffffff" stroke-width="1.5" />
    </g>
    <!-- 34: Markdown -->
    <g transform="translate(720, 44)">
      <rect width="36" height="36" rx="8" fill="#000000" stroke="#334155" stroke-width="1" />
      <text x="6" y="23" font-family="sans-serif" font-size="10" font-weight="900" fill="#ffffff">M↓</text>
    </g>
    <!-- 35: React -->
    <g transform="translate(768, 44)">
      <rect width="36" height="36" rx="8" fill="#20232a" />
      <ellipse cx="18" cy="18" rx="10" ry="4" fill="none" stroke="#61dafb" stroke-width="1.5" />
      <ellipse cx="18" cy="18" rx="10" ry="4" fill="none" stroke="#61dafb" stroke-width="1.5" transform="rotate(60 18 18)" />
      <ellipse cx="18" cy="18" rx="10" ry="4" fill="none" stroke="#61dafb" stroke-width="1.5" transform="rotate(120 18 18)" />
      <circle cx="18" cy="18" r="2" fill="#61dafb" />
    </g>
    <!-- 36: Express -->
    <g transform="translate(816, 44)">
      <rect width="36" height="36" rx="8" fill="#ffffff" />
      <text x="3" y="22" font-family="sans-serif" font-size="7.5" font-weight="900" fill="#000000">express</text>
    </g>
    <!-- 37: Spring -->
    <g transform="translate(864, 44)">
      <rect width="36" height="36" rx="8" fill="#6db33f" />
      <path d="M 12,24 C 12,14 24,12 24,12 C 24,12 22,24 12,24 Z" fill="#ffffff" />
    </g>

    <!-- Row 3 (y=88) -->
    <!-- 38: Ruby -->
    <g transform="translate(0, 88)">
      <rect width="36" height="36" rx="8" fill="#cc342d" />
      <polygon points="12,12 24,12 27,17 18,27 9,17" fill="#ffffff" />
    </g>
    <!-- 39: Next.js -->
    <g transform="translate(48, 88)">
      <rect width="36" height="36" rx="8" fill="#000000" stroke="#334155" stroke-width="1" />
      <text x="11" y="25" font-family="sans-serif" font-size="16" font-weight="900" fill="#ffffff">N</text>
    </g>
    <!-- 40: Polygon -->
    <g transform="translate(96, 88)">
      <rect width="36" height="36" rx="8" fill="#8247e5" />
      <polygon points="18,10 26,15 26,23 18,28 10,23 10,15" fill="none" stroke="#ffffff" stroke-width="2" />
    </g>
    <!-- 41: Python -->
    <g transform="translate(144, 88)">
      <rect width="36" height="36" rx="8" fill="#3776ab" />
      <path d="M 18,8 C 12,8 13,11 13,11 L 13,13 L 19,13 L 19,14 L 11,14 C 11,14 8,13 8,19 C 8,24 10,24 10,24 L 12,24 L 12,21 C 12,21 12,17 15,17 L 21,17 C 21,17 24,17 24,14 L 24,9 C 24,9 24.5,8 18,8 Z" fill="#ffd43b" />
    </g>
    <!-- 42: Apple -->
    <g transform="translate(192, 88)">
      <rect width="36" height="36" rx="8" fill="#000000" stroke="#334155" stroke-width="1" />
      <circle cx="18" cy="20" r="7" fill="#ffffff" />
      <ellipse cx="18" cy="11" rx="2" ry="3" fill="#ffffff" transform="rotate(30 18 11)" />
    </g>
    <!-- 43: PWA -->
    <g transform="translate(240, 88)">
      <rect width="36" height="36" rx="8" fill="#5a0fc8" />
      <text x="5" y="23" font-family="sans-serif" font-size="9" font-weight="900" fill="#ffffff">PWA</text>
    </g>
    <!-- 44: Tailwind -->
    <g transform="translate(288, 88)">
      <rect width="36" height="36" rx="8" fill="#0f172a" />
      <path d="M 11,18 C 13,13 17,13 18,16 C 19,19 23,19 25,16" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-linecap="round" />
      <path d="M 14,24 C 16,19 20,19 21,22 C 22,25 26,25 28,22" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-linecap="round" />
    </g>
    <!-- 45: Redux -->
    <g transform="translate(336, 88)">
      <rect width="36" height="36" rx="8" fill="#764abc" />
      <circle cx="18" cy="18" r="6" fill="none" stroke="#ffffff" stroke-width="2" />
    </g>
    <!-- 46: VS Code -->
    <g transform="translate(384, 88)">
      <rect width="36" height="36" rx="8" fill="#007acc" />
      <path d="M 24,10 L 19,14 L 14,10 L 12,12 L 17,18 L 12,24 L 14,26 L 19,22 L 24,26 Z" fill="#ffffff" />
    </g>
    <!-- 47: GraphQL alt -->
    <g transform="translate(432, 88)">
      <rect width="36" height="36" rx="8" fill="#1f2937" />
      <circle cx="18" cy="18" r="7" fill="#ec4899" />
    </g>
    <!-- 48: Slack/Matrix -->
    <g transform="translate(480, 88)">
      <rect width="36" height="36" rx="8" fill="#4a154b" />
      <circle cx="14" cy="14" r="3" fill="#e01e5a" />
      <circle cx="22" cy="14" r="3" fill="#36c5f0" />
      <circle cx="14" cy="22" r="3" fill="#2eb67d" />
      <circle cx="22" cy="22" r="3" fill="#ecb22e" />
    </g>
    <!-- 49: Figma -->
    <g transform="translate(528, 88)">
      <rect width="36" height="36" rx="8" fill="#000000" />
      <circle cx="14" cy="14" r="3.5" fill="#f24e1e" />
      <circle cx="22" cy="14" r="3.5" fill="#ff7262" />
      <circle cx="14" cy="22" r="3.5" fill="#a259ff" />
      <circle cx="22" cy="22" r="3.5" fill="#1abcfe" />
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "02_starred_topics.svg"), "w") as f:
    f.write(starred_topics_svg)

print("Created 02_starred_topics.svg")
# =========================================================================
# 3. assets/03_telemetry_chart.svg
# The stock / telemetry financial-style activity line chart
# =========================================================================
telemetry_chart_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 260" width="100%" height="100%">
  <defs>
    <linearGradient id="chart-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c18" />
      <stop offset="100%" stop-color="#040710" />
    </linearGradient>

    <linearGradient id="glow-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#60a5fa" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>

    <filter id="line-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .axis-text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: #64748b; }
    .grid-line { stroke: #1e293b; stroke-width: 1; stroke-dasharray: 2 4; }
  </style>

  <!-- Container Box -->
  <rect width="940" height="260" rx="8" fill="url(#chart-bg)" stroke="#1e293b" stroke-width="1.2" />

  <!-- Y-Axis Values & Grid Lines -->
  <g transform="translate(45, 0)">
    <!-- 320 -->
    <text x="0" y="54" class="axis-text">320</text>
    <line x1="30" y1="50" x2="870" y2="50" class="grid-line" />

    <!-- 315 -->
    <text x="0" y="104" class="axis-text">315</text>
    <line x1="30" y1="100" x2="870" y2="100" class="grid-line" />

    <!-- 310 -->
    <text x="0" y="154" class="axis-text">310</text>
    <line x1="30" y1="150" x2="870" y2="150" class="grid-line" />

    <!-- 305 -->
    <text x="0" y="204" class="axis-text">305</text>
    <line x1="30" y1="200" x2="870" y2="200" class="grid-line" />
  </g>

  <!-- The Telemetry Line Graph -->
  <g transform="translate(75, 0)">
    <path d="M 0,178 
             L 30,179 
             L 60,178 
             L 90,175 
             L 120,176 
             L 150,182 
             L 180,184 
             L 210,196 
             L 230,206 
             L 240,46 
             L 250,95 
             L 260,138 
             L 270,128 
             L 280,152 
             L 290,132 
             L 300,118 
             L 320,126 
             L 340,110 
             L 360,122 
             L 380,112 
             L 400,116 
             L 420,118 
             L 440,112 
             L 460,116 
             L 480,114 
             L 500,118 
             L 520,110 
             L 540,122 
             L 560,114 
             L 580,116 
             L 600,108 
             L 630,110 
             L 660,106 
             L 690,108 
             L 720,104 
             L 750,106 
             L 780,102 
             L 810,104 
             L 840,102"
          fill="none" 
          stroke="url(#glow-line)" 
          stroke-width="2.5" 
          stroke-linecap="round" 
          stroke-linejoin="round" 
          filter="url(#line-glow)" />
  </g>

  <!-- X-Axis Timestamps (Angled Labels) -->
  <g class="axis-text" font-size="10" transform="translate(80, 235)">
    <text transform="translate(0, 0) rotate(-35)">8 AM</text>
    <text transform="translate(55, 0) rotate(-35)">9 AM</text>
    <text transform="translate(110, 0) rotate(-35)">10 AM</text>
    <text transform="translate(165, 0) rotate(-35)">11 AM</text>
    <text transform="translate(220, 0) rotate(-35)">12 PM</text>
    <text transform="translate(275, 0) rotate(-35)">1 PM</text>
    <text transform="translate(330, 0) rotate(-35)">2 PM</text>
    <text transform="translate(385, 0) rotate(-35)">3 PM</text>
    <text transform="translate(440, 0) rotate(-35)">4 PM</text>
    <text transform="translate(495, 0) rotate(-35)">5 PM</text>
    <text transform="translate(550, 0) rotate(-35)">6 PM</text>
    <text transform="translate(605, 0) rotate(-35)">7 PM</text>
    <text transform="translate(660, 0) rotate(-35)">8 PM</text>
    <text transform="translate(715, 0) rotate(-35)">9 PM</text>
    <text transform="translate(770, 0) rotate(-35)">10 PM</text>
    <text transform="translate(825, 0) rotate(-35)">11 PM</text>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "03_telemetry_chart.svg"), "w") as f:
    f.write(telemetry_chart_svg)

print("Created 03_telemetry_chart.svg")
# =========================================================================
# 4. assets/04_metrics_and_art.svg
# 3 Columns: Activity Radar + Floating Isometric Pixel Island + 3D Contribution Calendar
# =========================================================================
metrics_and_art_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 250" width="100%" height="100%">
  <defs>
    <linearGradient id="metric-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c18" />
      <stop offset="100%" stop-color="#040710" />
    </linearGradient>

    <filter id="green-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .radar-label { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 10px; fill: #94a3b8; text-anchor: middle; font-weight: 600; }
  </style>

  <!-- 1. Left Card: Activity Radar Chart -->
  <g transform="translate(0, 0)">
    <rect width="300" height="250" rx="8" fill="url(#metric-bg)" stroke="#1e293b" stroke-width="1.2" />

    <!-- Spider Chart Grid Axes -->
    <g transform="translate(150, 130)">
      <!-- Concentric guide polygons -->
      <polygon points="0,-75 75,0 0,75 -75,0" fill="none" stroke="#1e293b" stroke-width="1" />
      <polygon points="0,-50 50,0 0,50 -50,0" fill="none" stroke="#1e293b" stroke-width="1" />
      <polygon points="0,-25 25,0 0,25 -25,0" fill="none" stroke="#1e293b" stroke-width="1" />
      <!-- Axis lines -->
      <line x1="0" y1="-80" x2="0" y2="80" stroke="#334155" stroke-width="1" />
      <line x1="-80" y1="0" x2="80" y2="0" stroke="#334155" stroke-width="1" />

      <!-- The Green Polygon (Radar Metric) -->
      <!-- Top: Code Review 21% -> y=-38 -->
      <!-- Right: Issues 7% -> x=18 -->
      <!-- Bottom: Pull requests 25% -> y=45 -->
      <!-- Left: Commits 47% -> x=-72 -->
      <polygon points="0,-38 18,0 0,45 -72,0" fill="#22c55e" fill-opacity="0.45" stroke="#4ade80" stroke-width="2" filter="url(#green-glow)" />

      <!-- Nodes -->
      <circle cx="0" cy="-38" r="3" fill="#ffffff" />
      <circle cx="18" cy="0" r="3" fill="#ffffff" />
      <circle cx="0" cy="45" r="3" fill="#ffffff" />
      <circle cx="-72" cy="0" r="3" fill="#ffffff" />
    </g>

    <!-- Labels -->
    <text x="150" y="32" class="radar-label"><tspan font-weight="700" fill="#e2e8f0">21%</tspan><tspan dy="12" x="150">Code Review</tspan></text>
    <text x="252" y="128" class="radar-label"><tspan font-weight="700" fill="#e2e8f0">7%</tspan><tspan dy="12" x="252">Issues</tspan></text>
    <text x="150" y="222" class="radar-label"><tspan font-weight="700" fill="#e2e8f0">25%</tspan><tspan dy="12" x="150">Pull requests</tspan></text>
    <text x="45" y="128" class="radar-label"><tspan font-weight="700" fill="#e2e8f0">47%</tspan><tspan dy="12" x="45">Commits</tspan></text>
  </g>

  <!-- 2. Middle Card: Floating Isometric Pixel Island with Tree & Deer -->
  <g transform="translate(320, 0)">
    <rect width="300" height="250" rx="8" fill="url(#metric-bg)" stroke="#1e293b" stroke-width="1.2" />

    <!-- Isometric Island Group -->
    <g transform="translate(150, 150)">
      <!-- Roots dangling into void -->
      <path d="M -70,20 L -65,45 L -60,20" stroke="#78350f" stroke-width="2" fill="none" />
      <path d="M -30,35 L -26,60 L -22,35" stroke="#92400e" stroke-width="2.5" fill="none" />
      <path d="M 0,40 L 4,72 L 8,40" stroke="#78350f" stroke-width="3" fill="none" />
      <path d="M 35,35 L 38,55 L 42,35" stroke="#92400e" stroke-width="2" fill="none" />
      <path d="M 60,20 L 64,48 L 68,20" stroke="#78350f" stroke-width="2" fill="none" />

      <!-- Isometric Earth Block (Sides) -->
      <!-- Left face -->
      <polygon points="-80,0 0,42 0,65 -80,23" fill="#451a03" />
      <polygon points="-80,8 0,50 0,65 -80,23" fill="#3f1d0b" />
      <!-- Right face -->
      <polygon points="0,42 80,0 80,23 0,65" fill="#78350f" />
      <polygon points="0,50 80,8 80,23 0,65" fill="#5c2d12" />

      <!-- Isometric Grass Top Surface -->
      <polygon points="0,-42 80,0 0,42 -80,0" fill="#22c55e" />
      <polygon points="0,-42 75,-2 0,38 -75,-2" fill="#4ade80" />
      <!-- Pixel grass highlights -->
      <rect x="-30" y="-10" width="8" height="4" fill="#86efac" />
      <rect x="20" y="5" width="10" height="4" fill="#16a34a" />
      <rect x="-5" y="15" width="8" height="4" fill="#86efac" />

      <!-- The Tree on the Left Side of Island -->
      <g transform="translate(-35, -25)">
        <!-- Trunk -->
        <rect x="-5" y="-30" width="10" height="30" fill="#78350f" />
        <line x1="-5" y1="-15" x2="-14" y2="-25" stroke="#78350f" stroke-width="3" />
        <line x1="5" y1="-20" x2="12" y2="-28" stroke="#78350f" stroke-width="3" />
        <!-- Foliage (Pixel clusters) -->
        <ellipse cx="0" cy="-45" rx="32" ry="24" fill="#15803d" />
        <ellipse cx="-12" cy="-48" rx="24" ry="18" fill="#22c55e" />
        <ellipse cx="14" cy="-44" rx="22" ry="18" fill="#4ade80" />
        <ellipse cx="0" cy="-55" rx="20" ry="16" fill="#86efac" />
      </g>

      <!-- The Pixel Deer standing under the tree -->
      <g transform="translate(15, -15)">
        <!-- Body -->
        <ellipse cx="0" cy="-6" rx="14" ry="8" fill="#d97706" />
        <!-- Neck & Head -->
        <polygon points="-8,-8 -2,-20 6,-18 2,-6" fill="#b45309" />
        <ellipse cx="4" cy="-22" rx="5" ry="4" fill="#d97706" />
        <!-- Snout -->
        <polygon points="7,-23 11,-21 8,-19" fill="#fef3c7" />
        <!-- Antlers -->
        <path d="M 2,-25 L -2,-34 M -2,-30 L 4,-31 M 2,-25 L 6,-34 M 4,-29 L 8,-30" stroke="#78350f" stroke-width="1.8" stroke-linecap="round" />
        <!-- Legs -->
        <line x1="-8" y1="-2" x2="-10" y2="12" stroke="#b45309" stroke-width="2.5" />
        <line x1="-3" y1="-2" x2="-4" y2="12" stroke="#92400e" stroke-width="2.5" />
        <line x1="5" y1="-2" x2="6" y2="12" stroke="#b45309" stroke-width="2.5" />
        <line x1="10" y1="-2" x2="9" y2="12" stroke="#92400e" stroke-width="2.5" />
        <!-- Little Tail -->
        <ellipse cx="-13" cy="-10" rx="3" ry="2" fill="#fef3c7" />
      </g>

      <!-- Small Rocks on grass -->
      <ellipse cx="45" cy="5" rx="6" ry="3" fill="#64748b" />
      <ellipse cx="52" cy="7" rx="4" ry="2" fill="#94a3b8" />
    </g>
  </g>

  <!-- 3. Right Card: 3D Isometric Contribution Calendar -->
  <g transform="translate(640, 0)">
    <rect width="300" height="250" rx="8" fill="url(#metric-bg)" stroke="#1e293b" stroke-width="1.2" />

    <!-- Top Label -->
    <g transform="translate(18, 20)">
      <circle cx="4" cy="4" r="3" fill="#38bdf8" />
      <text x="14" y="8" class="font-sans" font-size="11" font-weight="600" fill="#94a3b8">Full year calendar</text>
    </g>

    <!-- Small Stats Telemetry -->
    <g class="font-sans" font-size="9.5" fill="#94a3b8" transform="translate(170, 48)">
      <text y="0"><tspan fill="#38bdf8">✔</tspan> Current streak: 8 days</text>
      <text y="14"><tspan fill="#38bdf8">✔</tspan> Longest streak: 232 days</text>
      <text y="28"><tspan fill="#38bdf8">✔</tspan> Highest in a day: 19</text>
      <text y="42"><tspan fill="#38bdf8">✔</tspan> Average per day: 2.1</text>
    </g>

    <!-- 3D Extruded Isometric Contribution Calendar Strip -->
    <g transform="translate(45, 95)">
      <!-- Long diagonal isometric strip receding into perspective -->
      <!-- Base grid path -->
      <polygon points="0,40 180,-30 220,-15 40,55" fill="#0f172a" stroke="#1e293b" stroke-width="1" />

      <!-- Columns of 3D cubes -->
      <!-- Cluster 1 (Left / Front) -->
      <g transform="translate(10, 32)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#4ade80" />
        <polygon points="0,0 8,4 8,14 0,10" fill="#22c55e" />
        <polygon points="8,4 16,0 16,10 8,14" fill="#15803d" />
      </g>
      <g transform="translate(18, 24)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#86efac" />
        <polygon points="0,0 8,4 8,24 0,20" fill="#4ade80" />
        <polygon points="8,4 16,0 16,20 8,24" fill="#16a34a" />
      </g>
      <g transform="translate(26, 16)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#22c55e" />
        <polygon points="0,0 8,4 8,10 0,6" fill="#16a34a" />
        <polygon points="8,4 16,0 16,6 8,10" fill="#15803d" />
      </g>
      <g transform="translate(34, 8)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#4ade80" />
        <polygon points="0,0 8,4 8,18 0,14" fill="#22c55e" />
        <polygon points="8,4 16,0 16,14 8,18" fill="#16a34a" />
      </g>

      <!-- Cluster 2 (Mid / Receding) -->
      <g transform="translate(50, -2)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#86efac" />
        <polygon points="0,0 8,4 8,26 0,22" fill="#4ade80" />
        <polygon points="8,4 16,0 16,22 8,26" fill="#16a34a" />
      </g>
      <g transform="translate(68, -12)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#22c55e" />
        <polygon points="0,0 8,4 8,12 0,8" fill="#16a34a" />
        <polygon points="8,4 16,0 16,8 8,12" fill="#15803d" />
      </g>
      <g transform="translate(86, -22)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#4ade80" />
        <polygon points="0,0 8,4 8,16 0,12" fill="#22c55e" />
        <polygon points="8,4 16,0 16,12 8,16" fill="#16a34a" />
      </g>
      <g transform="translate(104, -32)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#86efac" />
        <polygon points="0,0 8,4 8,20 0,16" fill="#4ade80" />
        <polygon points="8,4 16,0 16,16 8,20" fill="#16a34a" />
      </g>
      <g transform="translate(122, -42)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#22c55e" />
        <polygon points="0,0 8,4 8,10 0,6" fill="#16a34a" />
        <polygon points="8,4 16,0 16,6 8,10" fill="#15803d" />
      </g>

      <!-- Second Row of Cubes alongside -->
      <g transform="translate(30, 48)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#16a34a" />
        <polygon points="0,0 8,4 8,8 0,4" fill="#15803d" />
        <polygon points="8,4 16,0 16,4 8,8" fill="#14532d" />
      </g>
      <g transform="translate(70, 24)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#4ade80" />
        <polygon points="0,0 8,4 8,14 0,10" fill="#22c55e" />
        <polygon points="8,4 16,0 16,10 8,14" fill="#16a34a" />
      </g>
      <g transform="translate(140, -18)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#86efac" />
        <polygon points="0,0 8,4 8,16 0,12" fill="#4ade80" />
        <polygon points="8,4 16,0 16,12 8,16" fill="#16a34a" />
      </g>
      <g transform="translate(170, -32)">
        <polygon points="0,0 8,-4 16,0 8,4" fill="#22c55e" />
        <polygon points="0,0 8,4 8,8 0,4" fill="#16a34a" />
        <polygon points="8,4 16,0 16,4 8,8" fill="#15803d" />
      </g>
    </g>

    <!-- Bottom Label -->
    <g transform="translate(18, 225)">
      <circle cx="4" cy="4" r="3" fill="#64748b" />
      <text x="14" y="8" class="font-sans" font-size="11" fill="#64748b">Half year calendar</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "04_metrics_and_art.svg"), "w") as f:
    f.write(metrics_and_art_svg)

print("Created 04_metrics_and_art.svg")
print("New assets suite successfully compiled.")
