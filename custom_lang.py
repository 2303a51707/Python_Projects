from flask import Flask, request
import json

app = Flask(__name__)

# -------------------------
# Interpreter Logic (safe)
# -------------------------
class CustomInterpreter:
    def __init__(self, config):
        self.config = config
        self.variables = {}

    def run(self, code):
        output = []
        lines = code.strip().split("\n")
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            tokens = line.split()

            try:
                # Variable assignment
                if tokens[0] == self.config.get("let", "let"):
                    var_name = tokens[1]
                    value = eval(" ".join(tokens[3:]), {}, self.variables)
                    self.variables[var_name] = value

                # Print statement
                elif tokens[0] == self.config.get("print", "print"):
                    expr = " ".join(tokens[1:])
                    value = eval(expr, {}, self.variables)
                    output.append(str(value))

                # If condition (only skips 1 line for demo)
                elif tokens[0] == self.config.get("if", "if"):
                    condition = " ".join(tokens[1:])
                    if not eval(condition, {}, self.variables):
                        i += 1  

                # While loop (safe, max 20 iterations)
                elif tokens[0] == self.config.get("while", "while"):
                    condition = " ".join(tokens[1:])
                    loop_body = []
                    i += 1
                    while i < len(lines) and lines[i].startswith("    "):
                        loop_body.append(lines[i].strip())
                        i += 1

                    count = 0
                    while eval(condition, {}, self.variables) and count < 20:
                        for stmt in loop_body:
                            output.extend(self.run(stmt))
                        count += 1
                    continue
            except Exception as e:
                output.append(f"Error: {e}")

            i += 1
        return output


# -------------------------
# Flask App
# -------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    default_config = {
        "let": "var",
        "print": "show",
        "if": "cond",
        "while": "loop"
    }
    default_code = """var x = 10
var y = 20
show x + y
cond x < y
show "x is smaller"
"""

    if request.method == "POST":
        try:
            config = json.loads(request.form.get("config", "{}"))
            code = request.form.get("code", "")

            interpreter = CustomInterpreter(config)
            output = interpreter.run(code)
            result = "\n".join(output) if output else "(no output)"

        except Exception as e:
            result = f"Error: {str(e)}"

    return f"""
    <html>
    <head>
        <title>Custom Language Builder</title>
    </head>
    <body style="font-family:Arial;margin:20px;">
        <h1>Custom Language Builder</h1>
        <form method="post">
            <h3>Step 1: Config (JSON)</h3>
            <textarea name="config" style="width:100%;height:120px;">{json.dumps(default_config, indent=4)}</textarea>
            <h3>Step 2: Code</h3>
            <textarea name="code" style="width:100%;height:120px;">{default_code}</textarea>
            <br><br>
            <button type="submit">Run</button>
        </form>
        <h3>Output:</h3>
        <pre style="background:#f4f4f4;padding:10px;border:1px solid #ccc;">{result}</pre>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
