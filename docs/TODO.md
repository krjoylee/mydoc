# ✅ TODO — 진행 체크리스트 (Progress Tracker)
> **문서 ID:** TODO-1.004  
> **최종 수정(Last Modified):** 2026-04-03  

---

## 범례 (Legend)
- ✅ 완료(Done)
- 🔄 진행중(In Progress)
- ⬜ 미착수(Not Started)
- ❌ 차단(Blocked)

---

## Phase 0: 프로젝트 초기화 (Initialization)

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ✅ | GitHub CLI 설치 | `winget install GitHub.cli` 완료 |
| ✅ | 명세서(SPEC.md) 작성 | `docs/SPEC.md` 생성 완료 |
| ✅ | 실행계획서(PLAN.md) 작성 | `docs/PLAN.md` 생성 완료 |
| ✅ | TODO 체크리스트 작성 | 이 문서 |
| 🔄 | GitHub 리포지토리 생성 | `gh repo create` 진행 중 |
| 🔄 | Git 초기화 & 리모트 연결 | `git init` 진행 중 |
| ⬜ | MkDocs Material 설치 | `pip install` 필요 |
| ⬜ | `.gitignore` 생성 | Python/Node 패턴 |

## Phase 1: 코어 사이트 구축 (Core Site Build)

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ⬜ | `mkdocs.yml` 설정 | Material Theme 구성 |
| ⬜ | `index.md` 랜딩 페이지 | 프로젝트 소개 작성 |
| ⬜ | 커스텀 CSS 적용 | 마킹 스타일, 레이아웃 |
| ⬜ | 커스텀 템플릿 (`main.html`) | 보안 게이트 JS |
| ⬜ | 샘플 문서 — `antigravity/home.md` | Steve 마킹 예시 포함 |

## Phase 2: GitHub Actions CI/CD

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ⬜ | `deploy.yml` 워크플로우 | push → gh-deploy |
| ⬜ | `sync-docs.yml` 워크플로우 | 크론/수동 트리거 |
| ⬜ | GitHub Pages 활성화 | gh-pages 브랜치 |
| ⬜ | 초기 배포 테스트 | URL 접근 확인 |

## Phase 3: 동기화 엔진 (Sync Engine) — 추후

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ⬜ | `sync_docs.py` 구현 | 크롤링 & 번역 |
| ⬜ | `merge_markings.py` 구현 | 마킹 보존 알고리즘 |
| ⬜ | 변경량 감지 로직 | Review Needed 라벨 |

## Phase 4: 라이브 에디터 (Live Editor) — 추후

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ⬜ | 인라인 에디터 UI | 상/하 분할 |
| ⬜ | 실시간 렌더링 | 마크다운 → HTML |
| ⬜ | TOC 동기 스크롤 | 양측 동시 이동 |

---

> **End of Document — TODO-1.004**
