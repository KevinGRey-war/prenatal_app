"""Genera el reporte PDF administrativo desde un payload JSON."""

import json
import sys
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


if len(sys.argv) != 3:
    raise SystemExit("Uso: generar_pdf.py <datos.json> <salida.pdf>")

entrada = Path(sys.argv[1])
salida = Path(sys.argv[2])
payload = json.loads(entrada.read_text(encoding="utf-8"))

PINK = colors.HexColor("#EC4899")
PINK_SOFT = colors.HexColor("#FCE7F3")
GOLD = colors.HexColor("#C9A227")
GOLD_SOFT = colors.HexColor("#FFF7D6")
INK = colors.HexColor("#24324B")
MUTED = colors.HexColor("#697386")
LINE = colors.HexColor("#E8DFF0")
WHITE = colors.white

styles = getSampleStyleSheet()
titulo = ParagraphStyle(
    "Titulo",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=24,
    textColor=INK,
    alignment=TA_LEFT,
    spaceAfter=4 * mm,
)
subtitulo = ParagraphStyle(
    "Subtitulo",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=13,
    leading=16,
    textColor=INK,
    spaceBefore=3 * mm,
    spaceAfter=3 * mm,
)
cuerpo = ParagraphStyle(
    "Cuerpo",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=11,
    textColor=INK,
)
pequeno = ParagraphStyle(
    "Pequeno",
    parent=cuerpo,
    fontSize=7.5,
    leading=9,
)
centrado = ParagraphStyle(
    "Centrado",
    parent=pequeno,
    alignment=TA_CENTER,
)
blanco = ParagraphStyle(
    "Blanco",
    parent=centrado,
    textColor=WHITE,
    fontName="Helvetica-Bold",
)


def texto(valor, estilo=pequeno):
    contenido = "" if valor is None else valor
    return Paragraph(escape(str(contenido)), estilo)


def encabezado_pie(canvas, documento):
    canvas.saveState()
    ancho, alto = landscape(A4)
    canvas.setStrokeColor(LINE)
    canvas.line(15 * mm, alto - 13 * mm, ancho - 15 * mm, alto - 13 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(15 * mm, alto - 10 * mm, "Vida Nueva - Reporte administrativo")
    canvas.drawRightString(ancho - 15 * mm, 9 * mm, f"Página {documento.page}")
    canvas.drawString(15 * mm, 9 * mm, "Uso exclusivo de personal autorizado")
    canvas.restoreState()


salida.parent.mkdir(parents=True, exist_ok=True)
documento = SimpleDocTemplate(
    str(salida),
    pagesize=landscape(A4),
    rightMargin=15 * mm,
    leftMargin=15 * mm,
    topMargin=18 * mm,
    bottomMargin=16 * mm,
    title="Registro de usuarios y ranking",
    author="Vida Nueva",
)

historia = [
    Paragraph("Registro de usuarios y ranking", titulo),
    Paragraph(
        f"Generado: {escape(payload['generado_en'])}",
        ParagraphStyle("Fecha", parent=cuerpo, textColor=MUTED),
    ),
    Spacer(1, 4 * mm),
]

resumen = payload["resumen"]
tarjetas = Table(
    [
        [
            texto("REGISTROS", blanco),
            texto("USUARIOS", blanco),
            texto("PROMEDIO", blanco),
            texto("MÁXIMO", blanco),
        ],
        [
            texto(resumen["total_registros"], centrado),
            texto(resumen["usuarios_unicos"], centrado),
            texto(f"{resumen['puntaje_promedio']:.1f} pts", centrado),
            texto(f"{resumen['puntaje_maximo']} pts", centrado),
        ],
    ],
    colWidths=[62 * mm] * 4,
    rowHeights=[9 * mm, 13 * mm],
)
tarjetas.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), INK),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("BACKGROUND", (0, 1), (-1, 1), PINK_SOFT),
            ("TEXTCOLOR", (0, 1), (-1, 1), PINK),
            ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 1), (-1, 1), 14),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 0.7, LINE),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
        ]
    )
)
historia.extend([tarjetas, Spacer(1, 5 * mm)])

