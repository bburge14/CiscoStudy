# Storage, Databases & Data Services

Workloads need to **store** data, **organize** it in databases, and **process** it
for insight. This lesson covers all three: AWS storage services, database services,
and the analytics, integration, and AI/ML services that turn stored data into
value. It's the broadest lesson in the course, so the tables do the heavy lifting —
learn each service by its one-line job.

## Three kinds of storage

The first thing to get straight is the three storage *types*, because the exam
tests which one fits a scenario.

> **Object storage** (S3) stores whole files as objects in a flat namespace.
> **Block storage** (EBS) acts like a hard drive attached to one server. **File
> storage** (EFS, FSx) is a shared file system many servers mount at once.

### Amazon S3 (object storage)

**Amazon S3 (Simple Storage Service)** stores objects in **buckets**. It's
virtually unlimited, accessed over the web, and extremely durable — AWS designs it
for **eleven 9's (99.999999999%) of durability** by automatically replicating data
across **multiple Availability Zones** in a Region. S3 offers **storage classes**
that trade retrieval speed and cost:

| S3 storage class | Best for |
|------------------|----------|
| **S3 Standard** | Frequently accessed data; multi-AZ, high durability |
| **S3 Intelligent-Tiering** | **Unknown or changing** access patterns — automatically moves data between tiers to optimize cost |
| **S3 Standard-IA / One Zone-IA** | Infrequently accessed data (One Zone-IA is cheaper but single-AZ) |
| **S3 Glacier** (Instant, Flexible, Deep Archive) | **Archival** — lowest cost, longer retrieval times |

> If access patterns are **unknown or variable** and you want cost optimized
> automatically, the answer is **S3 Intelligent-Tiering.** If it's cold **archive**
> data, it's **Glacier.**

### Block and file storage

| Service | Type | Use |
|---------|------|-----|
| **Amazon EBS** | Block | A durable **volume attached to a single EC2 instance** — like its hard disk |
| **Amazon EFS** | File | A **shared** file system many **Linux** instances mount at once (NFS), scales automatically |
| **Amazon FSx for Windows File Server** | File | Fully managed **Windows (SMB)** shared file storage with native Windows features |
| **Amazon FSx for Lustre** | File | High-performance file system for **HPC** and compute-intensive workloads |

> Need **Windows SMB** shared files? **FSx for Windows File Server.** Need shared
> **Linux** files across many instances? **EFS.** Need a disk for **one** instance?
> **EBS.**

### Hybrid storage and backup

- **AWS Storage Gateway** — connects **on-premises** applications to AWS cloud
  storage (a hybrid bridge, with cached or stored modes).
- **AWS Backup** — **centrally** automates and manages backups across many AWS
  services from one place.

## Databases

AWS's pitch for databases is **managed** services: let AWS handle patching,
backups, and hardware so you don't run a database server on EC2 yourself.

### Relational databases: RDS and Aurora

> **Amazon RDS (Relational Database Service)** is a **managed relational
> database** — AWS handles patching, backups, and hardware. It supports engines
> like MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server.

Two RDS features the exam loves:

- **Multi-AZ deployment** — RDS keeps a **standby copy in another Availability
  Zone** and **automatically fails over** to it if the primary fails. This is for
  **high availability**.
- **Read replicas** — additional **read-only copies** that **offload heavy read
  traffic** (like reporting queries) from the primary. This is for **read
  scaling/performance**, not failover.

> **Multi-AZ = availability/failover. Read replicas = offload reads/performance.**
> Don't mix them up.

**Amazon Aurora** is AWS's own MySQL- and PostgreSQL-compatible engine, built for
higher performance and availability than standard RDS.

### Other databases

| Service | Type | Use |
|---------|------|-----|
| **Amazon DynamoDB** | **NoSQL** key-value | Serverless, single-digit-millisecond performance at any scale |
| **Amazon ElastiCache** | In-memory cache | Speed up apps by caching (Redis/Memcached) |
| **Amazon Redshift** | Data warehouse | Large-scale **analytics** over structured data |
| **Amazon DocumentDB** | Document (MongoDB-compatible) | JSON document workloads |
| **Amazon Neptune** | Graph | Highly connected data (social, fraud graphs) |

## Data services: integrate, analyze, and learn

