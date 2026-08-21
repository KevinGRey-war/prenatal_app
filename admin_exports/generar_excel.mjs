import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";


const [inputPath, outputPath, previewPath] = process.argv.slice(2);

if (!inputPath || !outputPath) {
  throw new Error("Uso: generar_excel.mjs <datos.json> <salida.xlsx> [vista.png]");
}

const payload = JSON.parse(await fs.readFile(inputPath, "utf8"));
const workbook = Workbook.create();
const summarySheet = workbook.worksheets.add("Resumen");
const recordsSheet = workbook.worksheets.add("Registros");
const rankingSheet = workbook.worksheets.add("Ranking");

for (const sheet of [summarySheet, recordsSheet, rankingSheet]) {
  sheet.showGridLines = false;
}

const pink = "#EC4899";
const pinkSoft = "#FCE7F3";
const gold = "#C9A227";
const goldSoft = "#FFF7D6";
const ink = "#24324B";
const muted = "#697386";
const line = "#E8DFF0";
const white = "#FFFFFF";

const titleFormat = {
  fill: pink,
  font: { bold: true, color: white },
  verticalAlignment: "center",
};
const headerFormat = {
  fill: ink,
  font: { bold: true, color: white },
  verticalAlignment: "center",
  borders: { preset: "outside", style: "thin", color: ink },
};

// Referenced sheets are created before formulas are written.
const recordRows = payload.registros.map((row) => [
  row.posicion,
  row.usuario,
  row.puntaje,
  row.trimestre,
  row.fecha || "",
  row.origen,
]);
const rankingRows = payload.ranking.map((row) => [
  row.posicion,
  row.usuario,
  row.puntaje,
  row.trimestre,
  row.fecha || "",
]);

recordsSheet.mergeCells("A1:F1");
recordsSheet.getRange("A1:F1").values = [["Registro administrativo de participantes"]];
recordsSheet.getRange("A1:F1").format = titleFormat;
recordsSheet.getRange("A1:F1").format.rowHeight = 32;
recordsSheet.mergeCells("A2:F2");
recordsSheet.getRange("A2:F2").values = [[`Generado: ${payload.generado_en}`]];
recordsSheet.getRange("A2:F2").format = { font: { color: muted, italic: true } };
recordsSheet.getRange("A4:F4").values = [[
  "Posición",
  "Usuario",
  "Puntaje",
  "Trimestre",
  "Fecha y hora",
  "Origen",
]];
recordsSheet.getRange("A4:F4").format = headerFormat;

if (recordRows.length) {
  recordsSheet.getRangeByIndexes(4, 0, recordRows.length, 6).values = recordRows;
  const recordEnd = 4 + recordRows.length;
  recordsSheet.getRange(`A4:F${recordEnd}`).format.borders = {
    insideHorizontal: { style: "thin", color: line },
  };
  recordsSheet.getRange(`A5:A${recordEnd}`).format.numberFormat = "0";
  recordsSheet.getRange(`C5:C${recordEnd}`).format.numberFormat = '0 "pts"';
  recordsSheet.getRange(`C5:C${recordEnd}`).conditionalFormats.add("cellIs", {
    operator: "greaterThanOrEqual",
    formula: 80,
    format: { fill: goldSoft, font: { bold: true, color: "#6B4F00" } },
  });
  recordsSheet.getRange(`C5:C${recordEnd}`).conditionalFormats.add("cellIs", {
    operator: "between",
    formula: [60, 79],
    format: { fill: pinkSoft, font: { color: ink } },
  });
  recordsSheet.getRange(`C5:C${recordEnd}`).conditionalFormats.add("cellIs", {
    operator: "lessThan",
    formula: 60,
    format: { fill: "#FFF0F0", font: { color: "#8A1F1F" } },
  });
  const recordsTable = recordsSheet.tables.add(`A4:F${recordEnd}`, true, "RegistrosTable");
  recordsTable.style = "TableStyleMedium2";
}

recordsSheet.freezePanes.freezeRows(4);
recordsSheet.getRange(`A1:F${Math.max(4 + recordRows.length, 4)}`).format.verticalAlignment = "center";
recordsSheet.getRange("A:A").format.columnWidth = 11;
recordsSheet.getRange("B:B").format.columnWidth = 26;
recordsSheet.getRange("C:C").format.columnWidth = 13;
recordsSheet.getRange("D:D").format.columnWidth = 22;
recordsSheet.getRange("E:E").format.columnWidth = 20;
recordsSheet.getRange("F:F").format.columnWidth = 16;

rankingSheet.mergeCells("A1:E1");
rankingSheet.getRange("A1:E1").values = [["Ranking - mejor puntaje por participante"]];
rankingSheet.getRange("A1:E1").format = titleFormat;
rankingSheet.getRange("A1:E1").format.rowHeight = 32;
rankingSheet.getRange("A3:E3").values = [[
  "Posición",
  "Usuario",
  "Mejor puntaje",
  "Trimestre",
  "Fecha del resultado",
]];
rankingSheet.getRange("A3:E3").format = headerFormat;

