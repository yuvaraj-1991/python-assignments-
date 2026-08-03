#Here we will write code to read the log file

# error_count = 0
# warn_count = 0
# info_count = 0

# with open('application.log', 'r') as file:
#     for line in file:
#         if 'ERROR' in line:
#             error_count += 1
#         elif 'WARNING' in line:
#             warn_count += 1   
#         elif 'INFO' in line:
#             info_count += 1

# print(f'''
# ========== LOG SUMMARY ==========

# INFO Logs     : {info_count}
# WARNING Logs  : {warn_count}
# ERROR Logs    : {error_count}

# =================================
#         ''')

database_serv = 0
payment_serv = 0
invent_serv = 0
auth_serv = 0
order_serv = 0

with open('application.log', 'r') as file:
    for line in file:
        if 'AuthenticationService' in line:
            auth_serv += 1
        elif 'PaymentService' in line:
            payment_serv += 1
        elif 'InventoryService' in line:
            invent_serv += 1
        elif 'DatabaseService' in line:
            database_serv += 1
        elif 'OrderService' in line:
            order_serv += 1


print(f''' 

========== ERROR REPORT ==========

DatabaseService : {database_serv}

PaymentService : {payment_serv}

InventoryService : {invent_serv}

AuthenticationService : {auth_serv}

OrderService : {order_serv}

==================================

''')