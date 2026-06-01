# A/B Test Analyzer
An AI-powered tool that helps product teams design, interpret, and evaluate A/B test results. When metrics conflict (e.g., retention ↑ but revenue ↓), this tool uses LLM reasoning to simulate expert analysis and recommend next steps.

## Description
Product teams often struggle with interpreting A/B test results, especially when different metrics move in opposite directions. This tool leverages OpenAI's API to provide:

- **Hypothesis generation** - Understanding why metrics behaved the way they did
- **Metric suggestions** - Additional metrics to consider tracking
- **Result interpretation** - Clear analysis of what the data means
- **Recommendations** - Actionable next steps based on the results
## Getting Started
### Prerequisites
- Python 3.x
- OpenAI API key
### Installation
1. Clone the repository
2. Create and activate a virtual environment (recommended)
3. Install dependencies:pip install -r requirements.txt
4. Create a `.env`  file in the project root:OPENAI_API_KEY=your_api_key_here
### Usage
Run the Streamlit application:

```bash
streamlit run app.py
```
The app provides two main features:

1. **Single Experiment Analysis** - Enter your experiment results (e.g., "I tested onboarding, retention +5%, revenue -3%") and receive AI-powered analysis
2. **Variant Comparison** - Compare two variants of an experiment to evaluate trade-offs
Use the example buttons to quickly test the functionality.

## Configuration
| Variable | Description | Required |
| -----    | -----       | -----    |
| `OPENAI_API_KEY`  | Your OpenAI API key | Yes |
## Tech Stack
- **Python** - Core language
- **Streamlit** - User interface
- **OpenAI API** - LLM reasoning engine
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is open source. Please add a LICENSE file to specify the license type.