filtros = payload["filtros"]
tabla_filtros = Table(
    [
        [texto("Filtros aplicados", blanco), texto("Selección", blanco)],
        [texto("Usuario"), texto(filtros["usuario"])],
        [texto("Trimestres"), texto(filtros["trimestres"])],
        [texto("Puntaje"), texto(filtros["puntaje"])],
    ],
    colWidths=[42 * mm, 205 * mm],
)
tabla_filtros.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), INK),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("BACKGROUND", (0, 1), (0, -1), GOLD_SOFT),
            ("BOX", (0, 0), (-1, -1), 0.6, LINE),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
    )
)
historia.extend([tabla_filtros, Spacer(1, 4 * mm)])

historia.append(Paragraph("Ranking - mejor puntaje por participante", subtitulo))
ranking_data = [
    [
        texto("Pos.", blanco),
        texto("Usuario", blanco),
        texto("Puntaje", blanco),
        texto("Trimestre", blanco),
        texto("Fecha", blanco),
    ]
]

for fila in payload["ranking"]:
    ranking_data.append(
        [
            texto(fila["posicion"], centrado),
            texto(fila["usuario"]),
            texto(f"{fila['puntaje']} pts", centrado),
            texto(fila["trimestre"]),
            texto(fila["fecha"], centrado),
        ]
    )

tabla_ranking = Table(
    ranking_data,
    repeatRows=1,
    colWidths=[18 * mm, 75 * mm, 28 * mm, 55 * mm, 52 * mm],
)
estilo_ranking = [
    ("BACKGROUND", (0, 0), (-1, 0), PINK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]

if len(ranking_data) > 1:
    estilo_ranking.append(("BACKGROUND", (0, 1), (-1, 1), GOLD_SOFT))

tabla_ranking.setStyle(TableStyle(estilo_ranking))
historia.extend([tabla_ranking, PageBreak()])

historia.append(Paragraph("Todos los registros filtrados", subtitulo))
registros_data = [
    [
        texto("Pos.", blanco),
        texto("Usuario", blanco),
        texto("Puntaje", blanco),
        texto("Trimestre", blanco),
        texto("Fecha", blanco),
        texto("Origen", blanco),
    ]
]

for fila in payload["registros"]:
    registros_data.append(
        [
            texto(fila["posicion"], centrado),
            texto(fila["usuario"]),
            texto(f"{fila['puntaje']} pts", centrado),
            texto(fila["trimestre"]),
            texto(fila["fecha"], centrado),
            texto(fila["origen"], centrado),
        ]
    )

tabla_registros = Table(
    registros_data,
    repeatRows=1,
    colWidths=[16 * mm, 62 * mm, 25 * mm, 50 * mm, 49 * mm, 35 * mm],
)
estilo_registros = [
    ("BACKGROUND", (0, 0), (-1, 0), INK),
    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, colors.HexColor("#FCFAFD")]),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]
tabla_registros.setStyle(TableStyle(estilo_registros))
historia.extend(
    [
        tabla_registros,
        Spacer(1, 5 * mm),
        KeepTogether(
            Paragraph(
                "Documento de uso administrativo. Proteja los datos personales y comparta este reporte únicamente con personal autorizado.",
                ParagraphStyle(
                    "Privacidad",
                    parent=cuerpo,
                    backColor=GOLD_SOFT,
                    borderColor=GOLD,
                    borderWidth=0.6,
                    borderPadding=7,
                    textColor=colors.HexColor("#6B4F00"),
                ),
            )
        ),
    ]
)

documento.build(
    historia,
    onFirstPage=encabezado_pie,
    onLaterPages=encabezado_pie,
)
