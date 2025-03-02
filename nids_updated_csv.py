# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import MinMaxScaler
# import joblib
# import sys

# path='Uploaded_files/'
# val=sys.argv[1]
# path+=sys.argv[2];

# f=open(path)
# data=pd.read_csv(f)
# columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
#            'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
#            'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
#            'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
#            'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
#            'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
#            'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
#            'dst_host_srv_rerror_rate','level']
# data.columns = columns
# filtered_cols = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'wrong_fragment',
#             'hot', 'num_failed_logins', 'logged_in', 'num_compromised','is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
#            'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
#            'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
#            'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
#            'dst_host_srv_rerror_rate']
# data_Validate = data[filtered_cols]
# #label_encoders = {}
# # for column in ['protocol_type', 'service', 'flag']:
# #      le = LabelEncoder()
# #      data_Validate[column] = le.fit_transform(data_Validate[column])
# #      label_encoders[column] = le
# protocol_type_le = LabelEncoder()
# service_le = LabelEncoder()
# flag_le = LabelEncoder()
# data_Validate['protocol_type'] = protocol_type_le.fit_transform(data_Validate['protocol_type'])
# data_Validate['service'] = service_le.fit_transform(data_Validate['service'])
# data_Validate['flag'] = flag_le.fit_transform(data_Validate['flag'])
# df_validate=data_Validate.copy(deep=True)
# x_validate=df_validate.copy(deep=True)
# label_encoder = LabelEncoder() 
# scaler=MinMaxScaler()
# x1=x_validate.copy(deep=True)
# scaler=MinMaxScaler()
# scaler.fit(x1)
# scaled_data=scaler.transform(x1)
# scaled_data=pd.DataFrame(scaled_data)
# scaled_data.columns= x1.columns
# x_validate=pd.DataFrame(scaled_data)
# print(x_validate.shape)
# if(val=='knn'):
#     #knn_file  = "rf_model.sav"
#     knn_multi = joblib.load("rf_model.sav") 
#     x_predict_multi = knn_multi.predict(x_validate)
#     print(x_predict_multi)
#     #df_validate['multi class']=x_predict_multi
#     #df_validate.to_csv(path,index=False)
# print('completed')



import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import joblib
import sys

# File paths from command-line arguments
path = 'Uploaded_files/'
val = sys.argv[1]
path += sys.argv[2]

# Load CSV file
data = pd.read_csv(path)

# Define column names
columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
           'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
           'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
           'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
           'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
           'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
           'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
           'dst_host_srv_rerror_rate', 'level']
data.columns = columns

# Select relevant columns
filtered_cols = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'wrong_fragment',
                 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'is_guest_login', 'count', 'srv_count',
                 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
                 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
                 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
                 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']
data_Validate = data[filtered_cols]

# Label Encoding
protocol_type_le = LabelEncoder()
service_le = LabelEncoder()
flag_le = LabelEncoder()
data_Validate['protocol_type'] = protocol_type_le.fit_transform(data_Validate['protocol_type'])
data_Validate['service'] = service_le.fit_transform(data_Validate['service'])
data_Validate['flag'] = flag_le.fit_transform(data_Validate['flag'])

# Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data_Validate)
x_validate = pd.DataFrame(scaled_data, columns=data_Validate.columns)

# Mapping for predicted class labels
label_mapping = {
    0: 'back', 1: 'buffer_overflow', 2: 'ftp_write', 3: 'guess_passwd', 4: 'imap',
    5: 'ipsweep', 6: 'land', 7: 'loadmodule', 8: 'multihop', 9: 'neptune',
    10: 'nmap', 11: 'normal', 12: 'perl', 13: 'phf', 14: 'pod',
    15: 'portsweep', 16: 'rootkit', 17: 'satan', 18: 'smurf', 19: 'spy',
    20: 'teardrop', 21: 'warezclient', 22: 'warezmaster'
}

# Predict and map to labels
if val == 'knn':
    knn_multi = joblib.load("knn_model_sys.sav")  # Load model
    x_predict_multi = knn_multi.predict(x_validate)  # Predict class numbers
    mapped_predictions = [label_mapping[pred] for pred in x_predict_multi]  # Convert to class names

if val == 'svm':
    svm_multi = joblib.load("svm_model_sys.sav")  # Load model
    x_predict_multi = svm_multi.predict(x_validate)  # Predict class numbers
    mapped_predictions = [label_mapping[pred] for pred in x_predict_multi]  # Convert to class names
if val == 'rf':
    rf_multi = joblib.load("rf_model.sav")  # Load model
    x_predict_multi = rf_multi.predict(x_validate)  # Predict class numbers
    mapped_predictions = [label_mapping[pred] for pred in x_predict_multi]  # Convert to class names\
if val == 'lr':
    lr_multi = joblib.load("logistic_regression_model.sav")  # Load model
    x_predict_multi = lr_multi.predict(x_validate)  # Predict class numbers
    mapped_predictions = [label_mapping[pred] for pred in x_predict_multi]  # Convert to class names
if val == 'nb':
    nb_multi = joblib.load("nb_model_sys.sav")  # Load model
    x_predict_multi = nb_multi.predict(x_validate)  # Predict class numbers
    mapped_predictions = [label_mapping[pred] for pred in x_predict_multi]  # Convert to class names
if val == 'xgb':
    xgb_multi = joblib.load("xgb_model_sys.sav")  # Load model
    x_predict_multi = xgb_multi.predict(x_validate)  # Predict class numbers
    mapped_predictions = [label_mapping[pred] for pred in x_predict_multi]  # Convert to class names
    

# Append predictions to DataFrame
data['Predicted Attack'] = mapped_predictions

# Save updated CSV
data.to_csv(path, index=False)

print('Prediction completed. File updated with mapped class labels.')



