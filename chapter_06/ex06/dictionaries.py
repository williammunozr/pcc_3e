gcp_cloud_engineer = {'kubernetes': 'gke', 'sql_database': 'cloud sql'}

print(gcp_cloud_engineer['kubernetes'].upper())
print(gcp_cloud_engineer['sql_database'].title())

# append a new value to the dictionary
gcp_cloud_engineer['global_database'] = "cloud spanner"

print(gcp_cloud_engineer['global_database'].title())

# print the whole dictionary
print(gcp_cloud_engineer)

# looping through a dictionary
print("")
print("### looping through a dictionary ###")
for key, value in gcp_cloud_engineer.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

print("")

# removing key-value pairs
del gcp_cloud_engineer['sql_database']
print(gcp_cloud_engineer)

# use get function to get value from a dictionary
sql_database = gcp_cloud_engineer.get('sql_database', 'no sql database set')
print(sql_database)

global_database = gcp_cloud_engineer.get('global_database', 'no global database set')
print(global_database)
