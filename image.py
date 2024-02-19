import streamlit as st

# Define the title of the page
st.title("Product Grid Example")

# Set up a container to hold the grid
grid_container = st.container()

# Set the number of columns for the product grid
num_columns = 3

# Mock data for products (in real scenarios, this would be dynamic data)
products = [
    {"name": "Product 1", "price": "20€", "likes": 10, "description": "Sample description."},
    {"name": "Product 2", "price": "30€", "likes": 5, "description": "Sample description."},
    # ... Add more products as needed
]

with grid_container:
    # Start the columns
    cols = st.columns(num_columns)

    for index, product in enumerate(products):
        # Compute in which column to put the product
        col_index = index % num_columns
        with cols[col_index]:
            # You can add an image with st.image() here using a URL or filepath
            st.image("path_to_product_image.jpg", use_column_width=True)
            st.write(product["name"])
            st.write(product["price"])
            st.write(f"❤️ {product['likes']}")
            st.write(product["description"])

# It is important to note that as of my knowledge cutoff in April 2023, Streamlit had st.beta_columns
# which has been updated to st.columns in newer versions, so the above uses the newer `st.columns`.

# If you're using an older version of Streamlit, you need to replace `st.columns` with `st.beta_columns`.