if (rankingRows.length) {
  rankingSheet.getRangeByIndexes(3, 0, rankingRows.length, 5).values = rankingRows;
  const rankingEnd = 3 + rankingRows.length;
  rankingSheet.getRange(`A3:E${rankingEnd}`).format.borders = {
    insideHorizontal: { style: "thin", color: line },
  };
  rankingSheet.getRange(`A4:A${rankingEnd}`).format.numberFormat = "0";
  rankingSheet.getRange(`C4:C${rankingEnd}`).format.numberFormat = '0 "pts"';
  rankingSheet.getRange("A4:C4").format = {
    fill: goldSoft,
    font: { bold: true, color: "#6B4F00" },
  };
  const rankingTable = rankingSheet.tables.add(`A3:E${rankingEnd}`, true, "RankingTable");
  rankingTable.style = "TableStyleMedium2";
}

rankingSheet.freezePanes.freezeRows(3);
rankingSheet.getRange("A:A").format.columnWidth = 11;
rankingSheet.getRange("B:B").format.columnWidth = 27;
rankingSheet.getRange("C:C").format.columnWidth = 18;
rankingSheet.getRange("D:D").format.columnWidth = 22;
rankingSheet.getRange("E:E").format.columnWidth = 22;

summarySheet.mergeCells("A1:D1");
summarySheet.getRange("A1:D1").values = [["Resumen de registros y ranking"]];
summarySheet.getRange("A1:D1").format = titleFormat;
summarySheet.getRange("A1:D1").format.rowHeight = 34;
summarySheet.mergeCells("A2:D2");
summarySheet.getRange("A2:D2").values = [[`Generado: ${payload.generado_en}`]];
summarySheet.getRange("A2:D2").format = { font: { italic: true, color: muted } };
summarySheet.getRange("A4:B7").values = [
  ["Indicador", "Valor"],
  ["Registros filtrados", null],
  ["Usuarios únicos", null],
  ["Puntaje promedio", null],
];
summarySheet.getRange("A8:B8").values = [["Puntaje máximo", null]];
summarySheet.getRange("A4:B4").format = headerFormat;
summarySheet.getRange("A5:A8").format = {
  fill: pinkSoft,
  font: { bold: true, color: ink },
};

const recordsEnd = 4 + recordRows.length;
const rankingEnd = 3 + rankingRows.length;

if (recordRows.length) {
  summarySheet.getRange("B5").formulas = [[`=COUNTA('Registros'!B5:B${recordsEnd})`]];
  summarySheet.getRange("B7").formulas = [[`=AVERAGE('Registros'!C5:C${recordsEnd})`]];
  summarySheet.getRange("B8").formulas = [[`=MAX('Registros'!C5:C${recordsEnd})`]];
} else {
  summarySheet.getRange("B5:B8").values = [[0], [0], [0], [0]];
}

if (rankingRows.length) {
  summarySheet.getRange("B6").formulas = [[`=COUNTA('Ranking'!B4:B${rankingEnd})`]];
} else {
  summarySheet.getRange("B6").values = [[0]];
}

summarySheet.getRange("B5:B8").format = {
  fill: white,
  font: { bold: true, color: pink },
  horizontalAlignment: "right",
};
summarySheet.getRange("B5:B6").format.numberFormat = "0";
summarySheet.getRange("B7:B8").format.numberFormat = '0.0 "pts"';
summarySheet.getRange("A4:B8").format.borders = {
  preset: "outside",
  style: "thin",
  color: line,
};

summarySheet.getRange("A10:B10").values = [["Filtros aplicados", "Selección"]];
summarySheet.getRange("A10:B10").format = headerFormat;
summarySheet.getRange("A11:B13").values = [
  ["Usuario", payload.filtros.usuario],
  ["Trimestres", payload.filtros.trimestres],
  ["Puntaje", payload.filtros.puntaje],
];
summarySheet.getRange("A11:A13").format = { fill: goldSoft, font: { bold: true, color: "#6B4F00" } };
summarySheet.getRange("A15:D16").merge();
summarySheet.getRange("A15:D16").values = [[
  "Documento de uso administrativo. Proteja los datos de participantes y comparta el archivo únicamente con personal autorizado.",
]];
summarySheet.getRange("A15:D16").format = {
  fill: "#FFF9E8",
  font: { color: "#6B4F00", italic: true },
  wrapText: true,
  verticalAlignment: "center",
  borders: { preset: "outside", style: "thin", color: gold },
};
summarySheet.getRange("A:A").format.columnWidth = 24;
summarySheet.getRange("B:B").format.columnWidth = 36;
summarySheet.getRange("C:D").format.columnWidth = 14;

if (previewPath) {
  const preview = await workbook.render({
    sheetName: "Resumen",
    range: "A1:D16",
    scale: 1.5,
    format: "png",
  });
  await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
}

await fs.mkdir(path.dirname(outputPath), { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
