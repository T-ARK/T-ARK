import os

assets_dir = "/home/ark123/Documents/T-ARK/assets"
os.makedirs(assets_dir, exist_ok=True)

# -------------------------------------------------------------------------
# 1. assets/01_hero.svg
# -------------------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 390" width="100%" height="100%">
  <defs>
    <linearGradient id="hero-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070410" />
      <stop offset="50%" stop-color="#0c071d" />
      <stop offset="100%" stop-color="#05030c" />
    </linearGradient>

    <linearGradient id="purple-wave" x1="0%" y1="0%" x2="100%" y2="50%">
      <stop offset="0%" stop-color="#9333ea" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#c084fc" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.0" />
    </linearGradient>

    <linearGradient id="title-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="40%" stop-color="#f3e8ff" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <linearGradient id="pill-border-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9333ea" />
      <stop offset="50%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#9333ea" />
    </linearGradient>

    <filter id="purple-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SF Mono', Consolas, 'Fira Code', 'Courier New', monospace; }
  </style>

  <!-- Background Base -->
  <rect width="940" height="390" rx="16" fill="url(#hero-bg)" />

  <!-- Ambient Purple Cyber Waves (Top-Left & Sides) -->
  <path d="M -50,60 Q 150,20 280,120 T 600,80 Q 750,40 990,130 L 990,0 L -50,0 Z" fill="url(#purple-wave)" opacity="0.45" />
  <path d="M -30,120 Q 200,80 350,180 T 750,110 Q 880,90 990,190 L 990,0 L -30,0 Z" fill="url(#purple-wave)" opacity="0.25" />

  <!-- Abstract Hooded Hacker Silhouette Graphic (Right Side) -->
  <g transform="translate(620, 10)">
    <!-- Aura glow background -->
    <circle cx="160" cy="140" r="130" fill="#9333ea" opacity="0.18" filter="url(#purple-glow)" />

    <!-- Hood Outline / Body Silhouette -->
    <!-- Shoulders -->
    <path d="M 40,310 C 60,250 90,210 120,180 C 140,160 180,160 200,180 C 230,210 260,250 280,310 Z" fill="#0d081e" stroke="#7e22ce" stroke-width="2.5" opacity="0.95" />
    
    <!-- Hood Cape & Folds -->
    <path d="M 80,240 C 120,170 140,110 160,85 C 180,110 200,170 240,240 C 215,220 185,210 160,210 C 135,210 105,220 80,240 Z" fill="#130b2c" stroke="#a855f7" stroke-width="2" />
    
    <!-- Outer Hood Contour -->
    <path d="M 95,210 C 85,150 115,80 160,60 C 205,80 235,150 225,210 C 205,175 185,155 160,155 C 135,155 115,175 95,210 Z" fill="#170c36" stroke="#c084fc" stroke-width="2.5" filter="url(#soft-glow)" />

    <!-- Inner Hood Void (Pitch Black / Mystery) -->
    <path d="M 115,190 C 120,155 135,130 160,125 C 185,130 200,155 205,190 C 190,180 175,175 160,175 C 145,175 130,180 115,190 Z" fill="#070310" />

    <!-- Cyberpunk Glasses / Glowing Cyan-Violet Visor Line -->
    <path d="M 132,160 L 152,160 L 160,163 L 168,160 L 188,160" stroke="#c084fc" stroke-width="3" stroke-linecap="round" filter="url(#soft-glow)" />
    <circle cx="140" cy="160" r="1.5" fill="#38bdf8" />
    <circle cx="180" cy="160" r="1.5" fill="#38bdf8" />

    <!-- Neon Rim Lights on Garment -->
    <path d="M 60,310 C 80,270 105,240 120,230" stroke="#9333ea" stroke-width="2" fill="none" opacity="0.6" />
    <path d="M 260,310 C 240,270 215,240 200,230" stroke="#9333ea" stroke-width="2" fill="none" opacity="0.6" />
    <path d="M 125,240 L 145,310" stroke="#7e22ce" stroke-width="1.5" opacity="0.5" />
    <path d="M 195,240 L 175,310" stroke="#7e22ce" stroke-width="1.5" opacity="0.5" />
  </g>

  <!-- Left Content Area -->
  <g transform="translate(45, 45)">
    <!-- Top Sub-Header -->
    <text x="0" y="25" class="font-sans" font-size="16" font-weight="700" fill="#c084fc" letter-spacing="5">ARSHID CHANDRAN P K</text>

    <!-- Main Title: T-ARK_ -->
    <g transform="translate(0, 110)">
      <!-- Purple Drop Shadow / Glow -->
      <text x="0" y="0" class="font-sans" font-size="82" font-weight="900" font-style="italic" fill="#9333ea" opacity="0.8" filter="url(#purple-glow)" letter-spacing="2">T-ARK_</text>
      <!-- Crisp Foreground Gradient -->
      <text x="0" y="0" class="font-sans" font-size="82" font-weight="900" font-style="italic" fill="url(#title-grad)" letter-spacing="2">T-ARK_</text>
      
      <!-- Glitch Horizontal Slices -->
      <rect x="0" y="-48" width="220" height="3" fill="#070410" />
      <rect x="90" y="-22" width="180" height="2" fill="#070410" />
      <rect x="40" y="-47" width="130" height="1.5" fill="#c084fc" opacity="0.7" />
    </g>

    <!-- Slash Accent & Specializations -->
    <g transform="translate(0, 155)">
      <!-- Slash stripes /// -->
      <text x="0" y="0" class="font-mono" font-size="20" font-weight="900" fill="#a855f7" letter-spacing="1">///</text>
      <text x="38" y="-1" class="font-sans" font-size="15" font-weight="600" fill="#e9d5ff" letter-spacing="0.5">Data Science</text>
      <text x="142" y="-1" class="font-sans" font-size="15" fill="#7e22ce">|</text>
      <text x="156" y="-1" class="font-sans" font-size="15" font-weight="600" fill="#e9d5ff" letter-spacing="0.5">Web Development</text>
      <text x="303" y="-1" class="font-sans" font-size="15" fill="#7e22ce">|</text>
      <text x="317" y="-1" class="font-sans" font-size="15" font-weight="600" fill="#e9d5ff" letter-spacing="0.5">Cybersecurity Enthusiast</text>
    </g>

    <!-- Pill Banner: Highlights Bar -->
    <g transform="translate(0, 195)">
      <rect x="0" y="0" width="760" height="38" rx="19" fill="#0f0923" stroke="url(#pill-border-grad)" stroke-width="1.5" />
      <g class="font-sans" font-size="13" font-weight="600" fill="#f3e8ff">
        <text x="25" y="24">Data Science Student</text>
        <circle cx="185" cy="19" r="2.5" fill="#a855f7" />
        <text x="202" y="24">Backend Developer</text>
        <circle cx="347" cy="19" r="2.5" fill="#a855f7" />
        <text x="364" y="24">Building Scalable Applications</text>
        <circle cx="585" cy="19" r="2.5" fill="#a855f7" />
        <text x="602" y="24">Always Learning Something New</text>
      </g>
    </g>

    <!-- Action Buttons Row -->
    <g transform="translate(0, 260)">
      <!-- GitHub Button -->
      <g transform="translate(180, 0)">
        <rect x="0" y="0" width="105" height="36" rx="18" fill="#130c29" stroke="#7e22ce" stroke-width="1.2" />
        <path d="M 22,18 C 22,13.6 25.6,10 30,10 C 34.4,10 38,13.6 38,18 C 38,21.5 35.7,24.5 32.5,25.6 C 32.1,25.7 32,25.4 32,25.2 L 32,23.8 C 29.8,24.3 29.3,22.8 29.3,22.8 C 28.9,21.8 28.4,21.6 28.4,21.6 C 27.7,21.1 28.5,21.1 28.5,21.1 C 29.3,21.2 29.7,22 29.7,22 C 30.4,23.2 31.6,22.8 32,22.6 C 32.1,22.1 32.3,21.7 32.5,21.5 C 30.7,21.3 28.8,20.6 28.8,17.5 C 28.8,16.6 29.1,15.9 29.7,15.3 C 29.6,15.1 29.3,14.2 29.8,13.1 C 29.8,13.1 30.5,12.9 32,13.9 C 32.6,13.7 33.3,13.6 34,13.6 C 34.7,13.6 35.4,13.7 36,13.9 C 37.5,12.9 38.2,13.1 38.2,13.1 C 38.7,14.2 38.4,15.1 38.3,15.3 C 38.9,15.9 39.2,16.6 39.2,17.5 C 39.2,20.6 37.3,21.3 35.5,21.5 C 35.8,21.8 36,22.3 36,23 L 36,25.2 C 36,25.4 35.9,25.7 35.5,25.6 C 32.3,24.5 30,21.5 30,18" fill="#ffffff" transform="translate(-10, 0)" />
        <text x="44" y="23" class="font-sans" font-size="13" font-weight="600" fill="#ffffff">GitHub</text>
      </g>

      <!-- LinkedIn Button -->
      <g transform="translate(300, 0)">
        <rect x="0" y="0" width="112" height="36" rx="18" fill="#0077b5" stroke="#38bdf8" stroke-width="1.2" />
        <!-- in logo -->
        <rect x="14" y="10" width="16" height="16" rx="2" fill="#ffffff" />
        <text x="17" y="23" class="font-sans" font-size="12" font-weight="900" fill="#0077b5">in</text>
        <text x="38" y="23" class="font-sans" font-size="13" font-weight="600" fill="#ffffff">LinkedIn</text>
      </g>

      <!-- Portfolio Button -->
      <g transform="translate(427, 0)">
        <rect x="0" y="0" width="120" height="36" rx="18" fill="#130c29" stroke="#7e22ce" stroke-width="1.2" />
        <!-- Globe icon -->
        <circle cx="23" cy="18" r="8" fill="none" stroke="#38bdf8" stroke-width="1.5" />
        <ellipse cx="23" cy="18" rx="4" ry="8" fill="none" stroke="#a855f7" stroke-width="1.2" />
        <line x1="15" y1="18" x2="31" y2="18" stroke="#38bdf8" stroke-width="1.2" />
        <text x="40" y="23" class="font-sans" font-size="13" font-weight="600" fill="#ffffff">Portfolio</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "01_hero.svg"), "w") as f:
    f.write(hero_svg)

