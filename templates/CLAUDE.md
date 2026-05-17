# CLAUDE.md - Next.js + SQLite Guidelines

## Project Overview
Next.js 14+ with SQLite (using Drizzle or Prisma) and Tailwind CSS. Focused on developer productivity and AI agent compatibility.

## Tech Stack
- **Framework:** Next.js (App Router)
- **Database:** SQLite (Better-SQLite3 or LibSQL)
- **ORM:** Drizzle ORM (preferred) or Prisma
- **Styling:** Tailwind CSS + Shadcn UI
- **Validation:** Zod

## Development Commands
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run linting checks
- `npx drizzle-kit generate` - Generate database migrations
- `npx drizzle-kit push` - Push schema changes to SQLite

## Database Pattern (Drizzle)
- Schema: `src/db/schema.ts`
- Client: `src/db/index.ts`
- Migrations: `drizzle/`

## Coding Standards
- **Components:** Use React Server Components by default. Add `'use client'` only when needed.
- **Data Fetching:** Use Server Actions for mutations. Fetch data directly in RSCs.
- **Naming:**
  - Components: PascalCase (`UserButton.tsx`)
  - Hooks: camelCase (`useAuth.ts`)
  - API Routes: `route.ts` inside folder
- **Errors:** Use `error.tsx` for route-level error boundaries.

## SQLite Constraints
- Keep the database file (`sqlite.db`) in the root or a dedicated `data/` folder.
- Always include the database file in `.gitignore`.
- Use WAL mode for better concurrency: `PRAGMA journal_mode = WAL;`.
