<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td width="70%" align="left" valign="top">

# Isaac Nathan
**Full-Stack AI Engineer · Computer Engineering · Cloud Architecture**

[**Portfolio**](https://xangrybadger.github.io/isaac-vitae/) · [**LinkedIn**](https://www.linkedin.com/in/isaac-nathan-da-silva-barbosa-815b212ab/) · [**Email**](mailto:isaacnathandasilva@gmail.com)

</td>
<td width="30%" align="right" valign="top">

<img src="https://avatars.githubusercontent.com/xAngryBadger" width="120" style="border: 2px solid #456A4B; border-radius: 4px;" alt="Isaac Nathan" />

</td>
</tr>
</table>

<table border="0" cellspacing="0" cellpadding="8">
<tr>
<td width="50%" valign="top">

**🇧🇷 PT-BR**<br/>
Estudante de Engenharia de Computação (5º semestre) focado em arquitetura de sistemas pragmáticos. Na **Paware Softwares**, lidero migrações críticas para Azure Cosmos DB e orquestração de agentes de IA generativa. Minha abordagem ignora o *hype* para focar em integridade de dados e utilidade real.

</td>
<td width="50%" valign="top">

**🇺🇸 EN-US**<br/>
Computer Engineering student (5th semester) focused on pragmatic systems architecture. At **Paware Softwares**, I lead critical migrations to Azure Cosmos DB and generative AI agent orchestration. My approach bypasses *hype* to focus on data integrity and real-world utility.

</td>
</tr>
</table>

> *Utility over hype. Data integrity over demo polish. Ship what works.*

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
> Engineered migration of high-volume datasets from Google Drive to **Azure Cosmos DB** for Meritage Homes (USA), ensuring data integrity and security in production. Architected AI image-generation pipelines (Flux, DALL-E 3, Placid/Canva) for **HelloSocial**. Docker environments for testing and consistency in conversational AI agents.

> **SuperNerds** · Robotics Instructor · `Sep 2025 — Oct 2025`
>
> Taught programming logic and robotics to children and teens — Arduino, visual platforms, and hands-on projects connecting theory to real applications.

---

### Selected Engineering Projects

<table width="100%">
<tr>
<td width="8%" align="center">🦅</td>
<td>
<strong>HarpIA</strong> · <a href="https://github.com/xAngryBadger/harpia">source</a><br/>
Creative automation engine with 7+ AI models — GPT-4.1 agent with tool calling, autonomous agentic pipeline (copywriting, image search, design compositing, video generation). Zero-cost by default with SQLite + local PIL.<br/>
<code>Python</code> <code>GPT-4.1</code> <code>DALL-E 3</code> <code>Flux 2.0 Pro</code> <code>Sora</code> <code>Veo 3.1</code> <code>Azure Cosmos DB</code>
</td>
</tr>
<tr>
<td width="8%" align="center">📱</td>
<td>
<strong>Flora Sensus</strong> · <a href="https://github.com/xAngryBadger/flora-sensus">source</a><br/>
Offline-first forest inventory app with full sync engine — conflict detection, atomic rollback, UUID remapping for client-server reconciliation. React admin panel with XLSX/PDF/CSV export. 24K+ hand-crafted LOC, 30+ features.<br/>
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

Migrated high-volume legacy datasets from Google Drive to Azure Cosmos DB for a US homebuilding company. Key architectural decisions:

- **Schema validation layer** — Python-based consistency checks before every write, ensuring no data corruption during transfer
- **Parallel BLOB processing** — concurrent transfer of large binary objects with configurable throughput limits to avoid throttling
- **Automated rollback triggers** — on 4xx/5xx API responses, the pipeline halts and reverts the batch to a known-good checkpoint
- **Idempotent upsert pattern** — `create_if_missing / replace_if_exists` ensures re-runs don't duplicate or orphan records

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
- **Zero-cost fallback** — when no paid API is needed, a PIL compositor renders designs locally with 8 layout templates, brand colors, and badge overlays using SQLite for state persistence
- **Cron-ready** — file-locking prevents concurrent runs; stuck batch recovery handles orphaned processes automatically
- **Backend swap** — local SQLite for development, Azure Cosmos DB + Blob Storage for production, toggled via environment config

</details>

---

### Education & Certifications

**B.S. Computer Engineering** · Cruzeiro do Sul · 2024 — 2029 · 5th semester (in progress)

**Cisco Networking Academy** — Python Essentials 1 & 2 · Data Science Essentials · Data Analytics Essentials · Networking Basics (120h) · Intro to Cybersecurity

**Gov AI Program (PBIA)** — AI for Process Optimization & Decision-Making · 71h · Enap/Serpro

**KUMON** — English fluency · 3 years · enables technical documentation and meetings with international teams

---

### Stats

<img src="https://github-readme-stats.vercel.app/api?username=xAngryBadger&show_icons=true&theme=transparent&hide_border=true&bg_color=0D1117&title_color=456A4B&icon_color=8B6914&text_color=8B9481" width="48%" alt="Stats" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=xAngryBadger&layout=compact&theme=transparent&hide_border=true&bg_color=0D1117&title_color=456A4B&text_color=8B9481&langs_count=10" width="45%" alt="Top Languages" />

---

Mariana, MG — Brazil · Open to high-impact AI/Cloud collaborations
