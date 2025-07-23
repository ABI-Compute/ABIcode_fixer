# 🛠 Code_fixer

Code_fixer is an AI-powered command-line tool that automatically **detects**, **explains**, or **fixes bugs** in your code using [Aider](https://github.com/paulgb/aider). It's language-aware, fast to use, and designed to work across entire project folders — including subdirectories.

---

## 🚀 Features

- 🔍 **Detects programming language** automatically  
- 🛠 **Fixes bugs** across all files in a project (default mode)  
- 💡 **Explains bugs** without modifying code (`--explain`)  
- 👁️ **Review mode** lets you approve fixes before applying them  
- 🗣️ **Custom prompt** support for advanced use cases  
- 📁 **Recursive file scanning** across subfolders  

---

## 📦 Installation

1. Go to: (https://github.com/ABI-Compute/ABIcode_fixer/releases)
2. Download the zip file
3. Extract it to a suitable location
4. Add its folder to your system's PATH
5. Then in your folder that you extracted execute:
```bash
setup.bat
```

*Note: ABIcode_fixer is Windows only for now*
*The source code is open if you're on Mac or Linux*

---

## 🌐 Language Support and Compatibility

This tool relies on the [Aider](https://aider.chat) AI assistant to fix and explain code.  
Aider supports many programming languages, but its level of support varies depending on Tree-sitter integration and `tags.scm` availability.

---

### ✅ Fully Supported Languages

These languages benefit from deep Aider integration:

- Python  
- JavaScript / TypeScript  
- Rust  
- Go  
- Ruby  
- C++  
- PHP  
- HTML  
- CSS  

Features include:
- Full Tree-sitter-based repository mapping
- Precise function/class/variable tracking
- Structured editing and refactoring

---

### 🧩 Partially Supported Languages (Require `tags.scm` for full features)

For these languages, full support depends on the presence of a `tags.scm` file built on a [Tree-sitter grammar](https://tree-sitter.github.io/tree-sitter/):

| Language   | Status                        |
|------------|-------------------------------|
| Julia      | Community-supported prototype |
| Elixir     | Tree-sitter available         |
| Scala      | Tree-sitter available         |
| Haskell    | Emerging grammar              |
| Kotlin     | Experimental support          |

A `tags.scm` is a Tree-sitter query file that defines how to extract important symbols (like functions or classes) from the syntax tree.

Example:
```scheme
(function_definition
  name: (identifier) @function.name)

(class_definition
  name: (identifier) @class.name)
```

Place this file in the Tree-sitter grammar's `queries/` directory. Aider will use it to build an intelligent repo map and improve context awareness.

---

### ⚠️ Limited or Unsupported Languages

Languages not listed above may still be processed by Aider using LLM-based reasoning only. However, without syntax-aware Tree-sitter support, results may be less accurate or incomplete.

---

## 🧠 Contributing Language Support

To help add support for new languages:

1. Find or build a [Tree-sitter grammar](https://github.com/tree-sitter).
2. Write a `queries/tags.scm` file to define symbol extraction.
3. Submit a pull request to Aider or use it locally for your project.

More info: [Aider Language Docs](https://aider.chat/docs/languages.html#contributing-tags-scm)

---

## 📚 References

- 🤖 [Aider GitHub Repository](https://github.com/paulgb/aider)
- 📄 [Aider Language Support Docs](https://aider.chat/docs/languages.html)
- 🧵 [Tree-sitter Query Language](https://tree-sitter.github.io/tree-sitter/using-parsers#query-syntax)

---
