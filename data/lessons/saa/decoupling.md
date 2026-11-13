# Decoupling with SQS, SNS, EventBridge & Kinesis

Tightly coupled tiers fail together: when a fast web tier hands work directly to a
slower processing tier, a traffic spike drops requests and one component's outage
stalls the whole chain. **Decoupling** inserts a buffer or broker between
components so they scale and fail independently. The exam gives you a coupling
problem — bursty load, fan-out to many systems, ordered events, a workflow — and
asks for the right integration service.

## Amazon SQS: a buffer between producer and consumer

> **Amazon SQS is a fully managed message queue. A producer writes messages; a
> consumer polls and processes them at its own pace. The queue absorbs bursts so no
> request is lost when the consumer can't keep up.**

This is the default answer for "buffer bursts and decouple a fast tier from a slow
one." Four SQS behaviors are tested constantly:

- **Visibility timeout** — when a consumer receives a message, it is hidden for a
  period so a second consumer doesn't process it simultaneously. If processing
  takes longer than the timeout, the message can reappear and be handled twice, so
  size the timeout to the work.
- **Dead-letter queue (DLQ)** — a few malformed "poison" messages can fail over and
  over and block a queue. Configure a DLQ with a `maxReceiveCount` **redrive
  policy** so repeatedly failing messages move aside for inspection.
- **Long polling** — if consumers poll a frequently empty queue they rack up empty
  responses and cost. Enabling long polling (a receive wait time) cuts empty
  receives.
- **FIFO queues** — standard queues are best-effort ordering and at-least-once
  delivery. Use a **FIFO queue** when you need messages processed in *exact order*
  with *no duplicates*.

## Amazon SNS: publish/subscribe fan-out

> **Amazon SNS delivers one published message to *many* subscribers at once
> (fan-out).** Publish an event to a topic and every subscriber — SQS queues,
> Lambda functions, HTTP endpoints — receives its own copy.

When a single upload must notify several independent systems (a thumbnail
generator, an indexer, an audit logger), publish once to an **SNS topic** with
multiple subscribers. A common robust pattern is **SNS → multiple SQS queues**
(fan-out with durable buffering per consumer). If each subscriber should get only a
relevant subset of messages, apply **subscription filter policies** so filtering
happens at the topic rather than in every consumer.

## Amazon EventBridge: event routing and scheduling

**Amazon EventBridge** is a serverless event bus that routes events from many AWS
services *and* third-party SaaS applications to different targets using
content-matching rules. Reach for it when the need is "route events based on their
content to different targets," especially across SaaS integrations.

EventBridge also schedules work: an **EventBridge scheduled rule** (or EventBridge
Scheduler) invokes a Lambda function on a fixed schedule — "every day at 02:00" —
with no server to maintain.

## AWS Step Functions: orchestrate a workflow

When several steps must run **in sequence** with built-in error handling, retries,
and visibility into which step failed, that is orchestration, not simple
messaging.

> **AWS Step Functions coordinates multi-step workflows as a state machine, with
> retries, error handling, and a visual record of exactly which step failed.**

If a question describes an ordered, multi-stage process that needs reliability and
visibility, Step Functions beats hand-wiring queues together.

## Amazon Kinesis: high-volume ordered streaming

**Amazon Kinesis Data Streams** ingests a high-volume, ordered stream of events and
lets **multiple independent consumers** each read the full stream in order and
**replay** it. Choose it over SQS when the requirements include ordered streaming,
multiple independent readers of the same data, and replay — SQS deletes a message
once consumed, so it cannot replay.

## Amazon MQ: migrating an existing broker

If you are migrating an on-premises application that already speaks standard
message-broker protocols — **JMS, AMQP, MQTT** — **Amazon MQ** is a managed broker
(ActiveMQ/RabbitMQ) that supports them with minimal code change. SQS and SNS use
AWS APIs, so they would require rewriting the app; MQ is the "lift-and-shift the
broker" answer.

## Choosing quickly

| Need | Service |
|------|---------|
| Buffer bursts, one consumer group | **SQS** |
| Fan-out one message to many systems | **SNS** |
| Route events by content, SaaS integration | **EventBridge** |
| Ordered, multi-step workflow with retries | **Step Functions** |
| Ordered stream, multiple readers, replay | **Kinesis Data Streams** |
| Migrate an app using JMS/AMQP/MQTT | **Amazon MQ** |

## Exam focus

- Buffer bursts / decouple producer from slower consumer → **SQS**. Exact order +
  no duplicates → **SQS FIFO**.
- **Visibility timeout** prevents double processing; a **DLQ with a
  `maxReceiveCount` redrive policy** isolates poison messages; **long polling** cuts
  empty-receive cost.
- Notify many independent systems at once → **SNS** fan-out; narrow each
  subscriber's messages → **subscription filter policies**.
- Route events by content from AWS/SaaS → **EventBridge**; run Lambda on a schedule
  → **EventBridge scheduled rule / Scheduler**.
- Sequential workflow with retries and visibility → **Step Functions**.
- Ordered streaming with multiple consumers and replay → **Kinesis Data Streams**.
- Migrate an app that speaks JMS/AMQP/MQTT with minimal changes → **Amazon MQ**.
