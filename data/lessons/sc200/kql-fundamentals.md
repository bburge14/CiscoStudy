# KQL Fundamentals for Detection & Hunting

**Kusto Query Language (KQL)** is the language you write detections and hunts in,
whether in Microsoft Sentinel or Defender XDR advanced hunting. SC-200 tests KQL at
a *practical* level: you should be able to read a query, predict its output, and
know which operator does what. This lesson builds the core vocabulary —
`where`, `project`, `summarize`, `join`, and `let` — with original, defensive
example queries. (Every query below is illustrative and read-only; KQL is a query
language and does not change data.)

## The pipe model

A KQL query starts with a **table** and flows data through a pipeline of operators
joined by the pipe character `|`. Each operator takes the rows from the left and
passes a transformed set to the right.

```kql
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID == 4625          // failed logon
| project TimeGenerated, Account, IpAddress, Computer
```

> Read a pipeline top-to-bottom: start with the table, then narrow and shape. A
> golden rule for performance is **filter early** — put `where` as high as possible
> so later operators work on fewer rows.

## `where` — filter rows

`where` keeps only the rows matching a predicate. You combine conditions with
`and` / `or`, and KQL has string operators worth knowing:

- `==` exact match; `=~` case-insensitive match.
- `has` matches a whole **term** and is faster; `contains` matches any substring.
- `startswith`, `endswith`, `in (...)`, and `matches regex` for patterns.
- Time filters use `ago()` and `between()`. (The Defender XDR advanced-hunting
  `Device*` tables use a **`Timestamp`** column; Sentinel / Log Analytics tables such as
  `SigninLogs` and `SecurityEvent` use **`TimeGenerated`** — match the column to where
  the query runs.)

```kql
DeviceProcessEvents
| where Timestamp between (ago(7d) .. now())
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has_any ("-enc", "FromBase64String", "DownloadString")
```

## `project` and `extend` — shape columns

- **`project`** chooses (and optionally renames or computes) the columns to keep.
- **`project-away`** drops columns you don't want.
- **`extend`** adds a new calculated column while keeping the existing ones.

```kql
SigninLogs
| where ResultType == 0
| extend City = tostring(LocationDetails.city)
| project TimeGenerated, UserPrincipalName, IPAddress, City
```

## `summarize` — aggregate and group

`summarize` collapses rows into aggregates, optionally grouped `by` one or more
columns. Common aggregation functions:

| Function | Returns |
|----------|---------|
| `count()` | number of rows |
| `countif(predicate)` | rows matching a condition |
| `dcount(col)` | distinct count of a column |
| `make_set(col)` | the set of distinct values |
| `min()` / `max()` | earliest/latest or smallest/largest |
| `arg_max(col, *)` | the full row where `col` is largest |

`bin()` buckets a continuous value — most often time — so you can aggregate per
interval:

```kql
SigninLogs
| where TimeGenerated > ago(1d)
| summarize FailedCount = countif(ResultType != 0),
            Countries   = dcount(tostring(LocationDetails.countryOrRegion))
          by UserPrincipalName, bin(TimeGenerated, 1h)
| where FailedCount > 20 or Countries > 1
```

> `summarize ... by X` is the heart of most detections: *count how often something
> happens per user / per host / per hour, then keep only the outliers.*

## `join` — combine two tables

`join` correlates rows from two tables on a shared key — essential when evidence
lives in different tables (a sign-in here, a process there).

```kql
let suspiciousLogons =
    DeviceLogonEvents
    | where ActionType == "LogonSuccess" and LogonType == "Network";
suspiciousLogons
| join kind=inner (
    DeviceProcessEvents
    | where FileName in~ ("net.exe", "whoami.exe", "nltest.exe")
  ) on DeviceId
| project Timestamp, DeviceId, AccountName, FileName, ProcessCommandLine
```

Know the **join kinds**: `inner` (matches in both), `leftouter` (all left rows,
plus matches), and `leftanti` (left rows with **no** match in the right — great for
"seen before but not in my allowlist"). A KQL nuance: the **default** join kind is
`innerunique`, which deduplicates the left key, so specify `kind=inner` when you
want every match.

## `let` — name things

`let` binds a name to a scalar, a list, or an entire table expression. Use it to
set thresholds once, build allowlists, or stage a sub-result for readability and
reuse.

```kql
let lookback = 24h;
let rareProcessThreshold = 3;
let knownAdminHosts = dynamic(["JUMPHOST01", "JUMPHOST02"]);
DeviceProcessEvents
| where TimeGenerated > ago(lookback)
| where DeviceName !in (knownAdminHosts)
| summarize Hosts = dcount(DeviceName) by FileName
| where Hosts <= rareProcessThreshold   // rarely-seen binaries = worth a look
```

## Putting it together

A typical hunt: start at a table, `where` down to the relevant events as early as
possible, `summarize` to count behavior per entity and per time bucket, `join` in
corroborating evidence from another table, `project` the columns an analyst needs,
and use `let` to keep thresholds and lists tidy at the top. Add `sort by`,
`top N`, or `render timechart` when you want ordering or a quick visualization.

## Exam focus

- KQL flows data through `|` pipes; **filter early** with `where` for performance.
- `where` filters **rows**; `project` selects/renames **columns**, `extend` adds a
  computed column, `project-away` removes columns.
- `summarize` aggregates with `count()`, `countif()`, `dcount()`, `make_set()`,
  `arg_max()`, grouped `by` columns; `bin(TimeGenerated, 1h)` buckets time.
- `join` correlates two tables `on` a key. Know **inner**, **leftouter**, and
  **leftanti** (rows with no match); the **default is `innerunique`**, so write
  `kind=inner` for all matches.
- `let` names a scalar, list, or table — use it for thresholds and allowlists.
- Useful extras: `ago()`/`between()` for time, `has` (faster, term) vs `contains`
  (substring), `=~` (case-insensitive), `sort`/`top`, and `render` for charts.
