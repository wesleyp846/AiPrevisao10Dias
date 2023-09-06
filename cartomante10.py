# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, LSTM, Dropout
# import matplotlib.pyplot as plt
# #from sklearn.model_selection import trains_test_split

# pd.set_option('display.max_columns', 500)

# df = pd.read_csv('C:\\Users\\avent\\Desktop\\ppy\\etl\\all_bovespa.csv')
# df['data_pregao'] = pd.to_datetime(df['data_pregao'], format='%Y-%m-%d')
# df_acao = df[df['sigla_acao'] == 'ITSA4']
# df_acao_fec = df_acao[['data_pregao', 'preco_fechamento']]
# df_acao_fec = df_acao_fec.set_index(pd.DatetimeIndex(df_acao_fec['data_pregao'].values))
# df_acao_fec.drop('data_pregao', axis=1, inplace=True)
# #print(df_acao_fec)
# # plt.figure(figsize=(16, 8))
# # plt.title('preco de fechamento')
# # plt.plot(df_acao_fec['preco_fechamento'])
# # plt.xlabel('data')
# qtd_linhas = len(df_acao_fec)
# qtd_linhas_treino = round(.70*qtd_linhas)
# qtd_linhas_teste = qtd_linhas-qtd_linhas_treino
# # info = (f'linhas treino = 0:{qtd_linhas_treino}   '
# #         f'linhas teste = {qtd_linhas_treino}:{qtd_linhas_treino + qtd_linhas_teste}')
# #print(info)
# scaler = StandardScaler()
# df_scaled = scaler.fit_transform(df_acao_fec)
# train = df_scaled[:qtd_linhas_treino]
# test = df_scaled[qtd_linhas_treino: qtd_linhas_treino+qtd_linhas_teste]
# #print(len(train), len(test))
# def creat_df(df, steps=1):
#     datax, datay = [], []
#     for i in range(len(df)-steps-1):
#         a = df[i:(i+steps), 0]
#         datax.append(a)
#         datay.append(df[i+steps, 0])
#     return np.array(datax), np.array(datay)
# steps = 15
# x_train, y_train = creat_df(train, steps)
# x_test, y_test = creat_df(test, steps)
# # print(x_train.shape)
# # print(y_train.shape)
# # print(x_test.shape)
# # print(y_test.shape)
# x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
# x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)
# model = Sequential()
# model.add(LSTM(35, return_sequences=True, input_shape=(steps, 1)))
# model.add(LSTM(35, return_sequences=True))
# model.add(LSTM(35))
# model.add(Dropout(0.2))
# model.add(Dense(1))
# model.compile(optimizer='adam', loss='mse')
# model.summary()
# validation = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, batch_size=15, verbose=2)
# plt.plot(validation.history['loss'], label='Training loss')
# plt.plot(validation.history['val_loss'], label='Validation loss')
# plt.legend