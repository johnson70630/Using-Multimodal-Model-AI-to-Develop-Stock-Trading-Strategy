# Using-Multimodal-Model-AI-to-Develop-Stock-Trading-Strategy

# Main Points

## Preface
- **Objective**: Improve the accuracy of portfolio return predictions to help investors make better decisions, increase returns, and reduce risks.
- **Technologies Used**: Implemented advanced machine learning techniques including Graph Neural Networks (GNN) to handle the complexity and variability of financial markets.

## Problem
- **Three Main Analysis Directions**:
  - **Fundamental Analysis**: Based on financial reports, updated monthly, with limited data for high-frequency analysis.
  - **Sentiment/Flow Analysis**: Includes market sentiment and capital flows.
  - **Technical Analysis**: Relies on market data like stock prices and volumes to predict future trends.
- **Challenge**: Traditional methods focus on single-company data, neglecting the impact of supply chain or competitor activities on a company's stock price.

## Approach
- **Combined Analysis**: Integrated sentiment (news) and technical (candlestick charts) analysis using GNN to predict portfolio returns, considering upstream, downstream, and competitive relationships among companies.
- **Data Integration**: Utilized multiple data sources to improve prediction accuracy, forming portfolios and backtesting overall prediction accuracy.

## Project Goal
- **Target Stocks**: Selected top 60 companies by market capitalization in Taiwan from 2014.
- **Goal**: Predict stock movements to build portfolios, based on the assumption of market inefficiency, integrating various forms of information to capture risk factor-driven returns.

## News Text Processing
- **Three Parts**:
  - **Data Collection**: Web scraping for relevant stock news.
  - **Text Analysis**: Used transformer-based language models to extract financial features from news.
  - **Integration with Other Data**: Combined text features with financial indicators for comprehensive analysis.
- **Data Collection**: Gathered news content for 58 stocks from 2014 to 2024, with predictions made every 12 days.
- **Modeling**: Used a Chinese BERT model for preprocessing news data, applying transformer architecture for accurate textual representation.

## Stock Chart Vector Processing
- **Data Collection**: Used Yahoo Finance API to obtain OHLC and volume data from 2013.7.1 to 2024.7.20.
- **Technical Analysis**: Added 20-day moving average (MA) to avoid excessive noise in charts.
- **Labeling**: Labeled data as 1 if the price increased after 10 days, otherwise 0.
- **Image Generation**: Created grayscale candlestick charts using numpy arrays, covering 60 trading days with normalized data.
- **CNN Training**: Trained a 3-layer CNN with 5x3 convolution size, outputting vectors for GNN training.
- **Additional Models**: Experimented with VGGNet, ResNet, and U-net.

## Macroeconomic Indicator Vector
- **Objective**: Provide the model with a broader view by integrating macroeconomic data, which is consistent across all stocks.
- **Data Collection**: Used Yahoo Finance API and FRED API to obtain relevant indicators.
- **Indicators**: Included exchange rates, volatility, commodity prices, CPI inflation, unemployment rates, interest rates, and money supply.
- **Normalization**: Performed 60-day normalization to ensure consistency.
- **GNN Training**: Passed the data to GNN for training.

## GNN (Graph Neural Network)
- **Stock Price Influences**: Considered not just company-specific data but also impacts from suppliers, customers, and competitors.
- **GNN Models**:
  - **Total Network Graph**: Includes all competitive relationships.
  - **Heterogeneous Graph**: Focuses only on competitive relationships.
  - **Homogeneous Graph**: Includes only cooperative relationships, such as those between suppliers and customers.
- **Node Creation**: Developed a new node related to all companies, using the Taiwan stock market index to represent overall market conditions.