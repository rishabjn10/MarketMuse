
# AI Crew for Marketing Strategy
## Introduction
This project demonstrates the use of the CrewAI framework to automate the creation of a marketing strategy. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

## Running the Script
- **Configure Environment**: Copy `.env.example` and set up the environment variables.
- **Install Dependencies**: Run `poetry lock && poetry install`.
- **Customize**: Modify `src/market_muse/main.py` to add custom inputs for your agents and tasks.
- **Customize Further**: Check `src/market_muse/config/agents.yaml` to update your agents and `src/market_muse/config/tasks.yaml` to update your tasks.
- **Execute the Script**: Run `poetry run market_muse` and input your project details.

## Details & Explanation
- **Running the Script**: Execute `poetry run market_muse`. The script will leverage the CrewAI framework to generate a detailed marketing strategy.
- **Key Components**:
  - `src/market_muse/main.py`: Main script file.
  - `src/market_muse/crew.py`: Main crew file where agents and tasks come together, and the main logic is executed.
  - `src/market_muse/config/agents.yaml`: Configuration file for defining agents.
  - `src/market_muse/config/tasks.yaml`: Configuration file for defining tasks.
  - `src/market_muse/tools`: Contains tool classes used by the agents.

