# Bash Scripting

A shell script is just a file of commands you could have typed by hand, plus the
control structures that make them repeatable and decision-driven. Bash scripting
is how a Linux administrator turns a one-time fix into a reliable, reusable tool.
This lesson covers the constructs the exam expects you to read and write.

## Anatomy of a script

The first line is the **shebang**, telling the kernel which interpreter to use:

```bash
#!/bin/bash
echo "Starting backup..."
```

Make it executable and run it:

```
$ chmod +x backup.sh
$ ./backup.sh            # runs via the shebang
$ bash backup.sh         # or invoke the interpreter explicitly
```

## Variables and quoting

Assign with **no spaces** around the `=`; expand with `$`:

```bash
name="web01"
count=5
echo "Host is $name"            # braces ${name} disambiguate when needed
```

Quoting matters enormously:

- **Double quotes** `"$name"` allow variable and command expansion — use these by
  default, and always quote variables to survive spaces.
- **Single quotes** `'$name'` are literal — no expansion at all.
- **Command substitution** `$(command)` captures a command's output into a
  variable: `today=$(date +%F)`.

### Special variables

| Variable | Meaning |
|----------|---------|
| `$0` | The script's name |
| `$1`, `$2`, … | Positional arguments |
| `$#` | Number of arguments |
| `$@` | All arguments (each separately quoted) |
| `$?` | Exit status of the last command (0 = success) |
| `$$` | PID of the current script |

Read interactive input with `read`:

```bash
read -p "Enter username: " user
```

## Conditionals

Decisions use `if … then … fi`. The condition is itself a command; a **zero exit
status means true**. The `[ ]` / `test` builtin and the newer `[[ ]]` evaluate
expressions:

```bash
if [ "$count" -gt 3 ]; then
    echo "plenty"
elif [ "$count" -eq 0 ]; then
    echo "none"
else
    echo "a few"
fi
```

Know the operator families — numeric comparisons use letter flags while string
comparisons use symbols:

| Test | Numbers | Strings |
|------|---------|---------|
| equal | `-eq` | `=` |
| not equal | `-ne` | `!=` |
| less / greater | `-lt` / `-gt` | — |

File tests are heavily used: `-f` (regular file exists), `-d` (directory exists),
`-e` (exists), `-r`/`-w`/`-x` (readable/writable/executable), `-z` (string empty),
`-n` (string non-empty).

```bash
if [ -f /etc/nginx/nginx.conf ]; then
    echo "config present"
fi
```

A `case` statement is cleaner than a long `if` chain for matching one value:

```bash
case "$1" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;
    *)     echo "usage: $0 {start|stop}" ;;
esac
```

## Loops

```bash
for host in web01 web02 web03; do
    echo "Pinging $host"
    ping -c1 "$host"
done

count=1
while [ "$count" -le 5 ]; do
    echo "attempt $count"
    count=$((count + 1))      # arithmetic expansion
done
```

`for` iterates a list, `while` repeats *as long as* its condition is true, and
`until` repeats *until* its condition becomes true. Arithmetic uses `$(( ))`.

## Functions

Group reusable logic into functions; arguments arrive as `$1`, `$2` inside them:

```bash
log() {
    echo "[$(date +%T)] $1"
}
log "backup finished"
```

A function (or script) returns an **exit status**. End with `exit 0` for success
or a non-zero code for failure — this is what `$?` and the calling automation
inspect.

## Redirection and pipes

Scripts route input and output with operators:

- `> file` overwrites stdout to a file; `>> file` appends.
- `2> file` redirects stderr; `&> file` redirects both; `2>&1` merges stderr into
  stdout.
- `< file` feeds a file as stdin; a **here-document** feeds inline text:

```bash
cat <<EOF > /etc/motd
Welcome to $name
EOF
```

- A **pipe** `|` sends one command's stdout into the next: `ps aux | grep nginx`.

## Writing robust scripts

Three `set` options harden a script and are worth recognizing:

- `set -e` — exit immediately if any command fails.
- `set -u` — treat use of an unset variable as an error.
- `set -x` — print each command as it runs (debugging trace).

> A dependable pattern is to start scripts with `set -euo pipefail`. It turns
> silent failures into loud, early ones — far better than a backup script that
> "succeeds" while quietly doing nothing.

## Exam focus

- Scripts start with a **shebang** (`#!/bin/bash`) and need execute permission
  (`chmod +x`). Variable assignment has **no spaces** around `=`; expand with
  `$var` or `${var}`.
- **Double quotes** expand variables; **single quotes** are literal;
  **`$(...)`** captures command output.
- Special vars: `$1`–`$9` (args), `$#` (count), `$@` (all), `$?` (last exit
  status, 0 = success), `$0` (script name).
- Conditions are commands; **exit status 0 is true**. Numeric comparisons use
  `-eq/-ne/-lt/-gt`; strings use `=`/`!=`. File tests: `-f`, `-d`, `-e`, `-z`,
  `-n`.
- Loops: `for` over a list, `while` while-true, `until` until-true; `case` for
  multiway matching. Arithmetic via `$(( ))`.
- Redirection: `>` overwrite, `>>` append, `2>` stderr, `&>`/`2>&1` both; `|`
  pipes; `<<EOF` is a here-doc.
- `set -e` (exit on error), `set -u` (error on unset var), `set -x` (trace) make
  scripts safer and debuggable.
