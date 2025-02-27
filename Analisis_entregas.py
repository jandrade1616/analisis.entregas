#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # importar librerías


# In[2]:


# leer conjuntos de datos en los DataFrames
df_orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter=';')
df_products = pd.read_csv('/datasets/products.csv', delimiter=';')
df_aisles = pd.read_csv('/datasets/aisles.csv', delimiter=';')
df_departments = pd.read_csv('/datasets/departments.csv', delimiter=';')
df_order_products = pd.read_csv('/datasets/order_products.csv', delimiter=';')


# In[3]:


print(df_orders.info())# mostrar información del DataFrame


# In[4]:


print(df_products.info())# mostrar información del DataFrame


# In[5]:


print(df_aisles.info())# mostrar información del DataFrame


# In[6]:


print(df_departments.info())# mostrar información del DataFrame


# In[7]:


print(df_order_products.info())# mostrar información del DataFrame


# In[8]:


# Revisa si hay pedidos duplicados
import pandas as pd

duplicated_orders = df_orders[df_orders.duplicated(subset='order_id', keep=False)]
print(duplicated_orders)
print(f"Number of duplicated orders: {duplicated_orders.shape[0]}")


# In[9]:


# Basándote en tus hallazgos,
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.
wednesday_orders_2am = df_orders[(df_orders['order_dow'] ==3) & (df_orders['order_hour_of_day']==2)]
print (wednesday_orders_2am)


# In[10]:


# Elimina los pedidos duplicados
import pandas as pd

df_orders_unique = df_orders.drop_duplicates(subset='order_id', keep='first')
print(df_orders_unique.head())


# In[11]:


# Vuelve a verificar si hay filas duplicadas
duplicated_orders = df_orders_unique[df_orders_unique.duplicated(subset='order_id', keep=False)]
print("Pedidos duplicados después de la limpieza:")
print(duplicated_orders)
print(f"Número de pedidos duplicados restantes: {duplicated_orders.shape[0]}")


# In[12]:


# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
print(f"Número de pedidos duplicados restantes: {duplicated_orders.shape[0]}")


# In[13]:


# Verifica si hay filas totalmente duplicadas
duplicated_rows_products = df_products[df_products.duplicated(keep=False)]
print(f"Número de filas totalmente duplicadas: {duplicated_rows_products.shape[0]}")


# In[14]:


# Revisa únicamente si hay ID de departamentos duplicados
df_products = pd.read_csv('/datasets/products.csv', delimiter=';')
duplicated_dept_ids = df_products[df_products.duplicated(subset='department_id', keep=False)]

print("IDs de departamentos duplicados:")
print(duplicated_dept_ids)

print(f"Número de IDs de departamentos duplicados: {duplicated_dept_ids.shape[0]}")


# In[15]:


# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
df_products['product_name_upper'] = df_products['product_name'].str.upper()
duplicated_product_names = df_products[df_products.duplicated(subset='product_name_upper', keep=False)]
print(f"Número de nombres de productos duplicados: {duplicated_product_names.shape[0]}")


# In[16]:


# Revisa si hay nombres duplicados de productos no faltantes
df_products_non_missing = df_products.dropna(subset=['product_name'])
duplicated_product_names = df_products_non_missing[df_products_non_missing.duplicated(subset='product_name_upper', keep=False)]
print(f"Número de nombres de productos duplicados (sin considerar faltantes): {duplicated_product_names.shape[0]}")


# In[17]:


# Revisa si hay filas totalmente duplicadas
duplicated_rows_departments = df_departments[df_departments.duplicated(keep=False)]
print(f"Número de filas totalmente duplicadas: {duplicated_rows_departments.shape[0]}")


# In[18]:


# Revisa únicamente si hay IDs duplicadas de productos
duplicated_department_ids = df_departments[df_departments.duplicated(subset='department_id', keep=False)]
print(f"Número de IDs de deparmentos duplicados: {duplicated_department_ids.shape[0]}")


# ### `aisles` data frame

# In[19]:


# Revisa si hay filas totalmente duplicadas
duplicated_rows_aisles = df_aisles[df_aisles.duplicated(keep=False)]
print(f"Número de filas totalmente duplicadas: {duplicated_rows_aisles.shape[0]}")


# In[20]:


