from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import streamlit as st
import numpy as np
def read_dataset(name,engine):
    try:
        dataset = pd.read_sql_table(name,engine)
    except:
        dataset = pd.DataFrame([])
    return dataset
def list_datasets(engine):
    datasets = engine.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;")
    return datasets.fetchall()
def write_dataset(name,dataset,engine):
    dataset.to_sql('%s' % (name),con=engine,index=False,if_exists='replace',chunksize=1000)
# def insert_table() :


if __name__ == '__main__':

    engine = create_engine("postgresql://postgres:longvu123@localhost:5432/postgres")
    engine_dataset = create_engine("postgresql://postgres:longvu123@localhost:5432/postgres")
    engine.execute("CREATE TABLE IF NOT EXISTS records (name text PRIMARY KEY, details text[])")
    st.set_page_config(layout="wide")

    st.title('Dashboard')
    column_1, column_2 = st.columns(2)
   
    # with column_1: 

    with column_2:
        try:
            read_title = st.empty()
            dataset_to_read = st.selectbox('Select dataset',([x[0] for x in list_datasets(engine_dataset)]))
            read_title.header('Dataset')
            if st.button('Open'):
                df = read_dataset(dataset_to_read,engine_dataset)
                df.head()
                st.subheader('Test')
                st.line_chart(df['value'])
                st.write(df)
            if st.button('Insert'):


                

                df = read_dataset(dataset_to_read,engine_dataset)
                df1 = engine.execute('INSERT INTO tbl1(value) SELECT value*99 FROM order_info11 ;')
                df1 = read_dataset
                


                
        except:
            pass



# from sqlalchemy import create_engine
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')
