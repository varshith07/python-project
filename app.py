import streamlit as st

def temp():
    choice=st.selectbox('select parameter',[' ','Celsius to Fahrenheit','Fahrenheit to celsius'])
    if choice=='Celsius to Fahrenheit':
        cel=st.number_input('enter celsius')
        
        faren=(cel*1.8)+32
        st.write(faren,'Fahrenheit')
    else:
        fahren=st.number_input('enter Fahrenheit')
        cels=((fahren-32)*5)/9
        st.write(cels,'celsius')
def length_function():
    choices=st.selectbox('select parameter',[' ','feets','meters to','hectares to','acres to'])
    if choices=='feets':
        feet=st.number_input('enter feets')
        box=st.selectbox('select',['meters','cm','inches'])
        if box=='meters':
            meter=0.305*feet
            st.write(meter,'meters')
        elif box=='cm':
            cms=30.48*feet
            st.write(cms,'centimeters')
        else:
            inch=12*feet
            st.write(inch,'inches')
    elif choices=='meters to':
        meters=st.number_input(' enter meters')
        box=st.selectbox('select',['feet','kms','miles'])
        if box=='feet':
            feet=meters/0.3048
            st.write(feet,'feets')
        elif box=='kms':
            kms=meters*0.001
            st.write(kms,'kms')
        else:
            miles=meters*0.000621
            st.write(miles,'miles')
    elif choices=='hectares to':
        hec=st.number_input('enter hectares')
        box=st.selectbox('select',['to acres','to yards'])
        if box=='to acres':
            acre=2.471*hec
            st.write(acre,'acres')
        else:
            yard=11959.9*hec
            st.write(yard,'square yards')
    else:
        acres=st.number_input('enter acres')
        box=st.selectbox('select',['to hectares','to yards'])
        if box=='to hectares':
            hec=0.405*acres
            st.write(hec,'hectares')
        else:
            yards=4840*acres
            st.write(yards,'yrads')
def weight():
    weigh=st.selectbox('select',['pounds','kgs'])
    if weigh=='pounds':
        pounds=st.number_input('enter weight in pounds')
        kgs=0.454*pounds
        st.write(kgs,'weight in kgs')
    else:
        kgs=st.number_input('enter weight in kgs')
        pounds=2.205*kgs
        st.write(pounds,'lbs')
if __name__=="__main__":
    st.title("Converter App")
    check=st.sidebar.selectbox('what to convert',[' ','Temperature','Length','weight'])
    if check=='Temperature':
        temp();
    elif check=='Length':
        length_function();
    elif check=='weight':
         weight();
    else:
        st.write('Our converter app converts length ,weight,temperatures.')
        st.write('we convert temperatures from celsius to fahrenheit and fahrenheit to celsius,')
        st.write('We convert different units of length.')
        st.write('\n')
        st.write('TEAM MEMBERS')
        st.success('T.Varshith')
        st.success('V.Yashwanth')
        st.success('J.Sai Nithin')
        st.success('Mohd.Moyeed')