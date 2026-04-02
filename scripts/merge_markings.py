"""
merge_markings.py — Steve 마킹 병합 스크립트 (Marking Merge Script)

기능: 동기화된 새 본문에 Steve의 기존 마킹(Level 3)을 자동 재부착
식별자: ***, <mark>, (Steve: ...)

사용법 (Usage):
    python scripts/merge_markings.py
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs" / "antigravity"

# Steve 마킹 패턴 정의 (Steve's marking patterns)
MARKING_PATTERNS = {
    "bold_italic": re.compile(r"\*\*\*(.+?)\*\*\*"),        # ***text***
    "highlight": re.compile(r"<mark>(.+?)</mark>"),          # <mark>text</mark>
    "note": re.compile(r"\(Steve:\s*(.+?)\)"),               # (Steve: text)
}


def extract_markings(content: str) -> list:
    """
    문서에서 Steve 마킹을 추출 (Extract Steve's markings from document)
    
    Returns:
        list of dict: [{"type": "bold_italic", "text": "...", "anchor": "heading-id"}, ...]
    """
    markings = []
    lines = content.split("\n")
    current_heading = None
    
    for line in lines:
        # 현재 헤딩 추적 (Track current heading for anchor)
        heading_match = re.match(r"^(#{1,6})\s+(.+)", line)
        if heading_match:
            heading_text = heading_match.group(2).strip()
            # 헤딩 ID 생성 (Generate heading ID)
            current_heading = re.sub(r"[^\w\s-]", "", heading_text.lower())
            current_heading = re.sub(r"[\s]+", "-", current_heading).strip("-")
        
        # 마킹 추출 (Extract markings)
        for mark_type, pattern in MARKING_PATTERNS.items():
            for match in pattern.finditer(line):
                markings.append({
                    "type": mark_type,
                    "full_match": match.group(0),
                    "text": match.group(1),
                    "anchor": current_heading,
                    "line": line.strip(),
                })
    
    return markings


def reattach_markings(new_content: str, markings: list) -> str:
    """
    새 본문에 마킹을 재부착 (Reattach markings to new content)
    
    앵커(Heading ID)를 기준으로 적절한 위치에 마킹을 재배치합니다.
    
    TODO: 실제 병합 알고리즘 구현
    - 앵커 매칭으로 섹션 위치 파악
    - 유사도 검사로 정확한 라인 매칭
    - 대규모 변경 시 [Review Needed] 처리
    """
    print(f"[MERGE] {len(markings)} 마킹 감지됨")
    
    # Placeholder — 추후 실제 병합 로직 구현
    for marking in markings:
        print(f"  [{marking['type']}] anchor={marking['anchor']}: {marking['text'][:30]}...")
    
    return new_content


def check_review_needed(old_content: str, new_content: str, threshold: float = 0.3) -> bool:
    """
    변경량이 임계값을 초과하는지 확인 (Check if changes exceed threshold)
    
    Returns:
        bool: True if review is needed
    """
    if not old_content or not new_content:
        return False
    
    old_lines = set(old_content.strip().split("\n"))
    new_lines = set(new_content.strip().split("\n"))
    
    if not old_lines:
        return False
    
    changed = len(old_lines.symmetric_difference(new_lines))
    total = len(old_lines.union(new_lines))
    change_ratio = changed / total if total > 0 else 0
    
    print(f"[REVIEW] 변경 비율: {change_ratio:.1%} (임계값: {threshold:.0%})")
    return change_ratio > threshold


def main():
    """메인 병합 실행 (Main merge execution)"""
    print("=" * 60)
    print("Anti-gravity Marking Merge — 마킹 병합 시작")
    print("=" * 60)
    
    if not DOCS_DIR.exists():
        print("[SKIP] 문서 디렉토리 없음")
        return
    
    for md_file in DOCS_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        markings = extract_markings(content)
        
        if markings:
            print(f"\n[FILE] {md_file.name}")
            for m in markings:
                print(f"  [{m['type']}] {m['full_match'][:50]}...")
        else:
            print(f"[FILE] {md_file.name} — 마킹 없음")
    
    print("\n" + "=" * 60)
    print("병합 완료 (Merge complete)")
    print("=" * 60)


if __name__ == "__main__":
    main()
