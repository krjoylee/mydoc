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
| ✅ | 테스트 계획서(TEST_PLAN.md) 작성 | `docs/TEST_PLAN.md` 생성 완료 |
| ✅ | 변경 로그(CHANGELOG.md) 작성 | `docs/CHANGELOG.md` 생성 완료 |
| ✅ | GitHub 로그인 | `gh auth login` (krjoylee) |
| ✅ | GitHub 리포지토리 생성 | `krjoylee/mydoc` (public) |
| ✅ | Git 초기화 & push | `main` 브랜치 push 완료 |
| ✅ | MkDocs Material 설치 | `pip install mkdocs-material` 완료 |
| ✅ | `.gitignore` 생성 | Python/Node/MkDocs 패턴 포함 |

## Phase 1: 코어 사이트 구축 (Core Site Build)

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ✅ | `mkdocs.yml` 설정 | Material Theme, 다크모드 구성 완료 |
| ✅ | `index.md` 랜딩 페이지 | 프로젝트 소개 & 퀵링크 완료 |
| ✅ | 커스텀 CSS 적용 | 보안 게이트, 마킹 스타일, 애니메이션 |
| ✅ | 커스텀 템플릿 (`main.html`) | 보안 게이트 JS 구현 완료 |
| ✅ | 샘플 문서 — `antigravity/home.md` | Steve 마킹 예시 포함 |
| ✅ | Emoji 확장 추가 | `:material-*:` 아이콘 렌더링 수정 |

## Phase 2: GitHub Actions CI/CD

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ✅ | `deploy.yml` 워크플로우 | push → gh-deploy 자동화 |
| ✅ | `sync-docs.yml` 워크플로우 | 크론/수동 트리거 설정 완료 |
| ✅ | GitHub Pages 활성화 | `gh-pages` 브랜치 자동 생성 |
| ✅ | 초기 배포 테스트 | https://krjoylee.github.io/mydoc/ 접근 확인 |

## Phase 3: 동기화 엔진 (Sync Engine) — 추후

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ⬜ | `sync_docs.py` 실제 크롤링 구현 | 스켈레톤 작성 완료, 로직 미구현 |
| ⬜ | `merge_markings.py` 병합 알고리즘 | 추출 로직 구현, 재부착 미구현 |
| ⬜ | 변경량 감지 로직 | Review Needed 라벨 |

## Phase 4: 라이브 에디터 (Live Editor) — 추후

| 상태 | 작업(Task) | 메모(Note) |
|---|---|---|
| ⬜ | 인라인 에디터 UI | 상/하 분할 |
| ⬜ | 실시간 렌더링 | 마크다운 → HTML |
| ⬜ | TOC 동기 스크롤 | 양측 동시 이동 |

---

> **End of Document — TODO-1.004**
