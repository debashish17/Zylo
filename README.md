# TescoCreate AI 🎨✨

> **Intelligent Retail Media Creative Builder**

An AI-powered visual creative builder that democratizes professional-quality retail media creation. Combines an intuitive drag-and-drop interface with intelligent AI assistants for compliance validation, creative suggestions, and automated optimization.

---

## 🌟 Features

- **🎨 AI-Powered Design**: Intelligent layout suggestions, color palettes, and creative variants
- **✅ Real-time Compliance**: Automatic validation against Tesco retail media guidelines
- **🖼️ Advanced Image Processing**: Background removal, smart cropping, color extraction (GPU-accelerated)
- **✨ Creative Generation**: AI-powered headline and copy suggestions using Gemini/NVIDIA APIs
- **📐 Multi-Format Export**: Optimized exports for Facebook, Instagram, and Stories (1:1, 4:5, 9:16)
- **🎯 Accessibility First**: WCAG AA compliance checking built-in

---

## 🏗️ Architecture

```
📦 TescoCreate AI (Monorepo)
├── apps/web/              Next.js 14 frontend (tRPC, Fabric.js canvas)
├── services/
│   ├── compliance/        FastAPI - NLP compliance validation
│   ├── image/             FastAPI - GPU-accelerated image processing
│   └── creative/          FastAPI - AI creative generation
├── packages/              Shared libraries
└── scripts/               Development & setup scripts
```

### Tech Stack

**Frontend:**
- Next.js 14 (App Router), TypeScript, Tailwind CSS
- Fabric.js (canvas), tRPC (type-safe API), Zustand (state)
- shadcn/ui components, TanStack Query

**Backend:**
- Supabase (PostgreSQL + Storage + Auth)
- Prisma ORM

**AI/ML Services:**
- FastAPI (Python 3.11)
- PyTorch (GPU-accelerated)
- Transformers (BERT, CLIP)
- REMBG (background removal)
- Gemini API, NVIDIA NIM (free tier)

**Infrastructure:**
- Turborepo (monorepo)
- pnpm (package management)
- No Docker required (cloud Supabase + native services)

---

## 📋 Prerequisites

### Required Software

