# 📝 변경 로그 (Changelog)
> **문서 ID:** CHANGELOG-1.004  
> **최종 수정(Last Modified):** 2026-04-03  

---

## [v0.1.0] — 2026-04-03 (초안 배포 / Initial Deployment)

### ✅ Phase 0: 프로젝트 초기화 (Completed)
- [08:00] 프로젝트 시작. GitHub CLI(`gh`) 설치 완료.
- [08:01] `docs/SPEC.md` — 통합 명세서 생성.
- [08:02] `docs/PLAN.md` — 실행 계획서 생성.
- [08:03] `docs/TODO.md`, `docs/TEST_PLAN.md`, `docs/CHANGELOG.md` 생성.
- [08:06] MkDocs 프로젝트 파일 일괄 생성:
  - `mkdocs.yml` — Material Theme 다크모드 설정
  - `docs/index.md` — 랜딩 페이지
  - `docs/getting-started.md` — 시작 가이드
  - `docs/antigravity/home.md` — 샘플 동기화 문서 (Steve 마킹 포함)
  - `.github/workflows/deploy.yml` — 배포 워크플로우
  - `.github/workflows/sync-docs.yml` — 동기화 워크플로우
  - `overrides/main.html` — 보안 게이트 템플릿
  - `overrides/assets/stylesheets/custom.css` — 커스텀 스타일
  - `scripts/sync_docs.py` — 동기화 스크립트 (스켈레톤)
  - `scripts/merge_markings.py` — 마킹 병합 스크립트
  - `requirements.txt`, `README.md`, `.gitignore`

### ✅ Phase 1: 코어 사이트 구축 (Completed)
- [08:10] `pip install mkdocs-material mkdocs-minify-plugin` 완료.
- [08:11] `mkdocs build` 정상 동작 확인.
- [08:12] 보안 게이트(비밀번호 입력) UI 구현 완료.
- [08:13] Steve 마킹 스타일 (Level 2/3, Highlight, Note) CSS 적용.

### ✅ Phase 2: GitHub Actions & 배포 (Completed)
- [08:13] `gh auth login` — GitHub 인증 완료 (`krjoylee` 계정).
- [08:14] `gh repo create mydoc --public` — 리포지토리 생성.
- [08:14] `git push -u origin main` — 메인 브랜치 push 완료.
- [08:15] `mkdocs gh-deploy --force` — GitHub Pages 배포 완료.
- [08:16] 사이트 접근 확인: https://krjoylee.github.io/mydoc/
- [08:18] `pymdownx.emoji` 확장 추가 — 아이콘 렌더링 수정.

### 🔧 수정 사항 (Fixes)
- `mkdocs.yml` YAML 파싱 에러 수정 (`fence_mermaid` → `fence_code_format`)
- GitHub 사용자명 `joy` → `krjoylee` 업데이트
- Emoji 확장 누락으로 인한 아이콘 미렌더링 수정

---

> **End of Document — CHANGELOG-1.004**
