const postcss = require("postcss");
const fs = require("fs");
const autoprefixer = require("autoprefixer");
const pxtorem = require("postcss-pxtorem");
const cssnano = require("cssnano");

// Read input CSS file
const inputCSS = fs.readFileSync("todo_list/static/css/style.css", "utf8");

// Process CSS with PostCSS
postcss([
  autoprefixer(),
  pxtorem({ rootValue: 16, propList: ["*"] }),
  cssnano({ preset: "default" })
])
  .process(inputCSS, { from: "todo_list/static/css/style.css", to: "todo_list/static/css/style.min.css" })
  .then((result) => {
    fs.writeFileSync("todo_list/static/css/style.min.css", result.css);
    console.log("✅ CSS processed and minified: todo_list/static/css/style.min.css");
  })
  .catch((error) => console.error("❌ Error processing CSS:", error));
