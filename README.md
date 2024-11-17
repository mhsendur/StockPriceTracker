### **Real-Time Stock Price Tracker**

<img width="1342" alt="Screenshot 2024-11-17 at 20 47 29" src="https://github.com/user-attachments/assets/235ae0de-264f-4de7-a15f-1c2ba1f12efd">

---


### **Project Description**

The **Real-Time Stock Price Tracker** is a Python-based application that provides live updates of stock prices, price changes, and trends. It features:
- A **dynamic table** to display live stock price information for multiple stocks.
- A **real-time price trend graph** for the selected stock.
- A **search bar** to dynamically add or remove stocks from the tracker.
- An interactive **dropdown menu** to select and visualize stock trends.

Built with `tkinter` for the GUI and `yfinance` for retrieving stock data, this project is an ideal introduction to real-time financial data visualization and GUI programming.

---

### **Features**
1. **Live Stock Price Table**:
   - Displays tracked stocks' current price, price change, and percentage change.
   - Color-coded rows:
     - **Green**: Positive price changes.
     - **Red**: Negative price changes.
     - **Gray**: Neutral or error states.

2. **Real-Time Stock Trend Graph**:
   - Visualizes the live price trend for the selected stock.
   - Automatically updates with new data every 30 seconds.
   - Displays the last **2 hours of data** (5-minute intervals).

3. **Dynamic Stock Management**:
   - **Add Stock**: Search and add any stock to the watchlist by its ticker symbol (e.g., `TSLA`, `AAPL`).
   - **Remove Stock**: Remove a stock from the watchlist dynamically.

4. **Interactive Dropdown Menu**:
   - Allows quick selection of a stock to view its price trend.

5. **Automatic Refreshing**:
   - Stock prices and graphs update automatically without requiring a restart.

---

### **Technologies Used**
- **Programming Language**: Python
- **GUI Framework**: `tkinter`
- **Financial Data API**: `yfinance`
- **Plotting Library**: `matplotlib`

---

### **Setup and Installation**

#### **Requirements**
- Python 3.7 or higher
- The following Python libraries:
  - `tkinter` (included with Python by default)
  - `matplotlib`
  - `yfinance`

#### **Installation Steps**
1. Install the required libraries:
   ```bash
   pip install yfinance matplotlib
   ```

2. Run the application:
   ```bash
   python stock_price_tracker.py
   ```

---

### **How to Use**

1. **Start the Application**:
   - Run the script to launch the tracker window.

2. **Live Stock Table**:
   - View stock symbols, prices, changes, and percentage changes in a color-coded table.

3. **Add Stock**:
   - Type the stock ticker symbol (e.g., `DIS`, `NFLX`) into the "Add Stock" field and click "Add".
   - The new stock will appear in the table and dropdown menu.

4. **Remove Stock**:
   - Select a stock from the dropdown menu and click "Remove Selected" to remove it from the tracker.

5. **View Stock Trends**:
   - Use the dropdown menu to select a stock.
   - View the live price trend graph below the table.

---

### **Example Stocks to Try**
Here are some stock ticker symbols to test with:
- `AAPL` (Apple)
- `GOOG` (Alphabet/Google)
- `TSLA` (Tesla)
- `MSFT` (Microsoft)
- `AMZN` (Amazon)
- `META` (Meta/Facebook)
- `NFLX` (Netflix)
- `NVDA` (NVIDIA)
- `BA` (Boeing)
- `V` (Visa)

  
