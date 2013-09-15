import sys
import numpy as np
from pandas import *
import random

def get_initial_prob_lst(filename, intial_prob_lst):
    num_columns = filename.readline()[:-1]
    filename.readline()
    dict_keys = filename.readline().split()
    dict_vals = filename.readline().split()
    filename.readline()
    filename.readline()
    intial_prob_lst += zip(dict_keys,dict_vals)
    return int(num_columns)

def parse_transition_matrix_into_df(filename):
    open_file = open(filename, 'r')
    initial_prob_lst = []
    df_lst = []
    num_columns = get_initial_prob_lst(open_file,initial_prob_lst)
    column_series = [x[0] for x in initial_prob_lst]
    for i in range(num_columns):
        curr_row = open_file.readline().split()
        row_index = curr_row[0]
        df_lst.append((row_index,curr_row[1:]))
    df = DataFrame.from_items(df_lst,orient='index',columns=column_series)
    return df, initial_prob_lst

def generate_state_lst_expanded(df):
    expanded_dict = {}
    for row_index in df.index:
         row = df.loc[row_index]
         expanded_dict[row_index] = [col_index for col_index in df.columns for i in range(int(row[col_index]))]
    print expanded_dict
    return expanded_dict

def run_simulation(df,initial_prob_lst):
    initial_prob_lst_expanded = [elem[0] for elem in initial_prob_lst for i in range(int(elem[1]))]
    start_state = random.choice(initial_prob_lst_expanded)
    curr_state = start_state
    freq_lst_expanded = generate_state_lst_expanded(df)
    for i in range(10):
        print "Current state is " + curr_state
        curr_state = random.choice(freq_lst_expanded[curr_state])
        

def main():
    filename = raw_input("Enter name of transition matrix: ")
    df,initial_prob_lst = parse_transition_matrix_into_df(filename)
    run_simulation(df,initial_prob_lst)

if __name__ == '__main__':
   sys.exit(main())