print("Created 01_hero.svg")
# -------------------------------------------------------------------------
# 2. assets/02_who_i_am_and_tech_stack.svg
# -------------------------------------------------------------------------
about_stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 530" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0822" />
      <stop offset="100%" stop-color="#090516" />
    </linearGradient>

    <linearGradient id="purple-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#3b1f66" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.7" />
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
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SF Mono', Consolas, 'Fira Code', 'Courier New', monospace; font-size: 11px; }
    .kw { fill: #c084fc; font-weight: 700; }
    .fn { fill: #60a5fa; }
    .str { fill: #86efac; }
    .prop { fill: #f3e8ff; }
    .val { fill: #fde047; }
    .cmt { fill: #94a3b8; font-style: italic; }
  </style>

  <!-- Left: // WHO I AM Header -->
  <text x="5" y="24" class="font-sans" font-size="16" font-weight="800" fill="#c084fc" letter-spacing="1.5">// WHO I AM</text>

  <!-- Left Side: Terminal Code Box -->
  <g transform="translate(0, 38)">
    <!-- Box frame -->
    <rect width="445" height="480" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />

    <!-- macOS Window Header Bar -->
    <rect width="445" height="32" rx="12" fill="#140c2e" />
    <circle cx="20" cy="16" r="5" fill="#ef4444" />
    <circle cx="36" cy="16" r="5" fill="#f59e0b" />
    <circle cx="52" cy="16" r="5" fill="#10b981" />
    <text x="222" y="20" class="font-sans" font-size="11" fill="#a78bfa" text-anchor="middle" font-weight="600">developer.py</text>

    <!-- Code Content -->
    <g class="font-mono" transform="translate(16, 52)">
      <text y="0"><tspan class="kw">class</tspan> <tspan class="val">Developer</tspan>:</text>
      <text y="16">    <tspan class="kw">def</tspan> <tspan class="fn">__init__</tspan>(<tspan class="kw">self</tspan>):</text>
      <text y="32">        <tspan class="prop">self.name</tspan> = <tspan class="str">"Arshid Chandran P K"</tspan></text>
      <text y="48">        <tspan class="prop">self.location</tspan> = <tspan class="str">"Kerala, India 🇮🇳"</tspan></text>
      <text y="64">        <tspan class="prop">self.degree</tspan> = <tspan class="str">"B.Tech - Computer Science</tspan></text>
      <text y="80">                       <tspan class="str">Engineering (Data Science)"</tspan></text>
      <text y="96">        <tspan class="prop">self.role</tspan> = <tspan class="str">"Aspiring Data Scientist &amp; Dev"</tspan></text>
      <text y="116">        <tspan class="prop">self.stack</tspan> = {</text>
      <text y="132">            <tspan class="str">"languages"</tspan>: [<tspan class="val">"Python"</tspan>, <tspan class="val">"C"</tspan>, <tspan class="val">"C++"</tspan>, <tspan class="val">"JS"</tspan>],</text>
      <text y="148">            <tspan class="str">"web"</tspan>: [<tspan class="val">"HTML5"</tspan>, <tspan class="val">"CSS3"</tspan>, <tspan class="val">"Responsive"</tspan>],</text>
      <text y="164">            <tspan class="str">"data_science"</tspan>: [<tspan class="val">"NumPy"</tspan>, <tspan class="val">"Pandas"</tspan>, <tspan class="val">"Scikit"</tspan>]</text>
      <text y="180">        }</text>
      <text y="200">        <tspan class="prop">self.currently_learning</tspan> = [</text>
      <text y="216">            <tspan class="str">"Machine Learning"</tspan>, <tspan class="str">"Cybersecurity"</tspan>,</text>
      <text y="232">            <tspan class="str">"Advanced Data Visualization"</tspan></text>
      <text y="248">        ]</text>
      <text y="268">        <tspan class="prop">self.interests</tspan> = [<tspan class="val">"Data Science"</tspan>, <tspan class="val">"AI"</tspan>,</text>
      <text y="284">            <tspan class="val">"Cybersecurity"</tspan>, <tspan class="val">"Photography"</tspan>, <tspan class="val">"Design"</tspan>]</text>
      <text y="304">        <tspan class="prop">self.languages_spoken</tspan> = [</text>
      <text y="320">            <tspan class="str">"English"</tspan>, <tspan class="str">"Malayalam"</tspan>, <tspan class="str">"Hindi"</tspan>, <tspan class="str">"Tamil"</tspan>]</text>
      <text y="340">        <tspan class="prop">self.fun_fact</tspan> = <tspan class="str">"I love debugging &amp; cameras 📷"</tspan></text>
      <text y="366">    <tspan class="kw">def</tspan> <tspan class="fn">motto</tspan>(<tspan class="kw">self</tspan>):</text>
      <text y="382">        <tspan class="kw">return</tspan> <tspan class="val">"Stay curious. Keep building."</tspan></text>
    </g>
  </g>

  <!-- Middle Column: 4 Mini-Cards + Quote -->
  <g transform="translate(460, 38)">
    <!-- Mini Card 1: Location -->
    <g transform="translate(0, 0)">
      <rect width="185" height="52" rx="10" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <g transform="translate(14, 15)">
        <!-- Pin icon -->
        <path d="M 10,2 C 5.5,2 2,5.5 2,10 C 2,15 10,22 10,22 C 10,22 18,15 18,10 C 18,5.5 14.5,2 10,2 Z" fill="none" stroke="#a855f7" stroke-width="1.8" />
        <circle cx="10" cy="10" r="3" fill="#c084fc" />
      </g>
      <text x="46" y="31" class="font-sans" font-size="12" font-weight="600" fill="#f3e8ff">Kerala, India 🇮🇳</text>
    </g>

    <!-- Mini Card 2: Degree -->
    <g transform="translate(0, 64)">
      <rect width="185" height="64" rx="10" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <g transform="translate(14, 18)">
        <!-- Graduation Cap icon -->
        <path d="M 2,9 L 12,3 L 22,9 L 12,15 Z" fill="#a855f7" />
        <path d="M 6,11.5 L 6,17 C 6,19 8.5,21 12,21 C 15.5,21 18,19 18,17 L 18,11.5" fill="none" stroke="#c084fc" stroke-width="1.6" />
        <line x1="22" y1="9" x2="22" y2="17" stroke="#a855f7" stroke-width="1.6" />
      </g>
      <text x="46" y="28" class="font-sans" font-size="11.5" font-weight="700" fill="#f3e8ff">B.Tech – CSE</text>
      <text x="46" y="44" class="font-sans" font-size="10.5" fill="#a78bfa">(Data Science)</text>
    </g>

    <!-- Mini Card 3: Role -->
    <g transform="translate(0, 140)">
      <rect width="185" height="52" rx="10" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <g transform="translate(14, 15)">
        <!-- Code tag icon </> -->
        <text x="0" y="16" class="font-mono" font-size="15" font-weight="900" fill="#a855f7">&lt;/&gt;</text>
      </g>
      <text x="46" y="31" class="font-sans" font-size="11.5" font-weight="600" fill="#f3e8ff">Aspiring Developer</text>
    </g>

    <!-- Mini Card 4: Interests -->
    <g transform="translate(0, 204)">
      <rect width="185" height="74" rx="10" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <g transform="translate(14, 18)">
        <!-- Heart icon -->
        <path d="M 10,18 L 8.5,16.5 C 3.5,12 0,8.8 0,5 C 0,2.2 2.2,0 5,0 C 6.6,0 8.1,0.7 9,1.9 C 9.9,0.7 11.4,0 13,0 C 15.8,0 18,2.2 18,5 C 18,8.8 14.5,12 9.5,16.5 L 10,18 Z" fill="none" stroke="#a855f7" stroke-width="1.6" transform="translate(1, 2)" />
      </g>
      <text x="44" y="26" class="font-sans" font-size="11" font-weight="600" fill="#f3e8ff">Data Science,</text>
      <text x="44" y="42" class="font-sans" font-size="11" fill="#a78bfa">Cybersecurity,</text>
      <text x="44" y="58" class="font-sans" font-size="11" fill="#a78bfa">Photography</text>
    </g>

    <!-- Cursive Calligraphic Quote -->
    <g transform="translate(10, 335)">
      <text x="0" y="0" font-family="'Brush Script MT', 'Segoe Script', 'Great Vibes', cursive, sans-serif" font-size="34" font-style="italic" fill="#c084fc" filter="url(#soft-glow)">"Build. Learn.</text>
      <text x="25" y="42" font-family="'Brush Script MT', 'Segoe Script', 'Great Vibes', cursive, sans-serif" font-size="34" font-style="italic" fill="#a855f7" filter="url(#soft-glow)">Improve."</text>
    </g>
  </g>

  <!-- Right Side: // TECH STACK -->
  <g transform="translate(660, 0)">
    <text x="5" y="24" class="font-sans" font-size="16" font-weight="800" fill="#c084fc" letter-spacing="1.5">// TECH STACK</text>

    <!-- Stack Card Container -->
    <g transform="translate(0, 38)">
      <rect width="275" height="480" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />

      <!-- Group 1: Languages -->
      <g transform="translate(18, 20)">
        <text x="0" y="0" class="font-sans" font-size="13" font-weight="700" fill="#e9d5ff">Languages</text>
        <g transform="translate(0, 12)">
          <!-- Python -->
          <g transform="translate(0, 0)">
            <rect width="36" height="36" rx="8" fill="#150d30" />
            <path d="M 18,6 C 12,6 12.5,8.5 12.5,8.5 L 12.5,11 L 18.5,11 L 18.5,12 L 10,12 C 10,12 7,11.5 7,17.5 C 7,23.5 9.5,23.5 9.5,23.5 L 11.5,23.5 L 11.5,20.5 C 11.5,20.5 11.5,17 15,17 L 21,17 C 21,17 24,17 24,14 L 24,9 C 24,9 24.5,6 18,6 Z" fill="#38bdf8" />
            <path d="M 18,30 C 24,30 23.5,27.5 23.5,27.5 L 23.5,25 L 17.5,25 L 17.5,24 L 26,24 C 26,24 29,24.5 29,18.5 C 29,12.5 26.5,12.5 26.5,12.5 L 24.5,12.5 L 24.5,15.5 C 24.5,15.5 24.5,19 21,19 L 15,19 C 15,19 12,19 12,22 L 12,27 C 12,27 11.5,30 18,30 Z" fill="#fbbf24" />
            <circle cx="15" cy="8.5" r="1.2" fill="#ffffff" />
            <circle cx="21" cy="27.5" r="1.2" fill="#ffffff" />
          </g>
          <!-- C -->
          <g transform="translate(42, 0)">
            <rect width="36" height="36" rx="8" fill="#150d30" />
            <circle cx="18" cy="18" r="13" fill="#1e40af" />
            <path d="M 23,12 C 21,10 16,10 14,13 C 12,16 12,20 14,23 C 16,26 21,26 23,24" fill="none" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" />
          </g>
          <!-- C++ -->
          <g transform="translate(84, 0)">
            <rect width="36" height="36" rx="8" fill="#150d30" />
            <circle cx="18" cy="18" r="13" fill="#2563eb" />
            <path d="M 16,13 C 14,11 11,11 10,13 C 9,15 9,18 10,20 C 11,22 14,22 16,20" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" />
            <text x="17" y="18" font-family="sans-serif" font-size="9" font-weight="900" fill="#ffffff">+</text>
            <text x="23" y="18" font-family="sans-serif" font-size="9" font-weight="900" fill="#ffffff">+</text>
          </g>
          <!-- JS -->
          <g transform="translate(126, 0)">
            <rect width="36" height="36" rx="8" fill="#eab308" />
            <text x="12" y="27" font-family="sans-serif" font-size="16" font-weight="900" fill="#000000">JS</text>
          </g>
          <!-- HTML5 -->
          <g transform="translate(168, 0)">
            <rect width="36" height="36" rx="8" fill="#ea580c" />
            <text x="10" y="26" font-family="sans-serif" font-size="16" font-weight="900" fill="#ffffff">5</text>
          </g>
          <!-- CSS3 -->
          <g transform="translate(210, 0)">
            <rect width="36" height="36" rx="8" fill="#0284c7" />
            <text x="10" y="26" font-family="sans-serif" font-size="16" font-weight="900" fill="#ffffff">3</text>
          </g>
        </g>
      </g>

      <!-- Group 2: Backend -->
      <g transform="translate(18, 120)">
        <text x="0" y="0" class="font-sans" font-size="13" font-weight="700" fill="#e9d5ff">Backend</text>
        <g transform="translate(0, 12)">
          <!-- Flask -->
          <g transform="translate(10, 0)">
            <rect width="45" height="45" rx="10" fill="#150d30" />
            <!-- Flask beaker -->
            <path d="M 19,10 L 26,10 L 26,16 L 33,28 C 34.5,30.5 32.5,33 29.5,33 L 15.5,33 C 12.5,33 10.5,30.5 12,28 L 19,16 Z" fill="none" stroke="#ffffff" stroke-width="2" />
            <circle cx="21" cy="27" r="2" fill="#c084fc" />
            <circle cx="25" cy="24" r="1.5" fill="#c084fc" />
          </g>
          <!-- MySQL -->
          <g transform="translate(85, 0)">
            <rect width="55" height="45" rx="10" fill="#150d30" />
            <text x="10" y="27" class="font-sans" font-size="11" font-weight="900" fill="#00758f">MySQL</text>
            <path d="M 14,14 C 20,8 35,8 42,16" stroke="#f29111" stroke-width="2" fill="none" />
          </g>
          <!-- PostgreSQL -->
          <g transform="translate(165, 0)">
            <rect width="45" height="45" rx="10" fill="#150d30" />
            <!-- Elephant head outline -->
            <path d="M 22,12 C 16,12 14,16 14,20 C 14,25 18,26 18,31 L 22,31 C 22,27 21,25 21,23 C 24,23 27,22 28,19 C 29,15 27,12 22,12 Z" fill="#336791" />
            <circle cx="20" cy="17" r="1.5" fill="#ffffff" />
          </g>
        </g>
      </g>

      <!-- Group 3: Tools -->
      <g transform="translate(18, 230)">
        <text x="0" y="0" class="font-sans" font-size="13" font-weight="700" fill="#e9d5ff">Tools</text>
        <g transform="translate(0, 12)">
          <!-- Git -->
          <g transform="translate(5, 0)">
            <rect width="42" height="42" rx="10" fill="#150d30" />
            <rect x="11" y="11" width="20" height="20" rx="3" transform="rotate(45 21 21)" fill="#f05032" />
            <circle cx="17" cy="21" r="2.5" fill="#ffffff" />
            <circle cx="25" cy="17" r="2.5" fill="#ffffff" />
            <line x1="17" y1="21" x2="25" y2="17" stroke="#ffffff" stroke-width="1.8" />
          </g>
          <!-- GitHub -->
          <g transform="translate(65, 0)">
            <rect width="42" height="42" rx="10" fill="#150d30" />
            <circle cx="21" cy="21" r="14" fill="#ffffff" />
            <circle cx="21" cy="21" r="11" fill="#000000" />
            <path d="M 15,22 C 15,28 27,28 27,22 Z" fill="#ffffff" />
          </g>
          <!-- VS Code -->
          <g transform="translate(125, 0)">
            <rect width="42" height="42" rx="10" fill="#150d30" />
            <path d="M 28,10 L 21,15 L 15,11 L 12,13 L 18,19 L 12,25 L 15,27 L 21,23 L 28,28 Z" fill="#007acc" />
          </g>
          <!-- Figma -->
          <g transform="translate(185, 0)">
            <rect width="42" height="42" rx="10" fill="#150d30" />
            <circle cx="16" cy="15" r="4.5" fill="#f24e1e" />
            <circle cx="25" cy="15" r="4.5" fill="#ff7262" />
            <circle cx="16" cy="23" r="4.5" fill="#a259ff" />
            <circle cx="25" cy="23" r="4.5" fill="#1abcfe" />
            <circle cx="16" cy="30" r="4.5" fill="#0acf83" />
          </g>
        </g>
      </g>

      <!-- Group 4: Data Science -->
      <g transform="translate(18, 345)">
        <text x="0" y="0" class="font-sans" font-size="13" font-weight="700" fill="#e9d5ff">Data Science</text>
        <g transform="translate(0, 12)">
          <!-- Python -->
          <g transform="translate(5, 0)">
            <rect width="45" height="50" rx="8" fill="#150d30" />
            <circle cx="22" cy="20" r="11" fill="#38bdf8" />
            <text x="8" y="42" class="font-sans" font-size="9" font-weight="700" fill="#a78bfa">Python</text>
          </g>
          <!-- NumPy -->
          <g transform="translate(65, 0)">
            <rect width="45" height="50" rx="8" fill="#150d30" />
            <circle cx="22" cy="20" r="11" fill="#4d77cf" />
            <text x="22" y="24" font-family="sans-serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">NP</text>
            <text x="7" y="42" class="font-sans" font-size="9" font-weight="700" fill="#a78bfa">NumPy</text>
          </g>
          <!-- Pandas -->
          <g transform="translate(125, 0)">
            <rect width="45" height="50" rx="8" fill="#150d30" />
            <!-- Bar chart lines -->
            <line x1="16" y1="26" x2="16" y2="14" stroke="#ff4154" stroke-width="3" stroke-linecap="round" />
            <line x1="22" y1="26" x2="22" y2="10" stroke="#130754" stroke-width="3" stroke-linecap="round" />
            <line x1="28" y1="26" x2="28" y2="18" stroke="#ff4154" stroke-width="3" stroke-linecap="round" />
            <text x="7" y="42" class="font-sans" font-size="9" font-weight="700" fill="#a78bfa">Pandas</text>
          </g>
          <!-- Scikit-learn -->
          <g transform="translate(185, 0)">
            <rect width="45" height="50" rx="8" fill="#150d30" />
            <circle cx="22" cy="20" r="11" fill="#f89939" />
            <text x="22" y="24" font-family="sans-serif" font-size="9" font-weight="900" fill="#ffffff" text-anchor="middle">SK</text>
            <text x="5" y="42" class="font-sans" font-size="8" font-weight="700" fill="#a78bfa">Scikit-learn</text>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "02_who_i_am_and_tech_stack.svg"), "w") as f:
    f.write(about_stack_svg)

print("Created 02_who_i_am_and_tech_stack.svg")
# -------------------------------------------------------------------------
# 3. assets/03_github_analytics.svg
# -------------------------------------------------------------------------
analytics_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 375" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0822" />
      <stop offset="100%" stop-color="#090516" />
    </linearGradient>

    <linearGradient id="purple-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#3b1f66" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.7" />
    </linearGradient>

    <linearGradient id="line-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6" />
      <stop offset="50%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#a855f7" />
    </linearGradient>

    <linearGradient id="area-glow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.0" />
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
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'SF Mono', Consolas, 'Fira Code', 'Courier New', monospace; }
  </style>

  <!-- Header -->
  <text x="5" y="24" class="font-sans" font-size="16" font-weight="800" fill="#c084fc" letter-spacing="1.5">// GITHUB ANALYTICS</text>

  <!-- Top 3 Cards Row -->
  <g transform="translate(0, 38)">
    <!-- Card 1: GitHub Stats -->
    <g transform="translate(0, 0)">
      <rect width="295" height="150" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <!-- Header icon + Title -->
      <g transform="translate(16, 18)">
        <path d="M 0,12 L 4,12 L 4,4 L 0,4 Z M 6,12 L 10,12 L 10,0 L 6,0 Z M 12,12 L 16,12 L 12,6 L 12,6 Z" fill="#a855f7" />
        <text x="22" y="11" class="font-sans" font-size="13" font-weight="700" fill="#f3e8ff">GitHub Stats</text>
      </g>

      <!-- Stats List -->
      <g class="font-sans" transform="translate(18, 55)">
        <text y="0" font-size="12" fill="#a78bfa">Repositories</text>
        <text x="120" y="0" font-size="14" font-weight="800" fill="#f3e8ff">12+</text>

        <text y="28" font-size="12" fill="#a78bfa">Contributions</text>
        <text x="120" y="28" font-size="14" font-weight="800" fill="#f3e8ff">100+</text>

        <text y="56" font-size="12" fill="#a78bfa">Followers</text>
        <text x="120" y="56" font-size="14" font-weight="800" fill="#f3e8ff">0+</text>
      </g>

      <!-- Purple Glowing Octocat Watermark -->
      <g transform="translate(205, 50)" opacity="0.85">
        <circle cx="35" cy="35" r="32" fill="#1b0e38" stroke="#8b5cf6" stroke-width="1.5" filter="url(#soft-glow)" />
        <path d="M 23,45 C 23,38 27,33 35,33 C 43,33 47,38 47,45 C 47,52 42,56 35,56 C 28,56 23,52 23,45" fill="#c084fc" />
        <circle cx="31" cy="40" r="2.5" fill="#0e0822" />
        <circle cx="39" cy="40" r="2.5" fill="#0e0822" />
        <!-- Ears -->
        <polygon points="26,35 24,27 30,31" fill="#c084fc" />
        <polygon points="44,35 46,27 40,31" fill="#c084fc" />
      </g>
    </g>

    <!-- Card 2: Most Used Languages -->
    <g transform="translate(322, 0)">
      <rect width="295" height="150" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <g transform="translate(16, 18)">
        <circle cx="7" cy="7" r="6" fill="none" stroke="#a855f7" stroke-width="2" />
        <text x="22" y="11" class="font-sans" font-size="13" font-weight="700" fill="#f3e8ff">Most Used Languages</text>
      </g>

      <!-- Donut Chart -->
      <g transform="translate(75, 90)">
        <!-- Donut slices (r=32, circumference=201) -->
        <!-- Background circle -->
        <circle cx="0" cy="0" r="30" fill="none" stroke="#1f143d" stroke-width="12" />
        <!-- Python: 58.7% -> dasharray 118 83, dashoffset 0 -->
        <circle cx="0" cy="0" r="30" fill="none" stroke="#38bdf8" stroke-width="12" stroke-dasharray="118 83" stroke-dashoffset="0" transform="rotate(-90)" />
        <!-- C++: 17.3% -> dasharray 35 166, dashoffset -118 -->
        <circle cx="0" cy="0" r="30" fill="none" stroke="#f43f5e" stroke-width="12" stroke-dasharray="35 166" stroke-dashoffset="-118" transform="rotate(-90)" />
        <!-- JavaScript: 12.0% -> dasharray 24 177, dashoffset -153 -->
        <circle cx="0" cy="0" r="30" fill="none" stroke="#facc15" stroke-width="12" stroke-dasharray="24 177" stroke-dashoffset="-153" transform="rotate(-90)" />
        <!-- Others: 11.0% -> dasharray 22 179, dashoffset -177 -->
        <circle cx="0" cy="0" r="30" fill="none" stroke="#94a3b8" stroke-width="12" stroke-dasharray="22 179" stroke-dashoffset="-177" transform="rotate(-90)" />
      </g>

      <!-- Legend -->
      <g class="font-sans" font-size="11" transform="translate(150, 52)">
        <circle cx="5" cy="5" r="4" fill="#38bdf8" />
        <text x="16" y="9" fill="#f3e8ff">Python</text>
        <text x="90" y="9" font-weight="700" fill="#a78bfa">58.7%</text>

        <circle cx="5" cy="27" r="4" fill="#f43f5e" />
        <text x="16" y="31" fill="#f3e8ff">C++</text>
        <text x="90" y="31" font-weight="700" fill="#a78bfa">17.3%</text>

        <circle cx="5" cy="49" r="4" fill="#facc15" />
        <text x="16" y="53" fill="#f3e8ff">JavaScript</text>
        <text x="90" y="53" font-weight="700" fill="#a78bfa">12.0%</text>

        <circle cx="5" cy="71" r="4" fill="#94a3b8" />
        <text x="16" y="75" fill="#f3e8ff">Others</text>
        <text x="90" y="75" font-weight="700" fill="#a78bfa">11.0%</text>
      </g>
    </g>

    <!-- Card 3: Streak Stats -->
    <g transform="translate(645, 0)">
      <rect width="295" height="150" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <g transform="translate(16, 18)">
        <!-- Flame icon -->
        <path d="M 6,0 C 7,4 10,6 10,9 C 10,12 7.5,14 5,14 C 2.5,14 0,12 0,9 C 0,7 2,5 4,2 Z" fill="#ec4899" transform="translate(0, 0)" />
        <text x="20" y="11" class="font-sans" font-size="13" font-weight="700" fill="#f3e8ff">Streak Stats</text>
      </g>

      <!-- Big Number -->
      <g transform="translate(20, 52)">
        <text x="0" y="38" class="font-sans" font-size="38" font-weight="900" fill="#ffffff" filter="url(#soft-glow)">232</text>
        <text x="2" y="60" class="font-sans" font-size="12" font-weight="600" fill="#a78bfa">Day Streak</text>
      </g>

      <!-- Contribution Heat Squares Matrix (Right side) -->
      <g transform="translate(115, 48)">
        <!-- Grid of 11 cols x 6 rows of purple shades -->
        <!-- Col 0 -->
        <rect x="0" y="0" width="8" height="8" rx="2" fill="#2d1254" />
        <rect x="0" y="11" width="8" height="8" rx="2" fill="#581c87" />
        <rect x="0" y="22" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="0" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="0" y="44" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="0" y="55" width="8" height="8" rx="2" fill="#7e22ce" />

        <!-- Col 1 -->
        <rect x="11" y="0" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="11" y="11" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="11" y="22" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="11" y="33" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="11" y="44" width="8" height="8" rx="2" fill="#581c87" />
        <rect x="11" y="55" width="8" height="8" rx="2" fill="#a855f7" />

        <!-- Col 2 -->
        <rect x="22" y="0" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="22" y="11" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="22" y="22" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="22" y="33" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="22" y="44" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="22" y="55" width="8" height="8" rx="2" fill="#c084fc" />

        <!-- Col 3 -->
        <rect x="33" y="0" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="33" y="11" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="33" y="22" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="33" y="33" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="33" y="44" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="33" y="55" width="8" height="8" rx="2" fill="#581c87" />

        <!-- Col 4 -->
        <rect x="44" y="0" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="44" y="11" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="44" y="22" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="44" y="33" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="44" y="44" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="44" y="55" width="8" height="8" rx="2" fill="#a855f7" />

        <!-- Col 5 -->
        <rect x="55" y="0" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="55" y="11" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="55" y="22" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="55" y="33" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="55" y="44" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="55" y="55" width="8" height="8" rx="2" fill="#7e22ce" />

        <!-- Col 6 -->
        <rect x="66" y="0" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="66" y="11" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="66" y="22" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="66" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="66" y="44" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="66" y="55" width="8" height="8" rx="2" fill="#c084fc" />

        <!-- Col 7 -->
        <rect x="77" y="0" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="77" y="11" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="77" y="22" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="77" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="77" y="44" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="77" y="55" width="8" height="8" rx="2" fill="#a855f7" />

        <!-- Col 8 -->
        <rect x="88" y="0" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="88" y="11" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="88" y="22" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="88" y="33" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="88" y="44" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="88" y="55" width="8" height="8" rx="2" fill="#7e22ce" />

        <!-- Col 9 -->
        <rect x="99" y="0" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="99" y="11" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="99" y="22" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="99" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="99" y="44" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="99" y="55" width="8" height="8" rx="2" fill="#c084fc" />

        <!-- Col 10 -->
        <rect x="110" y="0" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="110" y="11" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="110" y="22" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="110" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="110" y="44" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="110" y="55" width="8" height="8" rx="2" fill="#a855f7" />

        <!-- Col 11 -->
        <rect x="121" y="0" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="121" y="11" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="121" y="22" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="121" y="33" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="121" y="44" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="121" y="55" width="8" height="8" rx="2" fill="#c084fc" />

        <!-- Col 12 -->
        <rect x="132" y="0" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="132" y="11" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="132" y="22" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="132" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="132" y="44" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="132" y="55" width="8" height="8" rx="2" fill="#a855f7" />

        <!-- Col 13 -->
        <rect x="143" y="0" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="143" y="11" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="143" y="22" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="143" y="33" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="143" y="44" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="143" y="55" width="8" height="8" rx="2" fill="#7e22ce" />

        <!-- Col 14 -->
        <rect x="154" y="0" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="154" y="11" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="154" y="22" width="8" height="8" rx="2" fill="#c084fc" />
        <rect x="154" y="33" width="8" height="8" rx="2" fill="#a855f7" />
        <rect x="154" y="44" width="8" height="8" rx="2" fill="#7e22ce" />
        <rect x="154" y="55" width="8" height="8" rx="2" fill="#c084fc" />
      </g>
    </g>
  </g>

  <!-- Bottom Wide Card: Contribution Activity -->
  <g transform="translate(0, 205)">
    <rect width="940" height="155" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
    <g transform="translate(20, 20)">
      <!-- Activity pulse icon -->
      <path d="M 0,8 L 4,8 L 7,2 L 11,14 L 14,8 L 18,8" fill="none" stroke="#a855f7" stroke-width="2" />
      <text x="26" y="11" class="font-sans" font-size="13" font-weight="700" fill="#f3e8ff">Contribution Activity</text>
    </g>

    <!-- Graph Visualization -->
    <g transform="translate(45, 60)">
      <!-- Baseline Axis -->
      <line x1="0" y1="50" x2="850" y2="50" stroke="#372061" stroke-width="1" />

      <!-- Area fill path -->
      <path d="M 0,50 L 0,42 Q 40,46 80,35 T 160,42 T 240,25 T 320,38 T 400,20 T 480,35 T 560,15 T 640,30 T 720,25 T 800,10 L 850,22 L 850,50 Z" fill="url(#area-glow)" />

      <!-- Curved Spline Line -->
      <path d="M 0,42 Q 40,46 80,35 T 160,42 T 240,25 T 320,38 T 400,20 T 480,35 T 560,15 T 640,30 T 720,25 T 800,10 L 850,22" fill="none" stroke="url(#line-glow)" stroke-width="2.8" filter="url(#soft-glow)" />

      <!-- Glowing Node Dots -->
      <circle cx="0" cy="42" r="3.5" fill="#c084fc" />
      <circle cx="80" cy="35" r="3.5" fill="#c084fc" />
      <circle cx="160" cy="42" r="3.5" fill="#c084fc" />
      <circle cx="240" cy="25" r="3.5" fill="#c084fc" />
      <circle cx="320" cy="38" r="3.5" fill="#c084fc" />
      <circle cx="400" cy="20" r="3.5" fill="#c084fc" />
      <circle cx="480" cy="35" r="3.5" fill="#c084fc" />
      <circle cx="560" cy="15" r="3.5" fill="#c084fc" />
      <circle cx="640" cy="30" r="3.5" fill="#c084fc" />
      <circle cx="720" cy="25" r="3.5" fill="#c084fc" />
      <circle cx="800" cy="10" r="4.5" fill="#ffffff" stroke="#a855f7" stroke-width="2" />
      <circle cx="850" cy="22" r="3.5" fill="#c084fc" />

      <!-- Month Labels -->
      <g class="font-sans" font-size="11" fill="#a78bfa" transform="translate(0, 68)">
        <text x="-5" y="0">Nov</text>
        <text x="75" y="0">Dec</text>
        <text x="155" y="0">Jan</text>
        <text x="235" y="0">Feb</text>
        <text x="315" y="0">Mar</text>
        <text x="395" y="0">May</text>
        <text x="475" y="0">Jun</text>
        <text x="555" y="0">Jul</text>
        <text x="635" y="0">Aug</text>
        <text x="715" y="0">Sep</text>
        <text x="795" y="0">Oct</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "03_github_analytics.svg"), "w") as f:
    f.write(analytics_svg)

print("Created 03_github_analytics.svg")
# -------------------------------------------------------------------------
# 4. assets/04_experience.svg
# -------------------------------------------------------------------------
experience_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 220" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0822" />
      <stop offset="100%" stop-color="#090516" />
    </linearGradient>

    <linearGradient id="purple-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#3b1f66" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.7" />
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .badge { fill: #1c1038; stroke: #7e22ce; stroke-width: 1; }
    .badge-text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 10px; font-weight: 600; fill: #e9d5ff; }
  </style>

  <!-- Header -->
  <text x="5" y="24" class="font-sans" font-size="16" font-weight="800" fill="#c084fc" letter-spacing="1.5">// EXPERIENCE</text>

  <!-- Two Wide Experience Cards -->
  <g transform="translate(0, 38)">
    <!-- Card 1: Data Science -->
    <g transform="translate(0, 0)">
      <rect width="455" height="170" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <!-- Title & Meta -->
      <g transform="translate(18, 22)">
        <!-- Chart icon -->
        <path d="M 0,10 L 3,10 L 3,3 L 0,3 Z M 5,10 L 8,10 L 8,0 L 5,0 Z M 10,10 L 13,10 L 13,6 L 10,6 Z" fill="#a855f7" />
        <text x="18" y="9" class="font-sans" font-size="11.5" font-weight="700" fill="#ffffff">Data Science Projects</text>
        <text x="145" y="9" class="font-sans" font-size="11" fill="#a78bfa">— Self-Directed Learning | 2024 - Present</text>
      </g>

      <!-- Badges Row -->
      <g transform="translate(18, 42)">
        <rect x="0" y="0" width="50" height="20" rx="4" class="badge" />
        <text x="9" y="14" class="badge-text">Python</text>

        <rect x="56" y="0" width="50" height="20" rx="4" class="badge" />
        <text x="64" y="14" class="badge-text">Pandas</text>

        <rect x="112" y="0" width="50" height="20" rx="4" class="badge" />
        <text x="120" y="14" class="badge-text">NumPy</text>

        <rect x="168" y="0" width="58" height="20" rx="4" class="badge" />
        <text x="174" y="14" class="badge-text">Matplotlib</text>

        <rect x="232" y="0" width="96" height="20" rx="4" class="badge" />
        <text x="238" y="14" class="badge-text">Data Visualization</text>

        <rect x="334" y="0" width="38" height="20" rx="4" class="badge" />
        <text x="342" y="14" class="badge-text">EDA</text>
      </g>

      <!-- Bullet Points -->
      <g class="font-sans" font-size="11" fill="#cbd5e1" transform="translate(20, 85)">
        <circle cx="2" cy="-4" r="2.5" fill="#a855f7" />
        <text x="12" y="0">Built and analyzed datasets using Python to extract insights and identify trends</text>

        <circle cx="2" cy="20" r="2.5" fill="#a855f7" />
        <text x="12" y="24">Applied data preprocessing and cleaning techniques</text>

        <circle cx="2" cy="44" r="2.5" fill="#a855f7" />
        <text x="12" y="48">Designed visualizations to communicate findings clearly</text>
      </g>
    </g>

    <!-- Card 2: Web Development -->
    <g transform="translate(485, 0)">
      <rect width="455" height="170" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <!-- Title & Meta -->
      <g transform="translate(18, 22)">
        <!-- Globe icon -->
        <circle cx="6" cy="6" r="6" fill="none" stroke="#a855f7" stroke-width="1.5" />
        <ellipse cx="6" cy="6" rx="3" ry="6" fill="none" stroke="#a855f7" stroke-width="1" />
        <line x1="0" y1="6" x2="12" y2="6" stroke="#a855f7" stroke-width="1" />
        <text x="18" y="9" class="font-sans" font-size="11.5" font-weight="700" fill="#ffffff">Web Development Projects</text>
        <text x="175" y="9" class="font-sans" font-size="11" fill="#a78bfa">— Self-Directed Learning | 2023 - Present</text>
      </g>

      <!-- Badges Row -->
      <g transform="translate(18, 42)">
        <rect x="0" y="0" width="48" height="20" rx="4" class="badge" />
        <text x="8" y="14" class="badge-text">HTML5</text>

        <rect x="54" y="0" width="44" height="20" rx="4" class="badge" />
        <text x="62" y="14" class="badge-text">CSS3</text>

        <rect x="104" y="0" width="68" height="20" rx="4" class="badge" />
        <text x="111" y="14" class="badge-text">JavaScript</text>

        <rect x="178" y="0" width="105" height="20" rx="4" class="badge" />
        <text x="184" y="14" class="badge-text">Responsive Design</text>

        <rect x="289" y="0" width="75" height="20" rx="4" class="badge" />
        <text x="295" y="14" class="badge-text">Git &amp; GitHub</text>
      </g>

      <!-- Bullet Points -->
      <g class="font-sans" font-size="11" fill="#cbd5e1" transform="translate(20, 85)">
        <circle cx="2" cy="-4" r="2.5" fill="#a855f7" />
        <text x="12" y="0">Designed and developed responsive websites</text>

        <circle cx="2" cy="20" r="2.5" fill="#a855f7" />
        <text x="12" y="24">Focused on user experience and clean design</text>

        <circle cx="2" cy="44" r="2.5" fill="#a855f7" />
        <text x="12" y="48">Deployed a personal portfolio on GitHub Pages</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "04_experience.svg"), "w") as f:
    f.write(experience_svg)

