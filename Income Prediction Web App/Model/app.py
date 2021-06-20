import streamlit as st
import pandas as pd 
import pickle 
from PIL import Image
pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)

st.header(' 𝑰𝒏𝒄𝒐𝒎𝒆 𝑷𝒓𝒆𝒅𝒊𝒄𝒕𝒊𝒐𝒏 𝑾𝒆𝒃 𝑨𝒑𝒑')

image = Image.open("income.jpg")
st.image(image,use_column_width=True)

def prediction(data):
    prediction = model.predict(data)
    print(prediction)
    return prediction

def user_input_features():

    
    # age = st.number_input('Enter Age',key='age')
    age = st.slider('Age',min_value=17,max_value=90,key='age')
    workclass = st.selectbox('Work Class',('Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked'),key='workclass')
    
    education_num = st.slider('Education Num',min_value=1,max_value=16,key='education_num')
    marital_status = st.selectbox('Marital Status',('Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'),key='marital_status')
    occupation = st.selectbox('Occupation',('Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'),key='occupation')
    relationship = st.selectbox('Relationship',( 'Not-in-family', 'Husband', ' Wife', ' Own-child', ' Unmarried',' Other-relative'),key='relationship')
    race = st.selectbox('Race',(' White',' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo' ' Other'),key='race')
    sex = st.selectbox('Sex',('Male','Female'),key='sex')
    
    
    capital_loss = st.slider('Enter Capital Loss',min_value=0.0,max_value=1.0,key='capital_loss')
    
    country = st.selectbox('Country',(' United-States',' Cuba', ' Jamaica', ' India',' Mexico', ' South',' Puerto-Rico', ' Honduras' ,' England',' Canada',' Germany',' Iran', ' Philippines' ,' Italy' ,' Poland',' Columbia' ,' Cambodia' ,' Thailand',' Ecuador' ,' Laos', ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',' El-Salvador', ' France' ,' Guatemala', ' China', ' Japan' ,' Yugoslavia',' Peru' ,' Outlying-US(Guam-USVI-etc)', ' Scotland', ' Trinadad&Tobago',' Greece', ' Nicaragua' ,' Vietnam' ,' Hong' ,' Ireland' ,' Hungary',' Holand-Netherlands'),key='country')
    education_level = st.selectbox('Education Level',('Compulsory','Bachelors','Associate','High_School_grad','Professor','Masters'),key='education_level')
    
    capital_gain = st.slider('Enter capital gain',min_value=0.0,max_value=1.0,key='capital_gain')
    hours_per_week = st.slider('Hour Per Week',min_value=1,max_value=90,key='hour_per_week')
    # hours_per_week = st.number_input('Enter hours',key='hrs')

    data = {'age':age,
            'workclass':workclass,
            'education_num':education_num,
            'marital_status':marital_status,
            'occupation':occupation,
            'relationship':relationship,
            'race':race,
            'sex':sex,
            'capital_loss':capital_loss,
            'country':country,
            'education_level':education_level,
            'capital_gain':capital_gain,
            'hours_per_week':hours_per_week}

    features = pd.DataFrame(data,index=[0])
    return features

input_df = user_input_features()
input_df
raw_data = pd.read_csv('clean_data.csv')
data = raw_data.drop(columns=['salary'])
df = pd.concat([input_df,data],axis=0,ignore_index=True)


encode = ['workclass','marital_status','occupation','relationship','race','sex','country','education_level']
for col in encode:
    # dummy = pd.get_dummies(df[col], prefix=col)
    dummy = pd.get_dummies(data, prefix_sep='_',drop_first = True)
    df = pd.concat([df,dummy], axis=1)
    del df[col]

# Selects only the first row (the user input data)

df = df[:1]



df = df.loc[:,~df.columns.duplicated()]


show_input_features = ''
result = ''

if st.button("Predict"): 
    # st.subheader('Input_Dataset')
    # show_input_features = st.write(df) 
    # st.subheader('1 If The Person Earn More Than 50K  And 0 If The Person Earn Less Than 50K')
    result = prediction(df)

    if result == [0]:
        st.title('Person Earns Less than 50K')
        # img = Image.open("l.jpg")
        # st.image(img,use_column_width=True)
    else:
        st.title('Person Earns More than 50K')
        # image = Image.open("income.jpg")
        # st.image(image,use_column_width=True)

    
# dst.success(str(result)) 




