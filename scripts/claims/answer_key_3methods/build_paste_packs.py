"""One plain-text paste pack per text: explanation (reference packet section 1) + claim sheet + G file, verbatim."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKT = Path("./grounding_judge_pilot/reference_packets")
for f in sorted(HERE.glob("claims_*.csv")):
    tid = f.stem[len("claims_"):]
    md = (PKT / f"{tid}.md").read_text(encoding="utf-8")
    sec = md.split("## 1. Explanation (full text)", 1)[1].split("\n## 2.", 1)[0]
    m = re.search(r"~~~~~~text\n(.*?)\n~~~~~~", sec, re.S)
    assert m, tid
    parts = [f"=== 1. EXPLANATION (reference_packets/{tid}.md, section 1) ===", m.group(1),
             f"=== 2. CLAIM SHEET (claims_{tid}.csv) ===", f.read_text(encoding="utf-8").rstrip("\n"),
             f"=== 3. G FILE (G_{tid}.csv) ===", (HERE / f"G_{tid}.csv").read_text(encoding="utf-8").rstrip("\n")]
    (HERE / "paste_packs" / f"{tid}.txt").write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(tid)
