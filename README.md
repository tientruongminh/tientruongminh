<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=260&color=0:020617,35:0f766e,70:22c55e,100:111827&text=Tien%20Truong%20Minh&fontColor=f8fafc&fontSize=52&fontAlignY=36&desc=HCMUS%20Data%20Science%20%7C%20AI%20Engineering%20%40%20Amoiq%20%7C%20Systems%20Builder&descAlignY=58&descSize=16&animation=fadeIn" alt="Tien Truong Minh" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2600&pause=800&color=34D399&center=true&vCenter=true&width=900&lines=I+build+AI+systems+that+ship.;Research+ideas+%E2%86%92+clean+architecture+%E2%86%92+real+platforms.;WiFi+CSI+%7C+agents+%7C+ML+systems+%7C+backend+infrastructure" alt="Typing introduction" />

<br />
<br />

<a href="https://github.com/tientruongminh/rf-worldpose"><img src="https://img.shields.io/badge/featured-RF--WorldPose-10b981?style=for-the-badge&labelColor=020617" alt="RF-WorldPose" /></a>
<img src="https://img.shields.io/badge/HCMUS-Year%203%20Data%20Science-0f766e?style=for-the-badge&labelColor=020617" alt="HCMUS Data Science" />
<img src="https://img.shields.io/badge/Amoiq-AI%20Engineering-14b8a6?style=for-the-badge&labelColor=020617" alt="AI Engineering at Amoiq" />

</div>

---

## Hello, I am Tien

I am a third-year **Data Science student at HCMUS** and currently working in **AI Engineering at Amoiq**. I like building things that sit between research and production: agent systems, ML pipelines, backend services, data infrastructure, and interfaces that make complex systems usable.

My favorite type of project is not a small demo. I like taking a hard idea, breaking it into clean architecture, then pushing it toward a real platform with contracts, runbooks, tests, deployment paths, and enough engineering depth that someone else can continue building on it.

```text
research question
   -> system design
      -> working prototype
         -> production-grade architecture
            -> documentation, tests, deployment, iteration
```

<table>
<tr>
<td width="50%" valign="top">

### What I am focused on

- AI engineering and applied ML systems
- Agent tooling and automation workflows
- WiFi CSI / RF sensing research
- Data pipelines and model evaluation
- Backend infrastructure for AI products
- Product-grade frontend experiences

</td>
<td width="50%" valign="top">

### How I like to build

- Start from a clear architecture
- Make data contracts explicit
- Keep research code reproducible
- Add observability and failure paths early
- Turn useful experiments into reusable systems
- Write documentation that another engineer can run

</td>
</tr>
</table>

---

## Selected projects

<table>
<tr>
<td width="33%" valign="top">

### RF-WorldPose

A production/research platform for WiFi CSI human sensing and WiFi-only skeleton/DensePose inference.

**Stack:** ESP32-S3, Rust/Tokio, FastAPI, Dagster, PyTorch, Helios GH200, ONNX, Triton.

<a href="https://github.com/tientruongminh/rf-worldpose"><img src="https://img.shields.io/badge/open-repository-10b981?style=flat-square&labelColor=020617" alt="Open RF-WorldPose" /></a>

</td>
<td width="33%" valign="top">

### Flowboard

An open-source infinite canvas for AI product videos: drag nodes for model, product, scene, and video generation, then connect the workflow.

**Stack:** Python, AI workflow orchestration, local-first creative tooling.

<a href="https://github.com/tientruongminh/flowboard"><img src="https://img.shields.io/badge/open-repository-14b8a6?style=flat-square&labelColor=020617" alt="Open Flowboard" /></a>

</td>
<td width="33%" valign="top">

### Memento-Skills

A system around agent skill design: making AI agents easier to extend, reuse, and reason about through structured capabilities.

**Stack:** Python, agent tooling, skill systems, automation.

<a href="https://github.com/tientruongminh/Memento-Skills"><img src="https://img.shields.io/badge/open-repository-2dd4bf?style=flat-square&labelColor=020617" alt="Open Memento-Skills" /></a>

</td>
</tr>
</table>

---

## Current deep build: RF-WorldPose

I am building **RF-WorldPose**, a full-stack research platform for sensing people through WiFi channel state information instead of cameras.

```text
ESP32-S3 CSI nodes
   -> CRC-protected UDP packets
      -> Rust edge gateway
         -> NATS JetStream + local SQLite buffer
            -> S3/MinIO Bronze data lake
               -> Dagster ETL: Bronze -> Silver -> Gold
                  -> PyTorch RFWorldPose model
                     -> Helios GH200 Slurm training
                        -> MLflow, model cards, eval gates
                           -> ONNX edge inference / Triton cloud inference
```

The goal is to treat RF sensing like a serious ML platform: device firmware, gateway reliability, dataset versioning, training reproducibility, model governance, deployment, monitoring, and rollback all belong in the same system.

---

## Toolbox

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,rust,go,fastapi,postgres,docker,kubernetes,ts,nextjs,react,nodejs,linux,git,github,bash" alt="Tech stack" />

</div>

<br />

<table>
<tr>
<td width="25%" align="center">

**AI / ML**

PyTorch<br />
Dataset pipelines<br />
Model evaluation<br />
LoRA / distillation

</td>
<td width="25%" align="center">

**Backend**

FastAPI<br />
Rust/Tokio<br />
PostgreSQL<br />
NATS / S3

</td>
<td width="25%" align="center">

**Frontend**

Next.js<br />
React<br />
Canvas UI<br />
Product interfaces

</td>
<td width="25%" align="center">

**Ops**

Docker<br />
Kubernetes<br />
Prometheus<br />
Runbooks

</td>
</tr>
</table>

---

## GitHub signal

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=tientruongminh&show_icons=true&theme=vue-dark&hide_border=true&bg_color=020617&title_color=34d399&icon_color=34d399&text_color=e5e7eb" alt="GitHub stats" />
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=tientruongminh&layout=compact&theme=vue-dark&hide_border=true&bg_color=020617&title_color=34d399&text_color=e5e7eb" alt="Top languages" />

<br />
<br />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=tientruongminh&bg_color=020617&color=e5e7eb&line=34d399&point=5eead4&area=true&hide_border=true" alt="Contribution graph" />

</div>

---

## Build philosophy

> I care about systems that can survive contact with reality: noisy data, broken infrastructure, changing requirements, and users who need the thing to work.

I am still learning, but I like learning by building projects that force me to understand the whole path: from data and algorithms to APIs, deployment, UX, documentation, and iteration.

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=130&section=footer&color=0:111827,50:0f766e,100:020617" alt="Footer" />

</div>