# Revisa únicamente si hay IDs duplicadas de productos
duplicated_aisle_ids = df_aisles[df_aisles.duplicated(subset='aisle_id', keep=False)]
print(f"Número de IDs de productos duplicados: {duplicated_aisle_ids.shape[0]}")


# In[21]:


# Revisa si hay filas totalmente duplicadas
duplicated_rows_order = df_order_products[df_order_products.duplicated(keep=False)]
print(f"Número de filas totalmente duplicadas: {duplicated_rows_order.shape[0]}")


# In[22]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
duplicated_order_ids = df_order_products[df_order_products.duplicated(subset='product_id', keep=False)]
print(f"Número de IDs de productos duplicados: {duplicated_order_ids.shape[0]}")


# In[23]:


# Encuentra los valores ausentes en la columna 'product_name'
missing_product_names = df_products[df_products['product_name'].isna()]
print(f"Número de valores ausentes en 'product_name': {missing_product_names.shape[0]}")


# In[24]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
aisle_100_missing_product_names = missing_product_names[missing_product_names['aisle_id'] == 100]
all_missing_related_to_aisle_100 = missing_product_names.shape[0] == aisle_100_missing_product_names.shape[0]
print(f"¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100? {all_missing_related_to_aisle_100}")


# In[25]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
department_21_missing_product_names = missing_product_names[missing_product_names['department_id'] == 21]
all_missing_related_to_department_21 = missing_product_names.shape[0] == department_21_missing_product_names.shape[0]
print(f"¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21? {all_missing_related_to_department_21}")


# In[26]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.

aisle_100_data = df_aisles[df_aisles['aisle_id'] == 100]
department_21_data = df_departments[df_departments['department_id'] == 21]


missing_product_details = missing_product_names.merge(df_aisles, on='aisle_id', how='left')
missing_product_details = missing_product_details.merge(df_departments, on='department_id', how='left')

all_missing_related_to_aisle_100 = missing_product_names['aisle_id'].eq(100).all()
all_missing_related_to_department_21 = missing_product_names['department_id'].eq(21).all()

print(f"\n¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100? {all_missing_related_to_aisle_100}")
print(f"¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21? {all_missing_related_to_department_21}")


# In[27]:


# Completa los nombres de productos ausentes con 'Unknown'
df_products['product_name'] = df_products['product_name'].fillna('Unknown')
missing_product_names = df_products[df_products['product_name'].isna()]
print(f"Número de valores ausentes en 'product_name' después de completar: {missing_product_names.shape[0]}")


# In[28]:


# Encuentra los valores ausentes
missing_orders_names = df_orders[df_orders.isna()]
print(f"Número de valores ausentes en 'orders_name': {missing_orders_names.shape[0]}")


# In[29]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?
missing_days_since_prior_order = df_orders['days_since_prior_order'].isnull()


missing_count = missing_days_since_prior_order.sum()
non_first_order_nans = df_orders[missing_days_since_prior_order & (df_orders['order_number'] != 1)]
non_first_order_nans_count = non_first_order_nans.shape[0]

print(f'Total de valores nulos en "days_since_prior_order": {missing_count}')
print(f'Valores nulos en "days_since_prior_order" que no son el primer pedido: {non_first_order_nans_count}')


# In[30]:


# Encuentra los valores ausentes
missing_orders_products = df_order_products[df_order_products.isna()]
print(f"Número de valores ausentes en 'orders_products': {missing_orders_products.shape[0]}")


# In[31]:


import pandas as pd
df_order_products = pd.read_csv('/datasets/order_products.csv', delimiter=';')

missing_orders_products = df_order_products[df_order_products.isna()]
max_values = missing_orders_products.max()
min_values = missing_orders_products.min()

print("Valores máximos en columnas")
print(max_values)
print("Valores mínimos en columnas:")
print(min_values)


# In[32]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
missing_add_to_cart_order = df_order_products[df_order_products['add_to_cart_order'].isna()]
order_ids_with_missing_add_to_cart_order = missing_add_to_cart_order['order_id'].unique()
print(f"Número de pedidos con valores ausentes en 'add_to_cart_order': {len(order_ids_with_missing_add_to_cart_order)}")
print("IDs de pedidos con valores ausentes en 'add_to_cart_order':")
print(order_ids_with_missing_add_to_cart_order)


# In[33]:


# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
# Agrupa todos los pedidos con datos ausentes por su ID de pedido.
# Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.
missing_add_to_cart_order = df_order_products[df_order_products['add_to_cart_order'].isna()]
product_counts_per_order = missing_add_to_cart_order.groupby('order_id')['product_id'].count()
min_product_count = product_counts_per_order.min()
all_orders_above_64 = min_product_count > 64

print(f"El valor mínimo del conteo de productos en pedidos con valores ausentes en 'add_to_cart_order' es: {min_product_count}")
print(f"¿Todos los pedidos con valores ausentes tienen más de 64 productos? {all_orders_above_64}")


# In[34]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.
df_order_products['add_to_cart_order'].fillna(999, inplace=True)
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].astype(int)
print(df_order_products['add_to_cart_order'].dtypes)
print(df_order_products['add_to_cart_order'].isna().sum())


# In[35]:


import pandas as pd
df_orders = pd.read_csv('/datasets/instacart_orders.csv', delimiter=';')
valid_hours = df_orders['order_hour_of_day'].between(0, 23).all()
print(f"¿Todos los valores de 'order_hour_of_day' están entre 0 y 23? {valid_hours}")


# In[36]:


valid_days = df_orders['order_dow'].between(0, 6).all()
print(f"¿Todos los valores de 'order_dow' están entre 0 y 6? {valid_days}")


# In[37]:


import pandas as pd
from matplotlib import pyplot as plt
order_hour_counts = df_orders['order_hour_of_day'].value_counts().sort_index()
plt.figure(figsize=(7.5, 4.5))
order_hour_counts.plot(kind='bar')
plt.title('Número de pedidos por hora del día')
plt.xlabel('Hora del día')
plt.ylabel('Pedidos')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()


# In[38]:


import pandas as pd
from matplotlib import pyplot as plt
order_hour_counts = df_orders['order_dow'].value_counts().sort_index()
plt.figure(figsize=(7.5, 4.5))
order_hour_counts.plot(kind='bar')
plt.title('Número de pedidos por día de la semana')
plt.xlabel('Día de la semana')
plt.ylabel('Pedidos')
plt.xticks(range(0, 7),["Domingo","Lunes","Martes","Mircoles","Juves","Viernes","Sabado"])
plt.show()


# In[39]:


