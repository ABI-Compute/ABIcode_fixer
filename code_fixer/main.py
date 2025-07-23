import argparse
import subprocess
import os
import sys

def get_unique_languages(path):
    """Return a deduplicated list of detected languages from all files in all subfolders."""
    detected_languages = []
    files = get_code_files(path)

    for file in files:
        lang = detect_language_for_file(file)
        if lang and lang not in detected_languages:
            detected_languages.append(lang)

    return detected_languages

def get_code_files(path):
    """Recursively collect all non-hidden, non-binary files in a folder tree."""
    code_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if not file.startswith('.'):
                full_path = os.path.join(root, file)
                if os.path.isfile(full_path):
                    code_files.append(full_path)
    return code_files

def detect_language_for_file(path):
    fname = os.path.basename(path).lower()
    
    # High-level languages
    if fname.endswith(".py") or fname.endswith(".pyw"):
        return "python"
    elif fname.endswith(".js"):
        return "javascript"
    elif fname.endswith(".ts"):
        return "typescript"
    elif fname.endswith(".rb"):
        return "ruby"
    elif fname.endswith(".php"):
        return "php"
    elif fname.endswith(".java"):
        return "java"
    elif fname.endswith(".cs"):
        return "csharp"
    elif fname.endswith(".swift"):
        return "swift"
    elif fname.endswith(".go"):
        return "go"
    elif fname.endswith(".kt") or fname.endswith(".kts"):
        return "kotlin"
    elif fname.endswith(".dart"):
        return "dart"
    elif fname.endswith(".scala"):
        return "scala"
    elif fname.endswith(".lua"):
        return "lua"
    elif fname.endswith(".r"):
        return "r"
    elif fname.endswith(".jl"):
        return "julia"
    elif fname.endswith(".m") or fname.endswith(".mm"):
        return "objective-c"
    elif fname.endswith(".vb"):
        return "visualbasic"
    elif fname.endswith(".ex") or fname.endswith(".exs"):
        return "elixir"
    elif fname.endswith(".hs"):
        return "haskell"
    elif fname.endswith(".pl"):
        return "perl"
    elif fname.endswith(".fs") or fname.endswith(".fsi") or fname.endswith(".fsx"):
        return "fsharp"
    elif fname.endswith(".clj") or fname.endswith(".cljs") or fname.endswith(".cljc"):
        return "clojure"
    elif fname.endswith(".nim"):
        return "nim"
    elif fname.endswith(".zig"):
        return "zig"

    # Web and frontend
    elif fname.endswith(".html") or fname.endswith(".htm"):
        return "html"
    elif fname.endswith(".css"):
        return "css"
    elif fname.endswith(".scss") or fname.endswith(".sass"):
        return "scss"
    elif fname.endswith(".vue"):
        return "vue"
    elif fname.endswith(".svelte"):
        return "svelte"
    elif fname.endswith(".xml"):
        return "xml"

    # C/C++ and low-level
    elif fname.endswith(".c") or fname.endswith(".h"):
        return "c"
    elif fname.endswith(".cpp") or fname.endswith(".cc") or fname.endswith(".cxx") or fname.endswith(".hpp"):
        return "cpp"
    elif fname.endswith(".asm") or fname.endswith(".s"):
        return "assembly"
    elif fname.endswith(".rs"):
        return "rust"
    elif fname.endswith(".exe"):
        return "executable"

    # Scripting and config
    elif fname.endswith(".sh"):
        return "shell"
    elif fname.endswith(".bat"):
        return "batch"
    elif fname.endswith(".ps1"):
        return "powershell"
    elif fname.endswith(".toml"):
        return "toml"
    elif fname.endswith(".json"):
        return "json"
    elif fname.endswith(".yaml") or fname.endswith(".yml"):
        return "yaml"
    elif fname.endswith(".ini"):
        return "ini"

    # Functional build/config
    elif fname == "dockerfile":
        return "dockerfile"
    elif fname == ".gitignore":
        return "gitignore"
    elif fname == "makefile":
        return "makefile"
    elif fname == "build.gradle" or fname.endswith(".gradle") or fname.endswith(".gradle.kts"):
        return "gradle"
    elif fname == "pom.xml":
        return "maven"
    elif fname == "build.xml":
        return "ant"
    elif fname == "build.zig":
        return "zig-build"
    elif fname == "package.json":
        return "node"
    elif fname == "requirements.txt":
        return "pip"
    elif fname == "pyproject.toml":
        return "python-build"
    elif fname == "cargo.toml":
        return "cargo"
    elif fname == "go.mod":
        return "go-module"
    elif fname == "CMakeLists.txt":
        return "cmake"

    # Markup, docs, DB
    elif fname.endswith(".sql"):
        return "sql"
    elif fname.endswith(".md"):
        return "markdown"
    
    return None

def init_git_repo():
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", "Initial commit"], stdout=subprocess.DEVNULL)

def run_aider(files, mode="fix", review=False, custom_prompt=None):
    if custom_prompt:
        message = custom_prompt
    else:
        if mode == "fix":
            message = "Fix all bugs in this code and make safe improvements."
        elif mode == "explain":
            message = "Explain all bugs in this code and suggest how to fix them. Do not modify the files."
        else:
            raise ValueError("Invalid mode.")

    cmd = ["aider"] + files + ["--message", message]

    print(f"\n[*] Running Aider in '{mode}' mode{' with review' if review else ''}...\n")
    subprocess.run(cmd)

    if mode == "fix" and not review:
        subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", "Code_fixer auto-fix commit"], stdout=subprocess.DEVNULL)

def main():
    parser = argparse.ArgumentParser(description="🛠 Code_fixer: Fix or explain code using AI")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--fix", action="store_true", help="Fix code (default if no flag is passed)")
    group.add_argument("--explain", action="store_true", help="Only explain bugs, don't change code")
    
    parser.add_argument("--review", action="store_true", help="Review proposed changes before applying")
    parser.add_argument("--lang", help="Specify the code language (e.g. python, js, cpp)")
    parser.add_argument("--path", default=".", help="Path to the project directory")
    parser.add_argument("--prompt", help="Custom prompt to send to aider, overrides default messages")

    args = parser.parse_args()
    path = os.path.abspath(args.path)
    os.chdir(path)

    # Detect language if not provided
    langs = [args.lang] if args.lang else get_unique_languages(path)

    if not langs:
        print("❌ Could not detect any supported programming languages. Use --lang to specify manually.")
        sys.exit(1)
    elif len(langs) > 1:
        print(f"⚠️  Multiple languages detected: {', '.join(langs)}")
        print(f"[i] Defaulting to: {langs[0]}")

    lang = langs[0]
    print(f"[i] Using language: {lang}")

    # Get list of code files to fix/explain
    files = get_code_files(path)

    if not files:
        print("❌ No files found in the directory.")
        sys.exit(1)

    init_git_repo()

    mode = "fix"
    if args.explain:
        mode = "explain"

    run_aider(files, mode=mode, review=args.review, custom_prompt=args.prompt)

    if mode == "fix":
        print("\n✅ Code_fixer finished applying fixes!")
    elif mode == "explain":
        print("\n📋 Code_fixer finished explaining bugs.")

if __name__ == "__main__":
    main()