print("Created 04_experience.svg")

# -------------------------------------------------------------------------
# 5. assets/05_featured_projects.svg
# -------------------------------------------------------------------------
projects_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 250" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0822" />
      <stop offset="100%" stop-color="#090516" />
    </linearGradient>

    <linearGradient id="purple-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#3b1f66" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.7" />
    </linearGradient>

    <pattern id="circuit" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 0 10 L 20 10 M 10 0 L 10 20" stroke="#a855f7" stroke-width="0.3" opacity="0.12" />
      <circle cx="10" cy="10" r="1.5" fill="#a855f7" opacity="0.15" />
    </pattern>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .badge { fill: #1c1038; stroke: #7e22ce; stroke-width: 1; }
    .badge-text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 9.5px; font-weight: 600; fill: #e9d5ff; }
    .link-text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; font-weight: 700; fill: #38bdf8; }
  </style>

  <!-- Header -->
  <text x="5" y="24" class="font-sans" font-size="16" font-weight="800" fill="#c084fc" letter-spacing="1.5">// FEATURED PROJECTS</text>

  <!-- 4 Cards in Row -->
  <g transform="translate(0, 38)">
    <!-- Card 1: Personal Portfolio Website -->
    <g transform="translate(0, 0)">
      <rect width="220" height="200" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <rect width="220" height="200" rx="12" fill="url(#circuit)" />

      <!-- Top Icon: Laptop -->
      <g transform="translate(18, 16)">
        <rect x="0" y="0" width="28" height="18" rx="2" fill="none" stroke="#38bdf8" stroke-width="1.8" />
        <rect x="3" y="3" width="22" height="12" fill="#0284c7" opacity="0.4" />
        <line x1="-4" y1="20" x2="32" y2="20" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
      </g>

      <!-- Title & Desc -->
      <g transform="translate(18, 62)">
        <text class="font-sans" font-size="13" font-weight="700" fill="#ffffff">Personal Portfolio</text>
        <text y="16" class="font-sans" font-size="13" font-weight="700" fill="#ffffff">Website</text>
        <text y="38" class="font-sans" font-size="10.5" fill="#a78bfa">Fully responsive portfolio</text>
        <text y="52" class="font-sans" font-size="10.5" fill="#a78bfa">showcasing projects &amp; skills.</text>
      </g>

      <!-- Badges -->
      <g transform="translate(18, 138)">
        <rect x="0" y="0" width="46" height="18" rx="4" class="badge" />
        <text x="6" y="13" class="badge-text">HTML5</text>

        <rect x="52" y="0" width="42" height="18" rx="4" class="badge" />
        <text x="59" y="13" class="badge-text">CSS3</text>

        <rect x="100" y="0" width="62" height="18" rx="4" class="badge" />
        <text x="105" y="13" class="badge-text">JavaScript</text>
      </g>

      <!-- Link -->
      <text x="18" y="182" class="link-text">View Project →</text>
    </g>

    <!-- Card 2: Data Analysis & Visualization Toolkit -->
    <g transform="translate(240, 0)">
      <rect width="220" height="200" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <rect width="220" height="200" rx="12" fill="url(#circuit)" />

      <!-- Top Icon: EDA / Analytics -->
      <g transform="translate(18, 16)">
        <path d="M 0,20 L 6,20 L 6,10 L 0,10 Z M 8,20 L 14,20 L 14,4 L 8,4 Z M 16,20 L 22,20 L 16,14 L 16,14 Z M 24,20 L 30,20 L 30,0 L 24,0 Z" fill="#38bdf8" />
      </g>

      <!-- Title & Desc -->
      <g transform="translate(18, 62)">
        <text class="font-sans" font-size="12.5" font-weight="700" fill="#ffffff">Data Analysis &amp;</text>
        <text y="16" class="font-sans" font-size="12.5" font-weight="700" fill="#ffffff">Visualization Toolkit</text>
        <text y="38" class="font-sans" font-size="10.5" fill="#a78bfa">EDA pipeline with Python &amp;</text>
        <text y="52" class="font-sans" font-size="10.5" fill="#a78bfa">automated analytics suite.</text>
      </g>

      <!-- Badges -->
      <g transform="translate(18, 138)">
        <rect x="0" y="0" width="48" height="18" rx="4" class="badge" />
        <text x="6" y="13" class="badge-text">Python</text>

        <rect x="54" y="0" width="48" height="18" rx="4" class="badge" />
        <text x="60" y="13" class="badge-text">Pandas</text>

        <rect x="108" y="0" width="56" height="18" rx="4" class="badge" />
        <text x="113" y="13" class="badge-text">Matplotlib</text>
      </g>

      <!-- Link -->
      <text x="18" y="182" class="link-text">View Project →</text>
    </g>

    <!-- Card 3: Smart Banking System -->
    <g transform="translate(480, 0)">
      <rect width="220" height="200" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <rect width="220" height="200" rx="12" fill="url(#circuit)" />

      <!-- Top Icon: Bank / Pillars -->
      <g transform="translate(18, 16)">
        <polygon points="14,0 0,8 28,8" fill="#38bdf8" />
        <rect x="2" y="9" width="4" height="10" fill="#38bdf8" />
        <rect x="9" y="9" width="4" height="10" fill="#38bdf8" />
        <rect x="16" y="9" width="4" height="10" fill="#38bdf8" />
        <rect x="23" y="9" width="4" height="10" fill="#38bdf8" />
        <rect x="0" y="19" width="28" height="3" fill="#38bdf8" />
      </g>

      <!-- Title & Desc -->
      <g transform="translate(18, 62)">
        <text class="font-sans" font-size="13" font-weight="700" fill="#ffffff">Smart Banking System</text>
        <text y="24" class="font-sans" font-size="10.5" fill="#a78bfa">Banking management system.</text>
        <text y="38" class="font-sans" font-size="10.5" fill="#a78bfa">Focused on clean OOP design</text>
        <text y="52" class="font-sans" font-size="10.5" fill="#a78bfa">&amp; transaction security.</text>
      </g>

      <!-- Badges -->
      <g transform="translate(18, 138)">
        <rect x="0" y="0" width="46" height="18" rx="4" class="badge" />
        <text x="6" y="13" class="badge-text">HTML5</text>

        <rect x="52" y="0" width="42" height="18" rx="4" class="badge" />
        <text x="59" y="13" class="badge-text">CSS3</text>

        <rect x="100" y="0" width="32" height="18" rx="4" class="badge" />
        <text x="106" y="13" class="badge-text">C++</text>

        <rect x="138" y="0" width="34" height="18" rx="4" class="badge" />
        <text x="144" y="13" class="badge-text">PHP</text>
      </g>

      <!-- Link -->
      <text x="18" y="182" class="link-text">View Project →</text>
    </g>

    <!-- Card 4: SQL Migrator -->
    <g transform="translate(720, 0)">
      <rect width="220" height="200" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
      <rect width="220" height="200" rx="12" fill="url(#circuit)" />

      <!-- Top Icon: Database -->
      <g transform="translate(18, 16)">
        <ellipse cx="14" cy="5" rx="14" ry="4" fill="#38bdf8" />
        <path d="M 0,5 L 0,12 C 0,14.5 6,16 14,16 C 22,16 28,14.5 28,12 L 28,5" fill="none" stroke="#38bdf8" stroke-width="1.6" />
        <path d="M 0,12 L 0,19 C 0,21.5 6,23 14,23 C 22,23 28,21.5 28,19 L 28,12" fill="none" stroke="#38bdf8" stroke-width="1.6" />
      </g>

      <!-- Title & Desc -->
      <g transform="translate(18, 62)">
        <text class="font-sans" font-size="13" font-weight="700" fill="#ffffff">SQL Migrator</text>
        <text y="24" class="font-sans" font-size="10.5" fill="#a78bfa">Database migration platform</text>
        <text y="38" class="font-sans" font-size="10.5" fill="#a78bfa">automating schema &amp; data</text>
        <text y="52" class="font-sans" font-size="10.5" fill="#a78bfa">transfers seamlessly.</text>
      </g>

      <!-- Badges -->
      <g transform="translate(18, 138)">
        <rect x="0" y="0" width="48" height="18" rx="4" class="badge" />
        <text x="6" y="13" class="badge-text">Python</text>

        <rect x="54" y="0" width="40" height="18" rx="4" class="badge" />
        <text x="61" y="13" class="badge-text">Flask</text>

        <rect x="100" y="0" width="48" height="18" rx="4" class="badge" />
        <text x="106" y="13" class="badge-text">MySQL</text>
      </g>

      <!-- Link -->
      <text x="18" y="182" class="link-text">View Project →</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(assets_dir, "05_featured_projects.svg"), "w") as f:
    f.write(projects_svg)

