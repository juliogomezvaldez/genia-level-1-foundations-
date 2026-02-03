    # Agentic Generative AI Developer Program – Level 1
    **Theme:** Foundations & Single-Agent Systems  
    **Duration:** 4 weeks (self-contained)  
    **Capstone (this level):** **Fact-Checking Auditor (Single-Agent)**

    ## Courses used (from your list only)
    - **ChatGPT Prompt Engineering for Developers** *OpenAI (Via DeepLearning.AI)* (1.5 Horas (9 lecciones en video)) [link](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- **OpenAI for Developers (Learning Path)** *OpenAI (Via Pluralsight)* (Variable (Multiples cursos)) [link](https://www.pluralsight.com/paths/openai-for-developers)
- **Generative AI for Beginners** *Microsoft* (1 Hora (Curso de video)) [link](https://learn.microsoft.com/en-us/shows/generative-ai-for-beginners/)
- **Fundamentals of Generative AI** *Microsoft* (37 Minutos (Modulo)) [link](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/)
- **Develop generative AI apps in Azure (AI-3016)** *Microsoft (Azure)* (7 Horas 29 Min) [link](https://learn.microsoft.com/en-us/training/paths/create-custom-copilots-ai-studio/)
- **AWS Cloud Quest: Generative AI Practitioner** *AWS* (Autoguiado (Juego)) [link](https://aws.amazon.com/blogs/training-and-certification/category/artificial-intelligence/generative-ai/)
- **PartyRock** *AWS* (Autoguiado (Herramienta)) [link](https://aws.amazon.com/ai/learn/)
- **Generative AI Foundations** *AWS* (No especificado) [link](https://aws.amazon.com/startups/learn/choosing-the-right-generative-ai-learning-path)
- **Generative AI Learning Plan for Technical Learners** *AWS* (Autoguiado) [link](https://aws.amazon.com/startups/learn/choosing-the-right-generative-ai-learning-path)
- **Amazon Q - Generative AI-powered Assistant Learning Plan** *AWS* (Autoguiado) [link](https://aws.amazon.com/training/learn-about/ai/)
- **Generative AI for Executives** *AWS* (50 Minutos) [link](https://skillbuilder.aws/generative-ai)
- **AWS Generative AI and AI Agents with Amazon Bedrock (Certificado Prof.)** *AWS (Via Coursera)* (8 Semanas (~3h/sem)) [link](https://www.coursera.org/professional-certificates/aws-generative-ai-developers)

    ---

    ## Week 1 – LLM foundations + prompt interfaces
    **Outcomes**
    - Understand LLM limits (context, latency, cost) and design around them.
    - Produce reliable structured outputs (JSON/Markdown).

    **Topics**
    - Prompt patterns: constraints, decomposition, structured schemas
    - Grounding basics: “evidence-first” answers and refusals

    **Lab**
    - Build a prompt suite with a small test harness and golden examples.

    **Deliverables**
    - Prompt library + golden set (20 cases)
    - CLI/notebook runner

    ## Week 2 – Tool calling (single tool) + robustness
    **Outcomes**
    - Add one tool with strict input/output contracts and error handling.

    **Topics**
    - Tool schemas, retries, timeouts, fallbacks
    - Citing evidence; handling conflicting evidence

    **Lab**
    - Implement a Search/Lookup tool wrapper with unit tests.

    **Deliverables**
    - Tool wrapper + tests
    - Output schema + validator

    ## Week 3 – End-to-end agent workflow
    **Outcomes**
    - Execute Extract → Retrieve → Decide → Report consistently.

    **Topics**
    - Workflow orchestration (sequential)
    - Chunking, rate limits, caching basics

    **Lab**
    - Run the system on 10–20 inputs; track failures and iterate.

    **Deliverables**
    - Report generator (Markdown) + sample outputs
    - Basic telemetry logs

    ## Week 4 – Capstone build + review
    **Outcomes**
    - Demo-ready system with documentation and test coverage.

    **Lab**
    - Complete capstone + peer review using templates in `/reviews`.

    **Deliverables**
    - Working repo, README, SPEC, sample runs
    - Peer review notes
