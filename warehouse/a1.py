def convert_currency(val):
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)
def convert_percent(val):
    new_val = val.replace('%', '')
    return float(new_val) / 100
def splitAddress(dataset):
    dataset = df.Address.coppy()
    for i in range(0,len(dataset.Address)):
        a= dataset.Address[i].split(',')
        df['Quan'][i] = a[len(a)-2]
    for i in dataset['Quan']:
        if 'Quận' not in i and 'Huyện' not in i:
            dataset = dataset.drop(dataset[dataset['Quan']==i].index)


df['X'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