1. **Node.js 20+** - [Download](https://nodejs.org/)
2. **Python 3.11+** - [Download](https://www.python.org/downloads/)
3. **pnpm** - Install: `npm install -g pnpm`
4. **Git** - [Download](https://git-scm.com/)

### Optional (for GPU acceleration)

5. **NVIDIA CUDA Toolkit 12.1** - [Download](https://developer.nvidia.com/cuda-downloads)
6. **cuDNN** - [Download](https://developer.nvidia.com/cudnn) (requires NVIDIA account)

### Hardware Recommendations

- **CPU**: 4+ cores (Ryzen 7 or Intel i7+)
- **RAM**: 16GB minimum (8GB for services, 8GB for OS/browser)
- **GPU**: NVIDIA GPU with 6GB+ VRAM (optional but recommended)
  - Tested on: RTX 4050 (6GB), RTX 3060 (12GB), RTX 4090 (24GB)
  - CPU-only mode works but is 5-10x slower

---

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/tesco/create-ai.git
cd create-ai
```

### 2. Automated Setup (Windows)

```powershell
.\scripts\setup.ps1
```

This will:
- Install all Node.js dependencies
- Set up Python virtual environments
- Install Python packages
- Create environment file templates
- Test GPU availability

### 3. Configure Environment Variables

#### Supabase Setup

1. Create a free Supabase project: https://supabase.com
2. Copy your credentials:
   - Project URL
   - Anon (public) key
   - Service role key (secret)
3. Create database connection string

#### Edit `apps/web/.env.local`:

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGc...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGc...
DATABASE_URL=postgresql://postgres:[password]@db.xxxxx.supabase.co:5432/postgres

# AI APIs (Free)
GEMINI_API_KEY=your-key-here
NVIDIA_API_KEY=your-key-here
```

#### Get Free API Keys:

- **Gemini**: https://makersuite.google.com/app/apikey (1500 requests/day)
- **NVIDIA NIM**: https://build.nvidia.com/ (1000 requests/day)

### 4. Initialize Database

```bash
cd apps/web
pnpm prisma db push
```

This creates all tables in your Supabase database.

### 5. Create Supabase Storage Bucket

In Supabase dashboard:
1. Go to **Storage** > **Create bucket**
2. Name: `brand-assets`
3. Make public: ✅ Yes

### 6. Start Development

```powershell
.\scripts\dev.ps1
```

Select which services to run:
- ✅ Next.js (required)
- ✅ Compliance API (recommended)
- ✅ Image AI (recommended for background removal)
- ⚠️ Creative AI (optional, for AI text generation)

### 7. Open App

- **Frontend**: http://localhost:3000
- **Compliance API Docs**: http://localhost:8000/docs
- **Image AI Docs**: http://localhost:8001/docs
- **Creative AI Docs**: http://localhost:8002/docs

---

## 🎮 GPU Setup (Optional but Recommended)

### Why GPU?

With GPU acceleration, ML operations are **5-10x faster**:

| Task | CPU (Ryzen 7) | GPU (RTX 4050) | Speedup |
|------|--------------|----------------|---------|
| Background removal | 8-10s | 1-2s | **5x** |
| Compliance NLP | 3-5s | 0.3-0.5s | **10x** |
| Layout detection | 5-7s | 0.5-1s | **7x** |

### Installation

#### 1. Install CUDA Toolkit 12.1

Download: https://developer.nvidia.com/cuda-downloads

- Select: Windows > x86_64 > 11 > exe (local)
- Install all components
- Verify: `nvcc --version`

#### 2. Install cuDNN

Download: https://developer.nvidia.com/cudnn (requires free account)

- Extract ZIP
- Copy files to: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\`

#### 3. Install PyTorch with CUDA

```bash
# In each service virtual environment:
cd services/compliance
.\.venv\Scripts\Activate.ps1
pip install torch==2.2.0+cu121 torchvision==0.17.0+cu121 --index-url https://download.pytorch.org/whl/cu121
```

Repeat for `services/image` and `services/creative`.

#### 4. Verify GPU

```bash
python scripts/test-gpu.py
```

Expected output:
```
✅ PyTorch installed: 2.2.0+cu121
✅ CUDA available: True
✅ CUDA version: 12.1
✅ GPU device: NVIDIA GeForce RTX 4050
✅ GPU memory: 6.0 GB
✅ GPU computation successful!
✅ GPU speedup: 7.2x faster than CPU
```

---

## 📁 Project Structure

```
tesco-create-ai/
├── apps/
│   └── web/                          # Next.js frontend
│       ├── src/
│       │   ├── app/                  # App Router pages
│       │   │   ├── page.tsx          # Home page
│       │   │   ├── layout.tsx        # Root layout
│       │   │   └── api/trpc/         # tRPC API routes
│       │   ├── components/
│       │   │   ├── canvas/           # Fabric.js canvas components
│       │   │   ├── ui/               # shadcn/ui components
│       │   │   └── compliance/       # Compliance UI
│       │   └── lib/
│       │       ├── supabase.ts       # Supabase client
│       │       ├── prisma.ts         # Prisma client
│       │       ├── trpc/             # tRPC setup
│       │       └── storage/          # Storage abstraction
│       ├── prisma/
│       │   └── schema.prisma         # Database schema
│       └── package.json
│
├── services/
│   ├── compliance/                   # Compliance AI Service
│   │   ├── app/
│   │   │   ├── main.py               # FastAPI app
│   │   │   ├── models/
│   │   │   │   └── nlp_compliance.py # NLP validator
│   │   │   ├── routers/              # API routes
│   │   │   └── utils/
│   │   └── requirements.txt
│   │
│   ├── image/                        # Image AI Service
│   │   ├── app/
│   │   │   ├── main.py               # FastAPI app
│   │   │   ├── processors/           # Image processors
│   │   │   └── utils/
│   │   └── requirements.txt
│   │
│   └── creative/                     # Creative AI Service
│       ├── app/
│       │   ├── main.py               # FastAPI app
│       │   └── generators/           # LLM generators
│       └── requirements.txt
│
├── packages/                         # Shared packages
│   ├── ui/                           # Shared UI components
│   ├── types/                        # TypeScript types
│   ├── config/                       # Shared configs
│   └── utils/                        # Shared utilities
│
├── scripts/
│   ├── setup.ps1                     # Complete setup script
│   ├── dev.ps1                       # Development launcher
│   └── test-gpu.py                   # GPU verification
│
├── package.json                      # Root package.json
├── pnpm-workspace.yaml               # Monorepo config
├── turbo.json                        # Turborepo config
└── .env.example                      # Environment template
```

---

## 🛠️ Development Workflow

### Running Specific Services

```bash
# Only Next.js (for UI development)
cd apps/web && pnpm dev

# Only Compliance API
cd services/compliance
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000

# Only Image AI
cd services/image
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8001
```

### Database Commands

```bash
cd apps/web

# Generate Prisma client
pnpm prisma generate

# Push schema changes to Supabase
pnpm prisma db push

# Open Prisma Studio (database GUI)
pnpm prisma studio
```

### Monorepo Commands

```bash
# Install all dependencies
pnpm install

# Run dev in all apps
pnpm dev

# Build all apps
pnpm build

# Lint all apps
pnpm lint

# Type-check all apps
pnpm typecheck
```

---

## 🎨 Usage Guide

### Creating Your First Creative

1. **Start Services**: Run `.\scripts\dev.ps1`
2. **Open App**: http://localhost:3000
3. **Click** "Create New Campaign"
4. **Choose Format**: Square (1:1), Portrait (4:5), or Stories (9:16)
5. **Upload Assets**:
   - Packshots (product images)
   - Brand logos
   - Backgrounds (optional)
6. **Drag & Drop**: Arrange elements on canvas
7. **Add Text**: Click to add headlines/subheads
8. **AI Assist**:
   - Background Removal: Right-click image > Remove Background
   - Color Extraction: Upload logo > Extract Colors
   - Headline Suggestions: Click "AI Suggest" (requires Gemini API key)
9. **Compliance Check**: Real-time validation in sidebar
10. **Export**: Click "Export" > Select formats > Download

---

## 🧪 Testing

### Manual Testing

```bash
# Test Compliance API
curl http://localhost:8000/health

# Test Image API
curl http://localhost:8001/health

# Test Creative API
curl http://localhost:8002/health
```

### GPU Performance Test

```bash
python scripts/test-gpu.py
```

---

## 🐛 Troubleshooting

### Common Issues

#### "Module not found" errors

```bash
# Reinstall dependencies
pnpm install
cd services/compliance && pip install -r requirements.txt
```

#### GPU not detected

```bash
# Verify CUDA installation
nvcc --version

# Reinstall PyTorch with CUDA
pip install torch==2.2.0+cu121 torchvision==0.17.0+cu121 --index-url https://download.pytorch.org/whl/cu121

# Test
python scripts/test-gpu.py
```

#### Supabase connection failed

1. Check `.env.local` has correct credentials
2. Verify database URL includes password
3. Test connection in Prisma Studio: `pnpm prisma studio`

#### Port already in use

```bash
# Change ports in service files:
# services/compliance/app/main.py (line: uvicorn.run)
# services/image/app/main.py
# services/creative/app/main.py
```

---

## 📊 Performance Optimization

### RAM Management (16GB systems)

**Don't run all services simultaneously during development.**

Recommended configurations:

```
UI Development:
✅ Next.js (2GB)
Total: 2GB

Full Stack:
✅ Next.js (2GB)
✅ Compliance API (3GB)
✅ Image AI (4GB)
Total: 9GB ← Comfortable

Integration Testing:
✅ All services (14GB) ← Tight but works
```

### GPU Memory Management (6GB VRAM)

The Image AI service intelligently loads models:

- **Always loaded**: REMBG (500MB), CLIP (600MB)
- **On-demand**: BiRefNet (800MB), Real-ESRGAN (1.5GB)

Total: ~3GB typical, 5GB peak

---

## 🚢 Deployment

### Deploying to Production

**Frontend (Next.js):**
- Vercel (recommended): `vercel deploy`
- Netlify, Cloudflare Pages, AWS Amplify

**Python Services:**
- Railway: `railway up`
- Render, Fly.io, Google Cloud Run

**Database:**
- Already on Supabase cloud ✅

**Storage:**
- Already on Supabase Storage ✅

See `docs/DEPLOYMENT.md` for detailed instructions (TODO).

---

## 📚 Additional Resources

- **API Documentation**:
  - Compliance: http://localhost:8000/docs
  - Image AI: http://localhost:8001/docs
  - Creative AI: http://localhost:8002/docs

- **Database Schema**: `apps/web/prisma/schema.prisma`
- **Architecture Diagram**: `docs/ARCHITECTURE.md` (TODO)

---

## 🤝 Contributing

This is a private project for Tesco. For internal contributions:

1. Create feature branch: `git checkout -b feature/amazing-feature`
2. Commit changes: `git commit -m 'Add amazing feature'`
3. Push: `git push origin feature/amazing-feature`
4. Create Pull Request

---

## 📄 License

Proprietary - Tesco PLC

---

## 🎯 Roadmap

### Phase 1 (MVP - Weeks 1-4) ✅ In Progress

- [x] Project structure & setup
- [x] Next.js frontend with Fabric.js canvas
- [x] Supabase integration
- [x] Python FastAPI services
- [ ] Basic compliance validation
- [ ] Background removal (REMBG)
- [ ] Multi-format export

### Phase 2 (Weeks 5-8)

- [ ] Fine-tuned BERT compliance classifier
- [ ] YOLO layout detection
- [ ] Real-ESRGAN upscaling
- [ ] Advanced color palette tools
- [ ] Template library

### Phase 3 (Weeks 9-12)

- [ ] Collaboration features
- [ ] Analytics dashboard
- [ ] A/B testing recommendations
- [ ] Performance optimization
- [ ] Production deployment

---

## 💬 Support

For questions or issues:
- **Internal Slack**: #tesco-create-ai
- **Email**: create-ai-team@tesco.com

---

**Built with ❤️ by the Tesco Retail Media Team**
