<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="70%" align="left" valign="top">

# Isaac Nathan
**Full-Stack AI Engineer · Computer Engineering · Cloud Architecture**

[**Portfolio**](https://xangrybadger.github.io/isaac-vitae/) · [**LinkedIn**](https://www.linkedin.com/in/isaac-nathan-da-silva-barbosa-815b212ab/) · [**Email**](mailto:isaacnathandasilva@gmail.com)

</td>
<td width="30%" align="right" valign="top">

<img src="assets/foto-isaac.jpg" width="120" style="border: 2px solid #456A4B; border-radius: 4px;" alt="Isaac Nathan" />

</td>
</tr>
</table>

<table border="0" cellspacing="0" cellpadding="8">
<tr>
<td width="50%" valign="top">

**🇧🇷 PT-BR**<br/>
Meu primeiro contato com Python foi em 2022 na UFOP (Química Industrial) — Thonny IDE, sem GPT, aulas extras à tarde só para continuar aprendendo. Depois de 2 anos em Engenharia Química na UFSJ, voltei para Mariana e mudei para Computação. Construí o ForestAI do zero usando Stack Overflow e Thonny, anotando manualmente centenas de imagens de drone da Fundação Renova. Hoje na **Paware Softwares**, migrei bases para Azure Cosmos DB (Meritage Homes, EUA) e orquestro agentes de IA para o HelloSocial. Aprendo resolvendo problemas reais, não seguindo tutoriais.

</td>
<td width="50%" valign="top">

**🇺🇸 EN-US**<br/>
My first Python contact was in 2022 at UFOP (Industrial Chemistry) — Thonny IDE, no GPT, extra afternoon classes just to keep learning. After 2 years in Chemical Engineering at UFSJ, I came home and pivoted to Computer Engineering. I built ForestAI from scratch using Stack Overflow and Thonny, manually annotating hundreds of drone images from Fundação Renova. Now at **Paware Softwares**, I migrated databases to Azure Cosmos DB (Meritage Homes, USA) and orchestrate AI agents for HelloSocial. I learn by solving real problems, not following tutorials.

</td>
</tr>
</table>

---

### Origin

**2022** — Fell in love with Python at UFOP (Industrial Chemistry). Thonny IDE, pre-GPT era, extra afternoon classes just to code more.

**2022–2024** — Two years in Chemical Engineering at UFSJ (Ouro Branco). Away from code, but watching the AI field closely.

**2024** — Pivoted to Computer Engineering at Cruzeiro do Sul. Built **ForestAI** from the ground up — Stack Overflow and Thonny, not AI-assisted. Manually annotated hundreds of drone images from Fundação Renova, trained species detection models (YOLO, PyTorch, DeepForest) on local GPU, interpreted training curves on TensorBoard. The hard way — and it stuck.

**2024–2025** — Self-taught expansion: system scripts, PC optimization, Windows deployments (Registry, Group Policy, Massgrave). IT services for home and church. Exchanging code and ideas with two childhood friends — one in Portugal, one in the South.

**Mid-2025** — One of those friends saw ForestAI and introduced me to Paware Softwares. The rest is below.

---

### Core Stack

**AI & Data** — `GPT-4.1` · `DALL-E 3` · `Flux` · `Ollama` · `PyTorch` · `DeepForest` · `Azure OpenAI`

**Backend** — `Python` · `FastAPI` · `Azure Cosmos DB` · `Docker` · `Node.js`

**Frontend** — `React 19` · `TypeScript` · `Flutter` · `Tailwind CSS v4`

**Infra & Tools** — `Linux (CachyOS/Hyprland)` · `Git` · `PocketBase` · `PyInstaller/Inno Setup`

---

### Professional Trajectory

> **Paware Softwares** · Full-Stack Developer · `Oct 2025 — Present`
>
> Built automated extraction scripts (cookie-based auth) to pull legacy datasets from Google Drive for **Meritage Homes (USA)** — working directly with Luciano Amado (Orlando, FL). Scripts handled file compression, renaming, and injection into presentation panels ready for **WhatsApp agent embedding** (which had strict file size limits). Hit a cross-platform wall: Android displayed files natively, but iPhone required `application/octet-stream` headers to force ZIPs to open in Firefox. When duplicated files exposed gaps, I introduced **Docker** for reproducible test environments and wrote a validation layer that became the backbone of the final migration to **Azure Cosmos DB**. Now architected AI image-generation pipelines (Flux, DALL-E 3, Placid/Canva) for **HelloSocial**.

> **SuperNerds** · Robotics Instructor · `Sep 2025 — Oct 2025`
>
> Taught programming logic and robotics to children and teens — Arduino and LEGO platforms. Learned both in under two weeks from my coding background, then developed hands-on projects connecting theory to real applications. Balanced mornings here with Paware at night.

---

### Selected Engineering Projects

<table width="100%">
<tr>
<td width="8%" align="center">🦅</td>
<td>
<strong>HarpIA</strong> · <a href="https://github.com/xAngryBadger/harpia">source</a><br/>
Creative automation engine with 7+ AI models — GPT-4.1 agent with tool calling, autonomous agentic pipeline (copywriting, image search, design compositing, video generation). Stack leve por padrão (SQLite + local PIL), com fallback para APIs pagas quando necessário.<br/>
<code>Python</code> <code>GPT-4.1</code> <code>DALL-E 3</code> <code>Flux 2.0 Pro</code> <code>Sora</code> <code>Veo 3.1</code> <code>Azure Cosmos DB</code>
</td>
</tr>
<tr>
<td width="8%" align="center">📱</td>
<td>
<strong>Flora Sensus</strong> · <a href="https://github.com/xAngryBadger/flora-sensus">source</a><br/>
Offline-first forest inventory app with full sync engine — conflict detection, atomic rollback, UUID remapping for client-server reconciliation. React admin panel with XLSX/PDF/CSV export. ~24K LOC — arquitetura e lógica de sync construídas do zero; código gerado com apoio de LLM (web) e revisado manualmente.<br/>
<code>Flutter</code> <code>Dart</code> <code>Drift/SQLite</code> <code>React</code> <code>PocketBase</code>
</td>
</tr>
<tr>
<td width="8%" align="center">🌲</td>
<td>
<strong>SRF System</strong> · <a href="https://github.com/xAngryBadger/srf-system">source</a><br/>
Operational planning engine for large-scale forest restoration — generates executive dossiers, activity schedules, manages tariffs/crews/territories. NiceGUI + Rich CLI interface.<br/>
<code>Python</code> <code>pandas</code> <code>NiceGUI</code> <code>Rich</code> <code>openpyxl</code>
</td>
</tr>
<tr>
<td width="8%" align="center">🌿</td>
<td>
<strong>ForestAI</strong> · <a href="https://github.com/xAngryBadger/forestai">source</a><br/>
Forest species detection and classification with Deep Learning — full pipeline: DeepForest training, stratified splits, bounding box validation. Ongoing research project.<br/>
<code>PyTorch</code> <code>DeepForest</code> <code>OpenCV</code> <code>scikit-learn</code>
</td>
</tr>
<tr>
<td width="8%" align="center">🦊</td>
<td>
<strong>Fennec Excel</strong> · <a href="https://github.com/xAngryBadger/Sahara-Fenneck">source</a><br/>
Desktop app connecting Excel to a local AI agent (Ollama) — ReAct reasoning loop, 6+ OAuth integrations (Gmail, Teams, Calendar, Drive, Outlook, Trello), auto-checkpoint, native Windows installer.<br/>
<code>Python</code> <code>Ollama</code> <code>CustomTkinter</code> <code>xlwings/COM</code> <code>Inno Setup</code>
</td>
</tr>
<tr>
<td width="8%" align="center">🤖</td>
<td>
<strong>MaineCoon</strong> · <a href="https://github.com/xAngryBadger/minepal">source</a><br/>
Minecraft bot with natural language commands via LLM (NVIDIA NIM API) — mine, craft, follow, navigate, interact through chat. Reinforcement learning module for autonomous behavior.<br/>
<code>Node.js</code> <code>mineflayer</code> <code>NVIDIA NIM API</code> <code>Reinforcement Learning</code>
</td>
</tr>
</table>

---

### Technical Spotlights

<details>
<summary><b>Azure Cosmos DB Migration — Meritage Homes</b></summary>
<br/>

What started as cookie-based scripts to extract datasets from Google Drive for Luciano Amado's team (Orlando, FL) revealed duplicated and inconsistent files — a problem that couldn't be solved by simply pushing data to a new database. The pipeline had to handle more than just migration:

- **Cookie-based extraction layer** — automated scripts using session cookies to bypass Google Drive access controls, pulling hundreds of files on schedule
- **File compression + renaming + panel injection** — datasets had to be compressed, renamed according to Meritage's naming conventions, and injected into presentation panels ready for WhatsApp agent embedding (which imposed strict file size limits)
- **Cross-platform MIME type resolution** — Android devices displayed files natively, but iPhone refused to open ZIPs inline; the fix was serving them with `application/octet-stream` headers to force Firefox to handle the download
- **Docker for reproducibility** — duplicated files across runs made local testing unreliable; containerized the entire extraction + validation pipeline so every run starts from a known state
- **Schema validation layer** — Python-based consistency checks before every write, catching the duplicates and schema mismatches that the original scripts missed
- **Automated rollback triggers** — on 4xx/5xx API responses, the pipeline halts and reverts the batch to a known-good checkpoint
- **Idempotent upsert pattern** — `create_if_missing / replace_if_exists` ensures re-runs don't duplicate or orphan records

</details>

<details>
<summary><b>ForestAI — Computer Vision from Scratch</b></summary>
<br/>

Built without AI-assisted coding — Stack Overflow and Thonny IDE only. The project that started my learning curve from newbie to where I am now:

- **Manual data annotation** — hundreds of drone images from Fundação Renova, hand-labeled bounding boxes for forest species. Hard labor, but it taught me what the model actually sees
- **YOLO + DeepForest** — experimented with multiple detection architectures; DeepForest's RetinaNet backbone gave the best results for overhead canopy imagery
- **Local GPU training** — PyTorch on consumer hardware, stratified train/val splits to prevent overfitting on similar flight paths
- **TensorBoard interpretation** — learned to read loss curves, precision-recall tradeoffs, and detect when the model was memorizing vs. generalizing
- **The hard way was the point** — convoluted methods, no copilot, building intuition by breaking things. This foundation made every subsequent framework click faster

</details>

<details>
<summary><b>Flora Sensus — Offline Sync Engine Architecture</b></summary>
<br/>

Solved the "no-signal" problem in forestry field work with a custom sync engine:

- **Conflict detection** — server timestamps vs. local timestamps with last-write-wins policy and manual resolution fallback
- **UUID remapping** — client-generated UUIDs are reconciled with server-assigned IDs on sync, cascading through the full FK chain (Propriedade → UT → Parcela → Planta → Foto)
- **Atomic rollback** — if any part of a multi-table sync fails, the entire batch reverts via Drift transaction wrapping
- **Exponential backoff with jitter** — prevents thundering herd when multiple field devices reconnect simultaneously
- **Auth retry wrapper** — transparent token refresh on 401s, with ngrok bypass for development

</details>

<details>
<summary><b>HarpIA — Agentic Pipeline Design</b></summary>
<br/>

7+ AI models accessible through a unified interface, orchestrated by a GPT-4.1 agent:

- **Tool calling with schema enforcement** — the agent selects from a defined tool schema (image generation, copy writing, template selection, Pexels search) and the pipeline validates each tool call against the schema before execution
- **Multi-iteration reasoning loop** — up to 10 iterations of think → call → observe before returning a final result
- **Lightweight stack by default** — when no paid API is needed, a PIL compositor renders designs locally with 8 layout templates, brand colors, and badge overlays using SQLite for state persistence; falls back to paid APIs when necessary
- **Cron-ready** — file-locking prevents concurrent runs; stuck batch recovery handles orphaned processes automatically
- **Backend swap** — local SQLite for development, Azure Cosmos DB + Blob Storage for production, toggled via environment config

</details>

---

### Education & Certifications

**UFOP** · Industrial Chemistry · 2022 · *where Python began*

**UFSJ** · Chemical Engineering · 2022 — 2024 · *pivot period — away from code, watching AI closely*

**Cruzeiro do Sul** · Computer Engineering · 2024 — 2029 · 5th semester (in progress)

**Cisco Networking Academy** — Python Essentials 1 & 2 · Data Science Essentials · Data Analytics Essentials · Networking Basics (120h) · Intro to Cybersecurity

**Gov AI Program (PBIA)** — AI for Process Optimization & Decision-Making · 71h · Enap/Serpro

**KUMON** — English fluency · 3 years · enables technical documentation and meetings with international teams

---

### Stats

<img src="https://github-readme-stats-sigma-five.vercel.app/api?username=xAngryBadger&show_icons=true&theme=transparent&hide_border=true&bg_color=0D1117&title_color=456A4B&icon_color=8B6914&text_color=8B9481" width="48%" alt="Stats" />
<img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=xAngryBadger&layout=compact&theme=transparent&hide_border=true&bg_color=0D1117&title_color=456A4B&text_color=8B9481&langs_count=10" width="45%" alt="Top Languages" />

---

Mariana, MG — Brazil · Open to high-impact AI/Cloud collaborations
