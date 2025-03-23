# Stock Analysis Assistant 📈
![App interface](https://github.com/hkumar00/AI-Agents/blob/main/images/StockAnalysisApp.png)
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Agents](#agents)
  - [Technical Analysis Agent](#technical-analysis-agent)
  - [Fundamental Analysis Agent](#fundamental-analysis-agent)
  - [Decision Agent](#decision-agent)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview
The Stock Analysis Assistant is a Python-based application designed to provide comprehensive analysis of stock market data. Leveraging advanced AI models and a multi-agent architecture, the application offers both technical and fundamental analyses, culminating in actionable investment recommendations. The intuitive web interface, built with Streamlit, ensures accessibility for users of all experience levels.

## Features

- **Technical Analysis**: Evaluate stock performance using indicators such as SMA50, SMA200, RSI, and MACD.
- **Fundamental Analysis**: Assess financial health through metrics like market capitalization, P/E ratio, PEG ratio, and more.
- **Investment Recommendations**: Receive informed suggestions based on combined analyses.
- **User-Friendly Interface**: Interact seamlessly through a clean and responsive web application.

## Architecture
The application employs a modular multi-agent system:

- **Technical Analysis Agent**: Analyzes historical price data to identify trends and patterns.
- **Fundamental Analysis Agent**: Evaluates financial statements and ratios to determine intrinsic value.
- **Decision Agent**: Synthesizes insights from both analyses to provide actionable recommendations.

This architecture ensures a robust and comprehensive analysis of each stock.

## Installation
To set up the Stock Analysis Assistant locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/Stock-Analysis-Assistant.git
   cd Stock-Analysis-Assistant
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Ollama**:
   Follow the instructions at [Ollama's official website](https://www.ollama.ai/) to install the platform on your system.

## Usage

1. **Start the Ollama Server**:
   Ensure the Ollama server is running:
   ```bash
   ollama serve
   ```

2. **Launch the Streamlit Application**:
   Run the following command:
   ```bash
   streamlit run app.py
   ```

3. **Interact with the Application**:
   Access the web interface at `http://localhost:8501` and input a stock ticker to begin analysis.

## Agents

### Technical Analysis Agent
Utilizes historical price data to compute technical indicators:

- **SMA50 & SMA200**: Simple Moving Averages over 50 and 200 days.
- **RSI**: Relative Strength Index indicating overbought or oversold conditions.
- **MACD**: Moving Average Convergence Divergence to identify momentum shifts.

### Fundamental Analysis Agent
Assesses the company's financial health through metrics such as:

- **Market Capitalization**: Total market value of outstanding shares.
- **P/E Ratio**: Price-to-Earnings ratio indicating valuation.
- **PEG Ratio**: P/E ratio adjusted for earnings growth.
- **Revenue Growth**: Year-over-year revenue increase.

### Decision Agent
Integrates insights from both analyses to provide:

- **Buy/Sell/Hold Recommendations**: Based on combined technical and fundamental data.
- **Risk Assessment**: Evaluation of potential investment risks.

## Contributing
Contributions are welcome! To contribute:

1. **Fork the Repository**: Click the 'Fork' button at the top right corner.
2. **Create a New Branch**: For your feature or bug fix.
3. **Commit Changes**: Use clear and concise commit messages.
4. **Push to Branch**: Push your changes to your forked repository.
5. **Submit a Pull Request**: Describe your changes in detail.

Please adhere to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Ollama**: For providing the platform to run and manage LLMs locally.
- **Streamlit**: For the interactive web application framework.
- **Contributors**: Thanks to all who contribute to this project!
