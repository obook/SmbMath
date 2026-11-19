# Usage : python3 tools/icons.py
# Génère le jeu d'icônes SmbMath : grille 24x24, traits bordeaux, cases or.
import os, subprocess
N, R = "#7B2D26", "#A98435"
def p(d, c=N, w=2): return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def box(x, y, w, h): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="none" stroke="{R}" stroke-width="1.8"/>'
def dot(x, y, r=1.4, c=N): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
A_HI = p("M2 17 L7.5 3 L13 17 M4.2 12 H10.8")
A_LO = p("M2 21 L7.5 7 L13 21 M4.2 16 H10.8")
ICONS = {
 "fraction": box(7, 2, 10, 7) + p("M3 12 H21") + box(7, 15, 10, 7),
 "formulaire": box(2.5, 3, 5, 5) + p("M11 5.5 H21.5") + box(2.5, 9.5, 5, 5) + p("M11 12 H21.5")
   + box(2.5, 16, 5, 5) + p("M11 18.5 H21.5"),
 "squareroot": p("M2 13 L5 11.5 L8.5 20 L12.5 4 H22") + box(13.5, 7.5, 7.5, 10.5),
 "expression": A_HI.replace("17", "18") + p("M14 9 H18 M14 14 H18") + box(19, 6, 4.5, 11),
 "vector": p("M3 6 H20 M16.5 2.5 L20 6 L16.5 9.5") + box(3, 12, 18, 9),
 "vector-coordinates": p("M1.5 6 H10 M7.5 3.5 L10 6 L7.5 8.5") + box(2, 11, 8, 8)
   + p("M15.5 3 Q12.5 12 15.5 21 M20.5 3 Q23.5 12 20.5 21") + dot(18, 8.5) + dot(18, 15.5),
 "angle": p("M3 9 L12 3.5 L21 9") + box(3, 12, 18, 9),
 "ensembles": p("M6 21 V3 H13 Q18.5 3 18.5 8 Q18.5 13 13 13 H6 M13 13 L19 21") + p("M9.5 3 V21", R, 1.6),
 "systeme": p("M9 2.5 Q6 2.5 6 5.5 V9.5 Q6 12 3.5 12 Q6 12 6 14.5 V18.5 Q6 21.5 9 21.5") + box(11, 4, 11, 6) + box(11, 14, 11, 6),
 "implication": p("M2 9 H16 M2 15 H16 M13 4.5 L20.5 12 L13 19.5"),
 "equivalence": p("M6 9 H18 M6 15 H18 M9 4.5 L1.5 12 L9 19.5 M15 4.5 L22.5 12 L15 19.5"),
 "exposant": A_LO + box(15, 2, 7, 7),
 "indice": A_HI + box(15, 15, 7, 7),
 "fonction": p("M17.5 4 Q14 1.5 12.5 6 L9.5 19 Q8.5 23 5 21.5 M7 10 H16.5"),
 "operations": p("M6 2.5 V9.5 M2.5 6 H9.5 M14.5 6 H21.5 M3 15 L9 21 M9 15 L3 21 M14.5 18 H21.5") + dot(18, 14.6, 1.2) + dot(18, 21.4, 1.2),
 "comparaison": p("M5 3.5 L19 9.5 L5 15.5 M5 20.5 H19"),
 "relation": p("M19 4.5 H12 Q4.5 4.5 4.5 12 Q4.5 19.5 12 19.5 H19 M4.5 12 H17"),
 "options": p("M3 6 H21 M3 12 H21 M3 18 H21") + dot(9, 6, 2.4, R) + dot(16, 12, 2.4, R) + dot(7, 18, 2.4, R),
 "about": p("M12 11 V17.5") + f'<circle cx="12" cy="12" r="9.5" fill="none" stroke="{N}" stroke-width="2"/>' + dot(12, 7.3, 1.4, R),
 "star": p("M18 3.5 H5.5 L12 12 L5.5 20.5 H18"),
 "bigoplus": p("M4.5 10 A8 8 0 0 1 19 7.5 M19 2.5 V7.5 H14") + p("M19.5 14 A8 8 0 0 1 5 16.5 M5 21.5 V16.5 H10", R),
}
# Pastille ivoire : garde les icônes lisibles en thème clair comme sombre.
OUT = os.path.join(os.path.dirname(__file__), "..", "src", "icons")
for name, body in ICONS.items():
    body = ('<rect x="0.5" y="0.5" width="23" height="23" rx="4" fill="#F7F3EA" stroke="#7B2D26" stroke-width="1"/>'
            f'<g transform="translate(12 12) scale(0.78) translate(-12 -12)">{body}</g>')
    with open(f"{OUT}/{name}.svg", "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">{body}</svg>\n')

# Les entrées de sous-menu n'acceptent que des bitmaps nommés <id>_16.bmp / <id>_26.bmp (contenu PNG accepté).
for size in (16, 26):
    subprocess.run(["inkscape", f"{OUT}/formulaire.svg", "-w", str(size), "-h", str(size),
                    "-o", f"{OUT}/formulaire_{size}.png"], check=True, capture_output=True)
    os.replace(f"{OUT}/formulaire_{size}.png", f"{OUT}/formulaire_{size}.bmp")
