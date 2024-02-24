import psycopg2

try:
    conn = psycopg2.connect(
        database = "medical_warehouse",
        user = "postgres",
        password = "unity 3d",
        host = "localhost",
        port = "5432"
    )
    print("Connected to the database successfully!")
except psycopg2.Error as e:
    print(f"Unable to connect to the database: {e}")

def show_med_product():
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM medical_product")
            products = cur.fetchall()
            for product in products:
                print(product)
    except psycopg2.Error as e:
        print(f"Error reading products: {e}")


def add_new_med_product(name, count, price, time):
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO medical_product (name, count, price, time) VALUES (%s, %s, %s, %s)", (name, count, price, time))
        conn.commit()
        print("Product created successfully!")
    except psycopg2.Error as e:
        print(f"Error creating product: {e}")


def edit_med_product(name, count, price, time):
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATA medical_product SET count = count + %s, price = %s, time = %s WHERE name = %s", (name, count, price, time))
        conn.commit()
        print("Product updated successfully!")
    except psycopg2.Error as e:
        print(f"Error updating product: {e}")

def delete_product(name):
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM medical_product WHERE name = %s", (name,))
        conn.commit()
        print("Product deleted successfully!")
    except psycopg2.Error as e:
        print(f"Error deleting product: {e}")