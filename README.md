# Stock Tracker 📈

[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/stock_tracker.svg)](https://github.com/yourusername/stock_tracker/issues)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/stock_tracker.svg)](https://github.com/yourusername/stock_tracker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/stock_tracker.svg)](https://github.com/yourusername/stock_tracker/network)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/stock_tracker)
[![Coverage Status](https://img.shields.io/badge/coverage-85%25-yellowgreen.svg)](https://github.com/yourusername/stock_tracker)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/yourusername/stock_tracker)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)](https://github.com/yourusername/stock_tracker)

A robust Python application for tracking and analyzing stock market data using the Alpha Vantage API. This tool fetches real-time stock data, processes it, and provides comprehensive logging for monitoring pipeline operations.

## 🚀 Features

- **Real-time Stock Data Fetching**: Retrieve daily stock data using Alpha Vantage API
- **Multi-Symbol Support**: Track multiple stocks simultaneously (AAPL, TSLA, GOOGL, BAC)
- **Comprehensive Logging**: Detailed logging system with file and console output
- **Data Persistence**: Automatic saving of raw data with timestamps
- **Error Handling**: Robust error handling and validation
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Environment Configuration**: Secure API key management using environment variables

## 📁 Project Structure

```
stock_tracker/
├── configs/
│   └── config.yaml          # Configuration settings
├── data/
│   ├── clean/              # Processed data storage
│   └── raw/                # Raw API responses
├── logs/
│   └── pipeline.log        # Application logs
├── src/
│   ├── data_cleaner.py     # Data processing module
│   ├── data_fetcher.py     # API interaction module
│   └── data_visualizer.py  # Data visualization module
├── .env                    # Environment variables
├── .gitignore             # Git ignore rules
├── main.py                # Main application entry point
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Alpha Vantage API key (free at [alphavantage.co](https://www.alphavantage.co/))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Alibubere/stock_tracker.git
   cd stock_tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   ALPHA_VANTAGE_KEY=your_api_key_here
   ```

## 🚀 Usage

### Basic Usage

Run the main application to fetch stock data for predefined symbols:

```bash
python main.py
```

### Programmatic Usage

```python
from src.data_fetcher import fetch_stock

# Fetch data for a specific symbol
data = fetch_stock("AAPL")
if data:
    print("Stock data retrieved successfully!")
```

## 📊 Supported Stocks

Currently configured to track:
- **AAPL** - Apple Inc.
- **TSLA** - Tesla, Inc.
- **GOOGL** - Alphabet Inc.
- **BAC** - Bank of America Corporation

## 🔧 Configuration

The application uses YAML configuration files located in the `configs/` directory. Modify `config.yaml` to customize API endpoints and other settings.

## 📝 Logging

The application provides comprehensive logging:
- **File Logging**: All logs saved to `logs/pipeline.log`
- **Console Output**: Real-time feedback during execution
- **Log Levels**: INFO, ERROR for different event types

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ali Muin**
- GitHub: [Alibubere](https://github.com/Alibubere)
- Email: alibubere989@gmail.com
- LinkedIn: [Mohammad Ali Bubere](https://www.linkedin.com/in/mohammad-ali-bubere-a6b830384/)

## 🙏 Acknowledgments

- [Alpha Vantage](https://www.alphavantage.co/) for providing the stock market API
- Python community for excellent libraries and tools
- Contributors and users of this project

## 📈 Roadmap

- [ ] Add data visualization capabilities
- [ ] Implement data cleaning and preprocessing
- [ ] Add support for cryptocurrency tracking
- [ ] Create web dashboard interface
- [ ] Add email notifications for price alerts
- [ ] Implement technical analysis indicators

## 🐛 Bug Reports

If you encounter any bugs or issues, please [create an issue](https://github.com/yourusername/stock_tracker/issues) with detailed information about the problem.

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">
  Made with ❤️ by Mohammad Ali  
</div>