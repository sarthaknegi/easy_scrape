import pandas as pd



def tbody_data(pretty_table, main_dataframe, flag, choice):

    '''
    :param pretty_table: this is table data
    :param main_dataframe: the dataframe wherr the table data will be stored
    :param flag: this will tell if the dataframe have headers or not. o says no and 1 says yes.
    :param choice: this variable tells the which table to scrape if there are multiple tables with the same table name.
    :return: dataframe containing the table data

    '''

    tbody = pretty_table[choice].find_all('tbody')
    thead = tbody[0].find_all('th')
    if thead and flag == 1:
        thead_list = []
        for th in thead:
            thead_list.append(th.text)
        main_dataframe = pd.DataFrame(columns=thead_list)

    pos = 0 #to update the rows
    all_trs = tbody[0].find_all('tr')
    for tr in all_trs:
        data_list = []
        for data in tr.find_all('td'):
            data_list.append(data.text)

        try:
            main_dataframe.loc[pos] = data_list
        except:
            print(len(main_dataframe))
            if len(main_dataframe) >= 1:
                thead_list = list(main_dataframe.columns)
                new_thead_list = thead_list[1:]
                main_dataframe = pd.DataFrame(columns=new_thead_list)
                try:
                    main_dataframe.loc[pos] = data_list
                except:
                    main_dataframe = pd.DataFrame(columns=thead_list)
            else:
                main_dataframe = pd.DataFrame(columns=list(range(len(data_list))))
                main_dataframe.loc[pos] = data_list


        pos+=1


    return main_dataframe
