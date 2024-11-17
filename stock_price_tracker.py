import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

# Watchlist (initial stocks)
STOCKS = ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN", "META", "NFLX", "NVDA", "BA", "V"]

def fetch_stock_data(symbol):
    """
    Fetch live stock price data using yfinance.
    """
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d", interval="1m")  # Fetch intraday data (1-minute interval)
        latest = data.iloc[-1]  # Get the latest data point
        price = latest["Close"]  # Current price
        change = price - data["Open"][0]  # Change from day's open
        percent_change = (change / data["Open"][0]) * 100  # Percent change
        return price, change, percent_change, data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None, None, None, None

def update_data():
    """
    Fetch live stock data and update the GUI table.
    """
    for stock in STOCKS:
        # Insert row if it doesn't already exist
        if stock not in row_ids:
            row_ids[stock] = table.insert("", "end", values=(stock, "Loading...", "Loading...", "Loading..."))

        # Fetch stock data and update the row
        price, change, percent_change, _ = fetch_stock_data(stock)
        if price is not None:
            if change > 0:
                table.item(row_ids[stock], values=(stock, f"${price:.2f}", f"{change:+.2f}", f"{percent_change:+.2f}%"), tags=("positive",))
            elif change < 0:
                table.item(row_ids[stock], values=(stock, f"${price:.2f}", f"{change:+.2f}", f"{percent_change:+.2f}%"), tags=("negative",))
            else:
                table.item(row_ids[stock], values=(stock, f"${price:.2f}", f"{change:+.2f}", f"{percent_change:+.2f}%"), tags=("neutral",))
        else:
            table.item(row_ids[stock], values=(stock, "Error", "N/A", "N/A"), tags=("neutral",))

    # Update last refreshed time
    last_updated.set(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # Update the graph for the currently selected stock
    update_graph(selected_stock.get())
    # Schedule next update (e.g., every 30 seconds)
    root.after(30000, update_data)

def update_graph(stock):
    """
    Fetch historical data and update the graph for the selected stock.
    """
    try:
        # Fetch historical data for the past day with 5-minute intervals
        stock_data = yf.Ticker(stock)
        hist = stock_data.history(period="1d", interval="5m")  # Use 5-minute intervals
        times = hist.index  # Full datetime index
        prices = hist["Close"]  # Extract closing prices for the y-axis

        # Limit to the last 2 hours of data
        times = times[-24:]  # Last 24 data points (5 minutes * 24 = 2 hours)
        prices = prices[-24:]

        # Convert datetime index to matplotlib-compatible format
        times = [datetime.strftime(t, "%H:%M") for t in times]

        # Clear the current plot and redraw the graph
        ax.clear()
        ax.plot(times, prices, label=f"{stock} Price", color="blue")
        ax.set_title(f"Live Price Trend: {stock}")
        ax.set_xlabel("Time (HH:MM)")
        ax.set_ylabel("Price ($)")
        ax.legend(loc="upper left")
        ax.tick_params(axis="x", rotation=45)  # Rotate x-axis labels for better readability

        # Adjust layout to avoid x-axis labels being cut off
        plt.tight_layout()

        canvas.draw()
    except Exception as e:
        print(f"Error updating graph for {stock}: {e}")


def add_stock():
    add_button.config(state=tk.DISABLED)  # Disable button
    try:
        new_stock = search_entry.get().strip().upper()
        if new_stock and new_stock not in STOCKS:
            STOCKS.append(new_stock)
            row_ids[new_stock] = table.insert("", "end", values=(new_stock, "Loading...", "Loading...", "Loading..."))
            update_graph(new_stock)  # Update the graph for the new stock
            dropdown["values"] = STOCKS  # Update dropdown options
            search_entry.delete(0, tk.END)  # Clear the search bar
    finally:
        add_button.config(state=tk.NORMAL)  # Enable button
        search_entry.focus_set()  # Set focus back to the input field


def remove_stock():
    remove_button.config(state=tk.DISABLED)  # Disable button
    try:
        stock_to_remove = selected_stock.get()
        if stock_to_remove in STOCKS:
            STOCKS.remove(stock_to_remove)
            table.delete(row_ids.pop(stock_to_remove))
            dropdown["values"] = STOCKS  # Update dropdown options
            if STOCKS:
                selected_stock.set(STOCKS[0])
                update_graph(STOCKS[0])
            else:
                ax.clear()
                ax.set_title("No Stocks Selected")
                canvas.draw()
    finally:
        remove_button.config(state=tk.NORMAL)  # Enable button
        search_entry.focus_set()  # Set focus back to the input field


# Initialize GUI
root = tk.Tk()
root.title("Real-Time Stock Price Tracker")
root.geometry("1000x700")
root.configure(bg="black")  # Set background color to black

# Table for stock prices
columns = ("Symbol", "Price", "Change", "% Change")
table = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center", width=150)
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Define row styles (colors)
table.tag_configure("positive", background="green", foreground="white")
table.tag_configure("negative", background="red", foreground="white")
table.tag_configure("neutral", background="gray", foreground="white")

# Dictionary to store row IDs
row_ids = {}

# Last Updated Label
last_updated = tk.StringVar()
last_updated.set("Last Updated: Not yet updated")
tk.Label(root, textvariable=last_updated, fg="white", bg="black", font=("Helvetica", 12)).pack(pady=5)

# Search bar for adding stocks
search_frame = tk.Frame(root, bg="black")
search_frame.pack(pady=5)

search_label = tk.Label(search_frame, text="Add Stock:", fg="white", bg="black", font=("Helvetica", 10))
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)
search_entry.bind("<Button-1>", lambda e: search_entry.focus_set())  # Focus on click

add_button = tk.Button(search_frame, text="Add", command=add_stock, bg="#228B22", fg="black")
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(search_frame, text="Remove Selected", command=remove_stock, bg="#B22222", fg="black")
remove_button.pack(side=tk.LEFT, padx=5)

# Dropdown for stock selection
selected_stock = tk.StringVar(value=STOCKS[0])
dropdown = ttk.Combobox(root, textvariable=selected_stock, values=STOCKS, state="readonly", width=20)

# Ensure dropdown gains focus when clicked
dropdown.bind("<Button-1>", lambda e: dropdown.focus_set())

# Bind dropdown selection to graph update
dropdown.bind("<<ComboboxSelected>>", lambda e: update_graph(selected_stock.get()))
dropdown.pack(pady=5)

# Create a figure for the graph
fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
ax.set_title("Select a Stock to View Price Trend")
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Start fetching data
update_data()

# Run the GUI
root.mainloop()
