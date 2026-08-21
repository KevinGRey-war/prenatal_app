import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";


const [inputPath, outputDir] = process.argv.slice(2);

if (!inputPath || !outputDir) {
  throw new Error("Uso: verificar_excel.mjs <archivo.xlsx> <carpeta-vistas>");
}

await fs.mkdir(outputDir, { recursive: true });
const input = await FileBlob.load(inputPath);
const workbook = await SpreadsheetFile.importXlsx(input);

const summary = await workbook.inspect({
  kind: "workbook,sheet,table",
  maxChars: 8000,
  tableMaxRows: 8,
  tableMaxCols: 8,
  tableMaxCellChars: 100,
});
const formulas = await workbook.inspect({
  kind: "formula",
  sheetId: "Resumen",
  range: "A1:D16",
  maxChars: 4000,
  options: { maxResults: 30 },
});

await fs.writeFile(
  path.join(outputDir, "inspeccion_excel.json"),
  JSON.stringify({ summary, formulas }, null, 2),
  "utf8",
);

for (const sheetName of ["Resumen", "Registros", "Ranking"]) {
  const image = await workbook.render({
    sheetName,
    autoCrop: "all",
    scale: 1.5,
    format: "png",
  });
  const safeName = sheetName.toLocaleLowerCase("es");
  await fs.writeFile(
    path.join(outputDir, `excel_${safeName}.png`),
    new Uint8Array(await image.arrayBuffer()),
  );
}

console.log(JSON.stringify({ inputPath, outputDir, status: "ok" }));
