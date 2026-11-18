"""Gộp các trang trong src/ thành một index.html có tab.

Mỗi trang nguồn được nhúng nguyên vẹn vào một <iframe srcdoc>, nên CSS và JS
của hai trang không đụng nhau. Chạy:  python build.py
"""
import html
from pathlib import Path

ROOT = Path(__file__).parent
TABS = [
    ("danh-gia", "Đánh giá đầu tư", "src/danh-gia.html"),
    ("khac-biet", "Khác biệt ba phiên bản", "src/khac-biet.html"),
]

# Trong iframe srcdoc, link "#c1" được hiểu theo URL trang ngoài, nên bấm vào sẽ
# tải cả trang ngoài vào trong tab. Chặn lại và tự cuộn tới mục đó.
ANCHOR_FIX = """<script>
document.addEventListener('click',e=>{
  const a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a)return;
  e.preventDefault();
  const t=document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
  if(t)t.scrollIntoView();else scrollTo(0,0);
});
</script>
</body>"""


def page(src):
    text = (ROOT / src).read_text(encoding="utf-8")
    assert text.count("</body>") == 1, src
    return html.escape(text.replace("</body>", ANCHOR_FIX), quote=True)


buttons = "".join(
    f'<button role="tab" id="t-{k}" data-tab="{k}" aria-controls="p-{k}" aria-selected="false">{label}</button>'
    for k, label, _ in TABS
)
frames = "\n".join(
    f'<iframe role="tabpanel" id="p-{k}" data-tab="{k}" aria-labelledby="t-{k}" title="{label}" '
    f'srcdoc="{page(src)}"></iframe>'
    for k, label, src in TABS
)

PAGE = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>FPT Play × Tetrate Enterprise Gateway</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@500;600&display=swap" rel="stylesheet">
<style>
:root{{--bar:48px;--top:env(safe-area-inset-top,0px);color-scheme:light}}
html,body{{margin:0;height:100%;overflow:hidden;background:#F5F6F8}}
.tabs{{position:fixed;inset:0 0 auto;height:calc(var(--bar) + var(--top));padding:var(--top) 16px 0;display:flex;align-items:stretch;justify-content:center;gap:4px;background:#0F1B2D;z-index:2;overflow-x:auto}}
.tabs button{{font:600 14px/1 "Be Vietnam Pro",ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#A9B4C8;background:none;border:0;border-bottom:3px solid transparent;border-top:3px solid transparent;padding:0 18px;cursor:pointer;white-space:nowrap;transition:color .2s,border-color .2s}}
.tabs button:hover{{color:#fff}}
.tabs button[aria-selected=true]{{color:#fff;border-bottom-color:#E4501B}}
.tabs button:focus-visible{{outline:2px solid #fff;outline-offset:-4px;border-radius:6px}}
iframe{{position:fixed;left:0;top:calc(var(--bar) + var(--top));width:100%;height:calc(100% - var(--bar) - var(--top));border:0;visibility:hidden}}
iframe.on{{visibility:visible}}
</style>
</head>
<body>
<div class="tabs" role="tablist" aria-label="Nội dung">{buttons}</div>
{frames}
<script>
const tabs=[...document.querySelectorAll('.tabs button')],frames=[...document.querySelectorAll('iframe')];
function show(k,push){{
  if(!tabs.some(t=>t.dataset.tab===k))k=tabs[0].dataset.tab;
  tabs.forEach(t=>t.setAttribute('aria-selected',t.dataset.tab===k));
  frames.forEach(f=>f.classList.toggle('on',f.dataset.tab===k));
  if(push)history.replaceState(null,'','#'+k);
}}
tabs.forEach((t,i)=>{{
  t.addEventListener('click',()=>show(t.dataset.tab,true));
  t.addEventListener('keydown',e=>{{
    const d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(!d)return;
    const n=tabs[(i+d+tabs.length)%tabs.length];n.focus();show(n.dataset.tab,true);
  }});
}});
addEventListener('hashchange',()=>show(location.hash.slice(1)));
show(location.hash.slice(1));
</script>
</body>
</html>
"""

(ROOT / "index.html").write_text(PAGE, encoding="utf-8", newline="\n")
(ROOT / "khac-biet.html").write_text(
    '<!DOCTYPE html><meta charset="utf-8"><title>Đã chuyển</title>'
    '<meta http-equiv="refresh" content="0;url=./#khac-biet">'
    '<a href="./#khac-biet">Trang này đã gộp vào trang chính</a>\n',
    encoding="utf-8", newline="\n",
)
print("built index.html", (ROOT / "index.html").stat().st_size, "bytes")
