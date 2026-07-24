const fs = require("fs");
const path = require("path");

const root = __dirname;
const dist = path.join(root, "dist");
const serverDir = path.join(dist, "server");

function copyFile(source, target) {
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.copyFileSync(source, target);
}

function copyDir(source, target) {
  if (!fs.existsSync(source)) return;
  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    const from = path.join(source, entry.name);
    const to = path.join(target, entry.name);
    if (entry.isDirectory()) {
      copyDir(from, to);
    } else {
      copyFile(from, to);
    }
  }
}

fs.rmSync(dist, { recursive: true, force: true });
fs.mkdirSync(dist, { recursive: true });

copyFile(path.join(root, "index.html"), path.join(dist, "index.html"));
copyDir(path.join(root, "data"), path.join(dist, "data"));
copyDir(path.join(root, "docs"), path.join(dist, "docs"));
copyDir(path.join(root, ".openai"), path.join(dist, ".openai"));

const assetFiles = [
  "index.html",
  "data/markets.json",
  "data/leaderboard.json",
  "data/whales.json",
  "data/history.json",
  "data/wallet-alpha.json",
  "docs/screenshot-desktop.png",
  "docs/screenshot-mobile.png",
  "docs/hames-labs-profile-logo.png",
];

const mimeTypes = {
  ".html": "text/html; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
};

const assets = {};
for (const file of assetFiles) {
  const absolute = path.join(root, file);
  if (!fs.existsSync(absolute)) continue;
  assets[`/${file}`] = {
    mime: mimeTypes[path.extname(file)] || "application/octet-stream",
    body: fs.readFileSync(absolute).toString("base64"),
  };
}
assets["/"] = assets["/index.html"];

fs.mkdirSync(serverDir, { recursive: true });
fs.writeFileSync(
  path.join(serverDir, "index.js"),
  `const ASSETS = ${JSON.stringify(assets)};\n\n` +
    `function decode(base64) {\n` +
    `  const binary = atob(base64);\n` +
    `  const bytes = new Uint8Array(binary.length);\n` +
    `  for (let index = 0; index < binary.length; index += 1) bytes[index] = binary.charCodeAt(index);\n` +
    `  return bytes;\n` +
    `}\n\n` +
    `export default {\n` +
    `  async fetch(request) {\n` +
    `    const url = new URL(request.url);\n` +
    `    const asset = ASSETS[url.pathname] || ASSETS["/index.html"];\n` +
    `    return new Response(decode(asset.body), {\n` +
    `      headers: {\n` +
    `        "content-type": asset.mime,\n` +
    `        "cache-control": "public, max-age=60"\n` +
    `      }\n` +
    `    });\n` +
    `  }\n` +
    `};\n`,
  "utf8",
);

console.log("Static preview built in dist/");
