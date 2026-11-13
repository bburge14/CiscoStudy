# High-Performing Databases & Caching

AWS has a database for almost every access pattern, and the exam is really testing
whether you can read the pattern and pick the match. Relational with heavy reads?
Key-value at any scale? Microsecond caching? Petabyte analytics? This lesson maps
the shape of the workload to the right managed database, read-scaling feature, and
caching layer.

## Relational: RDS and Aurora

**Amazon RDS** is managed relational database hosting for engines like MySQL,
PostgreSQL, and SQL Server. **Amazon Aurora** is AWS's own MySQL- and
PostgreSQL-compatible engine built for the cloud.

> **Aurora delivers much higher performance than standard RDS MySQL/PostgreSQL,
> storage that scales automatically, and up to 15 read replicas sharing one
> storage layer.** Choose it when the ask is "MySQL-compatible but far faster, with
> auto-scaling storage."

Scaling reads is a recurring theme:

- **Read replicas** — add replicas and point read-only queries at them to scale
  read throughput and offload the primary.
- **Aurora reader endpoint + Replica Auto Scaling** — send reads to the single
  reader endpoint, which load-balances across all Aurora Replicas, and let the
  number of replicas scale automatically with read traffic.

Two more Aurora/RDS features the exam tests:

- **Aurora Serverless v2** — capacity scales up and down automatically for
  intermittent, unpredictable, or idle-much-of-the-time workloads, so you don't
  provision for peak.
- **Amazon RDS Proxy** — pools and shares database **connections**. When many
  Lambda functions each open their own connection and exhaust the database during
  spikes, RDS Proxy fixes it by pooling connections.

## Key-value at scale: DynamoDB

**Amazon DynamoDB** is a fully managed NoSQL key-value database with single-digit
millisecond latency at any scale. The exam tests capacity modes and indexing:

- **On-demand capacity mode** — pay per request with no capacity to forecast; the
  answer for **completely unpredictable** traffic with sudden spikes. (Provisioned
  mode with auto scaling suits steady, predictable load.)
- **Global Secondary Index (GSI)** — lets you query efficiently by a **non-key
  attribute** without scanning the whole table.

For caching in front of DynamoDB:

> **DynamoDB Accelerator (DAX) is an in-memory cache that drops read latency from
> milliseconds to *microseconds* for read-heavy workloads — and it's DynamoDB-API
> compatible, so no application rewrite.**

DAX is the answer whenever the requirement is "microsecond reads for DynamoDB
without changing the API calls."

## General-purpose caching: ElastiCache

For caching in front of a *relational* database — repeated identical queries for
popular items — use **Amazon ElastiCache**, which stores query results in memory to
cut database load and latency. It now runs three engines — **Valkey** (the open-source
Redis fork AWS now defaults to), **Redis OSS**, and **Memcached**; the exam's key
contrast is still Redis-style vs Memcached:

| Engine | Choose when you need |
|--------|----------------------|
| **ElastiCache for Redis** | Replication, high availability with failover, persistence, and advanced data structures (sorted sets, pub/sub) |
| **ElastiCache for Memcached** | A simple, multi-threaded cache with no persistence or replication |

If a question lists HA, failover, persistence, or rich data structures, the answer
is **Redis**; a plain, poolable cache points to Memcached.

## Analytics: Redshift

When the workload is **complex analytical queries** — large aggregations and joins
across petabytes of structured data — that is a data warehouse, not an OLTP
database.

> **Amazon Redshift is a columnar, massively parallel data warehouse for business-
> intelligence analytics at petabyte scale.** Don't reach for RDS or DynamoDB when
> the stem says "complex analytical queries" or "data warehouse."

## A worked example

A read-heavy web app on DynamoDB that needs microsecond reads adds **DAX** — no code
change. Its relational reporting database is strained by repeated popular queries,
so the team puts **ElastiCache for Redis** in front and adds **read replicas** for
the rest. A new feature needs to query orders by customer email (a non-key
attribute), so they add a **GSI**. The finance team's petabyte-scale trend analysis
runs on **Redshift**, kept separate from the transactional systems.

## Exam focus

- **Aurora** = MySQL/PostgreSQL-compatible, much faster than RDS, auto-scaling
  storage, up to 15 replicas. Scale reads with **read replicas**, or Aurora's
  **reader endpoint + Replica Auto Scaling**.
- Intermittent/unpredictable relational load → **Aurora Serverless v2**. Lambda
  exhausting DB connections → **RDS Proxy** (connection pooling).
- DynamoDB unpredictable traffic → **on-demand capacity mode**; query a non-key
  attribute → **Global Secondary Index (GSI)**; microsecond reads, same API →
  **DAX**.
- Cache relational query results in memory → **ElastiCache**; HA/failover/
  persistence/data structures → **Redis**; simple cache → **Memcached**.
- Complex analytical queries / data warehouse at petabyte scale → **Redshift**.
