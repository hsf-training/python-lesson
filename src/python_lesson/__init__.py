import uproot
import numpy as np

reference = None


def check_truth(df):
    global reference

    if reference is None:
        print('Loading reference dataset, this will take a moment...')
        reference = uproot.open(
            'https://cern.ch/starterkit/data/advanced-python-2018/real_data.root',
            httpsource={'chunkbytes': 10*1024*1024, 'limitbytes': 33554432, 'parallel': 64}
        )['DecayTree']['Jpsi_M'].arrays(library='pd')

    reference['original_index'] = np.arange(len(reference))

    tmp_df = df[['Jpsi_M']].merge(reference, on=['Jpsi_M'], how='left', indicator=True, validate='1:1')
    if len(tmp_df) != len(df):
        print(len(df))
        print(len(tmp_df))
        raise ValueError('Failed to match some events, did this come from the correct dataset')

    # n_signal = np.count_nonzero(tmp_df['catagory'] == 1)
    # n_background = np.count_nonzero(tmp_df['catagory'] == 0)
    n_signal = np.count_nonzero(tmp_df['original_index'] <= 1215)
    n_background = np.count_nonzero(tmp_df['original_index'] > 1215)
    print(f'Data contains {n_signal} signal events')
    print(f'Data contains {n_background} background events')

    tmp_df_signal_window = tmp_df.query('(3.0 < Jpsi_M < 3.2)')
    n_signal = np.count_nonzero(tmp_df_signal_window['original_index'] <= 1215)
    n_background = np.count_nonzero(tmp_df_signal_window['original_index'] > 1215)
    print(f'Significance metric is {n_signal/np.sqrt(n_signal + n_background):.2f}')
