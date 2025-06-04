import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title("Demo Dashboard")
    data = pd.DataFrame(
        np.random.randn(10, 2),
        columns=["column A", "column B"]
    )
    st.write("Random data")
    st.line_chart(data)


if __name__ == "__main__":
    main()
