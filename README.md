# Financial-forecast
Quarterly Revenue Forecast for Public Companies in A-Share Main-Board Market

Data Introduction

   Financial data refers to the three main kinds of financial reports: Balance Sheet, Income Statement and Cash Flow Statement. 
   These three tables form the basic set of companies’ financial information, which are the foundation of investment analysis.
   
   Balance Sheet: A balance sheet reports a company's assets, liabilities and shareholders' equity at a specific point in time,   
   and provides a basis for computing rates of return and evaluating its capital structure. It is a financial statement that  
   provides a snapshot of what a company owns and owes, as well as the amount invested by shareholders.
   
   Income Statement: A summary of a management's performance as reflected in the profitability (or lack of it) of an organization over a certain period. It is based on a fundamental accounting equation (Income = Revenue - Expenses) and shows the rate at      which the owners’ equity is changing for better or worse.
   
   Cash Flow Statement: It provides aggregate data regarding all cash inflows a company receives from its ongoing operations and 
   external investment sources, as well as all cash outflows that pay for business activities and investments during a given 
   quarter.

   Cash flow statement explains balance sheet. The final change of cash is reflected in Cash and Cash equivalents account. And through the cash flow during operating, investment and financing activities, net profits become into real cash change.

   Evaluation Criteria

   There consists of two columns – TICKER_SYMBOL.EXCHANGE_CD and Forecasting_Revenue for the file FDDC_financial_submit.csv.
  
   
  
   Base on the Balance Sheet, Income and Cash Flow Statements to filter features related to the revenue and clean data, and divide    data into training and test sets according to time then use regression tree to predict the first half year revenue on cloud 
   platform computing.(Python 3.6 running on Alibaba Cloud ECS with CentOS 7.4 operating system)
