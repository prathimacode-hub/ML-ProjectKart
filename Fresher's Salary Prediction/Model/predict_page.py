import streamlit as st
import pickle
import numpy as np 

def load_model():
    with open('xgboost_model.pkl','rb') as file:
        data = pickle.load(file)
    return data
data = load_model()

regressor_loaded = data['model']
le_gender = data['le_gender']
le_ssc_b = data['le_ssc_b']
le_hsc_b = data['le_hsc_b']
le_hsc_s = data['le_hsc_s']
le_degree_t = data['le_degree_t']
le_workex = data['le_workex']
le_specialisation = data['le_specialisation']
le_status = data['le_status']

def show_predict_page():
    st.title("Freshers Salary Prediction")

    st.write("""### We need some information to predict the salary""")
    gender = ('M', 'F')
    ssc_b = ('Others', 'Central')
    hsc_b = ('Others', 'Central')
    hsc_s = ('Commerce', 'Science', 'Arts')
    degree_t = ('Sci&Tech', 'Comm&Mgmt', 'Others')
    workex = ('No', 'Yes')
    specialisation = ('Mkt&HR', 'Mkt&Fin')
    status = ('Placed', 'Not Placed')
    ##['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'hsc_s', 'degree_p',
       ##'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p', 'status']

    gender = st.selectbox("Gender",gender,key='gender')
    ssc_p = st.slider(" Secondary School Certificate Percentage",min_value=30.0,max_value=99.0,key='ssc_p')
    ssc_b = st.selectbox("Secondary School Certificate Board",ssc_b,key='ssc_b')
    hsc_p = st.slider("Higher Secondary School Percentage",min_value=30.0,max_value=99.0,key='hsc_p')
    hsc_b = st.selectbox("Higher Secondary School Board",hsc_b,key='hsc_b')
    hsc_s = st.selectbox("Higher Secondary School Subject",hsc_s,key='hsc_s')
    degree_p = st.slider("Degree Percentage",min_value=30.0,max_value=99.0,key='degree_p')
    degree_t = st.selectbox("Degree Type",degree_t,key='degree_t')
    workex = st.selectbox("Work Experience",workex,key='workex')
    etest_p = st.slider("Entrance Test Percentage",min_value=30.0,max_value=99.0,key='etest_p')
    specialisation = st.selectbox("Specialisation of Subjects",specialisation,key='specialisation')
    mba_p = st.slider("MBA Percentage",min_value=30.0,max_value=99.0,key='mba_p')
    status = st.selectbox("Status",status,key='status')

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p, status ]])
        X[:,0] = le_gender.transform(X[:,0])
        X[:,2] = le_ssc_b.transform(X[:,2])
        X[:,4] = le_hsc_b.transform(X[:,4])
        X[:,5] = le_hsc_s.transform(X[:,5])
        X[:,7] = le_degree_t.transform(X[:,7])
        X[:,8] = le_workex.transform(X[:,8])
        X[:,10] = le_specialisation.transform(X[:,10])
        X[:,12] = le_status.transform(X[:,12])

        X = X.astype(float)

        salary = regressor_loaded.predict(X)
        st.success(f'The estimated salary is {salary}')