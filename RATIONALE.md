## MarketMuse – Rationale Behind Design Decisions

### 1. Prompt Design

I designed the agent prompts and task descriptions to match real-world roles found in influencer marketing teams. Each agent has a clear **role**, **goal**, and **backstory** that helps it stay focused and act like a real expert.  

- **Influencer Evaluation Agent** looks for the right influencers using things like engagement rate, audience age, and content type.
- **Campaign Prediction Agent** thinks about future campaign performance by using available influencer and market data.
- **Optimization Strategy Agent** gives smart suggestions to improve the campaign—like using different content styles or platforms.
- **Chief Campaign Director (optional)** can help manage the whole flow if needed, like a human project manager.

Each **task prompt** was written using simple, direct instructions. I give the agent just enough context (like brand type, audience, goals) so it knows what to do without being confused or needing extra input.

---

### 2. System Architecture

I used **CrewAI** because it’s perfect for agent-based workflows. Here's how the system is built:

- **Agents** are defined as specialists with different skills.
- **Tasks** are the jobs they perform, in a specific order.
- I used **Pydantic models** for outputs (e.g., campaign strategy, copy ideas) to keep the results clean and structured.
- **Groq LLM (LLaMA2)** is used under the hood to make the agents smart and fast.
- **Tools like SerperDev and ScrapeIbsiteTool** help agents search the Ib or pull extra data when needed.

I run everything using `Process.sequential`, meaning each agent runs in turn, and each task uses the result of the one before it.

---

### 3. Agent Coordination

The workflow is smooth and linear:

1. **Influencer Evaluation Agent** runs first → It finds and evaluates potential influencers.
2. **Campaign Prediction Agent** runs next → It takes those influencers and estimates how Ill the campaign might perform.
3. **Optimization Strategy Agent** runs after that → It looks at the predictions and suggests ways to improve the campaign.
4. **Campaign Summary Agent** (or the final task) → It combines everything into one clear report.

This step-by-step coordination ensures each agent only does what it’s best at, while passing helpful information to the next one.