print("Created 05_featured_projects.svg")

# -------------------------------------------------------------------------
# 6. assets/06_footer_section.svg
# -------------------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 270" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0822" />
      <stop offset="100%" stop-color="#090516" />
    </linearGradient>

    <linearGradient id="purple-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#3b1f66" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0.7" />
    </linearGradient>

    <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#9333ea" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#c084fc" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.8" />
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
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  </style>

  <!-- 3 Bottom Cards -->
  <g transform="translate(0, 0)">
    <!-- Card 1: // CURRENT FOCUS -->
    <g transform="translate(0, 0)">
      <text x="5" y="16" class="font-sans" font-size="14" font-weight="800" fill="#c084fc" letter-spacing="1">// CURRENT FOCUS</text>
      <g transform="translate(0, 26)">
        <rect width="295" height="150" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
        
        <!-- Target Icon on Left -->
        <g transform="translate(25, 45)">
          <circle cx="28" cy="28" r="26" fill="none" stroke="#a855f7" stroke-width="2.5" />
          <circle cx="28" cy="28" r="18" fill="none" stroke="#c084fc" stroke-width="2" />
          <circle cx="28" cy="28" r="10" fill="none" stroke="#38bdf8" stroke-width="2" />
          <circle cx="28" cy="28" r="4" fill="#ffffff" />
          <!-- Arrow line -->
          <line x1="42" y1="14" x2="56" y2="0" stroke="#c084fc" stroke-width="2.5" stroke-linecap="round" />
        </g>

        <!-- Checklist -->
        <g class="font-sans" font-size="12" font-weight="600" fill="#f3e8ff" transform="translate(100, 30)">
          <path d="M 0,6 L 4,10 L 12,2" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
          <text x="20" y="8">Backend Engineering</text>

          <path d="M 0,31 L 4,35 L 12,27" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
          <text x="20" y="33">Machine Learning</text>

          <path d="M 0,56 L 4,60 L 12,52" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
          <text x="20" y="58">Data Engineering</text>

          <path d="M 0,81 L 4,85 L 12,77" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
          <text x="20" y="83">Open Source</text>
        </g>
      </g>
    </g>

    <!-- Card 2: // CONNECT -->
    <g transform="translate(322, 0)">
      <text x="5" y="16" class="font-sans" font-size="14" font-weight="800" fill="#c084fc" letter-spacing="1">// CONNECT</text>
      <g transform="translate(0, 26)">
        <rect width="295" height="150" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
        
        <!-- Buttons Column / Row -->
        <g transform="translate(20, 52)">
          <!-- Email Button -->
          <g transform="translate(0, 0)">
            <rect width="78" height="34" rx="17" fill="#dc2626" />
            <!-- Mail icon -->
            <path d="M 12,12 L 24,12 L 24,22 L 12,22 Z" fill="none" stroke="#ffffff" stroke-width="1.2" />
            <path d="M 12,12 L 18,17 L 24,12" fill="none" stroke="#ffffff" stroke-width="1.2" />
            <text x="30" y="21" class="font-sans" font-size="11.5" font-weight="700" fill="#ffffff">Email</text>
          </g>

          <!-- LinkedIn Button -->
          <g transform="translate(86, 0)">
            <rect width="88" height="34" rx="17" fill="#0077b5" />
            <text x="14" y="22" class="font-sans" font-size="11" font-weight="900" fill="#ffffff">in</text>
            <text x="30" y="21" class="font-sans" font-size="11.5" font-weight="700" fill="#ffffff">LinkedIn</text>
          </g>

          <!-- GitHub Button -->
          <g transform="translate(182, 0)">
            <rect width="78" height="34" rx="17" fill="#130c29" stroke="#7e22ce" stroke-width="1" />
            <circle cx="16" cy="17" r="6" fill="#ffffff" />
            <text x="26" y="21" class="font-sans" font-size="11.5" font-weight="700" fill="#ffffff">GitHub</text>
          </g>
        </g>
      </g>
    </g>

    <!-- Card 3: // LET'S BUILD TOGETHER -->
    <g transform="translate(645, 0)">
      <text x="5" y="16" class="font-sans" font-size="14" font-weight="800" fill="#c084fc" letter-spacing="1">// LET'S BUILD TOGETHER</text>
      <g transform="translate(0, 26)">
        <rect width="295" height="150" rx="12" fill="url(#card-bg)" stroke="url(#purple-border)" stroke-width="1.2" />
        
        <g transform="translate(18, 38)">
          <text x="0" y="10" class="font-sans" font-size="11.5" fill="#f3e8ff">Feel free to explore my repositories,</text>
          <text x="0" y="28" class="font-sans" font-size="11.5" fill="#f3e8ff">connect, or collaborate!</text>
        </g>

        <!-- Handshake Icon on Right -->
        <g transform="translate(210, 42)">
          <circle cx="30" cy="30" r="28" fill="#1e103a" stroke="#8b5cf6" stroke-width="1.5" filter="url(#soft-glow)" />
          <!-- Handshake motif -->
          <path d="M 16,30 L 25,24 L 35,32 L 44,25" fill="none" stroke="#c084fc" stroke-width="2.5" stroke-linecap="round" />
          <path d="M 16,34 L 25,40 L 35,32" fill="none" stroke="#a855f7" stroke-width="2.5" stroke-linecap="round" />
        </g>
      </g>
    </g>
  </g>

  <!-- Bottom Footer Bar: DESIGN | DEVELOP | DEFEND -->
  <g transform="translate(0, 215)">
    <text x="470" y="20" class="font-sans" font-size="13" font-weight="800" fill="#e9d5ff" letter-spacing="6" text-anchor="middle">DESIGN &nbsp;&nbsp;|&nbsp;&nbsp; DEVELOP &nbsp;&nbsp;|&nbsp;&nbsp; DEFEND</text>
    
    <!-- Flowing Purple Energy Ribbons at bottom -->
    <path d="M 0,40 Q 200,10 470,35 T 940,25 L 940,55 L 0,55 Z" fill="url(#wave-grad)" opacity="0.6" filter="url(#soft-glow)" />
    <path d="M 0,48 Q 280,30 500,45 T 940,38 L 940,55 L 0,55 Z" fill="url(#wave-grad)" opacity="0.4" />
  </g>
</svg>'''

with open(os.path.join(assets_dir, "06_footer_section.svg"), "w") as f:
    f.write(footer_svg)

print("Created 06_footer_section.svg")
print("All 6 visual assets successfully compiled.")