The last subtopic is the grab-bag of services that move, analyze, and reason over
data. Group them in your mind by purpose.

### Application integration

These **decouple** components so systems are resilient and scalable:

- **Amazon SQS (Simple Queue Service)** — a managed **message queue** that holds
  messages until a consumer processes them. The classic way to **decouple**
  components.
- **Amazon SNS (Simple Notification Service)** — **pub/sub** messaging that pushes
  notifications to many subscribers at once.
- **Amazon EventBridge** — a **serverless event bus** that routes events from AWS
  services, your apps, and SaaS providers to targets.
- **AWS Step Functions** — **orchestrates** multiple services into a visual
  workflow of steps.

### Analytics

- **Amazon Athena** — run **SQL queries directly on data in S3**, serverless.
- **AWS Glue** — managed **ETL** (extract, transform, load) to prepare data.
- **Amazon Kinesis** — ingest and process **real-time streaming** data.
- **Amazon QuickSight** — **business intelligence** dashboards and visualizations.
- **Amazon EMR** — managed big-data processing (Hadoop, Spark).

### AI and machine learning

AWS offers both a platform to build your own models and ready-made AI services:

| Service | Does |
|---------|------|
| **Amazon SageMaker** | Platform to **build, train, and deploy** your own ML models |
| **Amazon Q** | AWS's **generative AI assistant** — **Q Developer** helps you build/operate on AWS; **Q Business** answers questions from your company's data |
| **Amazon Rekognition** | Image and video **analysis** |
| **Amazon Comprehend** | **Natural-language** text analysis |
| **Amazon Textract** | **Extract text** and data from documents |
| **Amazon Polly / Transcribe / Translate** | Text-to-speech / speech-to-text / translation |
| **Amazon Lex** | Build **chatbots** (the tech behind Alexa) |

> **Amazon Q** is the name to know for AWS's **generative AI assistant**, in two
> flavors: **Q Developer** (for building on AWS) and **Q Business** (for querying
> enterprise data).

## The whole thing in one paragraph

Storage comes in three shapes: **S3** (object, 11-nines durable, with classes like
**Intelligent-Tiering** for unknown patterns and **Glacier** for archive), **EBS**
(a disk for one instance), and shared file systems **EFS** (Linux) and **FSx**
(Windows SMB / Lustre), plus **Storage Gateway** (hybrid) and **AWS Backup**.
Databases are **managed**: **RDS** (relational, with **Multi-AZ** for failover and
**read replicas** for read scaling), **Aurora**, **DynamoDB** (NoSQL),
**ElastiCache** (caching), and **Redshift** (warehouse). Data services **integrate**
(**SQS**, **SNS**, **EventBridge**, **Step Functions**), **analyze** (**Athena**,
**Glue**, **Kinesis**, **QuickSight**, **EMR**), and apply **AI/ML**
(**SageMaker**, the **Amazon Q** assistant, and pre-trained services like
Rekognition, Comprehend, and Textract).

## Exam focus

- Storage types: **S3 = object**, **EBS = block (one instance)**, **EFS/FSx =
  shared file**. **FSx for Windows File Server** = Windows **SMB** shares; **EFS** =
  shared **Linux** files.
- **S3** is designed for **11 nines of durability** across multiple AZs.
  **Intelligent-Tiering** = unknown/changing access patterns; **Glacier** =
  archive.
- **RDS** = managed relational DB. **Multi-AZ** = **failover/availability**;
  **read replicas** = **offload read traffic/performance.** Keep them separate.
- **DynamoDB** = managed **NoSQL** (serverless, single-digit ms); **Redshift** =
  **data warehouse/analytics**; **ElastiCache** = in-memory caching.
- Integration: **SQS** = queue to **decouple**; **SNS** = pub/sub notifications;
  **EventBridge** = serverless **event bus**; **Step Functions** = workflow
  orchestration.
- Analytics: **Athena** = SQL on **S3**; **Glue** = ETL; **Kinesis** = real-time
  streaming; **QuickSight** = BI dashboards.
- AI/ML: **SageMaker** = build your own models; **Amazon Q** = generative AI
  assistant (**Q Developer** and **Q Business**); plus pre-trained services
  (Rekognition, Comprehend, Textract, Polly, Transcribe, Lex).
