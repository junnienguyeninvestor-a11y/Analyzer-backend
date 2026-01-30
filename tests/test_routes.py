# import pytest
# import os
# import sys

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.lib.controller import data_to_pd
from app.lib.use_service_account import fetch_data_from_sheet

data = fetch_data_from_sheet()
columns=["No", "link", "name", "connection", "country", "account", "date", "status", "balanced", "events"]
column_len = 10
df = data_to_pd(data, columns, column_len)
df_chatting_by_account = df[df["status"]=="Chatting"].groupby("account")[["name", "country"]].apply(lambda x: x.to_dict(orient='list')).to_dict()

print(df_chatting_by_account)