order_hour_counts = df_orders['days_since_prior_order'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
order_hour_counts.plot(kind='bar')
plt.title('Tiempo de espera de las personas hasta el siguiente pedido')
plt.xlabel('Días desde el pedido anterior')
plt.ylabel('Numero de pedidos')
plt.grid(True)
plt.show()

min_days_since_prior_order = df_orders["days_since_prior_order"].min()
max_days_since_prior_order = df_orders["days_since_prior_order"].max()

print (f"El tiempo de espera minimo de las personas para hacer otro pedido después de una comrpra es:{min_days_since_prior_order}")
print (f"El tiempo de espera maximo de las personas para hacer otro pedido después de una comrpra es:{max_days_since_prior_order}")



# In[40]:


wednesday_orders = df_orders[df_orders['order_dow'] == 3]['order_hour_of_day']
saturday_orders = df_orders[df_orders['order_dow'] == 6]['order_hour_of_day']


# In[41]:


wednesday_counts = wednesday_orders.value_counts().sort_index()
saturday_counts = saturday_orders.value_counts().sort_index()


# In[42]:


plt.figure(figsize=(14, 7))

plt.bar(wednesday_counts.index - 0.2, wednesday_counts.values, width=0.4, label='Miércoles', align='center')
plt.bar(saturday_counts.index + 0.2, saturday_counts.values, width=0.4, label='Sábado', align='center')
plt.title('Distribución de órdenes por hora del día: Miércoles vs. Sábado')
plt.xlabel('Hora del día')
plt.ylabel('Número de órdenes')
plt.xticks(range(0, 24))
plt.grid(True)
plt.legend()
plt.show()


# In[43]:


orders_per_customer = df_orders['user_id'].value_counts()


# In[44]:


plt.figure(figsize=(12, 6))
bars = orders_per_customer.value_counts().sort_index().plot(kind='bar')
plt.title('Distribución del número de órdenes por cliente')
plt.xlabel('Número de órdenes X Cliente')
plt.ylabel('Número de clientes')
plt.grid(True)


for bar in bars.patches:
    plt.text(
        bar.get_x() + bar.get_width() / 2, 
        bar.get_height() + 1000, 
        str(int(bar.get_height())), 
        ha='center', 
        fontsize=8, 
        color='black'
    )

plt.show()


# In[58]:


product_order_counts = df_order_products['product_id'].value_counts()

top_20_products = product_order_counts.head(20)
top_20_products_df = top_20_products.to_frame().reset_index()
top_20_products_df.columns = ['product_id', 'order_count']
top_products = top_20_products_df.merge(df_products, on='product_id')
top_products = top_products[['product_id', 'product_name', 'order_count']]

print("Los 20 principales productos que se piden con más frecuencia:")
print(top_products)


# In[77]:


plt.figure(figsize=(14, 7))
plt.bar(top_products['product_name'], top_products['order_count'], color='cyan')
plt.xlabel('Nombre del Producto')
plt.ylabel('Número de Pedidos')
plt.title('Top 20 Productos Más Frecuentemente Pedidos')
plt.xticks(rotation=45)
plt.grid(True)
    
plt.show()


# In[79]:


items_per_order = df_order_products.groupby('order_id')['product_id'].count()


# In[80]:


plt.figure(figsize=(14, 7))
plt.hist(items_per_order, bins=50, color='skyblue')
plt.xlabel('Número de Artículos por Pedido')
plt.ylabel('Frecuencia')
plt.title('Distribución del Número de Artículos por Pedido')
plt.grid(True)
plt.show()


# In[82]:


print(items_per_order)


# In[83]:


reordered_products = df_order_products[df_order_products['reordered'] == 1]
reordered_counts = reordered_products['product_id'].value_counts().head(20)


# In[85]:


reordered_counts_df = reordered_counts.to_frame().reset_index()
reordered_counts_df.columns = ['product_id', 'reorder_count']


# In[86]:


top_reordered_products = reordered_counts_df.merge(df_products, on='product_id')
top_reordered_products = top_reordered_products[['product_id', 'product_name', 'reorder_count']]


# In[87]:


print("Los 20 principales artículos que vuelven a pedirse con mayor frecuencia:")
print(top_reordered_products)


# In[91]:


total_product_orders = df_order_products['product_id'].value_counts()
reordered_products = df_order_products[df_order_products['reordered'] == 1]
reordered_counts = reordered_products['product_id'].value_counts()


# In[92]:


reorder_rate = (reordered_counts / total_product_orders).reset_index()
reorder_rate.columns = ['product_id', 'reorder_rate']
reorder_rate_df = reorder_rate.merge(df_products, on='product_id', how='left')
reorder_rate_df = reorder_rate_df[['product_id', 'product_name', 'reorder_rate']]
reorder_rate_df['reorder_rate'].fillna(0, inplace=True)


# In[93]:


print("Tasa de repetición del pedido para cada producto:")
print(reorder_rate_df)


# In[103]:


df_order_products_users = df_order_products.merge(df_orders[['order_id', 'user_id']], on='order_id')
total_user_orders = df_order_products_users.groupby('user_id')['reordered'].count()
user_reorders = df_order_products_users[df_order_products_users['reordered'] == 1].groupby('user_id')['reordered'].count()
user_reorder_rate = (user_reorders / total_user_orders).reset_index()
user_reorder_rate.columns = ['user_id', 'reorder_rate']
user_reorder_rate = user_reorder_rate.dropna()
print("Tasa de repetición de pedido para cada usuario:")
print(user_reorder_rate)


# In[104]:


plt.figure(figsize=(14, 7))
plt.hist(user_reorder_rate['reorder_rate'], bins=50, color='skyblue')
plt.xlabel('Tasa de Repetición de Pedido')
plt.ylabel('Frecuencia')
plt.title('Distribución de la Tasa de Repetición de Pedido para Cada Usuario')
plt.grid(True)
plt.show()


# In[96]:


first_in_cart = df_order_products[df_order_products['add_to_cart_order'] == 1]
first_in_cart_counts = first_in_cart['product_id'].value_counts().head(20)
first_in_cart_counts_df = first_in_cart_counts.to_frame().reset_index()
first_in_cart_counts_df.columns = ['product_id', 'first_count']


# In[97]:


top_first_in_cart_products = first_in_cart_counts_df.merge(df_products, on='product_id')
top_first_in_cart_products = top_first_in_cart_products[['product_id', 'product_name', 'first_count']]


# In[98]:


print("Los 20 principales artículos que la gente pone primero en sus carritos:")
print(top_first_in_cart_products)

