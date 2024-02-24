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


def buy(first_name, second_name, product_name, product_count, product_time):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT price FROM medical_product WHERE name = %s", (product_name,))
            product_price = cur.fetchone()
            cur.execute("INSERT INTO costumer (first_name, second_name, product_name, product_count, product_price, product_time) VALUES (%s, %s, %s, %s, %s, %s)", (first_name, second_name, product_name, product_count, product_price, product_time))
            cur.execute("UPDATE medical_product SET count = count - %s WHERE name = %s", (product_count, product_name))
        conn.commit()
        print("Product bought successfully!")
    except psycopg2.Error as e:
        print(f"Error buying product: {e}")

