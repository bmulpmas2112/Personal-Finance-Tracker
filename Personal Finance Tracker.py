# python -m streamlit run "Personal Finance Tracker.py" (code to run it on the website, enter it via terminal)

import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


pd.set_option('display.max_columns', None)

pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv("Money.csv")
data = df[["Date", "Description", "Amount", "Balance", "Category"]]
print(data.head())
def add_expense(date, description, amount, balance):
    global data
    new_entry = {
        "Date": date,
        "Description": description,
        "Amount": amount,
        "Balance": balance,
        "Category": category

    }
    new_row = pd.DataFrame([new_entry])
    data = pd.concat([data,new_row], ignore_index=True)
    print(f"added:{description} - {amount} ")


#add_expense("14/04/2026", "Video Game", 60, 350)
#add_expense("15/04/2026", "Amazon Subscription", 15, 360)
#add_expense("16/04/2026", "Headphones", 30, 380)

data.to_csv("Money.csv", index=False)
print("Saved to excel file")

expense_summary = data[data['Category'] != 'Amount'].groupby("Category")["Amount"].sum()




csv_file = "Money.csv"
if os.path.exists(csv_file):
    data = pd.read_csv(csv_file)
else:
    data = pd.DataFrame(columns=["Date", "Description", "Amount","Balance", "Category"])

st.title ("Smart Expense Tracker")

with st.form("expense_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    category = st.text_input("Category")
    amount  = st.number_input("Amount", min_value=0.0, format="%.2f")


    submitted = st.form_submit_button("Add")

    if submitted:
        new_expense = {"Date": date, "Description": description, "Amount": amount, "Category": category}
        data = pd.concat([data, pd.DataFrame([new_expense])], ignore_index=True)
        data.to_csv(csv_file, index=False)
        st.success(f"Added: {description} - {amount} ({date})")

st.subheader("All Expenses")
st.dataframe(data)

if not data.empty:
    st.subheader("Expense Breakdown by Category")

    category_totals = data.groupby("Category")["Amount"].sum()

    #Bar chart
    fig, ax = plt.subplots()
    category_totals.plot(kind="bar", ax=ax)
    ax.set_ylabel("Amount")
    st.pyplot(fig)

    #Pie Chart
    st.subheader("Category Distribution")
    fig2, ax2 = plt.subplots()
    category_totals.plot(kind = "pie", autopct="%1.1f%%", ax=ax2)
    st.pyplot(fig2)



plt.figure(figsize=(6,6))
expense_summary.plot.pie(autopct='%1.1f%%', startangle =90, shadow=True)
plt.title("Expenses Breakdown by Category")
plt.ylabel("")
plt.show()

plt.figure(figsize=(8,5))
expense_summary.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()






















#df = pd.read_csv("Money.csv")
#print(df.head(10))